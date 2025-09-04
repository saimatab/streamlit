import streamlit as st
import pandas as pd

rfm = pd.read_csv("data/rfm_with_clusters.csv")

cluster_meanings = {
    0: "Loyal high spenders: frequent orders, high monetary value",
    1: "Medium value customers: moderate frequency and spend",
    2: "New/low activity customers: recent first purchases, low frequency",
    3: "Churn risk / inactive: haven’t purchased for a long time"
}

st.title("Customer Segmentation Chatbot")

customer_id = st.text_input("Enter CustomerID:")

if customer_id:
    try:
        customer_id = int(customer_id)
        cluster = rfm.loc[rfm['CustomerID'] == customer_id, 'Cluster'].values[0]
        meaning = cluster_meanings.get(cluster, "No description available")
        st.success(f"Customer {customer_id} belongs to cluster {cluster}: {meaning}")
    except (IndexError, ValueError):
        st.error("CustomerID not found or invalid.")
