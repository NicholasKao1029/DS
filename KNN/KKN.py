from movies import training_set, training_labels, validation_set, validation_labels

def min_max_normalize(lst):
  minimum = min(lst)
  maximum = max(lst)
  normalized = []
  for x in lst:
    normalized.append((x-minimum)/(maximum-minimum))
  return normalized


def distance(movie1, movie2):
  total = 0
  for m1,m2 in zip(movie1, movie2):
    total += (m1 - m2) ** 2
  return total ** 0.5

def classify(unknown, dataset, labels, k):
  distances = []
  #Looping through all points in the dataset
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    #Adding the distance and point associated with that distance
    distances.append([distance_to_point, title])
  distances.sort()
  #Taking only the k closest points
  neighbors = distances[0:k]
  num_good = 0
  num_bad = 0
  for neighbor in neighbors:
    title = neighbor[1]
    if labels[title] == 0:
      num_bad += 1
    elif labels[title] == 1:
      num_good += 1
  if num_good > num_bad:
    return 1
  else:
    return 0


def find_validation_accuracy(training_set, training_labels, validation_set, validation_labels, k):
  num_correct = 0.0
  for title in validation_set:
    guess = classify(validation_set[title], training_set, training_labels,k)
    num_correct += (1 if guess == validation_labels[title] else 0)
  return num_correct/len(validation_set)

x = find_validation_accuracy(training_set, training_labels, validation_set, validation_labels, 3)
print(x)