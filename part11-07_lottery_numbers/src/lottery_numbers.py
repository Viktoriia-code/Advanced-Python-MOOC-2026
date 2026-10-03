class LotteryNumbers:
    def __init__(self, week_num: int, win_numbers: list):
        self.week_num = week_num
        self.win_numbers = win_numbers

    def number_of_hits(self, numbers: list):
        return len([num for num in numbers if num in self.win_numbers])

    def hits_in_place(self, numbers: list):
        return [num if num in self.win_numbers else -1 for num in numbers]
