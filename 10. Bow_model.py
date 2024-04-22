import numpy as np

class Bow_Model:
    def __init__(self, documents):
        self.vocab_vector = {}  
        self.documents = []
        
        for document in documents: 
            self.documents.append(document.split(" "))

    def fit(self): 
        for document in self.documents: 
            for word in document: 
                if word not in self.vocab_vector: 
                    self.vocab_vector[word] = len(self.vocab_vector)
    
    def transform(self): 
        bow_model = np.zeros((len(self.documents), len(self.vocab_vector)))
        print(self.vocab_vector)
        for i, document in enumerate(self.documents): 
            for word in document:
                bow_model[i][self.vocab_vector[word]] = 1

        print(bow_model) 

bow_model = Bow_Model(["I like to eat pizza", "I like to sleep less, doing more"])
bow_model.fit()
bow_model.transform()