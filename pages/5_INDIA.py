import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_extras.dataframe_explorer import dataframe_explorer
import plotly_express as px
from streamlit_extras.add_vertical_space import add_vertical_space
import io


def set_favicon():
    favicon_path = "./favicon.ico"
    st.set_page_config(page_title="India · PopPyViz", page_icon=favicon_path)


set_favicon()


@st.cache_data
def get_data():
    df = pd.read_excel("data/India-1950-2020.xlsx")
    return df


df = get_data()


@st.cache_data
def get_sum():
    df1 = pd.read_excel("data/India-Growth-1950-2020.xlsx")
    return df1


df1 = get_sum()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

st.markdown("<h1 style='text-align: center;'>India</h1>", unsafe_allow_html=True)

add_vertical_space(1)

year = st.slider(
    "Select a year to display India’s population pyramid.",
    min_value=1950,
    max_value=2020,
    value=1950,
)

st.markdown(f"<h4>Population Pyramid of India in {year}</h4>", unsafe_allow_html=True)
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
            -60000000,
            -40000000,
            -20000000,
            0,
            20000000,
            40000000,
            60000000,
        ],
        ticktext=[
            "60M",
            "40M",
            "20M",
            0,
            "20M",
            "40M",
            "60M",
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
    font=dict(family="adelle-sans"),
)
st.plotly_chart(fig)
st.markdown(
    f"""<p style='text-align:center;'><a href="https://www.populationpyramid.net/india/{year}/" target="_blank">View Data Source From {year}</a></p>""",
    unsafe_allow_html=True,
)

st.write("---")

st.markdown(
    "<h4>India’s Annual Population Growth Line Graph</h4>",
    unsafe_allow_html=True,
)
fig1 = px.line(
    df1,
    x="Year",
    y="Population",
    title="Annual Population Growth of India (1950 – 2020)",
    markers=True,
)
fig1.update_layout(
    font_family="sans-serif",
    title_font_family="adelle-sans",
    title_font_size=16,
    font=dict(family="adelle-sans"),
    yaxis_title="Population (Billions)",
)
st.plotly_chart(fig1)

st.write("---")

st.markdown(
    "<h4>India’s Population Pyramid Data (1950 – 2020)</h4>",
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
        df.to_excel(writer, sheet_name="India-Pyramid-1950-2020")
        writer.close()
        st.download_button(
            label="DOWNLOAD DATAFRAME",
            data=buffer,
            file_name="India-Pyramid-1950-2020.xlsx",
            mime="application/vnd.ms-excel",
        )
    buffer.flush()
    buffer.close()
with col3:
    pass

st.write("---")

st.markdown(
    "<h4>India’s Annual Population Growth Data (1950 – 2020)</h4>",
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
        df1.to_excel(writer, sheet_name="India-Growth-1950-2020")
        writer.close()
        st.download_button(
            label="DOWNLOAD DATAFRAME",
            data=buffer,
            file_name="India-Growth-1950-2020.xlsx",
            mime="application/vnd.ms-excel",
        )
    buffer.flush()
    buffer.close()
with col3:
    pass

st.sidebar.write(
    """
    <h1 style="font-weight: 300">Observations</h1><p>The population of India has experienced consistent growth from 1950 to 2020, as indicated by the data. During this period, the total population of India has more than tripled, demonstrating a rapid growth rate. This growth has been accompanied by a shift in the age distribution of the population. The data provides age-wise population estimates for different years, highlighting the changing composition of different age groups.

One notable change in the age structure is the consistent increase in the population of older age groups. This trend suggests improvements in healthcare and life expectancy, leading to an aging population in recent years. The changing population figures across different age groups also offer insights into fertility and mortality rates. The decrease in the child population and the increase in older age groups may indicate declining fertility rates and improvements in life expectancy.

By analyzing the age distribution, it is also possible to estimate the potential dependency ratio. This ratio compares the working-age population to the dependent population, including children and the elderly. Understanding this ratio helps to grasp the potential burden on the working-age population in terms of supporting dependents.

Moreover, changes in population size and structure have important implications for planning and policy development in various sectors, such as healthcare, education, employment, and social security. Understanding population trends is crucial for formulating effective strategies to address the needs and challenges associated with a growing population. By considering the demographic shifts and anticipating future trends, policymakers can develop appropriate population policies and implement development initiatives to ensure the well-being and sustainability of the nation.</p>
    """,
    unsafe_allow_html=True,
)
