import streamlit as st
if "books" not in st.session_state:    
    st.session_state.books = ["Хари Потър","Малкият принц","Хобит", "1984", "Под игото"]
    st.session_state.books.append(new_book)
    st.subheader("📖 Всички книги")
    for book in st.session_state.books:    
      st.write(book)
