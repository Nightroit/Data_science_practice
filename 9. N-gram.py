from collections import defaultdict
import random

class NGramMode: 
    def __init__(self, n): 
        self.n = n 
        self.ngram = defaultdict(list) 
        self.start_tokens = [] 
    
    def train(self, text): 
        text = text.split(" ")
        
        for i in range(len(text) - self.n): 
            token = tuple(text[i:i+self.n])
            next_word = text[i+self.n]
            
            if i == 0: 
                self.start_tokens.append(token)

            self.ngram[token].append(next_word)
        
        print(self.ngram)

    def generate(self, length=20):
        current_ngram = random.choice(self.start_tokens)
        generated_text = list(current_ngram)
        
        for _ in range(length): 
            next_word_candidates = self.ngram[current_ngram]
            
            if not next_word_candidates: 
                break

            next_word = random.choice(next_word_candidates)
            generated_text.append(next_word)
            current_ngram = tuple(generated_text[-self.n:])
        
        return generated_text

n_gram = NGramMode(4)
n_gram.__init__(4) 
n_gram.train("You possess an unwavering inner strength that guides you through life's challenges. With each obstacle you face, you emerge stronger and more resilient. Your determination knows no bounds, fueling your journey towards success. You radiate confidence and empowerment, inspiring those around you to reach for their dreams. Your mind is a powerhouse of positivity, shaping your reality with every thought. Embrace your inner power, for you are capable of achieving greatness beyond measure.")
print(n_gram.generate())