__author__ = 'Blayne'

from src import PlayerInfo, ClubInfo
import xlsxwriter
import time

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('stats.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 20)
worksheet.set_column('J:J', 20)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

worksheet.write('A1', 'Name', bold)
worksheet.write('B1', 'Age', bold)
worksheet.write('C1', 'App', bold)
worksheet.write('D1', 'Goal', bold)
worksheet.write('E1', 'Assist', bold)
worksheet.write('F1', 'Yellow', bold)
worksheet.write('G1', 'Y/R', bold)
worksheet.write('H1', 'Red', bold)
worksheet.write('I1', 'Mins', bold)
worksheet.write('J1', 'Mins Played', bold)

lines = [line.strip() for line in open('players.txt')]
i = 1
for l in lines:
    start = time.clock()
    pi = PlayerInfo(l)

    ci = ClubInfo("http://www.transfermarkt.co.uk" + pi.get_club())

    # Write some numbers, with row/column notation.
    worksheet.write(i, 0, pi.get_name())
    worksheet.write(i, 1, pi.get_age())
    worksheet.write(i, 2, pi.get_app())
    worksheet.write(i, 3, pi.get_goal())
    worksheet.write(i, 4, pi.get_assist())
    worksheet.write(i, 5, pi.get_yellow())
    worksheet.write(i, 6, pi.get_yellred())
    worksheet.write(i, 7, pi.get_red())
    worksheet.write(i, 8, int(pi.get_mins()))
    worksheet.write(i, 9, (int(pi.get_mins()) / float(ci.get_mins())) * 100)
    worksheet.write(i, 10, l)
    i += 1
    end = time.clock()
    print end - start
workbook.close()

