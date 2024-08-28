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

def check_daily_wage(daily_hr, wage_per_hr):
    """
    Description:
    This fuction calculates daily wage using formula
    Parameter:
    daily_hr: hours of work
    wage_per_hr: wage assined per hour
    Return:
    None
    """
    daily_wage = daily_hr * wage_per_hr
    print(f"Employee is present full day.")
    print(f"The daily wage is: {daily_wage}")
    
def main():
    daily_hr = 8
    wage_per_hr = 20
    choice=check_attend()
    if(choice==1):
        check_daily_wage(daily_hr, wage_per_hr)

    else:
        daily_wage = 0
        print("Employee is Absent...")
        print(f"The daily wage is: {daily_wage}")

if __name__=='__main__':
    main()
