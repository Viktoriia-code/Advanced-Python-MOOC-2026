class ListHelper:
  @classmethod
  def greatest_frequency(cls, my_list: list):
    max_count = 0
    max_char = None
    for i in range(len(my_list)):
      if my_list.count(my_list[i]) >= max_count:
        max_count = my_list.count(my_list[i])
        max_char = my_list[i]
    return max_char

  @classmethod
  def doubles(cls, my_list: list):
    result = []
    for i in range(len(my_list)):
      if my_list.count(my_list[i]) >= 2 and my_list[i] not in result:
        result.append(my_list[i])
    return len(result)