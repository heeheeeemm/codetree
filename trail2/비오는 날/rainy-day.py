class Weather:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather


n = int(input())

answer = None

for _ in range(n):
    date, day, weather = input().split()

    if weather == "Rain":
        if answer == None or date < answer.date:
            answer = Weather(date, day, weather)

print(answer.date, answer.day, answer.weather)