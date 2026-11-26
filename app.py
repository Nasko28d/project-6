import streamlit as st
new_book = st.text_input("Въведете заглавие на книга")
if "books" not in st.session_state:    
    st.session_state.books = ["Хари Потър","Малкият принц","Хобит", "1984", "Под игото"]
st.session_state.books.append(new_book)
st.subheader("Търсене на книга")
search = st.text_input("Каква книга търсите?")
if st.button("Търси"):    
  found = False    
for book in st.session_state.books:        
  if search.lower() in book.lower():            
    st.success("Намерена книга: " + book)            
    found = True    
  if found == False:        
    st.warning("Няма такава книга!")
