import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#judul aplikasi
st.title('Streamlit Simple App')

#menambahkan navigasi sidebare
page= st.sidebar.radio("Pilih halaman", ["Dataset","Visualisasi"])

if page == "Dataset":
    st.header("Halaman Dataset")

    #baca file csv
    data = pd.read_csv("pddikti_example.csv")

    #tampilkan data di streamlit
    st.write(data)

elif page == "Visualisasi":
    st.header("Halaman Visualisasi")
    st.set_option('deprecation.showPyplotGlobalUse',False)

    #baca file csv
    data = pd.read_csv("pddikti_example.csv")

    #filter berdasarkan universitas
    selected_university = st.selectbox('Pilih Universitas', data['universitas'].unique())
    filtered_data= data[data['universitas'] == selected_university]

    #buat visualisasi
    plt.figure(figsize=(12,6))

    for prog_studi in filtered_data['program_studi'].unique():
        subset = filtered_data[filtered_data['program_studi'] == prog_studi]


        #urutkan data berdasarkan id dengan urutan menurun
        subset = subset.sort_values(by="id", ascending=False)

        plt.plot(subset['semester'],subset['jumlah'], label=prog_studi)

    plt.title(f"visualisasi data untuk{selected_university}")
    plt.xlabel('semester')
    plt.xticks(rotation=90)
    plt.ylabel('jumlah')
    plt.legend()

    st.pyplot()