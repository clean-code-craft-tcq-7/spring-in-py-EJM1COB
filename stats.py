
def calculateStats(numbers):
  # implement the computation of statistics here and return the results
  stats['avg'] = sum(numbers) / len(numbers) if numbers else 0
  stats['min'] = min(numbers) 
  stats['max'] = max(numbers) 
  return stats
  return None
