from ResultsCollector import ResultsCollector
import os

if __name__ == '__main__':
    print 'Starting ResultsCollector'
    host = os.environ.get('RABBIT_HOST')
    task = ResultsCollector(host)
    task.start()
    print 'Waiting for the task to terminate.'
    task.wait_for()
    print 'Done.'
