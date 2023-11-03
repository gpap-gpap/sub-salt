import subprocess
import sys
import os
import time
import streamlit as st

try:
    # replace "yourpackage" with the package you want to import
    import mantis

# This block executes only on the first run when your package isn't installed
except ModuleNotFoundError as e:
    sleep_time = 45
    dependency_warning = st.warning(
        f"Installing mantis dependencies, this takes {sleep_time} seconds."
    )
    subprocess.Popen(
        [
            f"{sys.executable} -m pip install git+https://gpap-gpap:{st.secrets['git_token']}@github.com/gpap-gpap/anisotroPY.git@dev-fAVO"
        ],
        shell=True,
    )
    # wait for subprocess to install package before running your actual code below
    time.sleep(sleep_time)
    dependency_warning.empty()

# Rest of your code goes here
import mantis.rock_physics as manRP
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("mantis.mantis_plotting")
well_in = {"Vp": 3000, "Vs": 1500, "Rho": 2.3}
model_in = {"Q_sls": 10, "Log_omega_ref": np.log10(35)}
inputs = {**well_in, **model_in}
model = manRP.models(identifier="sls", **inputs)
om = np.linspace(-3, 3, 100)

st.write(f"{model}")
fig, ax = plt.subplots()
ax.plot(om, model.Cij(omega=om))
st.pyplot(fig)
