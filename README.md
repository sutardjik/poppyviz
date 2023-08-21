# PopPyraViz

An interactive website using the Streamlit framework that visualizes the population trends of six countries from 1950 to 2020 using population pyramids and annual growth line graphs. It offers users an engaging and informative way to explore demographic changes, providing interactive sliders for specific years and access to linked data sources for additional context.

## Home

- Folium (OpenStreetMap)
  - Pinned locations of countries' capitals
    - Hover on capital to view name
    - Click on capital to see geographic coordinates
- Individual Mapbox displays for each country
- Click on country name to access its page
- View complete list of pages and web app's outlined features through sidebar

## Countries

- Population pyramid alters according to chosen year with interactive slider
  - Data source link directs to specified year's PopulationPyramid.net page
- Annual population growth line graph
- Interactive dataframes
  - Data used to create pyramids and line graphs
    - Query by column name
    - Download as Excel spreadsheet
- Sidebar displays description of trend observations

## Country Comparison

- Annual population growth multiple-line graph for all six countries
  - Line trace can be excluded through single/double-click
- Sidebar displays description of trend observations

## Dependencies

- [Pandas](https://pandas.pydata.org/) (version 1.5.3): a powerful data manipulation and analysis library for rendering interactive dataframes
- [Plotly](https://plotly.com/python/) (version 5.13.0): a flexible and interactive visualization library, including Plotly Express for high-level visualizations
- [XlsxWriter](https://xlsxwriter.readthedocs.io/) (version 3.0.8): a Python library for creating Excel files
- [Pydeck](https://github.com/visgl/deck.gl/): a Python library for rendering Mapbox maps and creating interactive 3D visualizations
- [Folium](https://python-visualization.github.io/folium/) (version 0.14.0): a Python library for creating leaflet.js maps

For more information and documentation about these libraries, please refer to their respective websites or official documentation.

## Development

```bash
# ensure python 3.10 is installed
# clone repository
git clone https://github.com/sutardjik/poppyraviz.git
cd poppyraviz

# install streamlit
pip install streamlit

# check streamlit version
streamlit --version

# run the app
streamlit run HOME.py
```
