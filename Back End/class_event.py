

class Event:

    
    def__init__(self, DATASET, NOTES, PK, PATIENT.ID, EVENT, CLOSEST.DATE, CLOSEST DATE EVENT,
                HB, HCT, RCC, MCV, RETIC, PRBC, WEIGHT, MAJOR BLEED, ON.PUMP, CS.URGENCY, DIAGNOSIS,
                TREATMENT, RAW.DATA):
        self.DATASET = DATASET
        self.NOTES = NOTES
        self.PK = PK
        self.PATIENT.ID = PATIENT.ID
        self.EVENT = EVENT
        self.CLOSEST.DATE = CLOSEST.DATE
        self.CLOSEST DATE EVENT = CLOSEST DATE EVENT
        self.HB = HB
        self.HCT = HCT
        self.RCC = RCC
        self.MCV = MCV
        self.RETIC = RETIC
        self.PRBC = PRBC
        self.WEIGHT = WEIGHT
        self.MAJOR BLEED = MAJOR BLEED
        self.ON.PUMP = ON.PUMP
        self.CS.URGENCY = CS.URGENCY
        self.DIAGNOSIS = DIAGNOSIS
        self.TREATMENT = TREATMENT
        self.RAW.DATA = RAW.DATA


          def myfunc(self):
    print("DATASET" + self.DATASET,
          "NOTES" + self.NOTES,
          "PK" + PK,
          "PATIENT.ID" + self.PATIENT.ID,
          "EVENT" + self.EVENT,
          "CLOSEST.DATE" + self.CLOSEST.DATE,
          "CLOSEST DATE EVENT" + self.CLOSEST DATE EVENT,
          "HB" + self.HB,
          "HCT" + self.HCT,
          "RCC" + self.RCC,
          "MCV" + self.MCV,
          "RETIC" + self.RETIC,
          "PRBC" + self.PRBC,
          "WEIGHT" + self.WEIGHT,
          "MAJOR BLEED" + self.MAJOR BLEED,
          "ON.PUMP" + self.ON.PUMP,
          "CS.URGENCY" + self.CS.URGENCY,
          "DIAGNOSIS" + self.DIAGNOSIS,
          "TREATMENT" + self.TREATMENT,
          "RAW.DATA" + self.RAW.DATA)

p1 = Event(DATASET, NOTES, PK, PATIENT.ID, EVENT, CLOSEST.DATE,CLOSEST DATE EVENT,
           HB, HCT, RCC, MCV, RETIC, PRBC, WEIGHT, MAJOR BLEED, PUMP, CS.URGENCY,
           , DIAGNOSIS, TREATMENT, RAW.DATA)
p1.myfunc()





