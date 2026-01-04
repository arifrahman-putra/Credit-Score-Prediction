import pandas as pd
import streamlit as st
import plotly.express as px

@st.cache_data
def load_predicted():
    return pd.read_csv("Dataset/predicted_test.csv")

df_predicted = load_predicted()

#Streamlit visualization
USER = "Username"
PASS = "12345"

month_map = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12
}


# check for login attempts
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# if client hasn't been logged in
if not st.session_state.logged_in:
    st.title("🔒 Login to Access Dashboard")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == USER and password == PASS:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Your username or password is incorrect.")


else:
    st.success("✅ You are logged in, welcome to the dashboard.")
    st.header("Credit Score classification dashboard")

    # Display overall prediction data
    st.subheader("📋 Predictions Table")
    st.dataframe(df_predicted )


    # predicted Credit Score Distribution
    st.subheader("📊️ Credit Score distribution")
    uniqe_CS = df_predicted["Credit_Score"].unique() # get unique names
    CS_dist_dict = {}
    CS_counts = []
    for CS in uniqe_CS:
        df_CS = df_predicted [df_predicted["Credit_Score"] == CS]
        CS_count = len(df_CS)
        CS_counts.append(CS_count)

    CS_dist_dict["Credit_Score"] = uniqe_CS
    CS_dist_dict["Credit_Score_count"] = CS_counts
    df_CS_dist = pd.DataFrame(CS_dist_dict)

    fig_1 = px.bar(
        df_CS_dist,
        x="Credit_Score",
        y="Credit_Score_count",

        color="Credit_Score",
        color_discrete_map={
            "Good": "green",
            "Standard": "yellow",
            "Poor": "red"
        },
        title="Credit Score overall distribution",
        labels={"Credit_Score": "Credit Score", "Credit_Score_count": "Count"}

    )
    st.plotly_chart(fig_1, use_container_width=True)


    # predicted Credit Score Distribution
    st.subheader("🧑‍💻 Customer Drill-down")

    customer_names = df_predicted["Name"].unique()
    selected_customer = st.selectbox("Choose Customer:", customer_names)


    df_name = df_predicted[df_predicted["Name"] == selected_customer]

    page_size = 20
    num_pages = (len(df_name) + page_size - 1) // page_size

    # paging slider
    if num_pages > 1:
        page = st.slider("Page", min_value=1, max_value=num_pages, value=1)
    else:
        page = 1


    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    df_name_page = df_name.iloc[start_idx:end_idx]
    df_name_page["Month_num"] = df_name_page["Month"].map(month_map)

    fig_2 = px.line(
        df_name_page,
        x="Month",
        y="Monthly_Balance",
        color="Credit_Score",
        color_discrete_map={
            "Good": "green",
            "Standard": "yellow",
            "Poor": "red"
        },
        title=f"Monthly Balance trend of {selected_customer}",
        markers = True
    )

    fig_2.update_layout(
        xaxis_title="Month",
        yaxis_title="Monthly Balance (USD)"
    )

    st.plotly_chart(fig_2, use_container_width=True)


    fig_3 = px.line(
        df_name_page,
        x="Month",
        y="Total_EMI_per_month",
        color="Credit_Score",
        color_discrete_map={
            "Good": "green",
            "Standard": "yellow",
            "Poor": "red"
        },
        title=f"Monthly Total EMI trend of {selected_customer}",
        markers=True
    )

    fig_3.update_layout(
        xaxis_title="Month",
        yaxis_title="Monthly Total EMI"
    )

    st.plotly_chart(fig_3, use_container_width=True)


    fig_4 = px.line(
        df_name_page,
        x="Month",
        y="Amount_invested_monthly",
        color="Credit_Score",
        color_discrete_map={
            "Good": "green",
            "Standard": "yellow",
            "Poor": "red"
        },
        title=f"Monthly investment of {selected_customer} (USD)",
        markers=True
    )

    fig_4.update_layout(
        xaxis_title="Month",
        yaxis_title="Monthly Investment"
    )

    st.plotly_chart(fig_4, use_container_width=True)