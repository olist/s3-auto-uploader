import time
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



class FSWatcherEventHandler(FileSystemEventHandler):

    def __init__(self, patterns=None):
        super(MonitoringChangingEventHandler, self).__init__()
        self.patterns = ('xml', 'txt')

    def on_created(self, event):
        super(MonitoringChangingEventHandler, self).on_modified(event)

        if event.is_directory:
            return

        if event.src_path.lower().endswith(self.patterns):
            logging.info("Created  %s", event.src_path)

            file_name = event.src_path.split('/')[-1]
            s3_uploader = S3Uploader(bucket=settings.S3_CONFIG['bucket'])
            s3_url = s3_uploader.upload(event.src_path, file_name)

            logging.info("File Uploaded.")
            logging.info("S3 URL: {}.".format(s3_url))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = settings.MONITORING_PATH
    event_handler = MonitoringChangingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
