def add_score(subject_score, subject, score) :
    if subject != "" and score >= 0:
        subject_score[subject] = score
        return subject_score
    else :
        print("Invalid")
        exit()

print(add_score({'Math': 90, 'Science': 85}, 'English', 88))

