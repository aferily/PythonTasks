import os.path

def taskname_to_filename(taskname: str):
    filename = f'EdabitTasks/{taskname.lower().replace(' ', '_')}.py'
    if os.path.isfile(filename):
        return
    file = open(filename, 'w')
    file.close()

taskname = 'List of Multiples'
taskname_to_filename(taskname)