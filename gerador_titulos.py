#!/usr/bin/env python
# -*- coding=utf-8

TITLE = 0
SPEAKER = 1
HOUR = 2

def process_files(filename, lectures):
    fileobj = file(filename)
    xml_content = fileobj.read()
    fileobj.close()
    for lecture in lectures:
        lecture_file_name = lecture[0].replace(' ','_').lower()
        lecture_file_name = '{0}.svg'.format(lecture_file_name)
        lecture_file_name = lecture_file_name.replace('_&_','_')
        title = lecture[TITLE].replace('&','&amp;')
        xml_content = xml_content.replace('Título da Palestra',title)
        xml_content = xml_content.replace('Palestrante',lecture[SPEAKER])
        xml_content = xml_content.replace('Horário',lecture[HOUR])
        lecture_file_obj = file(lecture_file_name,'w')
        lecture_file_obj.write(xml_content)
        lecture_file_obj.close()

def command_line_parse():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                          help="SVG base Model", metavar="FILE")

    (options, args) = parser.parse_args()
    return options.filename

def main(filename):
    lectures = [('Cerimônia de Abertura & Infra-Estrutura DINF C3SL UFPR',
                 'Luis Carlos Erpen de Bona',
                 'October 21, 2010, 9:00am – 9:45am')]
    process_files(filename,lectures)

if __name__ == '__main__':
    filename = command_line_parse()
    main(filename)
