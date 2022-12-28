from os.path import dirname, join
import time
# first get all the commands identified
# then identify all the different types of components
# build the data structure and go through all the commands
# then set all the folders and after those files inside
# after that we will count and sum the size of the files
class Folder:
    def __init__(self, name, size, parent, children=[]) -> None:
        self.name = name
        self.size = size
        self.parent = parent
        self.children = children

    def __repr__(self):
        return f"/{self.name}:{self.size}"


class File:
    def __init__(self, name, size, parent) -> None:
        self.name = name
        self.size = size
        self.parent = parent

    def __repr__(self):
        return f"{self.name}:{self.size}"


class FileSystem:
    def __init__(self) -> None:
        self.root: Folder = None
        self.current = None

    def add_child(self, child, parent):
        if parent is not None and parent.children is not None:
            parent.children.append(child)

    def add_folder(self, folder: Folder, parent):
        if parent is None and self.root is None:
            self.root = folder
        else:
            if parent is not None:
                self.add_child(folder, parent)

    def go_to_parent(self):
        if self.current is not None and self.current.parent is not None:
            parent = self.current.parent
            self.current = parent

    def find_empty_folder(self, name, in_folder: Folder):
        if self.root is not None and name == self.root.name:
            return self.root

        if self.current is not None and name == self.current.name:
            return self.current

        if in_folder is not None and name == in_folder.name and len(in_folder.children) == 0:
            return in_folder

        if in_folder is None and self.root is not None:
            in_folder = self.root

        if in_folder is None:
            return None

        for folder in in_folder.children:
            if type(folder) is Folder:
                found = self.find_empty_folder(name, folder)
                if found is not None:
                    return found

    def find_folder_condition(self, in_folder: Folder, condition, folders):
        if condition(in_folder) is True and type(in_folder) == Folder:
            folders.append({ 'parent': in_folder.parent.name, 'name': in_folder.name, 'size': in_folder.size})

        for folder in in_folder.children:
            if type(folder) is Folder:
                self.find_folder_condition(folder, condition, folders)

    def set_current_folder(self, folder):
        if folder is not None:
            self.current = folder

    def get_size(self, current):
        if self.root is None:
            return 0

        if len(self.root.children) == 0:
            return 0

        current = self.root if current is None else current
        for item in current.children:
            if type(item) is File:
                item.parent.size += item.size
                print('File', item.name, item.parent.name, item.size)
            elif type(item) is Folder:
                self.get_size(item)
                item.parent.size += item.size
                print('Folder', item.name, item.parent.name, item.size)

    def __repr__(self):
        return f"Root: {self.root}"


class Cmd:
    def is_command(self, line) -> bool:
        return line[0] == '$'

    def perform_command(self, dir: FileSystem, command, arg, output) -> None:
        if command == 'cd':
            if arg == '..':
                dir.go_to_parent()
                return

            current_dir = dir.find_empty_folder(arg, dir.current)

            if current_dir is None and len(output) == 0:
                new_folder = Folder(name=arg, size=0, children=[], parent=dir.current)
                dir.add_folder(new_folder, dir.current)
                dir.set_current_folder(new_folder)
            else:
                dir.set_current_folder(current_dir)

        elif command == 'ls' and len(output) > 0:
            self.process_ls_command_output(output, dir)

    def process_ls_command_output(self, output, dir: FileSystem):
        for line in output:
            out = line.split(' ')
            if out[0] == 'dir':
                dir.add_folder(Folder(name=out[1], size=0, parent=dir.current, children=[]), dir.current)
            else:
                dir.add_child(File(name=out[1], size=int(out[0]), parent=dir.current), dir.current)

    def process_line(self, line, commands):
        if  self.is_command(line):
            command = line[2:]
            args = command.split(' ')
            commands.append((args, []))
        else:
            last_idx_added = len(commands) - 1;
            results = commands[last_idx_added][1]
            if results is not None:
                results.append(line)

    def process_commands(self, commands, dir: FileSystem):
        for command_line in commands:
            line = command_line[0]
            command = line[0] if len(line) > 0 else None
            arg = line[1] if len(line) == 2 else None
            output = command_line[1]

            self.perform_command(dir, command, arg, output)

    def get_commands(self, path):
        commands = []

        with open(path, 'r') as f:
            for line in f:
                clean_line = line.rstrip()
                self.process_line(clean_line, commands)
        return commands


def if_folder_condition(folder):
    if folder is None:
        return False

    if folder.size == 0:
        return False

    return folder.size <= 100000

if __name__ == '__main__':
    start_time = time.perf_counter()
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")

    cmd = Cmd()
    commands = cmd.get_commands(file_path)
    directory = FileSystem()
    cmd.process_commands(commands, directory)
    directory.get_size(None)

    folders = []
    directory.find_folder_condition(directory.root, if_folder_condition, folders)


    total = 0
    for folder in folders:
        total += folder['size']

    print('At most Folders Total', total)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"The execution time is: {execution_time}")