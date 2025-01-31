import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset yang sudah dibersihkan dan dieksplorasi
customer_df = pd.read_csv("cleaned_customer_data.csv")
product_df = pd.read_csv("cleaned_merge_product_data.csv")
seller_df = pd.read_csv("cleaned_seller_city_data.csv")


# Sidebar
st.sidebar.title("E-Commerce Public Dataset")
menu = st.sidebar.radio("Pilih Analisis:", ["Produk Terjual", "Demografi Pelanggan", "Penjual per Daerah"])

# 1. Produk Paling Banyak dan Sedikit Terjual
if menu == "Produk Terjual":
    st.title("\U0001F4C8 Produk Paling Banyak dan Sedikit Terjual")
    product_sales = product_df.groupby(by="product_category_name")["product_id"].count().reset_index()
    product_sales = product_sales.rename(columns={"product_id" : "total_sold"})
    product_sales = product_sales.sort_values(by="total_sold", ascending=True)

    most_sold = product_sales.head(10)
    least_sold = product_sales.tail(10)


    fig1, ax1 = plt.subplots(figsize=(8, 8))
    sns.barplot(data=most_sold, x="total_sold", y="product_category_name", palette="Greens", ax=ax1)
    ax1.set_title("10 Produk Terlaris")
    ax1.set_xlabel("Jumlah Terjual")
    ax1.set_ylabel("Kategori Produk")
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots(figsize=(8, 6))
    sns.barplot(data=least_sold, x="total_sold", y="product_category_name", palette="Reds", ax=ax2)
    ax2.set_title("10 Produk Paling Tidak Laku")
    ax2.set_xlabel("Jumlah Terjual")
    ax2.set_ylabel("Kategori Produk")
    st.pyplot(fig2)


# 2. Demografi Pelanggan
elif menu == "Demografi Pelanggan":
    st.title("\U0001F465 Demografi Pelanggan")

    plt.figure(figsize=(15, 10))
    sns.barplot(
        data=customer_df.head(20),
        x="total_customer",
        y="customer_city",
        legend=False,
        palette = "Blues_r",
     )
    plt.xlabel("Jumlah Pelanggan")
    plt.ylabel("Asal Kota")
    plt.title("Kota Dengan Pelanggan Terbanyak")
    plt.show()

    st.pyplot(plt)

# 3. Penjual Terbanyak berdasarkan Daerah
elif menu == "Penjual per Daerah":
    st.title("\U0001F4CD Daerah dengan Penjual Terbanyak")

    fig, ax = plt.subplots(figsize=(20,10))

    plt.figure(figsize=(15, 10))
    sns.barplot(
        data=seller_df.head(20),
        x="total_seller",
        y="seller_city",
        legend=False,
        palette = "Greens_r",
     )
    plt.xlabel("Jumlah Seller")
    plt.ylabel("Asal Kota")
    plt.title("Kota Dengan Seller Terbanyak")


    st.pyplot(plt)

# Informasi tambahan
st.sidebar.markdown("---")
