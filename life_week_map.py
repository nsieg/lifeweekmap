style(stroke_width=0.2, fill='#ffffff', font_family='Arial', font_size='3px')

START_GRID_X, START_GRID_Y = 12,12
START_TEXT_X, START_TEXT_Y = 5, 8

for year in range(90):
	if year % 5 == 0:
		text('%g' % year, (START_TEXT_X, START_GRID_Y + year * 3.1 + 1), fill='#000000')
	for week in range(52):		
		if year == 0 and (week + 1) % 5 == 0:
			text('%g' % (week + 1), (START_GRID_X + week * 3.74 - 1, START_TEXT_Y), fill='#000000')
		rect((-1, -1), (1, 1), transform='translate(%g, %g)' % (START_GRID_X + week * 3.75, START_GRID_Y + year * 3.1))