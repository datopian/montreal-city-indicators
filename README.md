---
permalink: /index.html
---
#Montreal KPI Dashboard
## To generate data subsets
`$ python kpis.py`

This will download the _indicateurs.csv_ dataset and output the following csv files:

### `parks.csv`
* KPI 2554
* 'Operating costs for parks per hectare'
* 'Coûts d’exploitation relatifs aux parcs par hectare'

### `trips.csv`
* KPI 2510
* 'Number of trips by public transport per capita'
* 'Nombre de déplacements en transport collectif par habitant'

### `libs.csv`
* KPI 2692
* 'Library operating costs per capita'
* 'Coûts d’exploitation des bibliothèques par habitant'

## To update output data
* Evaluate available performance indicators using http://ville.montreal.qc.ca/vuesurlesindicateurs/
* Update `kpis.py` with new kpi information
* Run `$ python kpis.py`
### Example KPI definition from `kpis.py`
```python
kpis = {
  '2554': ('Operating costs for parks per hectare', 'Coûts d’exploitation relatifs aux parcs par hectare', 'parks'),
# ...
}
```

Dict key represents _KPIID_, the associated list contains the _english_ and _french_ definition for the KPI, and the name of the _target csv file_ (`parks.csv` in this case).

## Publish Data
* generate data subsets (above)
* make sure https://datahub.io/docs/features/data-cli is installed locally
* `$ data push`

Simple, static web page that uses [dashboard-js](https://github.com/datahq/dashboard-js) library to render visualizations.

## Dashboard Development

### HTML and CSS

To improve layout, simply edit stylesheets in `css/` directory. The only HTML file is `index.html`.

### Widgets

We've modularized widgets into separate json files in `widgets/`. The `js/prepare.js` script bundles all json files into `config` variable in a way that `dashboard-js` can use it.

To add a new one, you need to create a json file in the directory. See other examples for syntax.
