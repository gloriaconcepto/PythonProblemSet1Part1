# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 11:15:52 2018

@author: mmk
"""
#my team partner name is Emmanuel Asiegbu
#"\033[34m log(x) = \033[0m"
#enter your annual salary
annual_salary = float(input("\033[34m Enter your annual salary \033[0m : "))
#enter the percent save
percent_save = float (input("\033[34m Enter the percent of your salary to save, as a decimal \033[0m :  "))
# enter the total cost of the house
total_house_cost = float(input("\033[34m Enter the cost of your dream home \033[0m :  "))
#  Enter the semi­annual raise
semi_annual_raise = float(input("\033[34m Enter the semi­annual raise, as a decimal \033[0m :  "))
#set the current saving to zero
current_saving = float(0)
#set the intial month to zero
month = 0
#calculate the monthly salary
month_salary = float(annual_salary / 12)
#portion save
portion_saved = float (percent_save * month_salary)
#portion down payment
portion_down_payment = float (total_house_cost * 0.25)
#rate of return  
rate_of_return = 0.04

#loop until current_saving is greater than portion_down_payment

while (current_saving < portion_down_payment):
    
       
        if (month == 0):
            current_saving += portion_saved
            
    
        else :
            #check if it is a multiply of six
             if(month % 6 ==0):
                 month_salary += (semi_annual_raise * month_salary)
                 portion_saved = float (percent_save * month_salary)
                 current_saving += portion_saved  + (current_saving * rate_of_return)/12 #+ (semi_annual_raise * month_salary )
                
             else :
                    current_saving += portion_saved  + (current_saving * rate_of_return)/12
                   
        month +=1       

    
        
print ("\033[34m Number of months \033[0m:" , month)  
           
