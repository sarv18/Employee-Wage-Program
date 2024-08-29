import random

def check_attend():
    """
    Description:
    This fuction makes random choice from 0 or 1 or 2 or 3
    Parameter:
    None
    Return:
    choice : random choice from 0 or 1 or 2 or 3
    """
    choice = random.randint(0, 3)
    return choice

def check_daily_wage(daily_hr, wage_per_hr):
    """
    Description:
    This fuction calculates daily wage using formula
    Parameter:
    daily_hr: hours of work
    wage_per_hr: wage assigned per hour
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
    wage_per_hr: wage assigned per hour
    Return:
    None
    """
    daily_half_wage = partime_hr * wage_per_hr
    print(f"Employee is present for half time.") 
    print(f"Part time wage is: {daily_half_wage}")

DAILY_WAGE = 160
HALF_DAILY_WAGE = 80

def check_monthly_wage():
    """
    Description:
    This fuction calculates monthly wage of employee using formula
    Parameter:
    None
    Return:
    None
    """
    daily_wage_count = 0
    half_daily_count = 0
    absent_count = 0

    for i in range(20):
        choice = check_attend()
        if choice == 1:
            daily_wage_count += 1

        elif choice == 2:
            half_daily_count += 1

        else:
            absent_count +=1

    total_monthly_wage = DAILY_WAGE * daily_wage_count + HALF_DAILY_WAGE * half_daily_count
    print(f"Employee is part time present for {half_daily_count} days")
    print(f"Emplyee is present full time for {daily_wage_count}")
    print(f"Employee absent count for {absent_count} days")
    print(f"Total monthly wage is = {total_monthly_wage}")
 
 
def check_for_hundred_hr_twenty_days():
    """
    Description:
    This fuction calculates monthly wage of employee for 100 hrs and 20 days
    Parameter:
    None
    Return:
    None
    """
    
    daily_wage_count = 0
    half_daily_count = 0
    absent_count=0
    total_hr=0

    for i in range(20):
        if(total_hr <= 100):
            choice = check_attend()
            if choice == 1:
                daily_wage_count += 1
                total_hr +=8

            elif choice == 2:
                half_daily_count += 1
                total_hr +=4

            else:
                absent_count +=1

    total_monthly_wage = DAILY_WAGE * daily_wage_count + HALF_DAILY_WAGE * half_daily_count
    print()
    print("The Employee wage for 100 hr and 20 working days given below:")
    
    print(f"The Total hours of work are {total_hr} hrs")
    print(f"Total monthly wage is = {total_monthly_wage}")   
    
    
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
        
        case 3:
            check_monthly_wage()
            check_for_hundred_hr_twenty_days()
            
        

if __name__=='__main__':
    main()
