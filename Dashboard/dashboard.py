import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

customer_df = pd.read_csv("Dashboard/cleaned_customer_data.csv")
product_df = pd.read_csv("Dashboard/cleaned_merge_product_data.csv")
seller_df = pd.read_csv("Dashboard/cleaned_seller_city_data.csv")

st.sidebar.title("E-Commerce Public Dataset")
menu = st.sidebar.radio("Pilih Analisis:", ["Produk Terjual", "Demografi Pelanggan", "Penjual per Daerah"])

if menu == "Produk Terjual":
    st.title("\U0001F4C8 Produk Paling Banyak dan Sedikit Terjual")

    top_n = st.sidebar.slider("Pilih jumlah produk yang ingin ditampilkan:", min_value=5, max_value=20, value=10)

    product_sales = product_df.groupby("product_category_name")["product_id"].count().reset_index()
    product_sales = product_sales.rename(columns={"product_id": "total_sold"})
    product_sales = product_sales.sort_values(by="total_sold", ascending=False)

    most_sold = product_sales.head(top_n)
    least_sold = product_sales.tail(top_n)

    fig1, ax1 = plt.subplots(figsize=(8, 8))
    sns.barplot(data=most_sold, x="total_sold", y="product_category_name", palette="Greens", ax=ax1)
    ax1.set_title(f"{top_n} Produk Terlaris")
    ax1.set_xlabel("Jumlah Terjual")
    ax1.set_ylabel("Kategori Produk")
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots(figsize=(8, 6))
    sns.barplot(data=least_sold, x="total_sold", y="product_category_name", palette="Reds", ax=ax2)
    ax2.set_title(f"{top_n} Produk Paling Tidak Laku")
    ax2.set_xlabel("Jumlah Terjual")
    ax2.set_ylabel("Kategori Produk")
    st.pyplot(fig2)

elif menu == "Demografi Pelanggan":
    st.title("\U0001F465 Demografi Pelanggan")

    top_n = st.sidebar.slider("Pilih jumlah kota yang ingin ditampilkan:", min_value=5, max_value=20, value=10)

    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(
        data=customer_df.head(top_n),
        x="total_customer",
        y="customer_city",
        palette="Blues_r",
        ax=ax
    )
    ax.set_xlabel("Jumlah Pelanggan")
    ax.set_ylabel("Asal Kota")
    ax.set_title(f"{top_n} Kota Dengan Pelanggan Terbanyak")
    st.pyplot(fig)

elif menu == "Penjual per Daerah":
    st.title("\U0001F4CD Daerah dengan Penjual Terbanyak")

    top_n = st.sidebar.slider("Pilih jumlah kota yang ingin ditampilkan:", min_value=5, max_value=20, value=10)

    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(
        data=seller_df.head(top_n),
        x="total_seller",
        y="seller_city",
        palette="Greens_r",
        ax=ax
    )
    ax.set_xlabel("Jumlah Seller")
    ax.set_ylabel("Asal Kota")
    ax.set_title(f"{top_n} Kota Dengan Seller Terbanyak")
    st.pyplot(fig)

st.sidebar.markdown("---")