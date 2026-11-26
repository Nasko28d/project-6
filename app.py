import streamlit as st
if "books" not in st.session_state:
    st.session_state.books = ["Хари Потър", "Малкият принц", "Хобит", "1984", "Под игото"]
st.subheader("Добавяне на книга")
new_book = st.text_input("Въведете заглавие на книга")
if st.button("Добави"):
    if new_book.strip():  # Проверява дали не е празно
        st.session_state.books.append(new_book.strip())
        st.success(f"Книгата '{new_book}' е добавена!")
    else:
        st.warning("Моля, въведете заглавие на книга!")
st.subheader("Търсене на книга")
search = st.text_input("Каква книга търсите?")
if st.button("Търси"):
    found = False
    for book in st.session_state.books:
        if search.lower() in book.lower():
            st.success("Намерена книга: " + book)
            found = True
    if not found:
        st.warning("Няма такава книга!")
st.subheader("Изтриване на книга")
if len(st.session_state.books) > 0:
    selected_book = st.selectbox("Изберете книга:", st.session_state.books)
    if st.button("Изтрий"):
        st.session_state.books.remove(selected_book)
        st.success("Книгата е изтрита!")
        st.rerun()
else:
    st.info("Библиотеката е празна!")
