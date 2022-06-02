budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memories = int(input())

price_video_card = video_cards * 250

price_processor = processors * (price_video_card * 0.35)

price_ram = ram_memories * (price_video_card * 0.10)

needed_price_for_all = price_video_card + price_processor + price_ram

if video_cards > processors:
    needed_price_for_all = needed_price_for_all - (needed_price_for_all * 0.15)

left_money = abs(budget - needed_price_for_all)

if budget >= needed_price_for_all:
    print(f'You have {left_money:.2f} leva left!')

if budget < needed_price_for_all:
    print(f'Not enough money! You need {left_money:.2f} leva more!')