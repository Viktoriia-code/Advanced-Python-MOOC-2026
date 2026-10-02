class WeatherStation:
  def __init__(self, name):
    self.__name = name
    self.__observations = []

  def __str__(self):
    return f"{self.__name}, {len(self.__observations)} observations"

  def add_observation(self, observation: str):
    self.__observations.append(observation)

  def latest_observation(self):
    observations_number = len(self.__observations)
    if observations_number == 0:
      return ""
    else:
      return self.__observations[observations_number-1]

  def number_of_observations(self):
    return len(self.__observations)