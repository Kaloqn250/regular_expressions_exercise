import re

pattern = r">>([A-Za-z]+)<<(\d+.?\d+)!(\d+)"
input_line = input()
bought_furniture = []
total_cost = 0

while input_line != 'Purchase':
    match = re.search(pattern, input_line)
    if match:
        furniture, cost, quantity = match.groups()
        bought_furniture.append(furniture)
        total_cost += float(cost) * int(quantity)

    input_line = input()

print('Bought furniture:')
for item in bought_furniture:
    print(item)
print(f'Total money spend: {total_cost:.02f}')
