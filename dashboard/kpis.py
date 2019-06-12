# coding=utf-8
import urllib.request
import csv
from datapackage import Package
import os

cwd = os.getcwd()
print(cwd)

source = 'http://donnees.ville.montreal.qc.ca/dataset/58fe2507-e1bd-48e6-8ae8-f4b993e5c870/resource/97d5e8e4-1bc5-4b49-ad33-a8336f7f37a2/download/indicateurs.csv'
archive = 'data/indicators/indicateurs.csv' #save it locally
kpis = {
  '2554': ('Operating costs for parks per hectare', 'Coûts d’exploitation relatifs aux parcs par hectare', 'parks'),
  '2510': ('Number of trips by public transport per capita', 'Nombre de déplacements en transport collectif par habitant', 'trips'),
  '2692': ('Library operating costs per capita', 'Coûts d’exploitation des bibliothèques par habitant', 'libs')
}

data = {}

urllib.request.urlretrieve(source, archive)

# sort out the kpis we are tracking
with open(archive) as file:
  reader = csv.reader(file)
  headers = next(reader) 
  for row in reader:
    if row[0] in kpis.keys():
      if row[0] not in data:
        data[row[0]] = []
        data[row[0]].append(headers)
      data[row[0]].append(row)

# write each tracked kpi to its own csv file
for kpid in kpis.keys():
  filename = 'data/kpis/' + kpis[kpid][-1] + '.csv'
  with open(filename, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data[kpid])

##
# Package KPIS (Subsets)
##
os.chdir(cwd + '/data/kpis')
kpiPackage = Package()
kpiPackage.infer('*.csv')
kpiPackage.descriptor['name'] = 'montreal-kpis'
kpiPackage.descriptor['license'] = 'https://creativecommons.org/publicdomain/zero/1.0/'
kpiPackage.commit()
kpiPackage.save(cwd + '/data/kpis/datapackage.json')
kpiPackage.save(cwd + '/data/kpis/datapackage.zip')

##
# Package Indicators (Master)
##
os.chdir(cwd + '/data/indicators')
indPackage = Package()
indPackage.basePath = cwd + '/data/indicators'
indPackage.infer(cwd + '/data/indicators/*.csv')
indPackage.descriptor['name'] = 'montreal-indicators'
indPackage.descriptor['license'] = 'https://creativecommons.org/publicdomain/zero/1.0/'
indPackage.commit()
indPackage.name = "montreal-city-indicators"
indPackage.save(cwd + '/data/indicators/datapackage.json')
indPackage.save(cwd + '/data/indicators/datapackage.zip')
