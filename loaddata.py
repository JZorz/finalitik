# Full path and name to your csv file
filepath="C:\\Users\\SkyKnight\\finalitik\\SP2014_SPL.csv"
# Full path to your django project directory
djprohome="C:\\Users\\SkyKnight\\finalitik\\finalitik\\"

import sys,os
sys.path.append(djprohome)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from tab.models import Tab

import csv
import datetime

csvFile = open(filepath)
dataReader = csv.reader(csvFile, dialect='excel-tab', quotechar='"')

var = 0

for row in dataReader:
    if var != 0:
        tabela = Tab()
        tabela.groupname = row[3]
        tabela.konto = row[5]
        tabela.znesek = row[8]
        tabela.datum = datetime.datetime.today()
        tabela.save()
    else:
        var = 1