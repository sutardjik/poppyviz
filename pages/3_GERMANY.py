import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_extras.dataframe_explorer import dataframe_explorer
import plotly_express as px
from streamlit_extras.add_vertical_space import add_vertical_space
import io


def set_favicon():
    favicon_path = "./favicon.ico"
    st.set_page_config(page_title="Germany · PanPop", page_icon=favicon_path)


set_favicon()
st.cache_data.clear()


@st.cache_data
def get_data():
    df = pd.read_excel("data/Germany-1950-2020.xlsx")
    return df


df = get_data()


@st.cache_data
def get_sum():
    df1 = pd.read_excel("data/Germany-Growth-1950-2020.xlsx")
    return df1


df1 = get_sum()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

st.markdown("<h1 style='text-align: center;'>Germany</h1>", unsafe_allow_html=True)

add_vertical_space(1)

year = st.slider(
    "Select a year to display Germany’s population pyramid.",
    min_value=1950,
    max_value=2020,
    value=1950,
)

st.markdown(f"<h4>Population Pyramid of Germany in {year}</h4>", unsafe_allow_html=True)
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
            -4000000,
            -3000000,
            -2000000,
            -1000000,
            0,
            1000000,
            2000000,
            3000000,
            4000000,
        ],
        ticktext=["4M", "3M", "2M", "1M", 0, "1M", "2M", "3M", "4M"],
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
    f"""<p style='text-align:center;'><a href="https://www.populationpyramid.net/germany/{year}/" target="_blank">View Data Source From {year}</a></p>""",
    unsafe_allow_html=True,
)

add_vertical_space(1)
st.write("---")
add_vertical_space(1)

st.markdown(
    "<h4>Germany’s Annual Population Growth Line Graph</h4>",
    unsafe_allow_html=True,
)

fig1 = px.line(
    df1,
    x="Year",
    y="Population",
    title="Annual Population Growth of Germany (1950 – 2020)",
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
    "<h4>Germany’s Population Pyramid Data (1950 – 2020)</h4>",
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
        df.to_excel(writer, sheet_name="Germany-Pyramid-1950-2020")
        writer.close()
        st.download_button(
            label="DOWNLOAD DATAFRAME",
            data=buffer,
            file_name="Germany-Pyramid-1950-2020.xlsx",
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
    "<h4>Germany’s Annual Population Growth Data (1950 – 2020)</h4>",
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
        df1.to_excel(writer, sheet_name="Germany-Growth-1950-2020")
        writer.close()
        st.download_button(
            label="DOWNLOAD DATAFRAME",
            data=buffer,
            file_name="Germany-Growth-1950-2020.xlsx",
            mime="application/vnd.ms-excel",
        )
    buffer.flush()
    buffer.close()

with col3:
    pass

st.sidebar.write(
    """
    <h1 style="font-weight: 300">Observations</h1><p>From the 1950s to the 1960s, Germany witnessed a remarkable period of post-war recovery characterized by significant population growth. As the nation rebuilt itself after the devastation of World War II, the economy began to flourish, and this newfound stability had a positive impact on the population. The country experienced what is commonly referred to as a “baby boom,” which involved a surge in births and subsequently led to a substantial increase in the overall population.

However, as the 1970s approached, Germany’s population growth rate began to slow down. This period, lasting until the 1990s, saw a decline in the fertility rate, resulting in a decrease in the number of births. Various factors contributed to this stabilization and decline, including changing societal attitudes towards family size, increased access to contraception, and the growing prominence of women in the workforce. Additionally, the country experienced emigration and a lower number of immigrants, which further contributed to the population stagnation or slight decline.

The reunification of Germany in the 1990s had a significant impact on the population. With the reunification of East and West Germany in 1990, the incorporation of the East German population led to a sudden increase in the overall population of Germany. This reunification event resulted in a notable one-time increase, altering the demographic landscape of the country.

Moving into the 2000s until 2020, Germany, like many other developed nations, faced the challenge of an aging population. The fertility rate remained relatively low, and as a consequence, the number of births declined in comparison to deaths. The combination of low birth rates and increased life expectancy contributed to a demographic shift characterized by a growing proportion of older individuals in the population. This trend brought about various social, economic, and healthcare implications as the country adapted to an aging society.</p>
    """,
    unsafe_allow_html=True,
)
