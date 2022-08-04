''' Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

Example 1:
Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].

Example 2:
Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].

Constraints:
0 <= low <= high <= 10^9 '''

a = int(input('Enter a low positive number'))
b = int(input('Enter a high positive number'))
x = []
if 0 > a > b > 10**9:
    print('Enter a correct number')
elif a > b:
    print('Mixed up low and high number\nTry again')
else:
    for i in range(a, b+1):
        if i % 2 != 0:
            x.append(i)
print(len(x))
print(f'The odd numbers between {a} and {b} are {x}')