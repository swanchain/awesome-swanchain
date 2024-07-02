import os
import random
import subprocess

import streamlit as st

accountname = os.getenv("ACCOUNTNAME")
workername = os.getenv("WORKERNAME",)
miner_url = os.getenv("MINER_URL")



def get_env_vars():
    st.write("#### AccountName")
    st.write(accountname)
    st.write("#### WorkerName")
    st.write(workername)
    st.write("#### Miner URL")
    st.write(miner_url)

def show_log():
    cmd = f"tail -n 30 ./aleo-miner.log"
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    logs = output.decode().replace('\n', '<br>')
    if error:
        st.write("Error while reading log file")
    else:
        st.write("## aleo-miner.log (last 30 lines)")
        st.markdown(f'<pre style="white-space: pre-wrap;">{logs}</pre>', unsafe_allow_html=True)

st.title("My Aloe Miner Dashboard")
get_env_vars()
show_log()