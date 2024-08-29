import random

class EmployeeWage:
    
    def __init__(self):
        self.daily_wage_count = 0
        self.half_daily_count = 0
        self.bsent_count = 0
        
    def check_attend(self):
        """
        Description:
        This fuction makes random choice from 0 or 1 or 2 or 3
        Parameter:
        self : Refers to the instance of the class EmployeeWage
        Return:
        choice : random choice from 0 or 1 or 2 or 3
        """
        choice = random.randint(0, 3)
        return choice

    def check_daily_wage(self, daily_hr, wage_per_hr):
        """
        Description:
        This fuction calculates daily wage using formula
        Parameter:
        self : Refers to the instance of the class EmployeeWage
        daily_hr: hours of work
        wage_per_hr: wage assigned per hour
        Return:
        None
        """
        daily_wage = daily_hr * wage_per_hr
        print(f"Employee is present full day.")
        print(f"The daily wage is: {daily_wage}")
        
    def check_part_time_wage(self, partime_hr, wage_per_hr):
        """
        Description:
        This fuction calculates part time wage using formula
        Parameter:
        self : Refers to the instance of the class EmployeeWage
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

    def check_monthly_wage(self):
        """
        Description:
        This fuction calculates monthly wage of employee using formula
        Parameter:
        self : Refers to the instance of the class EmployeeWage
        Return:
        None
        """
        daily_wage_count = 0
        half_daily_count = 0
        absent_count = 0

        for i in range(20):
            choice = self.check_attend()
            if choice == 1:
                daily_wage_count += 1

            elif choice == 2:
                half_daily_count += 1

            else:
                absent_count +=1

        total_monthly_wage = self.DAILY_WAGE * daily_wage_count + self.HALF_DAILY_WAGE * half_daily_count
        print(f"Employee is part time present for {half_daily_count} days")
        print(f"Emplyee is present full time for {daily_wage_count}")
        print(f"Employee absent count for {absent_count} days")
        print(f"Total monthly wage is = {total_monthly_wage}")
    
    
    def check_for_hundred_hr_twenty_days(self):
        """
        Description:
        This fuction calculates monthly wage of employee for 100 hrs and 20 days
        Parameter:
        self : Refers to the instance of the class EmployeeWage
        Return:
        None
        """
        
        daily_wage_count = 0
        half_daily_count = 0
        absent_count=0
        total_hr=0

        for i in range(20):
            if(total_hr <= 100):
                choice = self.check_attend()
                if choice == 1:
                    daily_wage_count += 1
                    total_hr +=8

                elif choice == 2:
                    half_daily_count += 1
                    total_hr +=4

                else:
                    absent_count +=1

        total_monthly_wage = self.DAILY_WAGE * daily_wage_count + self.HALF_DAILY_WAGE * half_daily_count
        print()
        print("The Employee wage for 100 hr and 20 working days given below:")
        
        print(f"The Total hours of work are {total_hr} hrs")
        print(f"Total monthly wage is = {total_monthly_wage}")   
        
    
DAILY_HR = 8
WAGE_PER_HR = 20
PART_TIME_HR = 4
   
def main():
    
    emp = EmployeeWage()
    
    choice = emp.check_attend()
    
    match choice:
        case 0:
            daily_wage = 0
            print("Employee is Absent...")
            print(f"The daily wage is: {daily_wage}")
            
        case 1:
            emp.check_daily_wage(DAILY_HR, WAGE_PER_HR)
            
        case 2:
            emp.check_part_time_wage(PART_TIME_HR, WAGE_PER_HR)            
        
        case 3:
            emp.check_monthly_wage()
            emp.check_for_hundred_hr_twenty_days()
            
        

if __name__=='__main__':
    main()
