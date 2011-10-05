#!/usr/bin/env python
# -*- coding=utf-8

TITLE = 0
SPEAKER = 1
DATETIME = 2

def break_line(s):
    lines = []
    line = ''
    x = 0
    for word in s.split():
        x += len(word) + 1
        if x > 45:
            lines.append(line.strip())
            x = 0
            line = ''
        line += ' ' + word

    lines.append(line.strip())
    if len(lines) == 1:
        lines.append('')
    return lines

def parse_palestras(filename='palestras.xml'):
    import re
    from BeautifulSoup import BeautifulStoneSoup
    import HTMLParser

    parser = HTMLParser.HTMLParser()

    palestras_file = open(filename)
    palestras_xml = palestras_file.read()
    palestras_file.close()
    palestras_soup = BeautifulStoneSoup(palestras_xml,
            convertEntities=BeautifulStoneSoup.HTML_ENTITIES)

    palestras_itens = palestras_soup.findAll('entry')
    palestrante_re = re.compile('(?<=<br>Onde:).+',re.M)
    horario_re = re.compile('\d{2} de out de 2010 \d{2}:\d{2} a \d{2}:\d{2}')

    palestras = []
    for i in palestras_itens:
        palestras.append((break_line(parser.unescape(i.title.contents[0])),
                         palestrante_re.findall(parser.unescape(i.summary.contents[0]))[0],
                         horario_re.findall(i.summary.contents[0])[0],))
    return palestras

def process_files(filename, lectures):
    fileobj = file(filename)
    model_svg = fileobj.read()
    fileobj.close()
    for lecture in lectures:
        title = [x.replace('&','&amp;') for x in lecture[TITLE]]
        print ' '.join(title)
        suffix = title[0][0]
        lecture_file_name = lecture[DATETIME].replace(' ','_').lower()
        lecture_file_name = lecture_file_name.replace(':','-').lower()
        lecture_file_name = '{0}-{1}.svg'.format(suffix,lecture_file_name)

        title[0] = title[0].replace('A: ','')
        title[0] = title[0].replace('B: ','')
        #xml_content = model_svg.replace('Title',title[0].encode('utf-8'))
        xml_content = model_svg.replace('Title',title[0])
        if len(title) > 1:
            #xml_content = xml_content.replace('Line1',title[1].encode('utf-8'))
            xml_content = xml_content.replace('Line1',title[1])
        xml_content = xml_content.replace('Line2',
                                          lecture[SPEAKER])
                                          #lecture[SPEAKER].encode('utf-8'))
        lecture_file_obj = file(lecture_file_name,'w')
        lecture_file_obj.write(xml_content)
        lecture_file_obj.close()

def command_line_parse():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename", default="modelo.svg",
                          help="SVG base Model", metavar="FILE")

    (options, args) = parser.parse_args()
    return options.filename

def main(filename):
    lectures = parse_palestras()
    process_files(filename,lectures)

if __name__ == '__main__':
    filename = command_line_parse()
    main(filename)
