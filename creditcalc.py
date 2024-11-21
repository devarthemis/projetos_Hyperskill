import math
import argparse
from calendar import month

# write your code here
# pr = float(input("Enter the loan  principal: "))
# s_calc = input("""What do you want to calculate?
# type "m" - for number of monthly payments,
# type "p" - for the monthly payment: """)
#
# if s_calc.lower() == "m":
#     pay = float(input("Enter the monthly payment: "))
#     mont = "month" if pr / pay == 1 else "months"
#     print(f"It will take {pr / pay:.0f} {mont} to repay the loan")
# elif s_calc.lower() == "p":
#     monthly = int(input("Enter the number of months: "))
#     pay = math.ceil(pr / monthly)
#     if pay * monthly  == pr:
#         print(f"Your monthly payment = {pay}")
#     else:
#         print(f"Your monthly payment = {pay} and the last payment = {pr - (monthly -1) * pay:.0f}.")

parser = argparse.ArgumentParser(prog="Calculadora de emprestimo")
parser.add_argument("--principal", type=float, help="Valor do empréstimo")
parser.add_argument("--payment", type=float, help="Pagamento mensal")
parser.add_argument("--periods", type=int, help="tempo para pagar")
parser.add_argument("--interest", type=float, help="juros")
parser.add_argument("--type", choices=["annuity","diff"], help="Tipo de pagamento")

args = parser.parse_args()
print(args)


def taxa_juros_nominal(tx_juros):
    tx_juros = float(tx_juros)
    i = (tx_juros/100.0)/12
    return i

def n_meses(v_emprestimo, v_anuidade, juros_nominal):
    aux = (v_anuidade/(v_anuidade - juros_nominal * v_emprestimo))
    n = round(math.log(aux, juros_nominal + 1))
    return n


def v_anuidade(v_emprestimo, n_meses, juros_nominal):
    a = math.ceil(v_emprestimo * ((juros_nominal * math.pow(1 + juros_nominal, n_meses))
                        / (math.pow(1 + juros_nominal, n_meses) - 1)))
    return a

def v_principal(anuidade, n_meses, juros_nominal):
    p = math.floor(args.payment/((juros_nominal*math.pow(1+juros_nominal,args.periods)/(math.pow(1+juros_nominal,args.periods) - 1))))
    return p

valid_type = True if args.type in  else False

if args.type == None or (args.type != None and args.payment != None) or args.interest == None:
    print("Incorrect parameters")

elif args.periods == None:
    n = n_meses(args.principal, args.payment, taxa_juros_nominal(args.interest))
    anos = n//12
    meses = n % 12
    month = "month" if meses >= 0 or meses <=1 else "months"
    print(f"It will take {anos} years and {meses} {month} to repay this loan!")

elif args.payment == None:
    pay = v_anuidade(args.principal, args.periods, taxa_juros_nominal(args.interest))
    print(f"You monthly = {pay}!")
elif args.principal == None:
    principal = v_principal(args.payment, args.periods, taxa_juros_nominal(args.interest))
    print(f"You monthly = {principal}!")

# v_emprestimo = args.payment/((taxa_juros_nominal(args.interest)*math.pow(1+taxa_juros_nominal(args.interest),args.periods)/(math.pow(1+taxa_juros_nominal(args.interest),args.periods) - 1)))
# print(v_emprestimo)


