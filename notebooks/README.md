First, create an account on plot.ly.

Find your api here: [https://plot.ly/settings/api]
make changes to this file:
`vi  ~/.plotly/.credentials`

Another way:
```
import plotly
plotly.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')
```

Plotly Offline allows you to create graphs offline and save them locally. There are also two methods for plotting offline: plotly.offline.plot() and plotly.offline.iplot().

* Use plotly.offline.plot() to create and standalone HTML that is saved locally and opened inside your web browser.
* Use plotly.offline.iplot() when working offline in a Jupyter Notebook to display the plot in the notebook.