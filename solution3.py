import numpy as np

def get_indices(N, n_batches, split_ratio):
    """Generates splits of indices from 0 to N-1 into uniformly distributed\
       batches. Each batch is defined by 3 indices [i, j, k] where\
       (j-i) = split_ratio*(k-j). The first batch starts with i = 0,\
       the last one ends with k = N - 1.
    Args:
        N (int): total counts
        n_batches (int): number of splits
        split_ratio (float): split ratio, defines position of j in [i, j, k].
    Returns:
        generator for batch indices [i, j, k]
    """
    k = ((N - 1) * (1 + split_ratio)) * (1 / (n_batches * split_ratio + 1))
    j = k * (1 / (1 + split_ratio))
    i = 0
    delta = k * (split_ratio * (1 / (1 + split_ratio)))
    for lineSegment in range(n_batches):
        yield np.array([int(i), int(j), int(k)])
        i = i + delta
        j = j + delta
        k = k + delta

def main():
    for inds in get_indices(100, 5, 0.25):
        print(inds)
    # expected result:
    # [0, 44, 55]
    # [11, 55, 66]
    # [22, 66, 77]
    # [33, 77, 88]
    # [44, 88, 99]


if __name__ == "__main__":
    main()