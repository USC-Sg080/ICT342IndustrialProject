import csv
f = open ('ICT342IndustrialProject-main\Dataset Server\Dataset Definitions.csv') #reading the dataset definitons file 
csv_f = csv.reader(f)
data = []

for row in csv_f:
    data.append(row) # sorting the row data as indiviudal list
f.close()

print(data[1:]) #printing all the rows

def convert_row(row):
    return """<Dataset Definitons>
    <dataset>%s</dataset>
    <notes>%s</notes>
    <clin.dset.descr>%s</clin.dset.descr>
    <clin.dset.name>%s</clin.dset.name>
    <pk>%s</pk>
    <patient.id>%s</patient.id>
    <dob>%s</dob>
    <sex>%s</sex>
    <weight>%s</weight>
    <height>%s</height>
    <comment>%s</comment>
    <pk.origin>%s</pk.origin>
</Dataset Definitions>""" % (row[0], row[1], row[2], row[3],row[4], row[5],row[6], row[7], row[8], row[9], row[10], row[11] )

with open('dataset_definitions.xml', 'w' ) as f:
    f.write('\n'.join([convert_row (row) for row in data]))

    


    
