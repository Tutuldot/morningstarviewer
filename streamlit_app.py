

import streamlit as st
import supabase
import pandas as pd

# Initialize Supabase client
SUPABASE_URL = st.secrets["supabase"]["url"]
SUPABASE_KEY = st.secrets["supabase"]["key"]
supabase_client = supabase.create_client(SUPABASE_URL, SUPABASE_KEY)



def get_product_info(search_text):
    response = supabase_client.rpc("get_productinfo", {"search_text": search_text}).execute()
    return response.data if response.data else []

# Streamlit UI
st.title("🔍 Product Search")

search_text = st.text_input("Enter product name:")

if st.button("Search"):
    if search_text:
        results = get_product_info(search_text)

        # Clear previous results and show in structured format
        st.write("### Search Results:")
        if results:
            for product in results:
                st.markdown(f"""
                <div style="
                    border: 2px solid #ddd;
                    padding: 15px;
                    border-radius: 10px;
                    background-color: #f9f9f9;
                    margin-bottom: 10px;">
                    
                    Item Name: {product['item_name']} - SKU: {product['variant_code']}
                    Description: {product['description']}
                    
                    💰 Acquisition Cost:Php {product['acquisition_cost']}
                    📦 Computed Acquisition Cost:Php {product['computed_acquisition_cost']}
                    ⚖️ Computed Weight:Php {product['computed_weight']}

                    💲 Selling Prices:
                    Selling Price (SP): Php {product['computed_selling_price1']}
                    Tiktok Floor Price (FP): Php {product['computed_selling_price2']}
                    Tiktok ceiling Price (FC): Php {product['computed_selling_price3']}

               
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No products found.")
    else:
        st.error("Please enter a search term.")