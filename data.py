import pandas
import random
class Data:
    def __init__(self,file):
        self.questionNumber = 0
        self.file = file
        self.data=None
        self.random_card= None
        self.get_data_ready()
        self.current_f_card= ''
        self.current_e_card= ''
        self.words_doent_know= {}
       

    def get_data_ready(self):
        data= pandas.read_csv(self.file)
        self.data= data_dict= data.to_dict(orient='records')
    
    def random_pick(self):
        self.random_card= random.choice(self.data)
        self.current_f_card= self.random_card['French']
        self.current_e_card= self.random_card['English']
        
    def need_to_learn(self):
        self.data.remove(self.random_card)
        new_data= pandas.DataFrame(self.data)
        new_data.to_csv('data/words_to_learn.csv', index=False)
        

    
