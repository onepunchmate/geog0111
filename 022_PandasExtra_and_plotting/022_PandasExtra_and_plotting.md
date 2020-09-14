The iconic cover shows the oscillation signal coming from the Pulsar PSR B1919+21 https://en.wikipedia.org/wiki/PSR_B1919%2B21

derived from https://github.com/igorol/unknown_pleasures_plot and https://matplotlib.org/3.1.1/gallery/animation/unchained.html


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc

from IPython.display import HTML

```


```python
url='https://raw.githubusercontent.com/igorol/unknown_pleasures_plot/master/pulsar.csv'
df=pd.read_csv(url,header=None)
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>...</th>
      <th>290</th>
      <th>291</th>
      <th>292</th>
      <th>293</th>
      <th>294</th>
      <th>295</th>
      <th>296</th>
      <th>297</th>
      <th>298</th>
      <th>299</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.81</td>
      <td>-0.91</td>
      <td>-1.09</td>
      <td>-1.00</td>
      <td>-0.59</td>
      <td>-0.82</td>
      <td>-0.43</td>
      <td>-0.68</td>
      <td>-0.71</td>
      <td>-0.27</td>
      <td>...</td>
      <td>-0.08</td>
      <td>0.19</td>
      <td>-0.19</td>
      <td>-0.18</td>
      <td>-0.20</td>
      <td>-0.26</td>
      <td>-0.52</td>
      <td>-0.44</td>
      <td>-0.58</td>
      <td>-0.54</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.61</td>
      <td>-0.40</td>
      <td>-0.42</td>
      <td>-0.38</td>
      <td>-0.55</td>
      <td>-0.51</td>
      <td>-0.71</td>
      <td>-0.79</td>
      <td>-0.52</td>
      <td>-0.40</td>
      <td>...</td>
      <td>-0.34</td>
      <td>-0.58</td>
      <td>-0.26</td>
      <td>-0.64</td>
      <td>-1.05</td>
      <td>-0.83</td>
      <td>-0.80</td>
      <td>-0.47</td>
      <td>-0.13</td>
      <td>-0.12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-1.43</td>
      <td>-1.15</td>
      <td>-1.25</td>
      <td>-1.13</td>
      <td>-0.76</td>
      <td>-0.25</td>
      <td>0.40</td>
      <td>0.26</td>
      <td>0.30</td>
      <td>0.36</td>
      <td>...</td>
      <td>-0.29</td>
      <td>0.16</td>
      <td>0.83</td>
      <td>0.99</td>
      <td>1.28</td>
      <td>0.11</td>
      <td>-0.77</td>
      <td>-0.88</td>
      <td>-0.45</td>
      <td>-1.01</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-1.09</td>
      <td>-0.85</td>
      <td>-0.72</td>
      <td>-0.74</td>
      <td>-0.26</td>
      <td>-0.04</td>
      <td>-0.19</td>
      <td>0.18</td>
      <td>0.03</td>
      <td>0.19</td>
      <td>...</td>
      <td>0.48</td>
      <td>0.52</td>
      <td>-0.14</td>
      <td>-1.13</td>
      <td>-1.07</td>
      <td>-1.03</td>
      <td>-0.78</td>
      <td>-0.40</td>
      <td>0.18</td>
      <td>0.27</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-1.13</td>
      <td>-0.98</td>
      <td>-0.93</td>
      <td>-0.90</td>
      <td>-1.14</td>
      <td>-1.00</td>
      <td>-0.90</td>
      <td>-1.18</td>
      <td>-1.30</td>
      <td>-1.07</td>
      <td>...</td>
      <td>-0.27</td>
      <td>-0.47</td>
      <td>-0.49</td>
      <td>-0.23</td>
      <td>-0.75</td>
      <td>-0.29</td>
      <td>-0.54</td>
      <td>-0.65</td>
      <td>-0.64</td>
      <td>-0.94</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>75</th>
      <td>0.62</td>
      <td>0.64</td>
      <td>0.59</td>
      <td>0.30</td>
      <td>0.01</td>
      <td>0.05</td>
      <td>-0.63</td>
      <td>0.07</td>
      <td>0.36</td>
      <td>0.78</td>
      <td>...</td>
      <td>0.20</td>
      <td>0.22</td>
      <td>0.23</td>
      <td>0.27</td>
      <td>-0.10</td>
      <td>-0.21</td>
      <td>-0.09</td>
      <td>-0.24</td>
      <td>-0.17</td>
      <td>-0.62</td>
    </tr>
    <tr>
      <th>76</th>
      <td>0.32</td>
      <td>0.31</td>
      <td>0.28</td>
      <td>0.42</td>
      <td>-0.24</td>
      <td>-0.48</td>
      <td>-0.73</td>
      <td>-0.64</td>
      <td>0.04</td>
      <td>0.02</td>
      <td>...</td>
      <td>-0.44</td>
      <td>-0.53</td>
      <td>-0.50</td>
      <td>-0.49</td>
      <td>-0.63</td>
      <td>-0.56</td>
      <td>-0.50</td>
      <td>-0.38</td>
      <td>-0.58</td>
      <td>-0.43</td>
    </tr>
    <tr>
      <th>77</th>
      <td>-0.09</td>
      <td>-0.14</td>
      <td>-0.24</td>
      <td>-0.24</td>
      <td>-0.66</td>
      <td>0.00</td>
      <td>0.29</td>
      <td>0.29</td>
      <td>0.60</td>
      <td>0.86</td>
      <td>...</td>
      <td>0.08</td>
      <td>-0.88</td>
      <td>-1.17</td>
      <td>-0.36</td>
      <td>-0.31</td>
      <td>-0.12</td>
      <td>0.29</td>
      <td>-0.02</td>
      <td>0.21</td>
      <td>0.44</td>
    </tr>
    <tr>
      <th>78</th>
      <td>0.11</td>
      <td>0.05</td>
      <td>0.05</td>
      <td>-0.05</td>
      <td>-0.03</td>
      <td>-0.29</td>
      <td>-0.08</td>
      <td>-0.54</td>
      <td>-0.01</td>
      <td>0.01</td>
      <td>...</td>
      <td>-0.73</td>
      <td>-0.54</td>
      <td>-0.53</td>
      <td>-0.92</td>
      <td>-0.68</td>
      <td>-0.87</td>
      <td>-1.31</td>
      <td>-1.02</td>
      <td>-1.10</td>
      <td>-1.62</td>
    </tr>
    <tr>
      <th>79</th>
      <td>0.12</td>
      <td>-0.12</td>
      <td>-0.12</td>
      <td>-0.45</td>
      <td>-0.24</td>
      <td>-0.48</td>
      <td>-0.57</td>
      <td>-0.19</td>
      <td>-0.07</td>
      <td>-0.59</td>
      <td>...</td>
      <td>0.12</td>
      <td>0.03</td>
      <td>-0.28</td>
      <td>0.02</td>
      <td>-0.01</td>
      <td>0.13</td>
      <td>0.09</td>
      <td>-0.01</td>
      <td>-0.03</td>
      <td>-0.23</td>
    </tr>
  </tbody>
</table>
<p>80 rows × 300 columns</p>
</div>




```python
vertical_margin = 20
horizontal_margin = 100
x_size = 28
y_size = 25
linewidth = 4
plot_name='images/new_order.png'


plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(x_size,y_size),frameon=False)

data = np.array(df)

n_lines = data.shape[0]
x = range(data.shape[1])

ax.set_yticks([])
ax.set_xticks([])
ax.set_xlim(min(x)-horizontal_margin, max(x)+horizontal_margin)
ax.set_ylim(-vertical_margin, df.shape[0] + vertical_margin)

def init():
    lines = []
    fills = []
    for i in range(n_lines):
        line = data[i]/3 + (n_lines - i)
        pltline = ax.plot(x, line, lw=linewidth, c='white', alpha=1, zorder=i/n_lines)
        pltfill = ax.fill_between(x, -5,line,  facecolor='black', zorder=i/n_lines)
        lines.append(pltline)
        fills.append(pltfill)
    return (lines,fills)

xx=init()
```


![png](022_PandasExtra_and_plotting_files/022_PandasExtra_and_plotting_4_0.png)



```python
data.shape
```




    (80, 300)




```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import mpl_toolkits.axes_grid1
import matplotlib.widgets
vertical_margin = 2.0
horizontal_margin = 10.0
x_size = 2.8
y_size = 2.5
linewidth = .4
fig, ax = plt.subplots(figsize=(x_size,y_size),frameon=False)


data = np.array(df)

n_lines = data.shape[0]
x = range(data.shape[1])

ax.set_yticks([])
ax.set_xticks([])
ax.set_xlim(min(x)-horizontal_margin, max(x)+horizontal_margin)
ax.set_ylim(-vertical_margin, df.shape[0] + vertical_margin)

def init():
    lines = []
    fills = []
    for i in range(n_lines):
        line = data[i]/3 + (n_lines - i)
        pltline = ax.plot(x, line, lw=linewidth, c='white', alpha=1, zorder=i/n_lines)
        pltfill = ax.fill_between(x, -5,line,  facecolor='black', zorder=i/n_lines)
        lines.append(pltline)
        fills.append(pltfill)
    return (lines,fills)

xx=init()
#plt.savefig(plot_name)
def update(i):
    # Shift all data to the right with wrap around
    old = data[-1,-1]
    data[-1,1:] = data[-1,:-1]
    # Fill-in new values
    data[-1,0] = old
    for i in range(n_lines):
        matplotlib.lines.Line2D(lines[i],data[i])
    return lines[0]

lines,fills = init()
anim = animation.FuncAnimation(fig, update, interval=10,frames=10,blit=True)

# call the animator. blit=True means only re-draw the parts that have changed.
```


![png](022_PandasExtra_and_plotting_files/022_PandasExtra_and_plotting_6_0.png)



```python
HTML(anim.to_html5_video())
```




<video width="200" height="180" controls autoplay loop>
  <source type="video/mp4" src="data:video/mp4;base64,AAAAIGZ0eXBNNFYgAAACAE00ViBpc29taXNvMmF2YzEAAAAIZnJlZQAAHN9tZGF0AAACoAYF//+c
3EXpvebZSLeWLNgg2SPu73gyNjQgLSBjb3JlIDE1MiAtIEguMjY0L01QRUctNCBBVkMgY29kZWMg
LSBDb3B5bGVmdCAyMDAzLTIwMTcgLSBodHRwOi8vd3d3LnZpZGVvbGFuLm9yZy94MjY0Lmh0bWwg
LSBvcHRpb25zOiBjYWJhYz0xIHJlZj0zIGRlYmxvY2s9MTowOjAgYW5hbHlzZT0weDM6MHgxMTMg
bWU9aGV4IHN1Ym1lPTcgcHN5PTEgcHN5X3JkPTEuMDA6MC4wMCBtaXhlZF9yZWY9MSBtZV9yYW5n
ZT0xNiBjaHJvbWFfbWU9MSB0cmVsbGlzPTEgOHg4ZGN0PTEgY3FtPTAgZGVhZHpvbmU9MjEsMTEg
ZmFzdF9wc2tpcD0xIGNocm9tYV9xcF9vZmZzZXQ9LTIgdGhyZWFkcz02IGxvb2thaGVhZF90aHJl
YWRzPTEgc2xpY2VkX3RocmVhZHM9MCBucj0wIGRlY2ltYXRlPTEgaW50ZXJsYWNlZD0wIGJsdXJh
eV9jb21wYXQ9MCBjb25zdHJhaW5lZF9pbnRyYT0wIGJmcmFtZXM9MyBiX3B5cmFtaWQ9MiBiX2Fk
YXB0PTEgYl9iaWFzPTAgZGlyZWN0PTEgd2VpZ2h0Yj0xIG9wZW5fZ29wPTAgd2VpZ2h0cD0yIGtl
eWludD0yNTAga2V5aW50X21pbj0yNSBzY2VuZWN1dD00MCBpbnRyYV9yZWZyZXNoPTAgcmNfbG9v
a2FoZWFkPTQwIHJjPWNyZiBtYnRyZWU9MSBjcmY9MjMuMCBxY29tcD0wLjYwIHFwbWluPTAgcXBt
YXg9NjkgcXBzdGVwPTQgaXBfcmF0aW89MS40MCBhcT0xOjEuMDAAgAAAGaFliIQAJ//+9bF8CmrJ
84oM6DIu4Zckya62IuJ744nkB+owAuCIeRVaYizSmJbHhpIbdySmCCr3YGRWH1dU3kzJeVzMNQwj
oRLFjYozaW64/xVN4daFjRM+nQ7h4NfHEmikjvWaQPmoFEtecWXP1jhBsNu+qT+3HN+LmzAtpUu6
PXU127Q4lUejexUtJVC83f7B5WpEJ5f4PwhJPniwGlV7QpNoZlfyck+RxmKH0li0N/j42zeIeJsE
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
">
  Your browser does not support the video tag.
</video>




```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init, blit=True)
plt.show()
```


![png](022_PandasExtra_and_plotting_files/022_PandasExtra_and_plotting_8_0.png)



```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider

TWOPI = 2*np.pi

fig, ax = plt.subplots()

t = np.arange(0.0, TWOPI, 0.001)
initial_amp = .5
s = initial_amp*np.sin(t)
l, = plt.plot(t, s, lw=2)

ax = plt.axis([0,TWOPI,-1,1])

axamp = plt.axes([0.25, .03, 0.50, 0.02])
# Slider
samp = Slider(axamp, 'Amp', 0, 1, valinit=initial_amp)

def update(val):
    # amp is the current value of the slider
    amp = samp.val
    # update curve
    l.set_ydata(amp*np.sin(t))
    # redraw canvas while idle
    fig.canvas.draw_idle()

# call update function on slider value change
samp.on_changed(update)

plt.show()
```


![png](022_PandasExtra_and_plotting_files/022_PandasExtra_and_plotting_9_0.png)


<html><head>


<!-- Load require.js. Delete this if your page already loads require.js -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha256-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"></script>
<script src="https://unpkg.com/@jupyter-widgets/html-manager@*/dist/embed-amd.js" crossorigin="anonymous"></script>
<script type="application/vnd.jupyter.widget-state+json">
{
    "version_major": 2,
    "version_minor": 0,
    "state": {}
}
</script>
</head>
<body>


</body>
</html>



```python

```