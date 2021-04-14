#冒泡排序
def BubbleSort1(nums):
    length = len(nums)
    for i in range(length):
        for j in range(length-2, i-1, -1): #注意边界条件range右边不取
            if nums[j]>nums[j+1]: #注意是两两相邻比较
                # tmp = nums[j+1]
                # nums[j+1] = nums[j]
                # nums[j] = tmp
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

#冒泡排序优化
def BubbleSort2(nums):
    length = len(nums)
    flag = True #flag表示是否发生数的交换，若没发生，则已为有序
    for i in range(length):
        if flag:
            flag = False #需在每一次'i'循环时将其置为false
            for j in range(length-2, i-1, -1):
                if nums[j]>nums[j+1]: #注意是两两相邻比较
                    # tmp = nums[j+1]
                    # nums[j+1] = nums[j]
                    # nums[j] = tmp
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    flag = True
        else:
            return nums
    return nums

#堆排序
def HeapSort(nums):
    j = 0
    # 从右向左，从下向上，首次构造堆(选取的是有孩子的节点)
    for j in range((len(nums)-1)//2, 0, -1): #记住length的长度为数组真正长度，所以需要-1
        HeapAdjust(nums, j, len(nums)-1)
    for j in range(len(nums)-1, 1, -1):
        tmp1 = nums[1]
        nums[1] = nums[j]
        nums[j] = tmp1
        HeapAdjust(nums, 1, j-1)

def HeapAdjust(nums,begin,end):
    tmp, i = 0, 0
    tmp = nums[begin]
    i = 2*begin
    while(i <= end):
        if (i<end and nums[i]<nums[i+1]):
            i = i + 1
        if tmp >= nums[i]:
            break
        nums[begin] = nums[i]
        begin = i
        i = i * 2
    nums[begin] = tmp

#归并排序
def Merge_sort(nums, tmp, begin,end): #tmp为辅助暂存数组
    if begin == end:
        return
    mid = (begin + end)//2
    #递归两个子序列
    Merge_sort(nums, tmp, begin, mid)
    Merge_sort(nums, tmp, mid+1, end)
    i = begin
    j = mid + 1
    k = begin
    #归并两个相对有序的子序列
    while(i <= mid and j <= end):
        if nums[i] < nums[j]:
            tmp[k] = nums[i]
            i = i + 1
            k = k + 1
        else:
            tmp[k] = nums[j]
            j = j + 1
            k = k +1
    while (i <= mid):
        tmp[k] = nums[i]
        k = k + 1
        i = i + 1
    while (j <= end):
        tmp[k] = nums[j]
        k = k + 1
        j = j + 1
    #将每一次的暂存tmp结果存回nums(很重要)，使nums保持相对有序,只回存已经相对有序的部分,从t到end
    t = begin
    while(t <= end):
        nums[t] = tmp[t]
        t = t + 1

#快速排序
def Quick_Sort(nums,low,high):
    begin = low
    end = high
    if low >= high: #!!!!!很重要
        return
    privotkey = nums[low]
    while(low < high):
        while(low < high and nums[high] >= privotkey):
            high -= 1
        nums[low], nums[high] = nums[high], nums[low]
        while(low < high and nums[low] <= privotkey):
            low += 1
        nums[low], nums[high] = nums[high], nums[low]
    Quick_Sort(nums, begin, low-1)
    Quick_Sort(nums, low+1, end)

if __name__ == '__main__':
    # nums_input= input('请输入需要排序的数组')
    # nums = [int(i) for i in nums_input.split(',')]
    nums = [-4, 0, 7, 4, 9, -5, -1, 0, -7, -1]

    # nums1 = BubbleSort1(nums)
    # print('冒泡排序', nums1)

    # nums2 = BubbleSort2(nums)
    # print('冒泡排序优化', nums2)

    # nums1 = [0] + nums
    # HeapSort(nums1)
    # print('堆排序', nums1[1:])

    # tmp = [0 for i in range(len(nums))]
    # Merge_sort(nums, tmp, 0, len(nums)-1) #数组第一个下标为0，最后一个下标为len(nums)-1
    # print('归并排序', nums)

    Quick_Sort(nums, 0, len(nums)-1)
    print('快速排序', nums)


