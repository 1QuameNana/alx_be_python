priority = input(' Priority high/medium/low:').lower()
task = input('Enter your task:').lower()
time_bound =input('Is it time bound?:').lower()
match priority:
    case 'high':
        if time_bound =='yes': 
            print(f'{task} is a {priority} priority task that requires immediate attention')
    case 'medium':
        if time_bound =='yes':
            print(f'{task} is a {priority} priority task and requires your seious attention')
        else:
            print(f'{task} is a {priority} priority task with no time bound therefore requires some level attention')
    case 'low':
        if time_bound =='no':
            print(f'{task} is a {priority} task. Consider completing it when you have free time')
        else:
            print(f'{task} is a {priority} priority task with time bound therefore requires some level attention')
            
    case _:
        print('Relax, there are no important tasks for you today')
