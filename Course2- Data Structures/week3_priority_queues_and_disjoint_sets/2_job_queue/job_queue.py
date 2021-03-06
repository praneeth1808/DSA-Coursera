# python3

class JobQueue:
    def read_data(self):
        self.num_threads, m = map(int, input().split())
        self.array = [[0] * 2 for i in range(self.num_threads)]
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)
        self.threads = [None] * len(self.jobs)
        self.start = [0] * len(self.jobs)

    def initiate(self):
        thread = 0
        for i in range(min(self.num_threads, len(self.jobs))):
            self.array[i] = [self.jobs[i], i]
            self.threads[i] = thread
            thread += 1
        for i in range(self.num_threads // 2, -1, -1):
            self.shiftDowm(i)

    def print_response(self):
        for i in range(len(self.jobs)):
            print(self.threads[i], self.start[i])

    def shiftDowm(self, i):
        min_index = i
        l = 2 * i + 1 if (2 * i + 1 < self.num_threads) else -1
        r = 2 * i + 2 if (2 * i + 2 < self.num_threads) else -1
        if (l != -1) and ((self.array[l][0] < self.array[min_index][0]) or (
                (self.array[l][0] == self.array[min_index][0]) and self.array[l][1] < self.array[min_index][1])):
            min_index = l
        if (r != -1) and ((self.array[r][0] < self.array[min_index][0]) or (
                (self.array[r][0] == self.array[min_index][0]) and (self.array[r][1] < self.array[min_index][1]))):
            min_index = r
        if i != min_index:
            self.array[i], self.array[min_index] = \
                self.array[min_index], self.array[i]
            self.shiftDowm(min_index)

    def assign_jobs(self):
        self.initiate()
        time = 0
        if len(self.jobs) > self.num_threads:
            for i in range(self.num_threads, len(self.jobs)):
                self.shiftDowm(0)
                time = self.array[0][0]
                self.threads[i] = self.array[0][1]
                self.start[i] = time
                self.array[0][0] += self.jobs[i]

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.print_response()


if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
