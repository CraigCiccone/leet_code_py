# MEDIUM
#
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps
# and retrieve the key's value at a certain timestamp.
#
# Implement the TimeMap class:
#
# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key 'key' with the value 'value' at the given time
# timestamp. String get(String key, int timestamp) Returns a value such that set was called previously, with
# timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest
# timestamp_prev. If there are no values, it returns "".
#
# Example 1:
#
# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]
#
# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and
#                                // timestamp 2, then the only value is at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"
#
# Constraints:
#
# 1 <= key.length, value.length <= 100
# key and value consist of lowercase English letters and digits.
# 1 <= timestamp <= 10^7
# All the timestamps timestamp of set are strictly increasing.
# At most 2 * 10^5 calls will be made to set and get.

from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        cur_data = self.data[key]

        low = 0
        high = len(self.data[key]) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if cur_data[mid][0] < timestamp:
                low = mid + 1
            elif cur_data[mid][0] > timestamp:
                high = mid - 1
            else:
                return cur_data[mid][1]

        return cur_data[high][1] if timestamp > cur_data[high][0] else ""


if __name__ == "__main__":
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    print(tm.get("foo", 1))  # bar
    print(tm.get("foo", 3))  # bar
    tm.set("foo", "bar2", 4)
    print(tm.get("foo", 4))  # bar2
    print(tm.get("foo", 5))  # bar2
    print(tm.get("a", 1))  # ""

    tm = TimeMap()
    tm.set("love", "high", 10)
    tm.set("love", "low", 20)
    print(tm.get("love", 5))  # ""
    print(tm.get("love", 10))  # high
    print(tm.get("love", 15))  # high
    print(tm.get("love", 20))  # low
    print(tm.get("love", 25))  # low
