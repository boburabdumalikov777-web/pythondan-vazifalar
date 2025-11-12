"""Create a function that takes the number of daily average recovered cases recovers,
daily average new_cases, current active_cases, and returns the number of days it will take to
reach zero cases.

Examples
end_corona(4000, 2000, 77000) ➞ 39

end_corona(3000, 2000, 50699) ➞ 51

end_corona(30000, 25000, 390205) ➞ 79"""

from math import ceil


def end_corona(recovers, new_cases, active_cases):
    x = recovers - new_cases
    y = ceil(active_cases / x)
    return y


print(end_corona(30000, 25000, 390205))  # ➞ 79
# ceil sonni yuqoriga yaxlitlashini qidirib tushundim (23.25=24)
