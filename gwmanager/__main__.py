# -*- coding: utf-8 -*-
import sys
import getopt
from robot import Robot


if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[2:], "p:d:", ["port="])
    except getopt.GetoptError:
        print("Wrong usage!")
        sys.exit(2)

    port = None
    for opt, arg in opts:
        if opt in ('-p', '--port'):
            port = arg

    if port is None:
        # A porta é obrigatória
        print("Port not found!")
        sys.exit(2)

    bot = Robot(port=port)

    if sys.argv[1] == 'start':
        try:
            bot.start()
        except (KeyboardInterrupt, SystemExit) as e:
            bot.stop()
            sys.exit(0)
    elif sys.argv[1] == 'stop':
        bot.stop()
    else:
        print("Wrong command %s" % sys.argv[1])
        sys.exit(2)
