class Student:
    #생성자
    def __init__(self):
        self.studentList=[]
        self.num=1

    def add(self, name, score):
        try:
            score = float(score)
            self.studentList.append([self.num, name, score])
            self.num+=1
        except:
            pass

    def printList(self):
        str=""
        for x in self.studentList :
            str += "%3d %-15s %.2f\n" %(x[0], x[1], x[2])

        return str

    def sortNum(self):
        self.studentList.sort(key = lambda  x : x[0])

    def sortName(self):
        self.studentList.sort(key = lambda  x : x[1].lower())


    def ascendingScore(self):
        self.studentList.sort(key = lambda  x : x[2])

    def descendingScore(self):
        self.studentList.sort(key = lambda  x : x[2], reverse=1)

    def saveData(self, fileName) :
        import pickle
        file = open(fileName+'.pkl', 'wb')
        pickle.dump(self.studentList, file)
        file.close()

    def loadData(self, fileName) :
        import pickle
        file = open(fileName+'.pkl', 'rb')
        self.studentList = pickle.load(file)
        file.close()