from datetime import datetime
from time import sleep
from pygame import mixer

def begin_lesson():
    print('Lesson begins.')
    mixer.music.play()

def ready_lesson():
    print('Lesson ready.')
    mixer.music.play()

def end_lesson():
    print('Lesson ends.')
    mixer.music.play()

def get_next_time(hm, times):
    next_times = [time for time in times if time > hm]
    if next_times == []:
        return min(lesson_begin_times)
    else:
        return min(next_times)

def time_diff(t1, t2):
    m1 = t1[0] * 60 + t1[1]
    m2 = t2[0] * 60 + t2[1]
    md = m1 + (0 if m1 >= m2 else 24 * 60) - m2
    return (md // 60, md % 60)

def ttos(t):
    return "%02d:%02d" % t

lessons = [
        ('08:30', '09:10'), ('09:20', '10:00'), ('10:10', '10:50'),
        ('11:00', '11:40'), ('11:50', '12:30'), ('12:40', '13:20'),
        ('13:30', '14:10'), ('14:20', '15:00'), ('15:10', '15:50'),
        ('16:00', '16:40'), ('16:50', '17:30'), ('17:40', '18:20')
    ]
    
lesson_begin_times = [tuple(map(int, lesson[0].split(':'))) for lesson in lessons]
lesson_ready_times = [(lesson[0], lesson[1] + 1) for lesson in lesson_begin_times]
lesson_end_times = [tuple(map(int, lesson[1].split(':'))) for lesson in lessons]

mixer.init()
mixer.music.load('bell.mp3')

while True:
    now = datetime.now()
    hm = (now.hour, now.minute)
    next_begin_time = get_next_time(hm, lesson_begin_times)
    next_ready_time = get_next_time(hm, lesson_ready_times)
    next_end_time = get_next_time(hm, lesson_end_times)
    ndiff = time_diff(next_begin_time, hm)
    next_time, diff, label = next_begin_time, ndiff, 'начало урока'
    ndiff = time_diff(next_ready_time, hm)
    if ndiff < diff:
        next_time, diff, label = next_ready_time, ndiff, 'урок готов'
    ndiff = time_diff(next_end_time, hm)
    if ndiff < diff:
        next_time, diff, label = next_end_time, ndiff, 'конец урока'
    print("Следующий звонок в %s (%s), через %s" % (ttos(next_time), label, ttos(diff)))
    if now.second < 3:
        if hm in lesson_begin_times:
            begin_lesson()
            sleep(5)
        elif hm in lesson_ready_times:
            ready_lesson()
            sleep(5)
        elif hm in lesson_end_times:
            end_lesson()
            sleep(5)
    sleep(1)
