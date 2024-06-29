Priority = input(' Priority high/medium/low:').lower()
Task = input('Enter your task:').lower()
Time_bound =input('Is it time bound?:').lower()
match Priority:
    case 'high':
        if Time_bound =='yes': 
            print(f'{Task} is a {Priority} priority task that requires immediate attention')
    case 'medium':
        if time_bound =='yes':
            print(f'{Task} is a {Priority} priority task and requires your seious attention')
        else:
            print(f'{Task} is a {Priority} priority task with no time bound therefore requires some level attention')
    case 'low':
        if Time_bound =='no':
            print(f'{Task} is a {priority} task. Consider completing it when you have free time')
        else:
            print(f'{Task} is a {Priority} priority task with time bound therefore requires some level attention')
            
    case _:
        print('Relax, there are no important tasks for you today')
