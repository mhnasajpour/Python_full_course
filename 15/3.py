def take_off(id, bounds_status, all_airplain, airplains_take_off, airplains_landing):
    if id not in all_airplain:
        return 'YOU ARE NOT HERE'
    if id in airplains_landing:
        return 'YOU ARE LANDING NOW'
    if id in airplains_take_off:
        return 'YOU ARE TAKING OFF'
    if False not in bounds_status:
        return 'NO FREE BOUND'
    airplains_take_off.append(id)
    bounds_status[bounds_status.index(False)] = id


def landing(id, bounds_status, all_airplain, airplains_take_off, airplains_landing):
    if id in all_airplain and id not in airplains_take_off and id not in airplains_landing:
        return 'YOU ARE HERE'
    if id in airplains_take_off:
        return 'YOU ARE TAKING OFF'
    if id in airplains_landing:
        return 'YOU ARE LANDING NOW'
    if id not in all_airplain and False not in bounds_status:
        return 'NO FREE BOUND'
    airplains_landing.append(id)
    all_airplain.append(id)
    bounds_status.reverse()
    bounds_status[bounds_status.index(False)] = id
    bounds_status.reverse()


def plane_status(id, all_airplain, airplains_take_off, airplains_landing):
    if id not in all_airplain:
        return '4'
    if id in airplains_take_off:
        return '2'
    if id in airplains_landing:
        return '3'
    return '1'


def bound_state(id, bounds_status):
    id = int(id) - 1
    return bounds_status[id] if bounds_status[id] else 'FREE'


airplains_count, bounds_many = list(map(int, input().split()))
all_airplain = [input() for _ in range(airplains_count)]
commands_count = int(input())

bounds_status = [False] * bounds_many
airplains_take_off = []
airplains_landing = []

for _ in range(commands_count):
    command, id = input().split()
    if command == 'TAKE-OFF':
        result = take_off(id, bounds_status, all_airplain, airplains_take_off, airplains_landing)
        if result:
            print(result)
    elif command == 'LANDING':
        result = landing(id, bounds_status, all_airplain, airplains_take_off, airplains_landing)
        if result:
            print(result)
    elif command == 'PLANE-STATUS':
        print(plane_status(id, all_airplain, airplains_take_off, airplains_landing))
    elif command == 'BAND-STATUS':
        print(bound_state(id, bounds_status))
