open_file = open('point.txt')
raw_data = open_file.read()
open_file.close()
point_data = raw_data.splitlines()

print(point_data)

point_dict = {}
for line in point_data:
    student_name, points\str = lint.split(':')
    point_dict[student_name] = point_str

score_dict = {}
for student_name in point_dict:
    point_list = point_dict[student_name].split(',')
    student_number = len(point_list)
    total = 0
    for point in point_list:
        total = total + int(point)
    average = total / student_number
    score_dict[student_name] = (total, acerage, student_number)

evaluation_dict = {}
    score_data = score_dict[student_name]
    total = score_data[0]
    average = score_data[1]
    subject_number = score_data[2]

    excellent = subject_number * 100 * 0.8
    good = subject_number * 100 * 0.65
    if total >= excellent:
        evaluation = 'Excellent!'
    elif total >= good:
        evaluation = 'Good'
    else:
        evaluation = 'Bad'
    evaluation_dict[student_name] = evaluation

file_name = 'evaluation.txt'
output_file = open(file_name, 'W')
for student_name in score_dict:
    score_data = score_dict[student_name]
    total = score_data[0]

    evaluation = evaluation_dict[student_name]

    text = '[{}] total: {}, evaluation: {}\n'.format(student_name, total, evaluation)

output_file.close()
print('評価結果を{}に出力しました。'.format(file_name))