from IPython.display import clear_output
import os
import time
!pip3 install pandas seaborn sympy beautifulsoup4 lxml pint scipy==1.1.0 numpy
!rm -rf ./ModSimPy
!rm -rf ./modsim.py
!git clone https://github.com/AllenDowney/ModSimPy.git
!cp "ModSimPy/code/modsim.py" .
clear_output()
print("Configured for ModSimPy. Restarting kernel.")
time.sleep(1)
os._exit(0)
