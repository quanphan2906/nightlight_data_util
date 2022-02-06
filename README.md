# How to use this utility function?

1. Make sure the datasets fit into your computer's RAM. I suggest at least 8GB of RAM.

2. Download Anaconda:

    - For MacOS: https://www.datacamp.com/community/tutorials/installing-anaconda-mac-os-x
    - For Windows: https://www.datacamp.com/community/tutorials/installing-anaconda-windows#test. Remember to set PATH for your anaconda and python (instruction is in the web link).

3. Download this repo. Don't change anything in the `nightlight_data_util` subfolder.

4. In Anaconda Prompt or your command line, navigate to the directory of this repo, and type:

    ```
    conda env create --file environment.yml
    ```

    After the environment has been created, type:

    ```
    conda activate nightlight_data_util
    ```

5. Download the QGIS software (https://qgis.org/en/site/forusers/download.html).

6. Put the raster files into the `datasets` folder. If you decide to put the raster files into any other folder besides `datasets`, make sure to modify the example files accordingly.

7. Modify the example files to your usage, (there are instructions on how to do so in those files), and run the file:

    ```
    python name_of_the_file.py
    ```

8. The resulting csv file will be spitted out in the same directory as example files.
