from student import ExamSys
from exam_system import generate_admission_tickets

a=ExamSys()
list=[]
def run():
    print("===== 学生信息与考场管理系统 ===== \n1. 查询学生信息 \n2. 随机点名 \n3. 生成考场安排表 \n4. 生成准考证文件 \n+--------------------------------------------------------------------------\n0. 退出系统 \n请输入功能编号：",end='')
    num=int(input())
    if num==1:
        a.find_student()
    elif num==2:
        a.random_roll_call()
    elif num==3:
        list.extend(a.generate_exam_arrangement())
    elif num==4:
        generate_admission_tickets(list)
    elif num==0:
        print("结束")

run()