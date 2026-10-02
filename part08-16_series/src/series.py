class Series:
  def __init__(self, title, seasons, genres):
    self.title = title
    self.seasons = seasons
    self.genres = genres
    self.rating = []
  
  def __str__(self):
    if len(self.rating) == 0:
      rating_str = "no ratings"
    else:
      rating_str = f"{len(self.rating)} ratings, average {sum(self.rating)/len(self.rating):.01f} points"
    genre_string = ", ".join(self.genres)
    return f"{self.title} ({self.seasons} seasons)\ngenres: {genre_string}\n{rating_str}"
  
  def rate(self, rating):
    if rating >= 0 and rating <= 5:
      self.rating.append(rating)
  
def minimum_grade(rating: float, series_list: list):
  result = []
  for series in series_list:
    if sum(series.rating)/len(series.rating) >= rating:
      result.append(series)
  return result

def includes_genre(genre: str, series: list):
  result = []
  for s in series:
    if genre in s.genres:
      result.append(s)
  return result
