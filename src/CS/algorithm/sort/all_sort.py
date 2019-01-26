# encoding=utf8
class Sort():
    def __init__(self, array, sort_name="quick_sort"):
        if sort_name == "quick_sort":
            self.quick_sort(array, 0, len(array) - 1)
        elif sort_name == "bubble_sort":
            self.bubble_sort(array)
        elif sort_name == "heap_sort":
            self.heap_sort(array)

    def quick_sort(self, array, start, end):
        # 判断low是否小于high,如果为false,直接返回
        if start < end:
            i, j = start, end
            # 设置基准数
            base = array[i]

            while i < j:
                # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
                while (i < j) and (array[j] >= base):
                    j = j - 1

                # 如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
                array[i] = array[j]

                # 同样的方式比较前半区
                while (i < j) and (array[i] <= base):
                    i = i + 1
                array[j] = array[i]
            # 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
            array[i] = base

            # 递归前后半区
            self.quick_sort(array, start, i - 1)
            self.quick_sort(array, j + 1, end)

    def heap_sort(self, array):
        pass

    def bubble_sort(self, array):
        for i in range(len(array)):
            for j in range(i, len(array)):
                if array[i] > array[j]:
                    array[i], array[j] = array[j], array[i]

    def merge_sort(self, array):
        # 不断递归调用自己一直到拆分成成单个元素的时候就返回这个元素，不再拆分了
        if len(array) == 1:
            return array

        # 取拆分的中间位置
        mid = len(array) // 2
        # 拆分过后左右两侧子串
        left = array[:mid]
        right = array[mid:]

        # 对拆分过后的左右再拆分 一直到只有一个元素为止
        # 最后一次递归时候ll和lr都会接到一个元素的列表
        # 最后一次递归之前的ll和rl会接收到排好序的子序列
        ll = self.merge_sort(left)
        rl = self.merge_sort(right)

        # 我们对返回的两个拆分结果进行排序后合并再返回正确顺序的子列表
        # 这里我们调用拎一个函数帮助我们按顺序合并ll和lr
        return self.merge(ll, rl)

    # 这里接收两个列表
    def merge(self, left, right):
        # 从两个有顺序的列表里边依次取数据比较后放入result
        # 每次我们分别拿出两个列表中最小的数比较，把较小的放入result
        result = []
        while len(left) > 0 and len(right) > 0:
            # 为了保持稳定性，当遇到相等的时候优先把左侧的数放进结果列表，因为left本来也是大数列中比较靠左的
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        # while循环出来之后 说明其中一个数组没有数据了，我们把另一个数组添加到结果数组后面
        result += left
        result += right
        return result


array = [3, 2, 1, 4, 5, 6]
bubble_sort = Sort(array, "bubble_sort")
print array

array = [3, 2, 1, 4, 5, 6]
heap_sort = Sort(array, "quick_sort")
print array

array = [3, 2, 1, 4, 5, 6]
merge_sort = Sort(array, "merge_sort")
print array
