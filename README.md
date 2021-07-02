# Feature_selection_Cox_regression
Performing feature selection using Univariate Cox regression to select prognostic genes


This script will help you identify prognostic genes/features associated to survival.

INPUT FILE -- An excel file with, where each row represents an experiment or sample ID and the columns represent expression values of different genes. Make sure that the experiment or sample ID is in column 1 and the event and survival time are in column 2 and 3 respectively. Offcourse the script can be used on any type of data to identify prognostic features.

Ones the input file is ready, download the required R packages. The script imports them to python, to do so specify the path where the packages are downloaded.

Packages to download:

Python --> NumPy and Pandas.

R --> rpy2 -- helps import packages from R to Python, survival -- to run the Cox regression analysis and writexl -- to export the output to an excel file.

If you run into any trouble do let me know.
