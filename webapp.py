import streamlit as st
from chat import get_response, bot_name


def main():

    st.set_page_config(
        page_title="Chatbot",
        page_icon=":robot:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title(f"{bot_name} 🤖")
    st.markdown("---")
    st.markdown("**Bienvenue !** Veuillez taper un message et appuyer sur le bouton *Envoyer* pour obtenir des informations sur le Paludisme. 💬🦟")
    

    user_input = st.text_input("Vous:", key="user_input")
    
    if st.button("Envoyer", key="send_button"):
        response, _ = get_response(user_input)
        st.text_area("Bot 🤖:", value=response, height=100, max_chars=None, key="chatbot_response")


        


if __name__ == '__main__':
    main()

