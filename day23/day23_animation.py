import os, time


def main():
    os.chdir('./animation_frames')
    os.environ['TERM'] = 'xterm-256color'

    frames = [f'{i}.txt' for i, _ in enumerate(os.listdir())]

    for frame in frames:
        os.system('clear')
        with open(frame, 'r') as file:
            print(file.read())
        time.sleep(.05)


if __name__ == '__main__':
    main()