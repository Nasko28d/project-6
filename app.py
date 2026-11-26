import streamlit as st
new_book = st.text_input("Въведете заглавие на книга")
if st.button("Добави книга"):
    if new_book != "":
        books.append(new_book)
        st.success("Книгата е добавена!")
    else:
        st.warning("Моля, въведете заглавие!")
if "books" not in st.session_state:    
st.session_state.books = ["Хари Потър","Малкият принц","Хобит", "1984", "Под игото"]
st.session_state.books.append(new_book)
st.subheader("📖 Всички книги")
for book in st.session_state.books:    
  st.write(book)
