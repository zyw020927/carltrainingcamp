704. 二分查找 

题目链接：https://leetcode.cn/problems/binary-search/
文章讲解：https://programmercarl.com/0704.%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.html
视频讲解：https://www.bilibili.com/video/BV1fA4y1o715

重点：target所在区间
引申：循环不变量法则

```python[]
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 定义target在左闭右闭的区间里，[left, right]
        left, right = 0, len(nums) - 1  
        # 定义target在左闭右开的区间里，[left, right)
        left, right = 0, len(nums)  

        # 在左闭右闭的区间里, left == right，在[left, right]是有效的空间
        while left <= right:
        # 在左闭右开的区间里, left == right，在[left, right)是无效的空间
        while left < right:

            middle = left + (right - left) // 2 # 防止溢出

            # target 在左区间
            if nums[middle] > target:
				right = middle  # target在[left, middle)中
                right = middle - 1  # target在[left, middle - 1]中

			# target在右区间
            elif nums[middle] < target:
				left = middle + 1 # target在[left, middle)中
                left = middle + 1  # target在[middle + 1, right]中
            else:
                return middle  # 数组中找到目标值，直接返回下标
        return -1  # 未找到目标值
```

27. 移除元素

题目链接：https://leetcode.cn/problems/remove-element/ 
文章讲解：https://programmercarl.com/0027.%E7%A7%BB%E9%99%A4%E5%85%83%E7%B4%A0.html
视频讲解：https://www.bilibili.com/video/BV12A4y1Z7LP 
