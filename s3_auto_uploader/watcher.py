import logging

from watchdog.events import FileSystemEventHandler

from s3_auto_uploader.s3 import S3Uploader


class FSWatcherEventHandler(FileSystemEventHandler):

    def __init__(self, bucket, patterns=None):
        super(FSWatcherEventHandler, self).__init__()
        self.bucket = bucket
        self.patterns = ('xml', 'txt')

    def on_created(self, event):
        super(FSWatcherEventHandler, self).on_modified(event)

        if event.is_directory:
            return

        if event.src_path.lower().endswith(self.patterns):
            logging.info("Created  %s", event.src_path)

            file_name = event.src_path.split('/')[-1]
            s3_uploader = S3Uploader(bucket=self.bucket)
            s3_url = s3_uploader.upload(event.src_path, file_name)

            logging.info("File Uploaded.")
            logging.info("S3 URL: {}.".format(s3_url))
