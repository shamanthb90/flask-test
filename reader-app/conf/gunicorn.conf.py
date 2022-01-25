import multiprocessing
import os

import gevent.monkey
from gunicorn import glogging

# monkey-patch gevent
gevent.monkey.patch_all()

# https://github.com/benoitc/gunicorn/blob/master/examples/example_config.py
#
# Server socket
#
#   bind - The socket to bind.
#
#       A string of the form: 'HOST', 'HOST:PORT', 'unix:PATH'.
#       An IP is a valid HOST.
#
#   backlog - The number of pending connections. This refers
#       to the number of clients that can be waiting to be
#       served. Exceeding this number results in the client
#       getting an error when attempting to connect. It should
#       only affect servers under significant load.
#
#       Must be a positive integer. Generally set in the 64-2048
#       range.
#
bind = '0.0.0.0:' + os.getenv('PORT', '8000')
backlog = 256

# Load application code before the worker processes are forked.
#
# By preloading an application you can save some RAM resources
# as well as speed up server boot times. Although, if you defer
# application loading to each worker process, you can reload your
# application code easily by restarting workers.
preload_app = os.getenv('GUNICORN_PRELOAD_APP', 'false')
preload_app = preload_app.lower() in ['1', 'true', 't', 'yes', 'y'] if preload_app else False

#
# Worker processes
#
#   workers - The number of worker processes that this server
#       should keep alive for handling requests.
#
#       A positive integer generally in the 2-4 x $(NUM_CORES)
#       range. You'll want to vary this a bit to find the best
#       for your particular application's work load.
#       The suggested number of workers is (2*CPU)+1.
#
#   worker_class - The type of workers to use. The default
#       sync class should handle most 'normal' types of work
#       loads. You'll want to read
#       http://docs.gunicorn.org/en/latest/design.html#choosing-a-worker-type
#       for information on when you might want to choose one
#       of the other worker classes.
#
#       A string referring to a Python path to a subclass of
#       gunicorn.workers.base.Worker. The default provided values
#       can be seen at
#       http://docs.gunicorn.org/en/latest/settings.html#worker-class
#
#   threads - The number of worker threads for handling requests. This will
#       run each worker with the specified number of threads.
#       A positive integer generally in the 2-4 x $(NUM_CORES) range
#
#   worker_connections - For the eventlet and gevent worker classes
#       this limits the maximum number of simultaneous clients that
#       a single process can handle.
#
#       A positive integer generally set to around 1000.
#
#   timeout - If a worker does not notify the master process in this
#       number of seconds it is killed and a new worker is spawned
#       to replace it.
#
#       Generally set to thirty seconds. Only set this noticeably
#       higher if you're sure of the repercussions for sync workers.
#       For the non sync workers it just means that the worker
#       process is still communicating and is not tied to the length
#       of time required to handle a single request.
#
workers = os.getenv('GUNICORN_NUM_WORKERS')
workers = int(workers) if workers else multiprocessing.cpu_count()
# threads = 4 * multiprocessing.cpu_count()
worker_class = 'gevent'
worker_connections = 256
timeout = 5 * 60

#
# Server mechanics
#
#   pidfile - The path to a pid file to nurse
#
#       A path string or None to not nurse a pid file.
#
pidfile = '/tmp/app.pid'

# worker_tmp_dir - A directory to use for the worker heartbeat temporary file
# If not set, the default temporary directory will be used.
worker_tmp_dir = '/dev/shm'

#
#   Logging
#
#   logfile - The path to a log file to nurse to.
#
#       A path string. "-" means log to stdout.
#
#   loglevel - The granularity of log output
#
#       A string of "debug", "info", "warning", "error", "critical"
#
logfile = '-'
loglevel = 'info'
accesslog = '-'
errorlog = '-'
access_log_format = 'remote_ip=%(h)s user_name=%(u)s method=%(m)s path="%(U)s" request_params={%(q)s} protocol=%(H)s status=%(s)s response_time=%(L)s response_length=%(b)s referer="%(f)s" user_agent="%(a)s"'

# logconfig - The log config file to use. Gunicorn uses the standard Python
# logging modul’s Configuration file format.
logconfig = None
glogging.Logger.error_fmt = '[%(asctime)s] [%(process)d:%(processName)s] %(levelname)s [%(name)s:%(funcName)s.%(lineno)d] %(message)s'
glogging.Logger.access_fmt = '[%(asctime)s] [%(process)d:%(processName)s] %(levelname)s [%(name)s:%(funcName)s.%(lineno)d] %(message)s'
glogging.Logger.syslog_fmt = '[%(asctime)s] [%(process)d:%(processName)s] %(levelname)s [%(name)s:%(funcName)s.%(lineno)d] %(message)s'
glogging.Logger.datefmt = '%d/%b/%Y:%H:%M:%S %z'


def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)


def pre_fork(server, worker):
    # Gunicorn preload flag not working with PyTorch: https://github.com/pytorch/pytorch/issues/49555
    # Solution: https://discuss.pytorch.org/t/multiple-networks-running-in-parallel-on-different-cpus/70482/3
    # import torch
    # torch.set_num_threads(1)
    # torch.set_num_interop_threads(1)
    pass


def pre_exec(server):
    server.log.info("Forked child, re-executing.")


def when_ready(server):
    server.log.info("Server is ready. Spawning workers")


def worker_int(worker):
    worker.log.info("worker received INT or QUIT signal")


def worker_abort(worker):
    worker.log.info("worker received SIGABRT signal")
