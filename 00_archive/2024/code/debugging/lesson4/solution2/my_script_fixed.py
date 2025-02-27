from utils import read_csv

def averages(filename):
    data = read_csv(filename)
    ages, weights = [], []
    for age, weight in data:
        ages.append(age)
        weights.append(weight)
    age_av = sum(ages) / len(ages)
    weight_av = sum(weights) / len(weights)
    return {"age": age_av, "weight": weight_av}

data_fn = "data.csv"
avs = averages(data_fn)
print(f"Averages\t")
for col, av in avs.items():
    print(f"{col}\t{av :.2f}")

