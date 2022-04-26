def checkDeadline(List,today):
    mon_list = ['01','02','03','04','05','06','07','08','09','10','11','12']
    day_list = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
    Deadline = List[1]
    if type(Deadline) != str:
        return False
    elif Deadline[:4] != '2020':
        return -1
    elif not Deadline[4:6] in mon_list:
        return -2
    elif not Deadline[6:] in day_list:
        return -3
    elif int(Deadline) < int(today):
        return -4
    else:
        return True

val=checkDeadline( ['drsungwon', '20200718', 'A001', 1],'20200712')
print(val)

def checkPriority(List):
    num = List[3]
    if num == 1 or num == 2 or num == 3:
        return True
    else:
        return False

val1=checkPriority(['drsungwon', '20200718', 'A001', 'a'])
print(val1)
