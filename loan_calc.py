import argparse
from math import ceil, log, pow

def annuity_payment(p, n, i):
    annuity = ceil((p * i * pow(1 + i, n)) / (pow(1 + i, n) - 1))
    print(f"Your monthly payment = {annuity}!")
    print(f"Overpayment = {annuity * n - p}")

def loan_principal(a, n, i):
    principal = a / ((i * pow(1 + i, n)) / (pow(1 + i, n) -1))
    print(f"Your loan principal = {principal}!")
    print(f"Overpayment = {a * n - principal}")

def num_of_payments(p, a, i):
    periods = ceil(log((a / (a - i * p)), (1 + i)))
    years = periods // 12
    months = periods % 12

    if years == 0:
        print(f"It will take {months} months to repay this loan!")
    elif months == 0:
        print(f"It will take {years} years to repay this loan!")
    else:
        print(f"It will take {years} years and {months} months to repay this loan!")

    print(f"Overpayment = {a * periods - p}")

def differentiated_payments(p, n, i):
    total = 0
    for m in range(1, n + 1):
        diff_payment = ceil((p / n) + i * (p - (p * (m - 1) / n)))
        total += diff_payment
        print(f"Month {m}: payment is {diff_payment}")
        
    print(f"\nOverpayment = {total - p}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", required=True, choices=["annuity", "diff"])
    parser.add_argument("--payment", type=float)
    parser.add_argument("--principal", type=float)
    parser.add_argument("--periods", type=int)
    parser.add_argument("--interest", type=float)
    
    args = parser.parse_args()
    a = args.payment
    p = args.principal
    n = args.periods

    if args.interest:
        i = (args.interest / 12) / 100

    func_args = [a, p, n, i]
    
    if any([x is not None and x < 0 for x in func_args]):
        print("Incorrect parameters")
        exit()

    elif args.type == "annuity":
        if args.payment is None:
            annuity_payment(p, n, i)
        elif args.principal is None:
            loan_principal(a, n, i)
        elif args.periods is None:
            num_of_payments(p, a, i)
    
    elif args.type == "diff":
        differentiated_payments(p, n, i)
        
if __name__ == "__main__":
    try:
        main()
    except:
        print("Incorrect parameters")
