def add_score(subject_score, subject, score) :
    if subject != "" and score >= 0:
        subject_score[subject] = score
        return subject_score
    else :
        print("Invalid")
        exit()

def calc_average_score(subject_score):
    if len(subject_score) == 0:
        return "0.00"
    total_score = sum(subject_score.values())
    count = len(subject_score)
    average = total_score / count
    avg = "{:.2f}".format(average)
    return avg

print(calc_average_score({'Math': 90, 'Science': 80, 'English': 70}))