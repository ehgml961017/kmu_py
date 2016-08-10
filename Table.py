from tkinter import *
#-*-UTF-8-*-
from Student import *
import pickle

win = Tk()
win.title("학생기록부")
#win.geometry("600x400")


mainStudent = Student()

def add():
    statusEntry.delete(1.0,END)
    name = nameEntry.get().rstrip().lstrip()
    for x in mainStudent.studentList:
        if name == x[1] :
            statusEntry.insert(END, "이미 존재하는 이름입니다.")
            return
    if name =='':
        statusEntry.insert(END, "이름을 입력해주세요. 공백은 이름이 될 수 없습니다.")
        return
    try:
        score = float(scoreEntry.get())
        mainStudent.add(nameEntry.get(), scoreEntry.get())
        nameEntry.delete(0,END)
        scoreEntry.delete(0,END)
        statusEntry.insert(END, "학생을 기록부에 등록하였습니다.")
        printList()
    except:
        statusEntry.insert(END,"숫자를 입력해주세요")

def dele():
    statusEntry.delete(1.0,END)
    try:
        tmpnum = int(numberEntry.get())
        for x in mainStudent.studentList :
            if tmpnum == x[0]:
                mainStudent.studentList.remove(x)
                statusEntry.insert(END, "delete")
                printList()
                return
        statusEntry.insert(END,"존재하지 않는 사용자 입니다.")
        printList()
    except:
        statusEntry.insert(END, "숫자를 입력해주세요.")
    nameEntry.delete(1.0,END)
    scoreEntry.delete(1.0,END)
    numberEntry.delete(1.0,END)


def save():
    statusEntry.delete(1.0,END)
    mainStudent.saveData(fileNameEntry.get())
    statusEntry.insert(END,"파일을 저장했습니다.")
    dateEntry.delete(1.0, END)

def open():
    statusEntry.delete(1.0,END)
    mainStudent.loadData(fileNameEntry2.get())
    statusEntry.insert(END,"파일을 불러왔습니다.")
    printList()

def sortName():
    statusEntry.delete(1.0, END)
    mainStudent.sortName()
    printList()
    statusEntry.insert(END,"이름순으로 정렬하였습니다.")


def sortNumber():
    statusEntry.delete(1.0, END)
    mainStudent.sortNum()
    printList()
    statusEntry.insert(END,"번호순으로 정렬하였습니다.")

def ascendingScore():
    statusEntry.delete(1.0, END)
    mainStudent.ascendingScore()
    printList()
    statusEntry.insert(END,"오름차순으로 정렬하였습니다.")

def descendingScore():
    statusEntry.delete(1.0, END)
    mainStudent.descendingScore()
    printList()
    statusEntry.insert(END,"내림차순으로 정렬하였습니다.")

def printList():
    dateEntry.delete(1.0,END)
    dateEntry.insert(END, mainStudent.printList())





aBlock = Frame(win) #맨위
aBlock.grid(row=0, column=0, sticky=W)
bBlock = Frame(win) #가운데1
bBlock.grid(row=1, column=0, sticky=N)
cBlock = Frame(win) #가운데2
cBlock.grid(row=2, column=0, sticky=W)
dBlock = Frame(win) #맨밑
dBlock.grid(row=3, column=0, sticky=W)

aBlockLeft = Frame(aBlock)
aBlockLeft.grid(row=0, column=0, sticky=N)
aBlockRight = Frame(aBlock)
aBlockRight.grid(row=0, column=1, sticky=N)


Label(aBlockLeft, text="이름: ").grid(row=0, column=0, sticky=E) #이름창
nameEntry = Entry(aBlockLeft, width=20, bg="light green")
nameEntry.grid(row=0, column=1, stick=W)

Label(aBlockRight, text="점수: ").grid(row=0, column=0, sticky=E) #점수
scoreEntry = Entry(aBlockRight, width=7, bg="light green")
scoreEntry.grid(row=0, column=1, stick=W)

Label(aBlockRight, text="번호: ").grid(row=1, column=0, sticky=E) #번호
numberEntry = Entry(aBlockRight, width=5, bg="light green")
numberEntry.grid(row=1, column=1, stick=W)

Label(aBlockRight, text="파일이름: ").grid(row=2, column=0, sticky=E) #저장용 파일이름
fileNameEntry = Entry(aBlockRight, width=20, bg="light blue")
fileNameEntry.grid(row=2, column=1, stick=W)

Label(aBlockRight, text="파일이름: ").grid(row=3, column=0, sticky=E) #열기용 파일이름
fileNameEntry2 = Entry(aBlockRight, width=20, bg="light blue")
fileNameEntry2.grid(row=3, column=1, stick=W)

#버튼만들기
addButton = Button(aBlockRight, text="추가", width=5, command=add).grid(row=0, column=3) #추가
delButton = Button(aBlockRight, text="삭제", width=5, command=dele).grid(row=1, column=3) #삭제
saveButton = Button(aBlockRight, text="저장", width=5, command=save).grid(row=2, column=3) #저장
openButton = Button(aBlockRight, text="열기", width=5, command=open).grid(row=3, column=3) #열기

#버튼만들기2
numButton = Button(bBlock, text="번호순", width=5, command=sortNumber).grid(row=0, column=0) #번호순
nameButton = Button(bBlock, text="이름순", width=5, command=sortName).grid(row=0, column=1) #이름순
descendingButton = Button(bBlock, text="점수내림차순", width=15, command=descendingScore).grid(row=0, column=2) #점수내림차순
ascendingButton = Button(bBlock, text="점수오름차순", width=15, command=ascendingScore).grid(row=0, column=3) #점수오름차순

#데이터출력창
dateEntry = Text(cBlock, width=61, height=10, bg="light pink")
dateEntry.grid(row=0, column=0, sticky=N)

#상태출력창
statusEntry = Text(dBlock, width=61, height=1, bg="deep pink")
statusEntry.grid(row=0, column=0, sticky=N)

win.mainloop()
