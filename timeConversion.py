def timeConversion(s):
    time_signal = s[-2:]
    if time_signal == 'PM':
        hour = int(s[:2])
        if hour != 12:
            hour += 12
    else:
        hour = s[:2]
        if hour == '12':
            hour = '00'
    return f"{hour}{s[2:-2]}"

s = input('')
print(timeConversion(s))