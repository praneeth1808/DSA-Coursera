# python3

def swap_down(data,n,i,swaps):
    smallest = i
    l = 2*i+1
    r = 2 * i + 2
    if l < n and data[l] < data[smallest]:
        smallest = l;
    if r < n and data[r] < data[smallest]:
        smallest = r;
    if smallest!=i:
        data[i], data[smallest] = data[smallest], data[i];
        swaps.append((smallest,i))
        swap_down(data, n, smallest,swaps);

def build_heap_fast(data,n,swaps):
    start_index=n//2 -1
    for i in range(start_index, -1, -1):
        swap_down(data, n, i,swaps);

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = []
    build_heap_fast(data,n,swaps)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
