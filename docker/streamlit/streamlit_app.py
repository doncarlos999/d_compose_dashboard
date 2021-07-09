import streamlit as st
from requests import get

def main():
    st.title("Test page")

    menu = ["Home"]
    choice = st.sidebar.selectbox("Home",menu)

    if choice == "Home":
        st.subheader("Home")
        ip = get('https://api.ipify.org').text
        st.markdown(f"http://{ip}:79")

if __name__ == '__main__':
	main()
