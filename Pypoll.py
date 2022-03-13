import csv 
import os

file_to_load = os.path.join("Resources", "election_results.csv") 

file_to_save = os.path.join("analysis","election_analysis.txt")

#open the election results and read the file 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

with open(file_to_save ,'w') as txt_file: 
    txt_file.write("Counties in the Election\n------------\nArapahoe\nDenver\nJefferson")
   
   

