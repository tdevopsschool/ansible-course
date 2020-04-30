#!/usr/bin/env python2

from workshop_ import WorkshopApplication

if __name__ == '__main__':
    app = WorkshopApplication(delay=600, valid=False)
    #app = WorkshopApplication(delay=10, valid=True)
    app.run()
