duration = int(input("Enter seconds: "))
mon, d, h, m, s, = duration // 2629743 % 12, duration // 86400 % 31, duration // 3600 % 24, duration // 60 % 60, duration % 60
print(f' {mon} месяцы, {d} дни, {h} часы, {m} минуты, {s} секунды')
