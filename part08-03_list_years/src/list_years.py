from datetime import date

def list_years(dates: list):
  year_list = []
  for d in dates:
    year_list.append(d.year)
  year_list.sort()
  return year_list