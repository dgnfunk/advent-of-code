from os.path import dirname, join

def day3_solution():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")

    with open(file_path, 'r') as f:
        assignments =  []
        assignments_overlap =  []
        for line in f:
            clean_line = line.rstrip()
            rooms_split = clean_line.split(',')
            assert len(rooms_split) == 2, F'Elves should be compare in pairs'
            ranges = [rooms.split('-') for rooms  in rooms_split]
            assert len(ranges) == 2, F'Rooms should have a start and end'

            elves_rooms = []
            for room in ranges:
                start = int(room[0])
                end = int(room[1])

                assert start >= 0, 'Should be a valid int for the start of the range'
                assert end >= 0, 'Should be a valid int for the end of the range'

                current_range = range(start, end+1)
                elves_rooms.append(set(current_range))

            assert len(elves_rooms) == 2, 'Elves must be pair by two'
            rooms_subset = None
            if elves_rooms[0].issubset(elves_rooms[1]):
                rooms_subset = elves_rooms[0]
            elif elves_rooms[1].issubset(elves_rooms[0]):
                rooms_subset = elves_rooms[1]

            room_intersection = elves_rooms[0] & elves_rooms[1]
            if len(room_intersection) > 0:
                assignments_overlap.append(room_intersection)
            
            elves_rooms = []
            if rooms_subset is not None:
                assignments.append(rooms_subset)

        print('Assignments', len(assignments))
        print('Assignments Overlap', len(assignments_overlap))

if __name__ == '__main__':
    day3_solution()