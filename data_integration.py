

import petl as etl
import csv


le1 = etl.fromcsv('dataset_definitions.csv')
t1 = etl.cut(le1,'DS1 Blood Data 2017 icu Coded','DS3A CARDIAC data 2012 to 2016',
             'DS3B CARDIAC data 2017','DS4A JUL 2012 TO JUN 2015 Carpia database')
             

le2 = etl.fromcsv('variable_definitions.csv')
t2 = et2.cut(le2,'VAR.DEFINITION','NOTES','DATASET','CLIN.DSET.DESCR',
             'CLIN.DSET.NAME','PK','PATIENT.ID','DOB','SEX','HEIGHT','WEIGHT',
             'COMMENT','PK.ORIGIN','EVENT','CLOSEST.DATE','CLOSEST.DATE.EVENT',
             'HB','HCT','RCC','MCV','RETIC','PRBC','MAJOR.BLEED','ON.PUMP',
             'CS.URGENCY','DIAGNOSIS','TREATMENT','RAW.DATA')


le3 = etl.fromcsv('event_definitions.csv')
t3 = etl.cut(le3,'HOSP.DISCHARGE','FINAL.PATHOLOGY','POSTOPERATIVE.PATHOLOGY',
             'PAM.INITIAL.PATHOLOGY','PAM.TREATMENT','PAM.FOLLOW.UP.PATHOLOGY',
             'PAM.TREATMENT.CURTAIL','PREOPERATIVE.MORTALITY','PREOPERATIVE.PATHOLOGY',
             'PREOPERATIVE.PRBC','SURGERY','INTRAOPERATIVE.PRBC','POSTOPERATIVE.PRBC',
             'FINAL.PATHOLOGY','PAM.WAITLIST','PAM.ADMISSION','PAM.TREATMENT',
             'POSTOPERATIVE.PRBC')


mvs=t1.join(t1)
mvs=t1.join(t2)
mvs=t1.join(t3)             
vis=mvs.join(le4)
vis.tocsv('')
so_1st = etl.fromcsv('')
