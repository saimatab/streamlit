# Customer Segmentation Chatbot

This project segments customers using RFM analysis and KMeans clustering, then provides a chatbot interface (CLI or Streamlit) to query customers by ID and get cluster info.

## Folder Structure
- data/: contains dataset and cluster results
- notebooks/: Jupyter notebooks for analysis
- scripts/: training and chatbot scripts
- streamlit_app/: optional Streamlit UI

## Usage
1. Place OnlineRetail.xlsx in data/
2. Run `python scripts/train_rfm_model.py` to generate clusters
3. Run `python scripts/chatbot.py` for CLI chatbot
4. Or run `streamlit run streamlit_app/app.py` for browser chatbot
