import argparse


def format_text_block(height, width, text):
    try:
        s = open(text).readlines()
        a, b = [], []

        for i in s:
            if len(i) == 1 and i.find('\n') != -1:
                a.append(i)
            else:
                a.append(i.replace('\n', ''))
        for line in ''.join(a).split('\n'):
            for i in range(0, len(line), width):
                b.append(line[i:i + width])
            else:
                b.append('')
        return '\n'.join(b[:height])
    except Exception as e:
        return e


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--frame-height', type=int)
    parser.add_argument('--frame-width', type=int)
    parser.add_argument('filename', type=str)
    args = parser.parse_args()
    print(format_text_block(args.frame_height, args.frame_width, args.filename))
