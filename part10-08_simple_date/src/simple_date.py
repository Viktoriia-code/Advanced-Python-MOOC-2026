class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
    
    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
    
    def __eq__(self, another):
        return self.year == another.year and self.month == another.month and self.day == another.day
    
    def __ne__(self, another):
        return self.year != another.year or self.month != another.month or self.day != another.day
    
    def __gt__(self, another):
        if self.year > another.year:
            return True
        elif self.year == another.year and self.month > another.month:
            return True
        elif self.year == another.year and self.month == another.month and self.day > another.day:
            return True
        return False

    def __lt__(self, another):
        if self.year < another.year:
            return True
        elif self.year == another.year and self.month < another.month:
            return True
        elif self.year == another.year and self.month == another.month and self.day < another.day:
            return True
        return False

    def __add__(self, days):
        new_date = SimpleDate(self.day + days, self.month, self.year)
        if new_date.day > 30:
            month_in_day = new_date.day // 30
            new_date.day = new_date.day % 30
            new_date.month += month_in_day
        
        if new_date.month > 12:
            year_in_month = new_date.month // 12
            new_date.month = new_date.month % 12
            new_date.year += year_in_month
        return new_date
    
    def __sub__(self, another):
        days1 = self.year*360 + self.month*30 + self.day
        days2 = another.year*360 + another.month*30 + another.day
        return abs(days1 - days2)