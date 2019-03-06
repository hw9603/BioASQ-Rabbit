# import logging
# from logging.config import fileConfig
# logging.config.fileConfig('logging.ini')

from CoreMMR import CoreMMR
from SoftMMR import SoftMMR
from HardMMR import HardMMR

if __name__ == '__main__':
    print 'Declaring the services'
    services = list()
    host = "ec2-13-58-28-131.us-east-2.compute.amazonaws.com"
    services.append(CoreMMR(host))
    # services.append(SoftMMR())
    # services.append(HardMMR())

    print 'Staring the services'
    for service in services:
        service.start()

    print 'Waiting for the services to terminate'
    for service in services:
        print 'Waiting for service {}'.format(service.__class__.__name__)
        service.wait_for()

    print 'Done.'
