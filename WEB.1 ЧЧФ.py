def human_read_format(size):
    my_list = ['Б', 'КБ', 'МБ', 'ГБ']
    count = 0
    while size > 1023:
        count += 1
        size = round(size / 1024)
    return f'{size}{my_list[count]}'
