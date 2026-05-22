{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9a966ef7-4059-47ed-bb72-1d3187ad2952",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "\n",
    "\n",
    "from supabase import create_client, Client\n",
    "\n",
    "supabase: Client = create_client(\n",
    "    st.secrets[\"SUPABASE_URL\"],\n",
    "    st.secrets[\"SUPABASE_KEY\"]\n",
    ")"
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
