import argparse
import sys
from math import *

count = 0
parser = argparse.ArgumentParser(description="This program calculates credit.")

parser.add_argument("-T", "--type", choices=["annuity", "diff"],
                    help="You need to choose only one.")
parser.add_argument("--principal", type=int,
                    help="Input principal.")
parser.add_argument("--payment", type=int,
                    help="Input payment for annuity.")
parser.add_argument("--periods", type=int,
                    help="Input periods.")
parser.add_argument("--interest", type=float,
                    help="Input interest.")

args = parser.parse_args()

ingr = [args.principal, args.payment, args.periods, args.interest]

if len(sys.argv) != 5:
    print('Incorrect parameters')
else:
    if args.type == "diff":
        if args.principal > 0 and args.periods > 0 and args.interest > 0:
            principal = args.principal
            periods = args.periods
            interest = (args.interest) / 1200

            for i in range(1, periods + 1):
                print(f'Month {i}: payment is {ceil((principal / periods) + interest * (principal - (principal * (i - 1) / periods)))}')
                count += ceil((principal / periods) + interest * (principal - (principal * (i - 1) / periods)))
            print(f'\nOverpayment = {count - principal}')

        else:
            print('Incorrect parameters')

    elif args.type == "annuity":
        ii = (args.interest) / 1200
        if args.payment == None and ingr[0] > 0 and ingr[2] > 0 and ingr[3] > 0:
            principal = args.principal
            periods = args.periods
            a = principal * ii * (1 + ii) ** periods / ((1 + ii) ** periods - 1)
            a = ceil((a))
            print(f'Your annuity payment = {a}!')
            print(f'Overpayment = {a * periods - principal}')

        elif args.principal == None and ingr[1] > 0 and ingr[2] > 0 and ingr[3] > 0:
            payment = args.payment
            periods = args.periods
            principal = payment / ((ii * (1 + ii) ** periods) / (-1 + (1 + ii) ** periods))
            principal = ceil(principal)
            print(f'Your loan principal = {principal}!')
            print(f'Overpayment = {payment * periods - principal}')

        elif args.periods == None and ingr[0] > 0 and ingr[1] > 0 and ingr[3] > 0:
            principal = args.principal
            payment = args.payment
            periods = log(payment / (payment - ii * principal), 1 + ii)
            periods = ceil(periods)

            if periods % 12 != 0 and periods // 12 > 0:
                print(f'It will take {periods // 12} years and {periods % 12} months to repay this loan!')
            elif periods % 12 == 0 and periods / 12 > 0:
                print(f'It will take {periods // 12} years to repay this loan!')
            elif periods % 12 != 0 and periods // 12 == 0:
                print(f'It will take {periods % 12} months to repay this loan!')
            print(f'Overpayment = {payment * periods - principal}')
    else:
        print('Incorrect parameters')
