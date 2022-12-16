from os.path import dirname, join

def get_stream():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")
    raw_move = None

    with open(file_path, 'r') as f:
        stream = f.readline()
        clean_line = stream.rstrip()
        raw_move = [*clean_line]
        
    return raw_move

def get_end_char_id(stream, end_char_id):
    for idx, char in enumerate(stream):
        # start of message
        end_idx = idx + end_char_id
        stream_packet = set(stream[idx:end_idx])

        if len(stream_packet) == end_char_id:
            # print('found packet', stream_packet, idx, end_idx)
            return end_idx

def day6_solution(stream):
    print('Get for packet', get_end_char_id(stream, 4))
    print('Get for messages', get_end_char_id(stream, 14))

if __name__ == '__main__':
    day6_solution(get_stream())