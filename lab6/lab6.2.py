"""
n (int): The upper limit of the summation
calculate_sum function at the below calculates the sum of the equation ∑ (−1)^(k+1) / k from k=1 to n
"""

total_sum = 0


def calculate_sum(n):
    global total_sum

    if n == 1:
        total_sum = -1 / 1
    else:
        calculate_sum(n - 1)
        total_sum += ((-1) ** (n + 1)) / n


print(total_sum)
