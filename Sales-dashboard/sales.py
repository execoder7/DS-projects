import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Sales Dashboard", layout='wide')

@st.cache
def get_excel_data():
    df = pd.read_excel("supermarkt_sales.xlsx", skiprows=3, usecols="B:R")

    df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.hour

    # Hide streamlit styles

    hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
    st.markdown(hide_st_style,unsafe_allow_html=True)



    return df


df = get_excel_data()


# --------- Sidebar ---------

st.sidebar.header("Please filter here")
city = st.sidebar.multiselect(
    "Select the City:",
    options=df['City'].unique(),
    default=df['City'].unique()
    
)

cust_type = st.sidebar.multiselect(
    "Select the Customer Type:",
    options=df['Customer_type'].unique(),
    default=df['Customer_type'].unique()
    
)


gender = st.sidebar.multiselect(
    "Select the Gender:",
    options=df['Gender'].unique(),
    default=df['Gender'].unique()
    
)


df_selection = df.query(
    "City == @city & Customer_type == @cust_type & Gender == @gender"
)




# -------- Mainpage --------

st.title(":bar_chart: Sales Dashboard")
st.markdown("")

# Top KPI's

total_sales = int(df_selection['Total'].sum())
avg_rating = round(df_selection['Rating'].mean(), 1)
star_rating= ":star:" * int(round(avg_rating, 0))
avg_sales_by_transaction = round(df_selection['Total'].mean(), 2)

lft_col, mid_col, rt_col = st.columns(3)

with lft_col:
    st.subheader("Total Sales:")
    st.subheader(f"US ${total_sales:,}")
with mid_col:
    st.subheader("Average rating")
    st.subheader(f"{avg_rating} {star_rating}")
with rt_col:
    st.subheader("Average Sales by Transaction")
    st.subheader(f"US ${avg_sales_by_transaction}")
    
st.markdown("---")    


# Sales by product line [bar chart]

sales_by_prodline = (
    df_selection.groupby('Product line')["Total"].sum().sort_values(ascending=False)
)
fig_prod_sales = px.bar(
    sales_by_prodline,
    orientation='h',
    title="<b>Sales by Product Line</b>",
    template="plotly_white"
)
fig_prod_sales.update_layout(
    xaxis_title="Total",
    yaxis_title="Product Line"
    )


# Sales by hour

sales_by_hour = df.groupby("Hour")['Total'].sum().sort_values(ascending=False)

fig_sales_hour = px.bar(
    sales_by_hour,
    title="Sales by Hour",
    template="plotly_white"
)
fig_sales_hour.update_layout(
    xaxis = dict(tickmode="linear"),
    xaxis_title="Hour",
    yaxis_title="Sales"
)

# Displaying charts in the same row

lft1_col, rt1_col = st.columns(2)

lft1_col.plotly_chart(
    fig_prod_sales,
    use_container_width=True
)
    
rt1_col.plotly_chart(
    fig_sales_hour,
    use_container_width=True
)






