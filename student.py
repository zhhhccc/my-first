import random
word=['序号','姓名','性别','班级','学号','学院']

class ExamSys:
    def __init__(self):
        self.data = self.load_students()

    def load_students(self):
        f = open("人工智能编程语言学生名单.txt", 'r', encoding='utf-8')
        f.readline()
        lists = []
        dic = {}
        while True:
            line = f.readline()
            if not line:
                break
            dic[line.split('\t')[4]] = line.split('\t')
        return (dic)

    def find_student(self):
        print("请输入要查询的学号:",end="")
        try:
            num = input()
            for i in range(6):
                print(word[i]+":"+self.data[num][i],end=' ')
        except:
            print("未找到该学号对应的学生，请检查输入是否正确。")

    def random_roll_call(self):
        num=input("请输入要随机生成的人数:")
        a=1
        if int(num)>10:
            print("人数过多")
        elif int(num)<=0:
            print("请输入大于0的数")
        else:
            for i in random.sample(range(2001101, 2001111), int(num)):
                print(str(a) + '. ' + self.data[str(i)][1] + ' ' + self.data[str(i)][4])
                a += 1