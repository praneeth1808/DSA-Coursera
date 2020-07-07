# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    i=0
    numberofStops=-1
    updated_stops=[0]+stops+[distance]
    n=len(stops)
    while i<=n:
        [start,next_stop]=[updated_stops[i],updated_stops[i+1]]
        i+=1
        if next_stop-start>tank:
            return -1
        numberofStops+=1
        while i<=n and updated_stops[i]-start<tank:
            i+=1
    return numberofStops

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
