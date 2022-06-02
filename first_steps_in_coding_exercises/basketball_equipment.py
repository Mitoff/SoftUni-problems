year_tax=int(input())
# Баскетболни кецове – цената им е 40% по-малка от таксата за една година
# Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
#Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
# Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка
shoes = year_tax - (year_tax*0.40)
suit = shoes - (shoes*0.20)
ball = suit / 4
accesories = ball / 5
total_expences= year_tax + shoes + suit + ball + accesories
print (total_expences)

