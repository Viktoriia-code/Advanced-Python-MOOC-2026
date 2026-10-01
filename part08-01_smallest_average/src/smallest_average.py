def smallest_average(person1: dict, person2: dict, person3: dict):
  # Calculate average results for each person
  person1_avg = (person1['result1'] + person1['result2'] + person1['result3']) / 3
  person2_avg = (person2['result1'] + person2['result2'] + person2['result3']) / 3
  person3_avg = (person3['result1'] + person3['result2'] + person3['result3']) / 3
    
  # Find the smallest average
  min_avg = min(person1_avg, person2_avg, person3_avg)
    
  # Determine which person has the smallest average
  if min_avg == person1_avg:
    return person1
  elif min_avg == person2_avg:
    return person2
  else:
    return person3