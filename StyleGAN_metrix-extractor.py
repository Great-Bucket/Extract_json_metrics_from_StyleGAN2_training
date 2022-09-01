# Extract FID metrics from StyleGAN2-ADA (PyTorch)
# Created by @ReedOBeirne, 2022
# Written with Python 3.9.12 for MAC
# Crawls thru a directory (and subdirectory) to find the metrics JSON file. Parses that, and writes to a file the requested fields.


import glob
import json
import datetime

# Path to directory containg the StyleGAN training outputs
myPath = '/YourPath-to-Metrics-files'

# creates a txt file to write the results to.
resultsTXT = open ('/Users/uername/Downloads/StyleGAN_Training_Results.txt', 'w') #rename and relocate this file, as you wish.

# Searches above path and subdirectories for this particular file
files = glob.glob(myPath + "/**/metric-fid50k_full.jsonl", recursive = True)

header='date and time | timestamp | fid50k_full | file path\n'
# print (header) | for testing (see below)
resultsTXT.write(header)

for file in files:

	with open(file, 'r') as json_file:
		json_list = list(json_file)

	for json_str in json_list:
		results_by_tick= json.loads(json_str)

		result_fid50k = results_by_tick['results']['fid50k_full']
		result_timestamp = results_by_tick['timestamp']
		result_datetime = datetime.datetime.fromtimestamp(result_timestamp)

		# outputs multiple versions of the date/time to be sure the right one is available.
		resultsTXT.write(str(result_datetime)+' | '+str(result_timestamp)+' | '+str(result_fid50k)+' | '+file+'\n')

		# for testing (see above)
		#print ('Delimited Results:')
		#print (result_datetime, " | ", result_timestamp, " | ", result_fid50k, " | ", file, "\n")
		#print(f'JSON Result: {results_by_tick}')
		#print ('\n---------------------------------\n')


resultsTXT.write('----------\nProgram execution date: '+ str(datetime.datetime.now()))
print ('done')


