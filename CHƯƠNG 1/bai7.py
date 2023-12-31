class Date:
    def __init__(self, day=1, month=1, year=2022):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f'{self.day}/{self.month}/{self.year}')

    def next(self):
        days_in_month = [31, 28 if self.year % 4 != 0 or (self.year % 100 == 0 and self.year % 400 != 0) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.day < days_in_month[self.month - 1]:
            self.day += 1
        else:
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1

# Ví dụ sử dụng lớp Stack
date = Date(27,9,2023)
date.display() # Output: "27/9/2023"
date.next()
date.display() # Output: "28/9/2023"
