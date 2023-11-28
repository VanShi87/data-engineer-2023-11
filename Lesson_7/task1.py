import sys
def reducer():

    def output():
        if current_page:
            average_time = total_time / count
            print(f'{current_page} {average_time}')

    current_page = None
    total_time = 0
    count = 0
    for line in sys.stdin:
        page, time = line.strip().split()
        time = int(time)
        if current_page == page:
            total_time += time
            count += 1
        else:
            output()
            current_page = page
            total_time = time
            count = 1
    output()

reducer()