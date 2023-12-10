def extraFunc(func):
    def wrapper(nums):
        odd = 0
        odd_sum = 0
        even = 0
        even_sum = 0

        for num in nums:
            if num % 2 == 0:
                even += 1
                even_sum += num
            else:
                odd += 1
                odd_sum += num

        print("Average of the odd:", odd_sum / odd)
        print("Average of the even:", even_sum / even)
        func(nums)

    return wrapper

@extraFunc
def average(nums):
    _sum = 0
    for num in nums:
        _sum += num
    print("Average is:", _sum / len(nums))

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
average(numbers)
