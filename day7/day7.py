def processData(text_list):
    isInHere = ['/']
    folder_dictionary = {'/': 0, }
    for command in text_list:
        if command[0:4] == '$ cd':
            if command == '$ cd ..\n':
                isInHere.pop()
            elif command == '$ cd /\n':
                pass
            else:
                depth = len(isInHere)
                if depth > 0:
                    folder_dictionary[command[5:-1] + '_' + isInHere[-1]] = 0
                    isInHere.append(command[5:-1] + '_' + isInHere[-1])
                else:
                    folder_dictionary[command[5:-1]] = 0
                    isInHere.append(command[5:-1])

        if command[0].isnumeric():
            for directory in isInHere:
                folder_dictionary[directory] += int(command.split(' ')[0])
    return (folder_dictionary)


class Filesystem:
    def __init__(self, text_list):
        self.datadict = processData(text_list)

    def sub100k(self):
        sumvar = 0
        for key in self.datadict:
            if self.datadict[key] <= 100000:
                sumvar += self.datadict[key]
        return sumvar


def main():
    input_text = Filesystem(open('day7input.txt').readlines())

    print(input_text.sub100k())

    space_needed = 30000000 - (70000000 - input_text.datadict['/'])
    directory_to_delete = '/'
    for directory in input_text.datadict:
        if space_needed < input_text.datadict[directory] < input_text.datadict[directory_to_delete]:
            directory_to_delete = directory
    print(input_text.datadict[directory_to_delete])


if __name__ == '__main__':
    main()
