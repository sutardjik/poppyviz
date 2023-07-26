import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_extras.dataframe_explorer import dataframe_explorer
import plotly_express as px
from streamlit_extras.add_vertical_space import add_vertical_space
import io


def set_favicon():
    favicon_path = "./favicon.ico"
    st.set_page_config(page_title="USA · PopPyraViz", page_icon=favicon_path)


set_favicon()
st.cache_data.clear()


@st.cache_data
def get_data():
    df = pd.read_excel("data/USA-1950-2020.xlsx")
    return df


df = get_data()


@st.cache_data
def get_sum():
    df1 = pd.read_excel("data/USA-Growth-1950-2020.xlsx")
    return df1


df1 = get_sum()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

st.markdown(
    "<h1 style='text-align: center;'>United States of America</h1>",
    unsafe_allow_html=True,
)

add_vertical_space(1)

year = st.slider(
    "Select a year to display USA’s population pyramid.",
    min_value=1950,
    max_value=2020,
    value=1950,
)

st.markdown(f"<h4>Population Pyramid of USA in {year}</h4>", unsafe_allow_html=True)
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
            -12000000,
            -9000000,
            -6000000,
            -3000000,
            0,
            3000000,
            6000000,
            9000000,
            12000000,
        ],
        ticktext=["12M", "9M", "6M", "3M", 0, "3M", "6M", "9M", "12M"],
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
    font=dict(family="adelle-sans"),
)
st.plotly_chart(fig)
st.markdown(
    f"""<p style='text-align:center;'><a href="https://www.populationpyramid.net/united-states-of-america/{year}/" target="_blank">View Data Source From {year}</a></p>""",
    unsafe_allow_html=True,
)

st.write("---")

st.markdown(
    "<h4>USA’s Annual Population Growth Line Graph</h4>",
    unsafe_allow_html=True,
)
fig1 = px.line(
    df1,
    x="Year",
    y="Population",
    title="Annual Population Growth of USA (1950 – 2020)",
    markers=True,
    height=500,
)
fig1.update_layout(
    font_family="sans-serif",
    title_font_family="adelle-sans",
    title_font_size=16,
    font=dict(family="adelle-sans"),
    yaxis_title="Population (Millions)",
)
st.plotly_chart(fig1)

st.write("---")

st.markdown(
    "<h4>USA’s Population Pyramid Data (1950 – 2020)</h4>",
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
        df.to_excel(writer, sheet_name="USA-Pyramid-1950-2020")
        writer.close()
        st.download_button(
            label="DOWNLOAD DATAFRAME",
            data=buffer,
            file_name="USA-Pyramid-1950-2020.xlsx",
            mime="application/vnd.ms-excel",
        )
    buffer.flush()
    buffer.close()
with col3:
    pass

st.write("---")

st.markdown(
    "<h4>USA’s Annual Population Growth Data (1950 – 2020)</h4>",
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
        df1.to_excel(writer, sheet_name="USA-Growth-1950-2020")
        writer.close()
        st.download_button(
            label="DOWNLOAD DATAFRAME",
            data=buffer,
            file_name="USA-Growth-1950-2020.xlsx",
            mime="application/vnd.ms-excel",
        )
    buffer.flush()
    buffer.close()
with col3:
    pass

st.sidebar.write(
    """
    <h1 style="font-weight: 300">Observations</h1><p>The population of the USA has experienced consistent growth over the past seven decades, with numbers increasing from around 148 million in 1950 to approximately 336 million in 2020. This indicates a significant expansion of the population over a span of 70 years. Analyzing the data by age brackets reveals notable trends in the age distribution. Over time, the population has shifted towards older age groups, indicating an aging population. This shift is evident in the increasing numbers found in higher age brackets, such as 65-69, 70-74, 75-79, and 80+.

Furthermore, the data highlights the influence of the baby boomer generation, a cohort characterized by a significant increase in birth rates following World War II. This generation is represented in higher numbers in age brackets that correspond to their birth years, including 55-59, 60-64, and 65-69. The baby boomers have had a long-term impact on the age structure of the population.

The data also suggests a decline in birth rates over the years, as seen by the decreasing numbers in lower age brackets, particularly in the 0-4 and 5-9 age groups. This decline signifies a decrease in the number of children in the overall population. On the other hand, there has been a significant increase in the population within higher age brackets, particularly the 80-84 and 85+ groups. This upward trend reflects improvements in healthcare, medical advancements, and increased life expectancy, resulting in a larger elderly population.

While the population has continued to grow, the rate of growth has shown signs of stabilization in recent years. This is indicated by the smaller increments between population counts in the later years compared to the earlier years. The data suggests a more stable and slower population growth rate in recent times.</p>
    """,
    unsafe_allow_html=True,
)
