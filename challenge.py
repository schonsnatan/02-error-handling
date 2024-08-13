CONSTANTE_BONUS = 1000

#Request the name for the user:
try:
    name = input("Type your name: ")
    if len(name)==0:
         raise ValueError("Please provide a name")
    elif name.isdigit():
         raise ValueError("Your name must have only letters")
    elif name.isspace():
         raise ValueError("Please type something")
    else:
         print("Olá,",name)
except ValueError as e:
    print(f"Error: {e}. Please take a look into the instructions.")
    exit()

#Request the salary:
try:
    sal = float(input("Informe seu salario: "))
    if sal<=0:
         raise ValueError("Inform a positive and non-zero value")
except ValueError as e:
     print(f"Error: {e}. Please take a look into the instructions.")
     exit()

#Request the bonus value:
try:
    bonus = float(input("Digite o seu bonus: "))
    if bonus < 0:
         raise ValueError("Inform a positive bonus.")
except ValueError as e:
     print(f"Error: {e}. Please take a look into the instructions.")
     exit()

#Print the informations for the user:
final_bonus = CONSTANTE_BONUS + sal * bonus
kpi = (sal + final_bonus) / 1000

print(f"Your KPI is: {kpi:.2f}")
print(f"{name}, your salary is ${sal:.2f} and your final bonus is ${final_bonus:.2f}")