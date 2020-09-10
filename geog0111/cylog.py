#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cryptography.fernet import Fernet
import numpy as np
from pathlib import Path
from getpass import getpass
import sys

__author__ = "P Lewis"
__copyright__ = "Copyright 2018 P Lewis"
__license__ = "GPLv3"
__email__ = "p.lewis@ucl.ac.uk"

class  Cylog():
    '''
    cylog provides a mechanism to partially hide username and
    password information that is required in plain text.

    It does this by storing a key and the encrypted version in
    a file accessible only to the user.
    
    Of course, when called (by the user) the (username, password)
    are exposed in plain text, so only use this when you 
    have to enter plain text username/password information.

    It is written as a utility to allow UCL MSc students to 
    show access to NASA Earthdata dataset download, without 
    the need to expose (username, password) in a submitted report.

    Stores (in a dictionary in ~/{dest_path}/.cylog.npz) an
    encrypted form of username and password (and key)
   
    Uses cryptography.fernet.Fernet() for encryption
 
    cylog().login() : returns plain text tuple
                      (username, password) 
    '''
    def __init__(self,site,init=False,stderr=False,verbose=False,destination_folder='.cylog'):
        '''
        Positional arguments:
        ----------
        site: 
           string of anchor URL for site to associate with username and
           password

        Keyword arguments 
        ----------
        init: bool
            to re-initialise the passord/username
            set to True. This will overwrite any existing password file.
 
        destination_folder: str
            The destination sub-folder, relative to ${HOME}.
            If this doesnt exist, it is created.

        verbose: Bool
            verbose True or False (False default)

        when prompted, please supply:

        username: str
            username
        password: str
            password
        ''' 
        self.site = site
        self.stderr = stderr or sys.stderr
        self.verbose = verbose

        self.dest_path = Path.home().joinpath(destination_folder)
        p = self.dest_path.joinpath('.cylog.npz')
        if (init == False) and p.exists():
            return 
        else:
            self._init(site=self.site,destination_folder=destination_folder)

    def msg(self,*args):
        '''message passing'''
        print('-->',*args,file=self.stderr)

    def _init(self,site=False,destination_folder='.cylog'):

        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        data = {'key':key}
        self.dest_path = Path.home().joinpath(destination_folder)

        self.msg(f'generating key file in {self.dest_path.as_posix()}')

        if not self.dest_path.exists():
            self.dest_path.mkdir()
        self.dest_path.chmod(0o700)
        p = self.dest_path.joinpath('.cylog.npz')

        self.msg(f'--> saving key file to {p.as_posix()}')

        np.savez(p,**data)
        p.chmod(0o600)


    def _setup(self,site=False,destination_folder='.cylog'):
        site = site or self.site

        # make sure keyfile exists
        # should check permissions too
        keyfile = self.dest_path.joinpath('.cylog.npz')
        if not keyfile.exists():
            self.msg(f"key file {keyfile.as_posix()} doesn't exist")
            self._init(site=site,destination_folder=destination_folder)

        self.msg(f"loading key file {keyfile.as_posix()}")
        data = dict(np.load(keyfile.as_posix()))
        if 'key' not in data.keys():
            self.msg(f"no key found in key file {keyfile.as_posix()}")
            self._init(site=site,destination_folder=destination_folder)

        key = data['key']

        while True:
            print(f'--> user login required for {site} <--')
            username = input("Enter your username: ")
            if username == "exit":
                print('exiting password setup')
                return
            password = getpass("please type your password")
            password_again=getpass("please re-type your password for confirmation")
            if password_again==password:
                print("password created")
                break
            else:
                print("Password does not match. Please try again")
        
        try:
            self.msg(f"ciphering key from key file {keyfile.as_posix()}")
            cipher_suite = Fernet(key)
        except:
            self.msg(f"problem with key from key file {keyfile.as_posix()}")
            self.msg(f"try deleting the file and re-running")
            return

        ciphered_user = cipher_suite.encrypt((username.encode()))
        ciphered_pass = cipher_suite.encrypt((password.encode()))
        data[f'ciphered_user_{site}'] = ciphered_user
        data[f'ciphered_pass_{site}'] = ciphered_pass

        self.msg(f"--> writing ciphers to file")

        self.dest_path = Path.home().joinpath(destination_folder)
        if not self.dest_path.exists():
            self.dest_path.mkdir()
        self.dest_path.chmod(0o700)
        p = self.dest_path.joinpath('.cylog.npz')
        np.savez(p,**data)
        p.chmod(0o600)
        self.msg(f"--> done writing ciphers to file")

    def login(self,site=False,force=False):
        '''
        Reads encrypted information from ~/{dest_path}/.cylog.npz

        Keyword arguments
        ----------
        site = False (so self.site is default)
               string of anchor URL for site to associate with username and
               password
        force = False
               force password re-entry for site

        Returns
        --------
        A tuple containing plain text (username,password) for (site or self.site)

        '''
        site = site or self.site
        force = force 

        keyfile = self.dest_path.joinpath('.cylog.npz')
        if not keyfile.exists():
            self.msg(f"key file {keyfile.as_posix()} doesn't exist")
            self._init(site=site,destination_folder=destination_folder)

        self.msg(f"loading key file {keyfile.as_posix()}")
        data = dict(np.load(keyfile.as_posix()))
        if 'key' not in data.keys():
            self.msg(f"no key found in key file {keyfile.as_posix()}")
            self._init(site=site,destination_folder=destination_folder)

        key = data['key']
        
        if (f'ciphered_user_{site}' not in data) or (f'ciphered_pass_{site}' not in data):
            self.msg(f"ciphered_user_{site} and/or ciphered_pass_{site} " +
                   f"missing from key file {keyfile.as_posix()}")
            print(f"try again ... or enter 'exit' as username to quit")
            self._setup(site=site)
            return self.login(site=site)

        if force:
            self.msg(f'forcing re-entry of password for {site}')
            self._setup(site=site)
            return self.login(site=site)

        return (Fernet(data['key']).decrypt(np.atleast_1d(data[f'ciphered_user_{site}'])[0]),\
                Fernet(data['key']).decrypt(np.atleast_1d(data[f'ciphered_pass_{site}'])[0]))


def main():
    site = "test site"
    print("round 1 : force re-entry")
    cy = Cylog(site,verbose=True).login(force=True)

    print("round 1 : just get it")
    cy = Cylog(site,verbose=True).login()
    print(f'result for {site}: {cy}')

if __name__ == "__main__":
    main()


