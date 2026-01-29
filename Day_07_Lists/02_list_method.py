marks = [54, 86, 98, 56, 32]
extra_marks = [25, 28,100]

print(marks)

marks.append(28) #This will change the original list
marks.insert(1, 99)
marks.remove(86)
marks.reverse()   
marks.sort()      
marks.pop()
marks.extend(extra_marks)

print(marks)