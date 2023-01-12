import datetime
import time
#  <<<- - - - - - - INFLATION CALCULATOR - - - - - - - - - >>>
#  <<<- - - - - - - Code By : MUSTAK AHMED - - - - - - - - - >>>
#  <<<- - - - - - - Timestrap : 12 April 2022 - - - - - - - - - >>>


print("\n\n:::: - - - - - - - -:: INFLATION CALCULATOR ::- - - - - - - - ::::\n\n")

name = input("Enter Your Name : ")
while True:
    Inf_rate = float(input("Enter Current inflation rate (in %) : "))
    inf_rate = Inf_rate/100

    curr_year = int(input("\nEnter Current Year : "))
    tar_year = int(input("\nEnter Target Year : "))
    Amount = int(input("\nEnter Your Amount (in INR): "))
    amount = Amount
    duration = (tar_year - curr_year)

    # main programme

    for i in range(duration):
        amount = amount + (amount*inf_rate)

    amount_int = int(amount)
    print(
        f"\n\nThe amount with inflation in {tar_year} is : {amount_int} INR\n")

    now = datetime.datetime.now()
    now_time = f"                   || - - - - - - - - - {now.day}.0{now.month}.{now.year} - - - - - - - - - || "
    f = open(f'{name}.txt', 'a')
    f.write(
        f"\n\n{now_time}\n\n Inflation rate : {Inf_rate}%     Current Year : {curr_year}    Target Year : {tar_year}\nInitial Amount : {Amount}\nAmount with Inflation is : {amount_int}\n")
    f.close()
    n = input("Press 'y' for Repeat : ")
    if n == 'y':
        continue
    else:
        break
