from ResultsCollector import ResultsCollector
import os

if __name__ == '__main__':
    print 'Starting ResultsCollector'
    # host = os.environ.get('RABBITMQ_HOST')
    host = "ec2-13-58-28-131.us-east-2.compute.amazonaws.com"
    task = ResultsCollector(host)
    task.start()
    print 'Waiting for the task to terminate.'
    task.wait_for()
    print 'Done.'
