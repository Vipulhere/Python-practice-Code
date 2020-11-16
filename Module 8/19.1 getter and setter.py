class employee:
    def __init__(self):
        self.job="None"
    def getjob(self):
        return self.job
    def setjob(self,job):
        self.job=job

bob=employee()
alexa=employee()
bob.setjob("Developer")
alexa.setjob("Designer")
print(bob.job)
print(alexa.job)