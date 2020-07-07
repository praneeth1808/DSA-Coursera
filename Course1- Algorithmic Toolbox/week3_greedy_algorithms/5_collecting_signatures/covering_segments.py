# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(n,segments):
    points = []
    SortedSeg=sorted(segments,key=lambda x : (x.end,x.start))
    i=0
    while i<n:
        start,end=SortedSeg[i]
        points.append(end)
        i+=1
        while i<n and end<=SortedSeg[i].end and end>=SortedSeg[i].start:
            i+=1
    #write your code here
    # for s in segments:
    #     points.append(s.start)
    #     points.append(s.end)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(n,segments)
    print(len(points))
    print(*points)
