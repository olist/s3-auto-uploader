from watchdog.events import FileSystemEventHandler


class FSWatcherEventHandler(FileSystemEventHandler):

    def __init__(self, patterns=None, ):
        super(FSWatcherEventHandler, self).__init__()
        self.patterns = ('xml', 'txt')

    def on_created(self, event):
        super(FSWatcherEventHandler, self).on_modified(event)

        if event.is_directory:
            return

        if event.src_path.lower().endswith(self.patterns):
            logging.info("Created  %s", event.src_path)

            file_name = event.src_path.split('/')[-1]
            s3_uploader = S3Uploader(bucket=settings.S3_CONFIG['bucket'])
            s3_url = s3_uploader.upload(event.src_path, file_name)

            logging.info("File Uploaded.")
            logging.info("S3 URL: {}.".format(s3_url))