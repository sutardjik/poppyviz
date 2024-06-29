import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_extras.dataframe_explorer import dataframe_explorer
import plotly_express as px
from streamlit_extras.add_vertical_space import add_vertical_space
import io


def set_favicon():
    favicon_path = "./favicon.ico"
    st.set_page_config(page_title="Kenya · PanPop", page_icon=favicon_path)


set_favicon()
st.cache_data.clear()


@st.cache_data
def get_data():
    df = pd.read_excel("data/Kenya-1950-2020.xlsx")
    return df


df = get_data()


@st.cache_data
def get_sum():
    df1 = pd.read_excel("data/Kenya-Growth-1950-2020.xlsx")
    return df1


df1 = get_sum()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

st.markdown("<h1 style='text-align: center;'>Kenya</h1>", unsafe_allow_html=True)

add_vertical_space(1)

year = st.slider(
    "Select a year to display Kenya’s population pyramid.",
    min_value=1950,
    max_value=2020,
    value=1950,
)

st.markdown(f"<h4>Population Pyramid of Kenya in {year}</h4>", unsafe_allow_html=True)
yr = df["Year"] == year
y = df[yr]["Age Group"]
x1 = df[yr]["Male Population"] * -1
x2 = df[yr]["Female Population"]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        y=y,
        x=x1,
        name="Male",
        orientation="h",
        showlegend=True,
        marker=dict(
            color="#B9CFDF",
            line=dict(color="#9CBCD2", width=1),
        ),
    )
)

fig.add_trace(
    go.Bar(
        y=y,
        x=x2,
        name="Female",
        orientation="h",
        showlegend=True,
        marker=dict(
            color="#EAD6D6",
            line=dict(color="#DDBBBB", width=1),
        ),
    )
)

fig.add_trace(
    go.Scatter(
        y=y,
        x=x1,
        name="Male",
        showlegend=False,
        mode="markers",
        marker_color="#81A9C5",
        marker_size=8,
    )
)

fig.add_trace(
    go.Scatter(
        y=y,
        x=x2,
        name="Female",
        showlegend=False,
        mode="markers",
        marker_color="#CFA0A0",
        marker_size=8,
    )
)

fig.update_layout(
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
    ),
    paper_bgcolor="#363845",
    plot_bgcolor="#363845",
    yaxis=dict(
        title="Age Group (Age)",
        title_font_size=15,
        tickfont_size=12,
        showgrid=False,
        titlefont_color="#FFFFFF",
        tickfont_color="#FFFFFF",
    ),
    xaxis=dict(
        title="Population (Millions)",
        title_font_size=15,
        tickfont_size=12,
        showgrid=False,
        titlefont_color="#FFFFFF",
        tickfont_color="#FFFFFF",
        tickvals=[
            -3500000,
            -3000000,
            -2500000,
            -2000000,
            -1500000,
            -1000000,
            -500000,
            0,
            500000,
            1000000,
            1500000,
            2000000,
            2500000,
            3000000,
            3500000,
        ],
        ticktext=[
            "3.5M",
            "3M",
            "2.5M",
            "2M",
            "1.5M",
            "1M",
            "0.5M",
            0,
            "0.5M",
            "1M",
            "1.5M",
            "2M",
            "2.5M",
            "3M",
            "3.5M",
        ],
    ),
    legend=dict(
        x=0,
        y=1,
        bgcolor="#363845",
        bordercolor="#363845",
    ),
    barmode="relative",
    bargap=0,
    bargroupgap=0,
    font=dict(family="FRAGMENT"),
)

st.plotly_chart(fig)

st.markdown(
    f"""<p style='text-align:center;'><a href="https://www.populationpyramid.net/kenya/{year}/" target="_blank">View Data Source From {year}</a></p>""",
    unsafe_allow_html=True,
)

add_vertical_space(1)
st.write("---")
add_vertical_space(1)

st.markdown(
    "<h4>Kenya’s Annual Population Growth Line Graph</h4>",
    unsafe_allow_html=True,
)

fig1 = px.line(
    df1,
    x="Year",
    y="Population",
    title="Annual Population Growth of Kenya (1950 – 2020)",
    markers=True,
)

fig1.update_layout(
    font_family="sans-serif",
    title_font_family="FRAGMENT",
    title_font_size=16,
    font=dict(family="FRAGMENT"),
    yaxis_title="Population (Millions)",
)

st.plotly_chart(fig1)

st.write("---")
add_vertical_space(1)

st.markdown(
    "<h4>Kenya’s Population Pyramid Data (1950 – 2020)</h4>",
    unsafe_allow_html=True,
)

filtered_df = dataframe_explorer(df)
s = filtered_df.style.format({"Year": lambda x: "{:.0f}".format(x)})
st.dataframe(s, use_container_width=True)

col1, col2, col3 = st.columns(3)
buffer = io.BytesIO()

with col1:
    pass

with col2:
    with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
        df.to_excel(writer, sheet_name="Kenya-Pyramid-1950-2020")
        writer.close()
        st.download_button(
            label="DOWNLOAD DATAFRAME",
            data=buffer,
            file_name="Kenya-Pyramid-1950-2020.xlsx",
            mime="application/vnd.ms-excel",
        )
    buffer.flush()
    buffer.close()

with col3:
    pass

add_vertical_space(1)
st.write("---")
add_vertical_space(1)

st.markdown(
    "<h4>Kenya’s Annual Population Growth Data (1950 – 2020)</h4>",
    unsafe_allow_html=True,
)

filtered_df1 = dataframe_explorer(df1)
s1 = filtered_df1.style.format({"Year": lambda x: "{:.0f}".format(x)})
st.dataframe(s1, use_container_width=True)

col1, col2, col3 = st.columns(3)
buffer = io.BytesIO()

with col1:
    pass

with col2:
    with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
        df1.to_excel(writer, sheet_name="Kenya-Growth-1950-2020")
        writer.close()
        st.download_button(
            label="DOWNLOAD DATAFRAME",
            data=buffer,
            file_name="Kenya-Growth-1950-2020.xlsx",
            mime="application/vnd.ms-excel",
        )
    buffer.flush()
    buffer.close()

with col3:
    pass

st.sidebar.write(
    """
    <h1 style="font-weight: 300">Observations</h1><p>Over the period from 1950 to 2020, Kenya’s population has experienced remarkable growth. The population has more than nine-folded, surging from approximately 5.8 million in 1950 to around 52 million in 2020. This demonstrates a significant expansion in the country’s population size.

Furthermore, the growth rate of Kenya’s population has displayed an upward trend. In the earlier years, the population growth rate was relatively lower, indicating a slower pace of increase. However, in recent decades, the growth rate has accelerated, reflecting a higher rate of population growth.

Despite the overall upward trajectory, Kenya’s population growth has not been entirely consistent. Fluctuations in the annual growth rate have been observed throughout the years. Some years witnessed higher population growth, while others experienced comparatively lower growth rates. These fluctuations can be attributed to a range of factors, including changes in birth rates, mortality rates, and migration patterns, which can influence population dynamics.

One interesting phenomenon is the population momentum observed in Kenya. This effect can be attributed to the large number of young individuals in the population. Even as birth rates decline, the population continues to grow due to the presence of a sizable young population entering reproductive age. This momentum is evident in the data, where there are instances of a decrease in the growth rate, but the population continues to increase steadily. 

These population trends in Kenya highlight the complex interplay between various factors influencing population growth. While the overall growth has been substantial, the fluctuations and momentum effect emphasize the need for a comprehensive understanding of demographic dynamics to make accurate projections and inform policy decisions.</p>
    """,
    unsafe_allow_html=True,
)
