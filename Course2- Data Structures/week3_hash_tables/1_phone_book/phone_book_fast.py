# python3
from random import randint

class PhoneBook:
    def __init__(self):
        self.q_count=int(input())
        self.queries = [input().split() for i in range(self.q_count)]
        self.prime = 10000019
        self.a=17
        self.b=9
        self.cardinality=1
        self.size=0
        self.num_map={0: []}
        self.results=[]

    def print_response(self):
        print('\n'.join(self.results))

    def solve_queries(self):
        for query in self.queries:
             if(query[0]=="add"):
                 self.add_num(query[1],query[2])
             elif (query[0] == "find"):
                 self.find_num(query[1])
             elif(query[0]=="del"):
                 self.del_num(query[1])
             else:
                 print("invalid Argument")
                 exit()

    def re_hash(self):
        self.cardinality*=2
        new_num_map={}
        for i in range(0,self.cardinality):
            new_num_map[i]=[]
        for key,contacts in self.num_map.items():
            for contact in contacts:
                new_num_map[self.get_hash(contact[0])].append((contact))
        self.num_map=new_num_map
    def add_num(self, num,name):
        if(self.size/self.cardinality>0.9):
            self.re_hash()
        num=int(num)
        hash_val=self.get_hash(num)
        for key,val in enumerate(self.num_map[hash_val]):
            if(val[0]==num):
                self.num_map[hash_val][key]=(num,name)
                return
        self.num_map[hash_val].append((num,name))
        self.size+=1

    def find_num(self, num):
        num=int(num)
        hash_val=self.get_hash(num)
        for (num_i,name_i) in self.num_map[hash_val]:
            if(num_i==num):
                self.results.append(name_i)
                return
        self.results.append("not found")
        return


    def del_num(self, num):
        num = int(num)
        hash_val = self.get_hash(num)
        for (key,val) in enumerate(self.num_map[hash_val]):
            if (val[0] == num):
                self.num_map[hash_val].remove(val)
                return
        return

    def get_hash(self,key):
        return ((self.a * key + self.b)% self.prime) % self.cardinality


if __name__ == '__main__':
    Phone_Book = PhoneBook()
    Phone_Book.solve_queries()
    Phone_Book.print_response()
