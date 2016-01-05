def first_elf_translate(nums):
    out = ''
    nums = list(nums)
    counts = list(map(int, nums[::2]))
    chars = nums[1::2]

    for count, char in zip(counts, chars):
        out += count*char

    return out

def elf_translate(nums):
    out = ''
    nums = list(nums)
    count = 1
    for idx, char in enumerate(nums):
        if idx + 3 > len(nums)+1:
            out += str(count) + char
            break

        if char == nums[idx+1]:
            count += 1
        else:
            out += str(count) + char
            count = 1
            
    return out
