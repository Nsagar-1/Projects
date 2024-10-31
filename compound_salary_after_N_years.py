class Compound:
    def compoundSalary(self):
        numYears = int(input("Enter the number of years: "))
        rate = float(input("Enter the rate: "))
        currentAmount = 0

        for i in range(1, numYears + 1):
            if i == 1:
                year = "1st"
            elif i == 2:
                year = "2nd"
            elif i == 3:
                year = "3rd"
            else:
                year = f"{i}th"

            salary = float(input(f"Enter the salary at the end of the {year} year: "))
            # Calculate the amount with compounding
            amount = salary * (1 + rate / 100) ** (numYears - i)
            currentAmount += amount

        return f"The total amount will be: ${round(currentAmount, 2)} in {numYears} years"



comp = Compound()
total_amount = comp.compoundSalary()
print(total_amount)

     
    
    


