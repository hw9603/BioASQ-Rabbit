from deiis.rabbit import Task, Message
from deiis.model import Serializer

from Concatenation import Concatenation
import os

if __name__ == "__main__":
    print 'Starting Tiler services.'
    host = os.environ.get("RABBIT_HOST")
    task = Concatenation(host)
    task.start()
    task.wait_for()


