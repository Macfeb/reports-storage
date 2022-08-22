###########
#Imports
###########
import os			#For getting script's path
import sys 			#For reading arguments
import shutil 			#For copying files
from datetime import date 	#For getting date

###########
#Setup vars
###########
if len(sys.argv) >= 3:			#If 3rd argument exists, use it as date
	dateToCopy = sys.argv[3]
else:					#If there's not 3rd argument, use today's date
	dateToCopy = str(date.today())
reportType = sys.argv[1]
reportFileName = sys.argv[1] + "_" + dateToCopy + ".csv" #Build report's filename from arguments
reportPath = sys.argv[2]
scriptPath = os.path.dirname(os.path.abspath(__file__))

###########
#Execution
###########


print("Today's date:", dateToCopy)
print(reportFileName)
print(reportPath)
print(scriptPath)

pathToCopy = reportPath + dateToCopy + "/" + reportFileName
destination = scriptPath + "/reports/" + reportFileName 

print("Copy from: "+pathToCopy)
print("Copy to:"+destination)

shutil.copyfile(pathToCopy,destination)
