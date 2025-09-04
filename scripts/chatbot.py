import pandas as pd

# Load clustered RFM data
rfm = pd.read_csv("data/rfm_with_clusters.csv")

# Define cluster meanings
cluster_meanings = {
    0: "Loyal high spenders: frequent orders, high monetary value",
    1: "Medium value customers: moderate frequency and spend",
    2: "New/low activity customers: recent first purchases, low frequency",
    3: "Churn risk / inactive: haven’t purchased for a long time"
}

print("Welcome to the Customer Segmentation Chatbot!")
print("Type a CustomerID to know their segment and description, or 'exit' to quit.")

while True:
    user_input = input("Enter CustomerID: ")
    if user_input.lower() == "exit":
        break
    try:
        customer_id = int(user_input)
        cluster = rfm.loc[rfm['CustomerID'] == customer_id, 'Cluster'].values[0]
        meaning = cluster_meanings.get(cluster, "No description available")
        print(f"Customer {customer_id} belongs to cluster {cluster}: {meaning}")
    except (IndexError, ValueError):
        print("CustomerID not found or invalid.")
