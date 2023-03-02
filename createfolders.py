import pandas as pd
import os
import csv

df = pd.read_csv('input.csv')
folderNames = df['folder_name']

want_serialise = input("Do you want your folders to be numbered? Press 0 for no, press 1 for yes.") # True if want all folders to be numbered.
counter = 1

for name in folderNames:
	if int(want_serialise)==1:
		name = str(counter) + ". " + name
		counter += 1
	os.mkdir(name)

print("Success! All hail lord Fendy")
