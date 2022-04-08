import pickle
goals={}

with open('./dataset/dev.pk', 'rb') as f:
    goals['test'] = pickle.load(f)
print(len(goals['test']))
for i in range(10):
  print(goals['test'][i]['disease_tag'])
  print("-----------------------------")
  # print("goals['test'].append("+str(goals['test'][i])+')')

