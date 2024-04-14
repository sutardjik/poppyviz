import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_extras.dataframe_explorer import dataframe_explorer
import plotly_express as px
from streamlit_extras.add_vertical_space import add_vertical_space
import io


def set_favicon():
    favicon_path = "./favicon.ico"
    st.set_page_config(page_title="Japan · PanPop", page_icon=favicon_path)


set_favicon()
st.cache_data.clear()


@st.cache_data
def get_data():
    df = pd.read_excel("data/Japan-1950-2020.xlsx")
    return df


df = get_data()


@st.cache_data
def get_sum():
    df1 = pd.read_excel("data/Japan-Growth-1950-2020.xlsx")
    return df1


df1 = get_sum()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

st.markdown("<h1 style='text-align: center;'>Japan</h1>", unsafe_allow_html=True)

add_vertical_space(1)

year = st.slider(
    "Select a year to display Japan’s population pyramid.",
    min_value=1950,
    max_value=2020,
    value=1950,
)

st.markdown(f"<h4>Population Pyramid of Japan in {year}</h4>", unsafe_allow_html=True)
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
        tickvals=[-6000000, -4000000, -2000000, 0, 2000000, 4000000, 6000000],
        ticktext=["6M", "4M", "2M", 0, "2M", "4M", "6M"],
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
    f"""<p style='text-align:center;'><a href="https://www.populationpyramid.net/japan/{year}/" target="_blank">View Data Source From {year}</a></p>""",
    unsafe_allow_html=True,
)

st.write("---")

st.markdown(
    "<h4>Japan’s Annual Population Growth Line Graph</h4>",
    unsafe_allow_html=True,
)

fig1 = px.line(
    df1,
    x="Year",
    y="Population",
    title="Annual Population Growth of Japan (1950 – 2020)",
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
    "<h4>Japan’s Population Pyramid Data (1950 – 2020)</h4>",
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
        df.to_excel(writer, sheet_name="Japan-Pyramid-1950-2020")
        writer.close()
        st.download_button(
            label="DOWNLOAD DATAFRAME",
            data=buffer,
            file_name="Japan-Pyramid-1950-2020.xlsx",
            mime="application/vnd.ms-excel",
        )
    buffer.flush()
    buffer.close()

with col3:
    pass

st.write("---")

st.markdown(
    "<h4>Japan’s Annual Population Growth Data (1950 – 2020)</h4>",
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
        df1.to_excel(writer, sheet_name="Japan-Growth-1950-2020")
        writer.close()
        st.download_button(
            label="DOWNLOAD DATAFRAME",
            data=buffer,
            file_name="Japan-Growth-1950-2020.xlsx",
            mime="application/vnd.ms-excel",
        )
    buffer.flush()
    buffer.close()

with col3:
    pass

st.sidebar.write(
    """<h1 style="font-weight: 300">Observations</h1>
    <p>From 1950 to 2010, Japan’s population experienced significant growth, reaching its peak in 2010. However, since then, the population has been declining. This decline can be attributed to various factors. The age distribution of Japan’s population has undergone a significant transformation over the years. In the 1950s, the population pyramid suggested a relatively balanced age distribution, with a gradual increase in the younger age groups. However, as time passed, the population aged significantly, leading to a larger proportion of the population concentrated in the older age groups. This aging population poses a significant demographic challenge for Japan, as it impacts the labor force, healthcare systems, and social welfare programs.

The declining birth rates in Japan can be inferred from the decreasing population in the younger age groups, particularly among children aged 0-4 and 5-9. This trend indicates that Japanese couples are having fewer children, contributing to the overall shrinking population. The decreasing fertility rates further support this observation, as evidenced by the narrowing base of the population pyramid. This suggests that Japanese couples are opting to have fewer children, resulting in a reduced number of younger individuals.

One positive aspect of the changing population dynamics is the increasing life expectancy in Japan. The rising number of individuals in the older age groups, particularly those aged 60 and above, indicates that Japanese people are living longer. This increase in life expectancy is a testament to advancements in healthcare and lifestyle improvements. However, it also leads to a higher proportion of the population falling into the elderly category, placing additional strain on healthcare systems and social support structures.

Since 2010, Japan has been grappling with population decline. This decline can be attributed to a combination of factors, including low birth rates, declining fertility rates, and an aging population. As a result, Japan faces numerous challenges in the coming years, particularly concerning its economy, labor force, and social security systems. The shrinking population has implications for workforce productivity, economic growth, and the sustainability of pension and healthcare systems. Addressing these demographic shifts will require strategic policies and initiatives to encourage higher birth rates, support working-age individuals, and ensure the well-being of the aging population.
    </p>""",
    unsafe_allow_html=True,
)
