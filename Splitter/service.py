# import logging
# from logging.config import fileConfig
# logging.config.fileConfig('logging.ini')

from Splitter import Splitter
import os

if __name__ == '__main__':
    print 'Declaring the services'
    services = list()
    host = os.environ.get("RABBIT_HOST")
    services.append(Splitter(host))

    print 'Staring the services'
    for service in services:
        service.start()

    print 'Waiting for the services to terminate'
    for service in services:
        print 'Waiting for service {}'.format(service.__class__.__name__)
        service.wait_for()

    print 'Done.'
