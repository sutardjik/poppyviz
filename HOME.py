import streamlit as st
import pandas as pd
from streamlit_extras.add_vertical_space import add_vertical_space
import pydeck as pdk
from streamlit_folium import st_folium
import folium


def set_favicon():
    favicon_path = "./favicon.ico"
    st.set_page_config(page_title="PopPyraViz", page_icon=favicon_path)


set_favicon()
st.cache_data.clear()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

st.markdown(
    "<h1 style='text-align: center;'>PopPyraViz</h1>",
    unsafe_allow_html=True,
)

add_vertical_space(1)

st.markdown(
    "<p style='text-align: center;'>Explores the population trends of six countries from 1950 to 2020 through population pyramids and annual population growth line graphs.</p>",
    unsafe_allow_html=True,
)
add_vertical_space(1)
m = folium.Map(location=[35, 45], tiles="OpenStreetMap", zoom_start=1.5)
data = pd.DataFrame(
    {
        "lon": [-77.0369, -47.8919, 13.4050, 36.8219, 77.2090, 139.6503],
        "lat": [38.9072, -15.7975, 52.5200, -1.2921, 28.6139, 35.6762],
        "name": [
            "Washington D.C.",
            "Brasília",
            "Berlin",
            "Nairobi",
            "New Delhi",
            "Tokyo",
        ],
        "desc": [
            "USA’s Capital: 38.9072° N, 77.0369° W",
            "Brazil’s Capital: 15.7975° S, 47.8919° W",
            "Germany’s Capital: 52.5200° N, 13.4050° E",
            "Kenya’s Capital: 1.2921° S, 36.8219° E",
            "India’s Capital: 28.6139° N, 77.2090° E",
            "Japan’s Capital: 35.6762° N, 139.6503° E",
        ],
    },
    dtype=str,
)

for i in range(0, len(data)):
    folium.Marker(
        location=[data.iloc[i]["lat"], data.iloc[i]["lon"]],
        popup=data.iloc[i]["desc"],
        tooltip=data.iloc[i]["name"],
    ).add_to(m)
st_data = st_folium(m, height=400, width=800)

st.markdown(
    "<p>The above map includes the pinned capitals of the USA, Brazil, Germany, Kenya, India, and Japan. Hover over the capitals to view their names, and click on them to see their geographic coordinates.</p>",
    unsafe_allow_html=True,
)

add_vertical_space(1)

st.markdown(
    "Population pyramids graphically illustrate the age and gender distribution of a given population using a bar chart graphic to display the number or percentages of males and females in each age group. Population pyramids provide a clear picture of a population’s age-gender composition and can also be used to display future trends in a population.<sup>1</sup> The pyramid shapes alter and vary over time as countries encounter different population phases. They can be triangular, columnar, rectangular-shaped (with vertical sides rather than sloped), or have an irregular profile.<sup>2</sup>",
    unsafe_allow_html=True,
)

add_vertical_space(1)

st.markdown(
    "The trend of a nation’s declining mortality and fertility resulting from social and economic progress is known as the Demographic Transition Model (DTM). The DTM is a five-stage population model that describes the demographic transition as high stationary, early expanding, late expanding, low stationary, and declining. Countries are categorized based on their industrial development and GDP into preindustrial societies, more economically developed countries (MEDCs), and less economically developed countries (LEDCs). MEDCs are industrialized nations with high GDPs, low poverty, and low population growth rates. Countries identified as LEDCs have low GDPs, high poverty, and high population growth rates.<sup>3</sup>",
    unsafe_allow_html=True,
)

st.markdown(
    "<h4>Stage 1 – High Stationary</h4><p>High stationary is observed in preindustrial societies characterized by high birth rates due to the lack of birth control, high infant mortality rates, and cultural norms that support large families. Additionally, there are high fatality rates due to illness, starvation, inadequate hygiene, and lack of treatment.<sup>4</sup> Stage 1 pyramids have a broad base with concave sides.<sup>2</sup></p>",
    unsafe_allow_html=True,
)

st.markdown(
    "<h4>Stage 2 – Early Expanding</h4><p>Early expanding generally describes LEDCs where birth rates are high, and death rates decline due to advancements in medicine and hygiene, leading to rapidly expanding populations.<sup>4</sup> Stage 2 pyramids have a broad base with straight sides, creating a pyramidal profile.<sup>2</sup></p>",
    unsafe_allow_html=True,
)

st.markdown(
    "<h4>Stage 3 – Late Expanding</h4><p>Late expanding refers to wealthier LEDCs where birth and death rates continue to decline. As countries become more developed, contraception, improved healthcare, education, and the emancipation of women become more accessible. The rate of population increase slows down, and low infant mortality rates indicate the shift towards forming smaller families.<sup>4</sup> Stage 3 pyramids have convex sides with rounded edges, where the lower-middle portion slightly bulges out, making the pyramid dome-shaped or bell-shaped.<sup>2</sup></p>",
    unsafe_allow_html=True,
)

st.markdown(
    "<h4>Stage 4 – Low Stationary</h4><p>Low stationary pertains to MEDCs characterized by stable population sizes due to low birth and death rates.<sup>4</sup> Stage 4 pyramids are barrel-shaped, with nearly vertical sides as the width of the pyramid bars remains the same from bottom to top.<sup>2</sup></p>",
    unsafe_allow_html=True,
)

st.markdown(
    "<h4>Stage 5 – Declining</h4><p>Declining is also observed in MEDCs where the country’s population decreases due to birth rates falling below death rates resulting from low fertility.<sup>4</sup> Stage 5 pyramids are urn-shaped, in which the pyramid inverts with a shrinking base and expanding top, indicating a high dependency on older adults.<sup>2</sup></p>",
    unsafe_allow_html=True,
)

add_vertical_space(1)

st.markdown(
    "The following section shows the countries, their map displays, and DTM stages. Click on any country name to access its page.",
    unsafe_allow_html=True,
)

add_vertical_space(1)

st.markdown(
    "To view the complete list of pages and outlined features of this web app, refer to the sidebar on the left.",
    unsafe_allow_html=True,
)

st.write("---")

add_vertical_space(1)

col1, col2 = st.columns(2)
with col1:
    st.pydeck_chart(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v11",
            initial_view_state=pdk.ViewState(
                latitude=40, longitude=-96, zoom=2, height=330, width=340
            ),
        )
    )
    st.markdown(
        """<h5><em><a href="/USA" target="_self">USA</a></em> // Stage 4 – Low Stationary</h5>""",
        unsafe_allow_html=True,
    )
with col2:
    st.pydeck_chart(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v11",
            initial_view_state=pdk.ViewState(
                latitude=-16, longitude=-54, zoom=2.55, height=330, width=340
            ),
        )
    )
    st.markdown(
        """<h5><em><a href="/BRAZIL" target="_self">Brazil</a></em> // Stage 4 – Low Stationary</h5>""",
        unsafe_allow_html=True,
    )

with col1:
    st.pydeck_chart(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v11",
            initial_view_state=pdk.ViewState(
                latitude=51.3, longitude=10, zoom=4.2, height=330, width=340
            ),
        )
    )
    st.markdown(
        """<h5><em><a href="/GERMANY" target="_self">Germany</a></em> // Stage  5 – Declining</h5>""",
        unsafe_allow_html=True,
    )
with col2:
    st.pydeck_chart(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v11",
            initial_view_state=pdk.ViewState(
                latitude=0.1, longitude=38, zoom=4.5, height=330, width=340
            ),
        )
    )
    st.markdown(
        """<h5><em><a href="/KENYA" target="_self">Kenya</a></em> // Stage 2 – Early Expanding</h5>""",
        unsafe_allow_html=True,
    )

with col1:
    st.pydeck_chart(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v11",
            initial_view_state=pdk.ViewState(
                latitude=23.2, longitude=81, zoom=2.8, height=330, width=340
            ),
        )
    )
    st.markdown(
        """<h5><em><a href="/INDIA" target="_self">India</a></em> // Stage 3 – Late Expanding</h5>""",
        unsafe_allow_html=True,
    )
with col2:
    st.pydeck_chart(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v11",
            initial_view_state=pdk.ViewState(
                latitude=38.3, longitude=139, zoom=3.5, height=330, width=340
            ),
        )
    )
    st.markdown(
        """<h5><em><a href="/JAPAN" target="_self">Japan</a></em> // Stage 5 – Declining</h5>""",
        unsafe_allow_html=True,
    )

st.write("---")

add_vertical_space(1)

st.markdown(
    f"""<p class="link" style='text-align:center;'>Built by <a href="https://sutardjik.github.io/" target="_blank">&#x4b;&#x61;&#x72;&#x65;&#x6e;
            &#x53;&#x75;&#x74;&#x61;&#x72;&#x64;&#x6a;&#x69;</a></p>""",
    unsafe_allow_html=True,
)

add_vertical_space(1)

st.markdown(
    "<sup>1 </sup>“Tools of the Trade: POPULATION PYRAMIDS,” Pennsylvania Department of Health, accessed February 17, 2023, https://www.health.pa.gov/topics/HealthStatistics/Statistical-Resources/UnderstandingHealthStats/Documents/Population_Pyramids.pdf.",
    unsafe_allow_html=True,
)

add_vertical_space(1)

st.markdown(
    "<sup>2 </sup>Jitender Saroha, “Types and Significance of Population Pyramids,” <em>World Wide Journal of Multidisciplinary Research and Development</em> 4, no. 4 (2018): 59-64. http://wwjmrd.com/upload/types-and-significance-of-population-pyramids_1523552342.pdf.",
    unsafe_allow_html=True,
)

add_vertical_space(1)

st.markdown(
    "<sup>3 </sup>Jill Rutherford and Gillian Williams, “Human Population Dynamics,” in <em>Environmental Systems and Societies: Course Companion</em>&nbsp; (United Kingdom: Oxford University Press, 2015), 355, http://ionma.org/share/ess/essbookcomplete.pdf.",
    unsafe_allow_html=True,
)

add_vertical_space(1)

st.markdown(
    "<sup>4 </sup>Rutherford and Williams, 364.",
    unsafe_allow_html=True,
)

st.sidebar.write(
    f"""<h1 style="font-weight: 300">Preface</h1><p class="link">
    PopPyraViz presents the population trends of six countries—the USA, Brazil, Germany, Kenya, India, and Japan—with population pyramids illustrated across 70 years. The annual population growth of the six countries from the same year interval is featured as line graphs. The population pyramids and population growth data are shown as interactive dataframes that can be downloaded as Excel spreadsheets and queried by column name. The annual population growth of the six countries is expressed as a multiple-line graph with the data displayed in an interactive dataframe, all examined in the <a href="/COUNTRY_COMPARISON" target="_self">Country Comparison</a> section.</p>
    """,
    unsafe_allow_html=True,
)
