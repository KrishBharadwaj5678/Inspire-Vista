import streamlit as st
import requests

st.set_page_config(
    page_title="Motivational Quotes Generator",
    page_icon="🎯",
    menu_items={
        "About":"""Discover an ever-growing library of motivational quotes tailored to empower and motivate you in every aspect of your life."""
    }
)

st.markdown("## :orange[Welcome to Your Daily Dose of Motivation !]")

st.write("<h5 style='line-height:28px;'>Feeling stuck or in need of a little inspiration? You've come to the right place! Our Motivational Quotes Generator is here to lift your spirits and help you seize the day.</h5>",unsafe_allow_html=True)

btn=st.button(":green[Motivate Me]")

if btn:
    try:
        data=requests.get("https://zenquotes.io/api/random")
        print(data.status_code)
        if(data.status_code==200):
            quote=data.json()[0]["q"]
            author=data.json()[0]["a"]
            st.write(f"<h4 style='text-align:center;line-height:29px;'>{quote}</h3>",unsafe_allow_html=True)
            st.write(f"<h5 style='text-align:right'>~ {author}</h4>",unsafe_allow_html=True)
    except:
        st.toast("Network Error",icon="🔌")

