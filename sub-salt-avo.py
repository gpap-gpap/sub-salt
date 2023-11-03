import streamlit as st
import subprocess
import sys
import os
import time

try:
    # replace "yourpackage" with the package you want to import
    import mantis as MAN

# This block executes only on the first run when your package isn't installed
except ModuleNotFoundError as e:
    st.write(f"worked to module not found")
    subprocess.Popen(
        [
            f"{sys.executable} -m pip install git+https://${st.secrets['git_token']}@github.com/gpap-gpap/anisotroPY.git@dev-fAVO"
        ],
        shell=True,
    )
    # wait for subprocess to install package before running your actual code below
    time.sleep(90)

# Rest of your code goes here
import MAN.rock_physics as manRP
import MAN.rock_physics.fluid as manFL

st.write(f"{MAN.__version__}")
