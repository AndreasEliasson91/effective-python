from person import Personnel
from staff import Teacher


if __name__ == '__main__':
    # Create a personnel list
    personnel_list = Personnel()

    teacher_1 = Teacher('Anna Andersson', '1970-10-05', ['Math', 'English'])
    teacher_1.id = personnel_list.get_staff_id()
    teacher_1.set_working_hours(start=8, finish=17)
    teacher_1.schedule = {
        '8.00-10.00': teacher_1.teaching_subjects[0],
        '10.00-10.30': 'Break',
        '10.30-12.00': teacher_1.teaching_subjects[1]
    }

    print(teacher_1.working_hours)

    personnel_list.staff.append(teacher_1)

    print(f'ID: {teacher_1.id}, Name: {teacher_1.name}, Birthday: {teacher_1.birthday}, Dict: {teacher_1.__dict__}')
    print(personnel_list)
    print(teacher_1.schedule)
