def get_start(interval):
    return interval[0]

def merge_intervals(intervals):
    #Sort the intervals by their start values using the get_start function
    intervals.sort(key=get_start)

    # Initialize the merged intervals list
    merged_intervals = []

    # Iterate through the sorted intervals
    for interval in intervals:
        # If the merged intervals list is empty or the current interval does not overlap with the last one in merged_intervals
        if not merged_intervals or merged_intervals[-1][1] < interval[0]:
            # Add the current interval to the merged list
            merged_intervals.append(interval)
        else:
            # There is an overlap, so merge the current interval with the last one in merged_intervals
            merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1]))

    return merged_intervals

if __name__ == "__main__":
    intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
    print("Merged intervals:", merge_intervals(intervals))
