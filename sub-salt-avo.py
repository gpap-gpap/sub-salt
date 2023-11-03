import subprocess
import sys
import os
import time
import streamlit as st

try:
    # replace "yourpackage" with the package you want to import
    import mantis as MAN

# This block executes only on the first run when your package isn't installed
except ModuleNotFoundError as e:
    sleep_time = 45
    dependency_warning = st.warning(
        f"Installing mantis dependencies, this takes {sleep_time} seconds."
    )
    subprocess.Popen(
        [
            f"{sys.executable} -m pip install git+https://gpap-gpap:${{st.secrets['git_token']}}@github.com/gpap-gpap/anisotroPY.git@no-data"
        ],
        shell=True,
    )
    # wait for subprocess to install package before running your actual code below
    time.sleep(sleep_time)
    dependency_warning.empty()

# Rest of your code goes here
import MAN.rock_physics as manRP
import MAN.rock_physics.fluid as manFL

st.write(f"{MAN.__version__}")
