
Task = input('Enter your task:')

Time_bound =input('Is it time-bound? (yes/no):')

Priority = input('Priority (high/medium/low):')

match Priority:
    case 'high':
        if Time_bound =='yes': 
            print(f' Reminder:{Task} is a {Priority} priority task that requires immediate attention')
    case 'medium':
        if Time_bound =='yes':
            print(f'Reminder:{Task} is a {Priority} priority task and requires your seious attention')
        else:
            print(f'REminder:{Task} is a {Priority} priority task with no time bound therefore requires some level attention')
    case 'low':
        if Time_bound =='no':
            print(f'Note:{Task} is a {priority} task. Consider completing it when you have free time')
        else:
            print(f'Note:{Task} is a {Priority} priority task with time bound therefore requires some level attention')
            
    case _:
        print('Note: Relax, there are no important tasks for you today')
