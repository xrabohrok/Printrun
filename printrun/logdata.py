

class logData:
        def __init__(self):
            self.records = []

        def startNewRecord(self):
            self.records.append({})

        def logFileName(self, filename):
            self.records[-1]["FileName"] = str(filename)

        def logStartTemp(self, startTemp):
            self.records[-1]["StartTemp"] = str(startTemp)

        def logPrintTemp(self, printTemp):
            self.records[-1]["PrintTemp"] = str(printTemp)

        def logPrintTime(self, printTime):
            self.records[-1]["PrintTime"] = str(printTime)
