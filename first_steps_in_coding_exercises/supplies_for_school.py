pens = int(input())
markers = int(input())
liquid = float(input())
percent = int(input())
total_pens = pens * 5.80
total_markers = markers * 7.20
total_liquid = liquid * 1.20
sum = total_pens+total_markers+total_liquid
total_sum = sum - (sum*percent/100)
print(total_sum)
