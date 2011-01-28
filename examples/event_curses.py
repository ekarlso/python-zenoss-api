# Zenoss-3.0.x JSON API Example (python)
#
# Curses-based event console.
#
# A very simple example showing use of the Zenoss JSON API. Program initializes
# the screen, and fetches the top events from a Zenoss server. The events are
# displayed in decending severity, with severities color-coded. Events update
# every 5 seconds or so. Use 'q' or 'Q' to quit.

import curses
import time
import texttable
import zenoss_api

def main(cw):
    # Set up colors
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
    cw.nodelay(1)

    # Initialize Zenoss API connection
    z = zenoss_api.ZenossAPIExample()

    cycles = 21
    # Quit on 'q' or 'Q'
    while cw.getch() not in [ord(x) for x in ['q', 'Q']]:
        # Only update every 20 cycles (20 * .25 seconds = 5 seconds)
        if cycles > 20:
            # Get events from Zenoss
            rawEvents = z.get_events()['events']

            # 'Clean' events list, initialized with title row
            events = [['Device', 'Component', 'Summary', 'Event Class']]
            # Initialize title row color to 0 (white on black)
            colors = [0]
            for x in rawEvents:
                # Iterate through raw event data, and pull the rows we want
                events.append([x['device']['text'], x['component']['text'],
                               x['summary'], x['eventClass']['text']])
                # Append the appropriate color
                colors.append(int(x['severity']))
            # Reverse colors as we will be popping off the end
            colors.reverse()

            # Setup the pretty table, getting a list of row strings
            height, width = cw.getmaxyx()
            table = texttable.Texttable(max_width=width)
            table.add_rows(events, True)
            tableCols = table.draw().split('\n')

            # Erase the screen
            cw.erase()
            currentColor = 0
            for column in range(height):
                # Change the color if we encounter a new row
                if tableCols[column][0] == '+':
                    currentColor = colors.pop()
                # Print the row to the screen
                cw.addstr(column, 0, tableCols[column],
                          curses.color_pair(currentColor if
                          tableCols[column][0] != '+' else 0))
            cycles = 0

        cycles += 1
        time.sleep(.25)

curses.wrapper(main)
