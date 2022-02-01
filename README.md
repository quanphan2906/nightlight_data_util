# How to use this utility function?
1. Make sure the datasets fit into your computer's RAM. I suggest at least 8GB of RAM.
2. Download Anaconda. Create a virtual environment with Python >= 3.7 (I suggest using Python 3.9) by typing `conda install --name my_env python=3.9` in the command line.
3. In that environment, download pandas and qgis:
  ```
  conda install pandas
  conda install -c conda-forge qgis
  ```
4. Download the QGIS software (https://qgis.org/en/site/forusers/download.html).
5. Download this repo. Don't change anything in the ```nightlight_data_util``` subfolder.
6. Put the raster files into the ```datasets``` folder. If you decide to put the raster files into any other folder besides ```datasets```, make sure to modify the ```example.py``` file.
7. Modify the ```example.py``` to your usage, (there are instructions on how to do so in ```example.py```), and run it within the above conda environment (where you have downloaded pandas and qgis).
8. The resulting csv file will be spitted out in the same directory as ```example.py```. Take the .csv file, move on with your project, and forget about this utility function. An example final .csv file can be found in ```nigeria_nightlight_data.csv```.

_Note 1_: After step 5, if you have already had a separate folder for your project, and would like to work from there, copy the nightlight_data_util folder and the example.ipynb there, and continue with step 6.
_Note 2_: Step 2 and 3 show you how to set up an Anaconda enviroment through command line or Anaconda prompt. There are other ways to set up such an environment, including using the Anaconda Navigator (a GUI software that comes with Anaconda). You're text editors (like PyCharm) may support creating Anaconda environment without having to interact with the command line. Please consult Google for these methods.

Happy coding!
