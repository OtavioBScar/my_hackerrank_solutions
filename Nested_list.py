if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    scores = []
    for student in records:
        score = student[1]
        scores.append(score)
    
    scores.sort()
    lowest = scores[0]
    second_lowest = ""
    
    for score in scores:
        if score > lowest:
            second_lowest = score
            break
    
    students = []
    for student in records:
        if student[1] == second_lowest:
            students.append(student[0])
    
    students.sort()
    for student in students:
        print(student)