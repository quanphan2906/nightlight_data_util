# How to use this utility function?
1. Make sure the datasets fit into your computer's RAM. I suggest at least 8GB of RAM.
2. Make sure you have Python >= 3.7
3. Download the QGIS software (https://qgis.org/en/site/forusers/download.html) and the necessary python libraries (check requirements.txt).
4. Download this repo. Don't change anything in the ```nightlight_data_util``` subfolder.
5. Put the raster files into the ```datasets``` folder. If you decide to put the raster files into any other folder besides ```datasets```, make sure to modify the ```example.py``` file.
5. Modify the ```example.py``` to your usage, (there are instructions on how to do so in ```example.py```), and run it with Python.
6. The resulting csv file will be spitted out in the same directory as ```example.py```. Take the .csv file, move on with your project, and forget about this utility function. An example final .csv file can be found in ```nigeria_nightlight_data.csv```.

_Note 1_: After step 3, if you have already had a separate folder for your project, and would like to work from there, copy the nightlight_data_util folder and the example.ipynb there, and continue with step 4 and 5.

Happy coding!