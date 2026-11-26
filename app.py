import streamlit as st
st.title("Моята библиотека")
books = [    "Хари Потър",    "Малкият принц",    "Хобит",    "1984",    "Под игото"]
st.subheader("Всички книги")
for book in books:    
  st.write("📖", book)
