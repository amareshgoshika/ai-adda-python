from PIL import Image
import streamlit as st

# Create a container for the top bar
top_bar = st.container()

# Add a logo to the top bar
image = Image.open("images/logo.png")
top_bar.image(image, width=100)

# Add a title to the top bar
top_bar.title("My Webpage Title")

# Add some links to the top bar
top_bar.subheader("Links")
top_bar.write("* Home")
top_bar.write("* About")
top_bar.write("* Contact")

# Display the top bar in the sidebar
with st.sidebar():
    top_bar
