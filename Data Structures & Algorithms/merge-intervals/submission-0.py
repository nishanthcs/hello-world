class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the array based on start time and then on end time ( if start timne is the same )
        # Go throught each interval and build the final list
        # push i0 to the list
        # compare i+1 with i in the list ; Compare end times. 
        # if E(i+1) == E(i) then finalE is max(Ei+1, Ei)
        # if E(i+1) < E(i) then finalE is E(i)
        # if E(i+1) > E(i) then finalE is E(i+1)
        # finaleE is max (E(i+1))

        sorted_intervals = sorted(intervals,key=lambda x: (x[0],x[1]))
        final_intervals = [sorted_intervals[0]]
        final_idx = 0

        for i in range(1,len(sorted_intervals)):
            if sorted_intervals[i][0] > final_intervals[final_idx][1]:
                # no overlap. start is greater than end
                final_intervals.append(sorted_intervals[i])
                final_idx +=1
            else:
                latest_interval = final_intervals.pop(final_idx)
                # incoming start is less than end of the final interval
                final_end = max(latest_interval[1], sorted_intervals[i][1])
                latest_interval[1] = final_end

                final_intervals.append(latest_interval)
        
        return final_intervals