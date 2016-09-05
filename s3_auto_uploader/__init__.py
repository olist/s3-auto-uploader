import logging
import time

from watchdog.observers import Observer

from s3_auto_uploader.watcher import FSWatcherEventHandler


__author__ = 'Olist Developers'
__email__ = 'developers@olist.com'
__version__ = '0.1.0'


def auto_uploader(path, bucket):

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    event_handler = FSWatcherEventHandler(bucket=bucket)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
