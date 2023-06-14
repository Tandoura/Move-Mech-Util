# Move-Mech-Util
Custom FPS Mechanical Keyboard designed in mind for CSGO
The Keyboard runs on KMK documenttion on how to customize KMK to your needs can be found here http://kmkfw.io/docs/Getting_Started/
You will need to install micropython on whatever device you use as a micrcontroller. documentation for the KB2040 used is here https://learn.adafruit.com/adafruit-kb2040/circuitpython

the files for the case and plate can be found in the github for 3d printing.
the spacebar stl can be found here https://matt3o.com/mt3-row-5-spacebar-stls-all-of-them/ choose 3U External stabilizers
it is pretty simple to install just download the firmware folder unzip and copy the files to the circuit.py drive.
NOTE the drive wont show up if you plug it in after uploading the code. i have it set so the drive will only mount if a certain key is being pressed while being plugged in. it is currently set to space bar, this can be changed in the boot file. if you dont want this just comment out the boot file.
