from person import Personnel
from staff import Teacher


if __name__ == '__main__':
    # Create a personnel list
    personnel_list = Personnel()

    teacher_1 = Teacher(personnel_list.get_staff_id(), 'Anna Andersson', '1970-10-05', ['Math', 'English'])
    teacher_1.set_working_hours(start=8, finish=17)

    teacher_1.schedule.add_lesson(teacher_1, 2, teacher_1.teaching_subjects[1], '10.30-12.00')

    # print(teacher_1.working_hours)
    #
    # personnel_list.staff.append(teacher_1)
    #
    # print(f'ID: {teacher_1.id}, Name: {teacher_1.name}, Birthday: {teacher_1.birthdate}, Dict: {teacher_1.__dict__}')
    # print(personnel_list)
    print(teacher_1.schedule.schedule['10.30-12.00'].subject)



