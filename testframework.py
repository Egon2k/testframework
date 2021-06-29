#!/usr/bin/python
import PySimpleGUI as sg

class logger:
    def get_time(self):
        return 'time'
    
    def get_date(self):
        return 'date'

def open_file():
    file = sg.popup_get_file('Open testframework file',
                             history = True,
                             size = (70, None),
                             file_types = (("Excel CSV", "*.csv"),)
                             )

    f = open(file, 'r+')
    filecontent = f.read().splitlines(True)
    f.close()

    return filecontent

def execute_message(parameter):
    sg.popup(parameter[0],
             title = 'Message')

def execute_wait(parameter):
    sg.popup('waiting for ' + parameter[0] + ' seconds - the procedure will continue afterwards...',
             title = 'Waiting...',
             auto_close = True,
             auto_close_duration = int(parameter[0]))

def execute_cmd(cmd, parameter):
    if cmd == "MESSAGE":
        execute_message(parameter)
    elif cmd == "WAIT":
        execute_wait(parameter)


def process_file(filecontent):
    if filecontent[0].startswith('TESTFRAMEWORK_FILE'):
        for line in filecontent[1:]:
            if len(line) > 2:
                try:
                    split_line = line[:-1].split(';')
                    cmd = split_line[0]
                    parameter = split_line[1:]
                except:
                    print('error in line: ' + line)
                    break

                execute_cmd(cmd, parameter)

    else:
        sg.popup('no valid testframework file')


if __name__ == "__main__":
    filecontent = open_file()
    process_file(filecontent)