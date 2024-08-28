import random

def check_attend():
    """
    Description:
    This fuction makes random choice from 0 or 1 or 2
    Parameter:
    None
    Return:
    choice : random choice from 0 or 1 or 2
    """
    choice = random.randint(0, 2)
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
    
def check_part_time_wage(partime_hr, wage_per_hr):
    """
    Description:
    This fuction calculates part time wage using formula
    Parameter:
    daily_hr: part time hours of work
    wage_per_hr: wage assined per hour
    Return:
    None
    """
    daily_half_wage = partime_hr * wage_per_hr
    print(f"Employee is present for half time.") 
    print(f"Part time wage is: {daily_half_wage}")

DAILY_HR = 8
WAGE_PER_HR = 20
PART_TIME_HR = 4
    
def main():

    choice=check_attend()
    
    match choice:
        case 0:
            daily_wage = 0
            print("Employee is Absent...")
            print(f"The daily wage is: {daily_wage}")
            
        case 1:
            check_daily_wage(DAILY_HR, WAGE_PER_HR)
            
        case 2:
            check_part_time_wage(PART_TIME_HR, WAGE_PER_HR)
        

if __name__=='__main__':
    main()
