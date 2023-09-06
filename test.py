def sort_by_last(nums):
    temp = {}

    for i in range(len(nums)):
        last_d = nums[i] % 10
        temp[nums[i]] = last_d

    sorted_temp = dict(sorted(temp.items(), key=lambda item: item[1]))
    sorted_list_by_last = [item[0] for item in sorted_temp.items()]
    return sorted_list_by_last

nums = [19, 81, 27, 42, 16, 55]
print(sort_by_last(nums))
