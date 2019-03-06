from deiis.rabbit import Task, Message
from deiis.model import Serializer

from Concatenation import Concatenation


if __name__ == "__main__":
    print 'Starting Tiler services.'
    host = "ec2-13-58-28-131.us-east-2.compute.amazonaws.com"
    task = Concatenation(host)
    task.start()
    task.wait_for()


