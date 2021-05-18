
from bottle import run , route , get , template
import petl as etl
import csv


@get('/CLIN.DSET.DESCR/DOB=<code>',method='GET')
def index(code):
    sost = etl.fromcsv('dataset_definitions.csv')
    s_fst = etl.cut(sost, 'DS1 Blood Data 2017 icu Coded','DS3A CARDIAC data 2012 to 2016'
                    ,'DS3B CARDIAC data 2017','DS4A JUL 2012 TO JUN 2015 Carpia database')
    t1=[]
    pstcd=str(code)
    for i in s_fst:
        if i[2]==pstcd:
            i2=i[:-1]
            t1.append(i2)
    return template('index',{"th":t1})


@get('/VAR.DEFINITION/DOB=<DOB>',method='GET')
def index(service):
    sost = etl.fromcsv('variable_definitions.csv')
    s_scnd = etl.cut(sost, 'VAR.DEFINITION','NOTES','DATASET','CLIN.DSET.DESCR',
             'CLIN.DSET.NAME','PK','PATIENT.ID','DOB','SEX','HEIGHT','WEIGHT',
             'COMMENT','PK.ORIGIN','EVENT','CLOSEST.DATE','CLOSEST.DATE.EVENT',
             'HB','HCT','RCC','MCV','RETIC','PRBC','MAJOR.BLEED','ON.PUMP',
             'CS.URGENCY','DIAGNOSIS','TREATMENT','RAW.DATA')
    t2=[]
    srvc=service
    for i in s_scnd:
        if i[0]==srvc:
            i2=i[1:]
            t2.append(i2)
    return template('index',{"th":t2})

@get('/EVENT/DOB=<DOB>',method='GET')
def index(service):
    sost = etl.fromcsv('event_definitions.csv')
    s_scnd = etl.cut(sost, 'HOSP.DISCHARGE','FINAL.PATHOLOGY','POSTOPERATIVE.PATHOLOGY',
             'PAM.INITIAL.PATHOLOGY','PAM.TREATMENT','PAM.FOLLOW.UP.PATHOLOGY',
             'PAM.TREATMENT.CURTAIL','PREOPERATIVE.MORTALITY','PREOPERATIVE.PATHOLOGY',
             'PREOPERATIVE.PRBC','SURGERY','INTRAOPERATIVE.PRBC','POSTOPERATIVE.PRBC',
             'FINAL.PATHOLOGY','PAM.WAITLIST','PAM.ADMISSION','PAM.TREATMENT',
             'POSTOPERATIVE.PRBC')
    t3=[]
    srvc=service
    for i in s_scnd:
        if i[0]==srvc:
            i2=i[1:]
            t3.append(i2)
    return template('index',{"th":t3})


if __name__=="__main__":
    run(debug=True, reloader=True)
