import logging
import boto3

from botocore.exceptions import ClientError


class S3Uploader(object):

    def __init__(self, bucket, expires_in=604800):
        super(S3Uploader, self).__init__()
        self.bucket = bucket
        self.expires_in = expires_in

    def _get_s3_client_resource(self, config_client=''):
        if config_client:
            return boto3.client('s3', config=config_client)
        return boto3.resource('s3')

    def _upload_file(self, data_file, bucket_key):
        s3_client = self._get_s3_client_resource()
        s3_client.Bucket(self.bucket).put_object(
            Key=bucket_key, Body=data_file)

    def _generate_url(self, bucket_key):

        s3_client = self._get_s3_client_resource(Config(signature_version='s3v4'))
        return s3_client.generate_presigned_url(
            ClientMethod='get_object',
            Params={'Bucket': self.bucket, 'Key': bucket_key},
            ExpiresIn=self.expires_in
        )

    def upload(self, src_path, file_name):
        data_file = open(src_path, 'rb')
        bucket_key = 'neogrid/{}'.format(file_name)

        try:
            self._upload_file(data_file, bucket_key)
        except ClientError as e:
            logging.error(e.response)

        try:
            url = self._generate_url(bucket_key)
        except ClientError as e:
            logging.error(e.response)

        return url