'''Anthony Karnati
akarnat1@binghamton.edu
Assignment 4, Exercise 3
A55
Chelsea Montgomery'''

'''
Determines tax to be paid based
on marital status and income
Output to monitor:
      Amount to be paid in taxes(int)
Input from keyboard:
      Marital Status (Married or Single) (str)
      Income (int)
Tasks allocated to functions:
      taxCalculator()-determines tax to be paid (int)'''

'''
Determines how much to pay in taxes
using nested if/else functions based on
marital status and income'''
#param-maritalStatus(str)
#param-taxableIncome(int)
def taxCalculator(maritalStatus, taxableIncome):
      if maritalStatus=="Single":
            if taxableIncome>0 and taxableIncome<8000:
                  return (taxableIncome*.10)
            else:
                  if taxableIncome>8000 and taxableIncome<32000:
                        return ((taxableIncome*.15)+800)
                  else:
                        if taxableIncome>32000:
                              return ((taxableIncome*.25)+4400)
      elif maritalStatus=="Married":
            if taxableIncome>0 and taxableIncome<16000:
                  return (taxableIncome*.10)
            else:
                  if taxableIncome>16000 and taxableIncome<64000:
                        return ((taxableIncome*.15)+1600)
                  else:
                        if taxableIncome>64000:
                              return ((taxableIncome*.25)+8800)


      #in the end, the tax to be paid is output

def main():
      #Get the marital status and income of user
      print('''This program will allow someone to figure out
how much they have to pay in taxes based on their
marital status and income.''')
      maritalStatusStr=input("What is your marital status(Married/Single)? ")

      taxableIncome=round((float(input("What is your taxable income? "))),2)    
            
            #input taxable income as int
      if (maritalStatusStr=="Single" or maritalStatusStr=="Married") and taxableIncome>0:
       
            print (taxCalculator(maritalStatusStr, taxableIncome))
      else:
            print("bad input, try again")

main()

            

            
      
