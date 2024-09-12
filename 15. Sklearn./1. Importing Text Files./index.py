from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer

dataset = load_files("./data", categories = ["class1", "class2"])

data = dataset.data

for elements in data:
    print(elements)

for elements in dataset.target:
    print(elements)
