import streamlit as st

st.set_page_config(page_title="Spaza Books", layout="centered")

st.title("📘 Spaza Books")
st.subheader("Simple accounting for township entrepreneurs")

menu = st.sidebar.radio("Go to", ["Sales", "Expenses", "Credit Book", "Reports"])

if menu == "Sales":
    st.write("💸 Record your daily sales here")

elif menu == "Expenses":
    st.write("📦 Track your shop expenses")

elif menu == "Credit Book":
    st.write("📔 List of people who owe you")

elif menu == "Reports":
    st.write("📊 Profit Summary and PDF Export")
