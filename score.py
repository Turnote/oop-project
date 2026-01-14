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


subject = input("Input : ")
subject_collection = [x.strip() for x in subject.split("|")]
if len(subject_collection) != 3  :
    print("Invalid")
    exit()
else :
    subject = subject_collection[1].strip("'")
    subject_score = eval((subject_collection[0]))
    raw_score = subject_collection[2]
    if raw_score.isdigit():
        score = int(raw_score)
    else:
        score = float(raw_score)
#print(subject_score,score)
    result = add_score(subject_score,subject,score)
    avg = calc_average_score(subject_score)
    print(f"{result}, Average score: {avg}")
