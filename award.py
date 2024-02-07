#from assignment 4 - error whilst creating it in line 29 - value 105 produces wrong error

# ask user time of event in minutes for swimming, cycling and running events

cycling = int(input("How long did your cycle ride take in minutes?: "))
swimming = int(input("How long did your swim take in minutes?: "))
running = int(input("How long did your run take in minutes?: "))

#calculate total time of triathalon
total = cycling + swimming + running

#print time in minutes for user
print("Your total triathalon time is "+ str(total) + " minutes!")

#logic section
#create a variable called award, which shall be used to display results

award = "result"

#if total is less than or equal to 100, award "Provisional Colours"
if(total <= 100):
    award = "Provincial Colours"

#if total is greater than or equal to 111, award "No award"
elif(total >= 111):
    award = "No award"

#if total time is between 100 and 105 minutes, award "Provincial Half Colours"
elif( (total >= 100) and (total < 105)): # both inequalities are incorrect. Should be > 100 to avoid contradicting stage 1 (but has no effect but of loop) however less than 105 shoudl be less than or equal to. Otherwise the 105 minute time is awarded no crtieria which is incorrect
    award = "Provincial Half Colours"

#remaining time is 106 to 110 minutes where we award Provincial Scroll
else:  
    award = "Provincial Scroll"

# print award
print("You have been awarded: " + award)
