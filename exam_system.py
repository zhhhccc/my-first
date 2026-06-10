import os

def generate_admission_tickets(list):
    try:
        os.mkdir("准考证")
    except:
        pass
    os.chdir("准考证")
    for i in range(1,11):
        m=open(f"{i:>2}.txt",'w')
        m.write(list[i-1])
