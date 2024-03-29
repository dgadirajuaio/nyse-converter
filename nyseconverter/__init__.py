import os
import glob
import logging
from dask import dataframe as dd


def main():
    log_file_path = os.environ['LOG_FILE_PATH']
    src_dir = os.environ['SRC_DIR']
    logging.basicConfig(
        filename=log_file_path,
        level=logging.INFO,
        format='%(levelname)s %(asctime)s %(message)s',
        datefmt='%Y-%m-%d %I:%M:%S %p'
    )
    logging.info('File format conversion started')
    src_file_pattern = os.environ.setdefault('SRC_FILE_PATTERN', 'NYSE*.txt.gz')
    # tgt_dir = os.environ['TGT_DIR']
    src_file_names = sorted(glob.glob(f'{src_dir}/{src_file_pattern}'))
    tgt_file_names = [
        file.replace('txt', 'json').replace('nyse_data', 'nyse_json') 
        for file in src_file_names
    ]
    df = dd.read_csv(
        src_file_names,
        names=['ticker', 'trade_date', 'open_price', 'low_price',
               'high_price', 'close_price', 'volume'],
        blocksize=None
    )
    logging.info('Data Frame is created and will be written in JSON format')
    df.to_json(
        tgt_file_names,
        orient='records',
        lines=True,
        compression='gzip'
    )
    logging.info('File format conversion completed')


if __name__ == '__main__':
    main()
