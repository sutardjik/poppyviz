# PanPop

An interactive web app using the Streamlit framework that visualizes the population trends of six countries from 1950 to 2020 using population pyramids and annual growth line graphs. PanPop explores demographic changes, providing interactive sliders for specific years and access to linked data sources for additional context.

## Home

- Folium (OpenStreetMap) with capitals of featured countries
- Individual Mapbox displays for each country

## Countries

- Population pyramid alters according to chosen year with interactive slider
  - Data source link directs to specified year's PopulationPyramid.net page
- Annual population growth line graph
- Interactive dataframes
  - Data used to create pyramids and line graphs
    - Query by column name
    - Download as Excel spreadsheet

## Country Comparison

- Annual population growth multiple-line graph for all six countries
  - Line trace can be excluded through single/double-click

## Dependencies

- [Pandas](https://pandas.pydata.org/): a powerful data manipulation and analysis library for rendering interactive dataframes
- [Plotly](https://plotly.com/python/): a flexible and interactive visualization library, including Plotly Express for high-level visualizations
- [XlsxWriter](https://xlsxwriter.readthedocs.io/): a Python library for creating Excel files
- [Pydeck](https://github.com/visgl/deck.gl/): a Python library for rendering Mapbox maps and creating interactive 3D visualizations
- [Folium](https://python-visualization.github.io/folium/): a Python library for creating leaflet.js maps

## Development

```bash
# ensure python 3.10 is installed
# clone project
git clone https://github.com/sutardjik/panpop.git
cd panpop

# install streamlit
pip install streamlit

# check streamlit version
streamlit --version

# upgrade streamlit version
pip install --upgrade streamlit

# run the app
streamlit run HOME.py
```
