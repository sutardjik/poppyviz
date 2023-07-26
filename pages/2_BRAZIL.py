import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_extras.dataframe_explorer import dataframe_explorer
import plotly_express as px
from streamlit_extras.add_vertical_space import add_vertical_space
import io


def set_favicon():
    favicon_path = "./favicon.ico"
    st.set_page_config(page_title="Brazil · PopPyraViz", page_icon=favicon_path)


set_favicon()
st.cache_data.clear()


@st.cache_data
def get_data():
    df = pd.read_excel("data/Brazil-1950-2020.xlsx")
    return df


df = get_data()


@st.cache_data
def get_sum():
    df1 = pd.read_excel("data/Brazil-Growth-1950-2020.xlsx")
    return df1


df1 = get_sum()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

st.markdown(
    "<h1 style='text-align: center;'>Brazil</h1>",
    unsafe_allow_html=True,
)

add_vertical_space(1)

year = st.slider(
    "Select a year to display Brazil’s population pyramid.",
    min_value=1950,
    max_value=2020,
    value=1950,
)

st.markdown(f"<h4>Population Pyramid of Brazil in {year}</h4>", unsafe_allow_html=True)
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
            -10000000,
            -8000000,
            -6000000,
            -4000000,
            -2000000,
            0,
            2000000,
            4000000,
            6000000,
            8000000,
            10000000,
        ],
        ticktext=["10M", "8M", "6M", "4M", "2M", 0, "2M", "4M", "6M", "8M", "10M"],
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
    f"""<p style='text-align:center;'><a href="https://www.populationpyramid.net/brazil/{year}/" target="_blank">View Data Source From {year}</a></p>""",
    unsafe_allow_html=True,
)

st.write("---")

st.markdown(
    "<h4>Brazil’s Annual Population Growth Line Graph</h4>",
    unsafe_allow_html=True,
)
fig1 = px.line(
    df1,
    x="Year",
    y="Population",
    title="Annual Population Growth of Brazil (1950 – 2020)",
    markers=True,
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
    "<h4>Brazil’s Population Pyramid Data (1950 – 2020)</h4>",
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
        df.to_excel(writer, sheet_name="Brazil-Pyramid-1950-2020")
        writer.close()
        st.download_button(
            label="DOWNLOAD DATAFRAME",
            data=buffer,
            file_name="Brazil-Pyramid-1950-2020.xlsx",
            mime="application/vnd.ms-excel",
        )
    buffer.flush()
    buffer.close()
with col3:
    pass

st.write("---")

st.markdown(
    "<h4>Brazil’s Annual Population Growth Data (1950 – 2020)</h4>",
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
        df1.to_excel(writer, sheet_name="Brazil-Growth-1950-2020")
        writer.close()
        st.download_button(
            label="DOWNLOAD DATAFRAME",
            data=buffer,
            file_name="Brazil-Growth-1950-2020.xlsx",
            mime="application/vnd.ms-excel",
        )
    buffer.flush()
    buffer.close()
with col3:
    pass

st.sidebar.write(
    """
    <h1 style="font-weight: 300">Observations</h1><p>Brazil’s population has exhibited steady growth over the years, albeit with some fluctuations. Starting at around 54 million in 1950, the total population has expanded significantly, reaching approximately 214 million by 2020. While specific age groups have experienced variations, there has been a noticeable shift towards an aging population, characterized by a decrease in younger age groups and an increase in older age groups. This demographic change suggests the presence of factors contributing to an older population structure. The data also highlights periods of higher population growth, particularly during the 1960s to 1980s. This growth can be attributed to several factors, including elevated birth rates, advancements in healthcare, and social and economic development during those times. However, in more recent years, the pace of population growth appears to have slowed compared to previous decades. This deceleration could be attributed to factors such as declining fertility rates, improved access to family planning, and other demographic dynamics. 
    </p>
    """,
    unsafe_allow_html=True,
)
