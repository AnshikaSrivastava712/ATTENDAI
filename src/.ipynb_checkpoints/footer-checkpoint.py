{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "92daee7c-e51a-441a-929a-4d8a1bd75ffb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "\n",
    "\n",
    "def footer_home():\n",
    "    logo_url = \"https://i.ibb.co/4r5X1FY/apnacollege.png\"\n",
    "    \n",
    "    st.markdown(f\"\"\"\n",
    "        <div style=\"margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center\">\n",
    "        <p style=\"font-weight:bold; color:white;\"> Created with ❤️ by </p>  \n",
    "        <img src='{logo_url}' style='max-height:25px' />\n",
    "        </div>\n",
    "                \n",
    "                \"\"\", unsafe_allow_html=True)\n",
    "\n",
    "\n",
    "def footer_dashboard():\n",
    "    logo_url = \"https://i.ibb.co/4r5X1FY/apnacollege.png\"\n",
    "    \n",
    "    st.markdown(f\"\"\"\n",
    "        <div style=\"margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center\">\n",
    "        <p style=\"font-weight:bold; color:black;\"> Created with ❤️ by </p>  \n",
    "        <img src='{logo_url}' style='max-height:25px' />\n",
    "        </div>\n",
    "                \n",
    "                \"\"\", unsafe_allow_html=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:.conda-jupyter_env]",
   "language": "python",
   "name": "conda-env-.conda-jupyter_env-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
