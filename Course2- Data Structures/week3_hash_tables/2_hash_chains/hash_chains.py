# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = {}
        for i in range(0,self.bucket_count):
            self.elems[i]=[]
        self.output = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        self.output.append('yes' if was_found else 'no')

    def write_chain(self, chain):
        self.output.append(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(self.elems[query.ind][::-1])
        else:

            try:
                ind = self._hash_func(query.s)
                found = query.s in self.elems[ind]
            except ValueError:
                ind = -1
                found = False
            if query.type == 'find':
                self.write_search_result(found)
            elif query.type == 'add':
                if not found:
                    self.elems[ind].append(query.s)
            else:
                if ind != -1 and found:
                    self.elems[ind].remove(query.s)

    def print_results(self):
        for each in self.output:
            print(each)
            

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())
        self.print_results()

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
