import streamlit as st
import pandas as pd
import os
from datetime import datetime, date , timedelta
import requests



# 🌙 Ramadan Theme Setup
st.set_page_config(page_title="Ramadan Mubarak 🌙", page_icon="🌙", layout="centered")

# 📌 CSV File for Storing Messages
CSV_FILE = "user_data.csv"

# 📌 Function to Save Data to CSV
def save_to_csv(name, email, message):
    new_data = pd.DataFrame([[name, email, message]], columns=["Name", "Email", "Message"])
    if os.path.exists(CSV_FILE):
        old_data = pd.read_csv(CSV_FILE)
        final_data = pd.concat([old_data, new_data], ignore_index=True)
    else:
        final_data = new_data
    final_data.to_csv(CSV_FILE, index=False)

# 🎉 Ramadan Greeting
st.title("🌙 Ramadan Mubarak!")
st.subheader("May this holy month bring you peace, happiness, and endless blessings! 🕌✨")

# # 📅 Countdown to Eid
# # Eid-ul-Fitr 2025 expected date
# eid_date = today + timedelta(days=30)

# # Aaj ki date
# today = date.today()

# # Countdown calculation
# days_left = (eid_date - today).days


# st.info(f"Only {days_left} days left until Eid-ul-Fitr! 🎉")



# Aaj ki date
today = date.today()

# Eid-ul-Fitr ki tareekh (30 din baad)
eid_date = today + timedelta(days=23)

# Countdown calculation
days_left = (eid_date - today).days

import streamlit as st
st.info(f"Only {days_left} days left until Eid-ul-Fitr! 🎉")

st.subheader("🌅 Sehri & Iftar Timings (Karachi, Pakistan)")

def get_sehri_iftar():
    city = "Karachi"
    country = "Pakistan"
    response = requests.get(f"https://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2")
    data = response.json()

    sehri_time = data["data"]["timings"]["Fajr"]
    iftar_time = data["data"]["timings"]["Maghrib"]

    return sehri_time, iftar_time

sehri_time, iftar_time = get_sehri_iftar()
st.markdown(f"**🌙 Sehri:** `{sehri_time}`")
st.markdown(f"**🌆 Iftar:** `{iftar_time}`")

# 🇦🇪 Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Daily Dua", "Contact"])

# 📌 Home Page Content
if page == "Home":
    st.subheader("Welcome to the Ramadan Web App! 🌟")
    st.write("This interactive web app is built using **Streamlit** to enhance your Ramadan experience.")

    name = st.text_input("Enter your name:", "")
    if name:
        st.success(f"As-salamu alaykum, {name}! May this Ramadan bring you barakah and peace. 🤲")

    if st.button("Save My Name"):
        save_to_csv(name, "", "")
        st.success("✅ Your name has been saved! Ramadan Mubarak!")

# 📚 Daily Ramadan Dua
elif page == "Daily Dua":
    st.subheader("Today's Special Dua 🤲")
    daily_duas = [
        "اللهم بلغنا رمضان وبارك لنا فيه",  # O Allah, let us reach Ramadan and bless us in it.
        "اللهم إنك عفو تحب العفو فاعف عنا",  # O Allah, You are Forgiving and love forgiveness, so forgive us.
        "اللهم تقبل منا صيامنا وقيامنا",  # O Allah, accept our fasting and prayers.
        "اللهم اجعلنا من عتقائك من النار",  # O Allah, make us among those freed from Hellfire.
    ]
    st.write(f"**Dua:** {daily_duas[today.day % len(daily_duas)]}")
    st.write("Recite this dua with sincerity, and may Allah accept our prayers. Ameen! ❤️")

# 💎 Contact Page
elif page == "Contact":
    st.subheader("Send Us Your Ramadan Wishes! 💌")
    email = st.text_input("Your Email:", "")
    message = st.text_area("Your Message:", "")

    if st.button("Send Message"):
        save_to_csv("", email, message)
        st.success("✅ Your message has been received! JazakAllah Khair!")

# 🌟 Footer
st.write("---")
st.write("Made with ❤️ in Ramadan | May Allah accept our deeds. 🤲")
