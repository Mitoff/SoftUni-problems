deposit_amount = float(input())
months = int(input())
annual_rate = float(input())
#suma = dep_suma + srok_depposit((srok_dep*god_lihv_proc)/12)
per_year = deposit_amount*(annual_rate/100)
per_month = per_year/12
total_amount = deposit_amount + (months*per_month)
print(total_amount)
