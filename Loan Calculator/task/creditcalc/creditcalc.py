import math
import argparse

'''Task number 3 and 4:'''

parser = argparse.ArgumentParser(description="This program calculate from the given parameters \
some annuity payment calculations.")
parser.add_argument("--type")  # 2 choices
parser.add_argument("--principal", type=int)  # loan principal
parser.add_argument("--payment", type=float)  #  annuity payment
parser.add_argument("--periods", type=int)  # months
parser.add_argument("--interest", type=float)  # interest rate


args = parser.parse_args()

args_list = vars(args).values()

num = 0



def number_of_payments(years, months, overpayment):
    if math.ceil(years) == 0 and math.ceil(months) == 1:
        return f"It will take 1 month to repay this loan!\nOverpayment = {math.ceil(overpayment)}"
    if math.ceil(years) == 0 and math.ceil(months) > 0:
        return f"It will take {math.ceil(months)} months to repay this loan!\nOverpayment = {math.ceil(overpayment)}"
    if math.ceil(months) == 12:
        return f"It will take {math.ceil(years) + 1} years to repay this loan!\nOverpayment = {math.ceil(overpayment)}"
    if math.ceil(years) > 0 and math.ceil(months) == 0:
        return f"It will take {math.ceil(years)} years to repay this loan!\nOverpayment = {math.ceil(overpayment)}"
    if math.ceil(years) != 0 and math.ceil(months) != 0:
        return f"It will take {math.ceil(years)} years and {math.ceil(months)} months to repay this loan!\nOverpayment = {math.ceil(overpayment)}"


def loan_principal_calculate(payment, periods, interest):
    loan_principal = payment / ((interest * math.pow(1 + interest, periods)) / (math.pow(1 + interest, periods) - 1))
    return loan_principal


def calculate_monthly_payment(principal, periods, interest):
    annuity_payment = principal * (interest * math.pow(1 + interest, periods)) / (math.pow(1 + interest, periods) - 1)
    return annuity_payment


def calculate_months(payment, interest, principal):
    months = math.log(payment / (payment - interest * principal)) / math.log(1 + interest)
    overpayment = payment * math.ceil(months) - principal
    years, months = divmod(months, 12)
    return number_of_payments(years, months, overpayment)


def calculate_differentiated_payment(P, i, n, m):
    Dm = P/n + i * (P - P * (m - 1) / n)
    return Dm


def calculate_diff_payments(principal, payment, periods):
    i = 0  # Since it's a differentiated payment, i.e., not an annuity
    diff_payments = []

    for month in range(1, periods + 1):
        Dm = calculate_differentiated_payment(principal, i, periods, month)
        diff_payments.append(Dm)

    return diff_payments


def calculate_interest_rate(interest, payment, principal, periods):
    if interest is not None:
        return (interest / 12 / 100)
    elif periods is None:
        print("Incorrect parameters")
        return None
    elif principal is not None and periods is not None:
        print("Incorrect parameters")
        return None
    else:
        interest = (payment / (principal * periods)) * 12 * 100
        return interest


def how_much_none(args_list, num):
    for i in args_list:
        if i == "None":
            num =+ 1
    return num


number_of_none = how_much_none(args_list, num)

def check_prerequisite():
    if (args.type == 'annuity' or args.type == 'diff') and args.interest is None:
        print("Incorrect parameters")
    elif args.type != 'annuity' and args.type != 'diff':
        print("Incorrect parameters")
    elif how_much_none(args_list, num) > 1:
        print("Incorrect parameters")
    elif args.type == 'diff' and args.payment:
        print("Incorrect parameters")
    elif args.type == 'annuity' and args.interest is None:
        print("Incorrect parameters")
    elif (args.payment or args.principal or args.periods or args.interest) <= 0:
        print("Incorrect parameters")


def DMs(principal, periods, interest):
    sum_Dms = 0
    for m in range(1, args.periods + 1):
        Dm = int(math.ceil(principal / periods + interest * (principal - principal * (m - 1) / periods)))
        print(f"Month {m}: payment is {int(Dm)}")
        sum_Dms += Dm
    return f"\nOverpayment = {sum_Dms - principal}"


payment = args.payment
periods = args.periods
interest = args.interest
principal = args.principal


if args.type != 'annuity' or args.type != 'diff':
    print("Incorrect parameters")
if args.type == 'annuity':
    check_prerequisite()
    interest = calculate_interest_rate(interest, payment, principal, periods)
    if args.principal and args.payment and args.interest:
        print(calculate_months(payment, interest, principal))
    if args.principal and args.periods and args.interest:
        payment = calculate_monthly_payment(principal, periods, interest)
        print(f'Your monthly payment = {math.ceil(payment)}!')
    if args.payment and args.periods and args.interest:
        loan_principal = loan_principal_calculate(payment, periods, interest)
        print(f'Your loan principal = {math.ceil(loan_principal)}!')
if args.type == 'diff':
    check_prerequisite()
    if args.principal and args.periods and args.interest:
        interest = calculate_interest_rate(interest, payment, principal, periods)
        DMs = DMs(principal, periods, interest)
        print(DMs)
    if args.principal and args.payment and args.periods:
        diff_payments = calculate_diff_payments(principal, payment, periods)




    '''
    Task number 2:
    
    def number_monthly_payments(loan_principal):
        print("Enter the monthly payment: ")
        payment = int(input())
        if loan_principal / payment == 1 or loan_principal <= payment:
            return f"It will take 1 month to repay the loan"
        else:
            return f"It will take {math.ceil(loan_principal / payment)} months to repay the loan"
    
    
    def monthly_payment(loan_principal):
        print("Enter the number of months: ")
        number_months = int(input())
        payment = math.ceil(loan_principal / number_months)
        if loan_principal == payment * number_months:
            return f"Your monthly payment = {payment}"
        else:
            remainder = loan_principal - payment * number_months
            return f"Your monthly payment = {payment} and the last payment = {payment + remainder}"
    
    
    def main():
        print("Enter the loan principal: ")
        loan_principal = int(input())
        print('What do you want to calculate? \ntype "m" - for number of monthly payments, \ntype "p" - for the monthly payment: ')
        user_choice = input()
        if user_choice == "m":
            months = number_monthly_payments(loan_principal)
            print(months)
        elif user_choice == "p":
            payment = monthly_payment(loan_principal)
            print(payment)
    
    
    main()
    '''


'''
        Task number 1:
        loan_principal = 'Loan principal: 1000'
        final_output = 'The loan has been repaid!'
        first_month = 'Month 1: repaid 250'
        second_month = 'Month 2: repaid 250'
        third_month = 'Month 3: repaid 500'
        
        # write your code here
        print(loan_principal)
        print(first_month)
        print(second_month)
        print(third_month)
        print(final_output)
'''