from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# 1. FILTER: Keep only numbers greater than 3
filtered_numbers = list(filter(lambda x: x > 3, numbers))
print("Filtered (x > 3):", filtered_numbers) # Output: [4, 5, 6]

# 2. MAP: Multiply each remaining number by 10
mapped_numbers = list(map(lambda x: x * 10, filtered_numbers))
print("Mapped (Multiply by 10):", mapped_numbers) # Output: [40, 50, 60]

# 3. REDUCE: Add them all together into one final total
final_sum = reduce(lambda total, current: total + current, mapped_numbers)
print("Reduced (Sum of all):", final_sum) # Output: 150 (40 + 50 + 60) # Output: 150