# Fitting propeller 

This is a script that creates a plot of the pull-up depending on the temperature of the propeller on the shaft.

## roject Description

When fitting a propeller to a shaft in a shipyard, it is important to have information about the minimum displacement at a given temperature. In most cases, such information is provided to the shipyard by the Shipowner, but there are also cases when such information is not available or incomplete. The script perform calculations and plot for following cases:

When we only have the displacement values given at two temperatures (usually 0 and 35 degrees celsius). In this case, a line is determined on the given points, in addition, minimum and maximum tolerance of the  pull-up can be given.The script creates a line graph. 
If you have a set of temperature and displacement as in point 1, but for the minimum and maximum pull-up, the script creates a line graph. 
Calculations made on the basis of the regulations of classification societies, this is the most difficult case, because it requires having this detailed data of the propeller and shaft. Classification societies on the basis of which calculations can be made in this script are: Bureau Veritas (BV), DNV, Lloyd's Register (LR) 
**NOTE: because of limited access to data, only the calculations for BV were tested on a real example.**

The program has a GUI made in Tkinter, graphs are supported by the matplotlib library (it is possible to save the graph to a graphic file), the result of the calculation can be saved to an xlsx file. Calculations performed can be saved and loaded from the list of saved projects if necessary. The data is stored in a local SQL database (sqllite3).

## Running the Project

To run the project in the terminal, you need to install python 3.9 or 3.10 and the following libraries:
```
- pandastable 
- pillow 
- matplotlib
- pandas
- openpyxl
```

Running the script in terminal: you need to be in the folder with the script and run it through the command:

```
python main.py
```

## Credits
The script used to handle window scrolling was created by JackTheEngineer and Serhiy1. [Link to github](https://gist.github.com/JackTheEngineer/81df334f3dcff09fd19e4169dd560c59)
