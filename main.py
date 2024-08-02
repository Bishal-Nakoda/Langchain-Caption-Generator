import streamlit as st
import langchain_helper

home, about = st.tabs(["Home", "About"])

with home:
    st.title('Image Caption Generator')

    caption = st.text_input("Pick a caption")
    if caption:
        response = langchain_helper.generate(caption)
        ans = response['text'].split('\n')

        st.header("Captions")
        for item in ans:
            if len(item)!=0:
                st.write(item)

with about:
        st.markdown(
        """
        ## About Caption Generator
        
        Welcome to the Caption Generator application! This tool is designed to help you create engaging and relevant captions for your images effortlessly. Whether you're a social media manager, a content creator, or just someone looking to add a creative touch to your photos, our Caption Generator has got you covered.
        
        """
    )