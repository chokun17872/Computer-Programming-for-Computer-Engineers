"""
Author: passa-
Problem: 12 Racing
Student Code: 6510503310
Branch: Computer Engineering
"""

def r_input():
    times = []
    while True:
        time = input()
        if len(time) == 0:
            break
        times.append(time)
    return times

def prettier(choice, time):
    prettier_time = ""
    if choice == "s":
        prettier_time += "0"*(2-len(time)) + time
    elif choice == "ms":
        prettier_time += "0"*(3-len(time)) + time
    return prettier_time

def to_ms(time):
    time = time.split(":")
    minute = int(time[0])
    second, m_second = list(map(int, time[1].split(".")))
    total_m_second = minute*60*1000 + second*1000 + m_second
    return total_m_second

def to_format(total_m_second):
    minute = total_m_second//60000
    total_m_second -= minute*60000
    second = total_m_second//1000
    total_m_second -= second*1000
    m_second = total_m_second
    second = prettier("s", str(second))
    m_second = prettier("ms", str(m_second))
    return str(minute) + ":" + second + "." + m_second

def solve(times):
    fastest = sorted(times)[0]
    return [to_format(time-fastest) for time in times]

## main ##

times = r_input()
ms_times = [to_ms(time) for time in times]
ans_lst = solve(ms_times)
for ans in ans_lst:
    print(ans)