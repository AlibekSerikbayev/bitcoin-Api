import streamlit as st
import requests

# API orqali ma'lumot olish funksiyasi
def get_bitcoin_data(api_key):
    url = "https://api.coincap.io/v2/assets/bitcoin"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["data"]
    else:
        return None

# Streamlit interfeysi
st.title("Bitcoin Ma'lumotlari")
st.write("CoinCap API orqali real vaqt ma'lumotlarini ko'ring")

# API kalitni kiritish
api_key = st.text_input("API kalitingizni kiriting:")

if api_key:
    bitcoin_data = get_bitcoin_data(api_key)

    if bitcoin_data:
        # Ma'lumotlarni chiqarish
        st.write(f"Joriy narx (priceUsd): ${float(bitcoin_data['priceUsd']):,.2f}")
        st.write(f"Oxirgi 24 soatlik hajm (volumeUsd24Hr): ${float(bitcoin_data['volumeUsd24Hr']):,.2f}")
    else:
        st.error("Ma'lumotlarni olishda xatolik yuz berdi. API kalitni tekshiring.")
else:
    st.info("Ma'lumotlarni ko'rish uchun API kalitni kiriting.")
