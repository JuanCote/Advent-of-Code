# switch a given range of lights. Task 1 - turn on, task 2 - turn off, task 3 - toggle
def toggle_lights(start_point: tuple, end_point: tuple, task: int):
    start_x, start_y, end_x, end_y = int(start_point[0]), int(start_point[1]), int(end_point[0]), int(end_point[1])
    for n in range(start_y, end_y+1):
        for j in range(start_x, end_x + 1):
            if task == 1:
                all_lights[(j, n)] = True
            elif task == 2:
                all_lights[(j, n)] = False
            elif task == 3:
                all_lights[(j, n)] = not all_lights[(j, n)]


# get number of task from string
def get_task(string: str):
    if string.startswith('turn on'):
        return 1
    elif string.startswith('turn off'):
        return 2
    elif string.startswith('toggle'):
        return 3


with open('day6.txt') as file:
    text = file.read()

text = text.split('\n')

all_lights = dict()
for i in range(0, 1000):
    for k in range(0, 1000):
        all_lights.update({(k, i): False})

for string in text:
    task = get_task(string)
    start_point, end_point = tuple(string.split(' ')[-3].split(',')), tuple(string.split(' ')[-1].split(','))
    toggle_lights(start_point, end_point, task)

result = [x for x in all_lights if all_lights[x] is True]
print(len(result))
