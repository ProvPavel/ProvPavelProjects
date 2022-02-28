import os


def get_files_sizes():
    listdir = os.listdir()
    res = []
    for i in listdir:
        if os.path.isfile(i):
            my_list = ['Б', 'КБ', 'МБ', 'ГБ']
            count = 0
            size = os.path.getsize(i)
            while size > 1023:
                count += 1
                size = round(size / 1024)
            res.append(f'{size}{my_list[count]}')
    return '\n'.join(res)
