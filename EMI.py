bank_names = {1: 'Axis Bank', 2: 'Bank of Baroda',

              3: 'Bank of India', 4: 'Punjab National Bank', 5: 'State Bank of India', 6: 'HDFC Bank'}
loan_types = {'a': 'Education loan', 'b': 'Home loan',
              'c': 'Personal loan', 'd': 'Car loan'}
bank_rate = {'Axis Bank': {'Education loan': 12.5, 'Home loan': 9, 'Personal loan': 10.2, 'Car loan': 7.5},
             'Bank of Baroda': {'Education loan': 11, 'Home loan': 12, 'Personal loan': 10, 'Car loan': 7.9},
             'Bank of India': {'Education loan': 10.6, 'Home loan': 10, 'Personal loan': 11, 'Car loan': 8.56},
             'Punjab National Bank': {'Education loan': 9.8, 'Home loan': 8.2, 'Personal loan': 11, 'Car loan': 7.32},
             'State Bank of India': {'Education loan': 11.7, 'Home loan': 6.4, 'Personal loan': 15, 'Car loan': 9},
             'HDFC Bank': {'Education loan': 9.2, 'Home loan': 11.6, 'Personal loan': 10.8, 'Car loan': 8.3}}


def select_bank():
    while True:
        try:
            print('\nChoose your bank')
            while True:
                b = int(input(
                    '\n1.Axis Bank.\n2.Bank of Baroda.\n3.Bank of India.\n4.Punjab National Bank\n5.State Bank of India.\n6.HDFC Bank\n7.Compare interest rates\n'))
                if b in range(1, 7):
                    return bank_names[b]
                if b == 7:
                    rate_comparison()
                else:
                    print('\nSelect an option from the given menu.\n')
        except ValueError:
            print('Invalid Input!')


def loan_category():
    print('\nSelect loan category.')
    while True:
        c = (input('\na.Education loan\nb.Home loan\nc.Personal loan\nd.Car loan\n'))
        c = c.lower()
        if c in ['a', 'b', 'c', 'd']:
            return loan_types[c]
        else:
            print('\nSelect an option from the given menu.')


def rate_comparison():

    global bnk_name
    mini = 1000
    print('Rate of interests of different banks for your selected category are displayed below')
    print('---------- ---------- --------- ---------- -------')
    for bnk in bank_rate:
        print(bnk, '-', loan, '-', bank_rate[bnk][loan], '%')
        if bank_rate[bnk][loan] < mini:
            mini = bank_rate[bnk][loan]
            bnk_name = bnk
    print(' ********************************')
    print('Minimum rate of interest is provided by', bnk_name, ':', mini, '%')


def emi_calculation():
    r = bank_rate[bank][loan]
    total_interest = (principal * t * r) / 1200
    amount = total_interest + principal
    monthly_EMI = amount / t
    print('Principal amount: Rs.', principal)
    print('Total interest: Rs.', round(total_interest, 3))
    print('Total payable amount at end of', t,
          'months is Rs.', round(amount, 3))
    print('Your monthly EMI1: Rs.', round(monthly_EMI, 3))
    print('--------------------------------------------------------------------------')


# Main
while True:
    try:
        print('\n\nWELCOME TO EMI CALCULATOR\n')
        n = int(input('Press 1 to continue and 0 to exit\n'))
        if n == 1:
            loan = loan_category()
            bank = select_bank()
            print('Rate of Interest:', bank_rate[bank][loan], '%')
            while True:
                try:
                    principal = float(input('\nEnter Principal Amount\n'))
                    if 9999 < principal < 99999999:
                        break
                    else:
                        print(
                            '\nMin Principal amount must be 10000. Max Principal amount 10Cr')
                except ValueError:
                    print(' Invalid Principal amount!\n')
            while True:
                try:
                    t = int(input('Enter time period in terms of months\n'))
                    if 23 < t < 300:
                        emi_calculation()
                        break
                    else:
                        print(
                            '\nMin time 2 yrs(24 months). Max time 25 yrs(300 months).\n')
                except ValueError:
                    print('Invalid Time Period!\n')

        if n == 0:
            break
    except ValueError:
        print('Invalid input!!\n')
