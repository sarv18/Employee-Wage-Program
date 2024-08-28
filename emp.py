import random

def check_attend():
    """
    Description:
    This fuction makes random choice from 0 or 1
    Parameter:
    None
    Return:
    choice : random choice from 0 or 1
    """
    choice = random.randint(0, 1)
    return choice

def main():

    choice=check_attend()
    if(choice==1):
        print("Employee is Present.. ")

    else:
        print("Employee is Absent...")

if __name__=='__main__':
    main()
