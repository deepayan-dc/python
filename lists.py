subjects = ["java", "dbms", "toc", "pslp", "cns"]
print(subjects)
print(subjects[0])
print(subjects[1])
print(subjects[2])
print(subjects[-1]) # negative indexing (access from the back)
print(subjects[1:4]) # slicing (access a range of elements)
numbers = [1, 2, 3, 4, 5]
subjects.extend(numbers) # extend the list with another list
print(subjects)
subjects.append("python") # add a single element to the end of the list
print(subjects)
subjects.insert(2, "machine learning")
print(subjects)
subjects.remove("cns")
print(subjects)
subjects.pop() # remove the last element
print(subjects)
print(subjects.index("toc"))
subjects.insert(7, 2)
print(subjects.count(2)) # count the number of occurrences of an element
subjects.remove(2)
subjects.pop()
subjects.pop()
subjects.pop()
subjects.pop()
subjects.pop()
print(subjects)
subjects.sort() # sort the list in ascending order
print(subjects)
numbers.sort(reverse=True) # sort the list in descending order
print(numbers)
subjects.reverse() # reverse the order of the list
print(subjects)
nums = numbers.copy() # create a copy of the list
print(nums)
nums.clear() # remove all elements from the list
print(nums)