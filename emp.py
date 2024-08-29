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
        daily_wage : Daily wage of employee
        """
        daily_wage = daily_hr * wage_per_hr
        return daily_wage
            
    def check_part_time_wage(self, partime_hr, wage_per_hr):
        """
        Description:
        This fuction calculates part time wage using formula
        Parameter:
        self : Refers to the instance of the class EmployeeWage
        daily_hr: part time hours of work
        wage_per_hr: wage assigned per hour
        Return:
        daily_half_wage : Daily half wage of employee
        """
        daily_half_wage = partime_hr * wage_per_hr
        return daily_half_wage

    DAILY_WAGE = 160
    HALF_DAILY_WAGE = 80

    def calculate_wage(self, max_hrs, daily_hrs, part_time_hrs, wage_per_hr, total_days):
        """
        Description:
        This fuction calculates total wage using formula
        Parameter:
        self : Refers to the instance of the class EmployeeWage
        max_hrs: Maximum no of hours
        daily_hr: daily hours of work
        part_time_hrs: part time hours of work
        wage_per_hr: wage assigned per hour
        total_days: Total no of days
        Return:
        None
        """
        self.daily_wage_count = 0
        self.half_daily_count = 0
        self.absent_count = 0
        self.total_hours = 0

        for _ in range(total_days):
            if self.total_hours < max_hrs:
                choice = self.check_attend()
                if choice == 1:
                    self.daily_wage_count += 1
                    self.total_hours += daily_hrs
                elif choice == 2:
                    self.half_daily_count += 1
                    self.total_hours += part_time_hrs
                else:
                    self.absent_count += 1

        total_monthly_wage = (self.check_daily_wage(daily_hrs, wage_per_hr) * self.daily_wage_count +
                              self.check_part_time_wage(part_time_hrs, wage_per_hr) * self.half_daily_count)

        print("The Employee wage for hours and working days given below:")
        print(f"The Employee is part-time present for {self.half_daily_count} days")
        print(f"The Employee is present full time {self.daily_wage_count} days")
        print(f"The Employee absent for {self.absent_count} days")
        print(f"Total hours are {self.total_hours} hrs")
        print(f"Total Monthly wage is: {total_monthly_wage}")
        
   
def main():
    
    emp1 = EmployeeWage()
    daily_hours1 = 8
    part_time_hours1 = 4
    wage_per_hour1 = 20
    total_days1 = 20

    emp2 = EmployeeWage()
    daily_hours2 = 10
    part_time_hours2 = 5
    wage_per_hour2 = 25
    total_days2 = 22

    print("Employee Wage for Company 1:")
    emp1.calculate_wage(100, daily_hours1, part_time_hours1, wage_per_hour1, total_days1)
    print("\nEmployee Wage for Company 2:")
    emp2.calculate_wage(120, daily_hours2, part_time_hours2, wage_per_hour2, total_days2)


if __name__=='__main__':
    main()
