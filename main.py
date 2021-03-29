import logging
from os import mkdir

import requests

FLIBUSTA_URL = 'https://flibusta.is/'

# Tables backups from flibusta.
# https://flibusta.is/sql/
TABLES_BACKUP_LIST = [
    'lib.libavtor.sql.gz',
    'lib.libtranslator.sql.gz',
    'lib.libavtorname.sql.gz',
    'lib.libbook.sql.gz',
    'lib.libfilename.sql.gz',
    'lib.libgenre.sql.gz',
    'lib.libgenrelist.sql.gz',
    'lib.libjoinedbooks.sql.gz',
    'lib.librate.sql.gz',
    'lib.librecs.sql.gz',
    'lib.libseqname.sql.gz',
    'lib.libseq.sql.gz'
]

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)


def get_backup_files():
    sql_dir = 'sql_backups'
    try:
        mkdir(sql_dir)
    except FileExistsError:
        pass
    log.info(f"Downloading {len(TABLES_BACKUP_LIST)} files into {sql_dir}")
    for table in TABLES_BACKUP_LIST:
        log.info(f"Downloading file {table}.")
        url = f"{FLIBUSTA_URL}/sql/{table}"
        r = requests.get(url, allow_redirects=True)
        open(f"{sql_dir}/{table}", 'wb').write(r.content)


if __name__ == '__main__':
    get_backup_files()
