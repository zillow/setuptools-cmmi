"""Unit tests for the main entry point."""
import os
import uuid

from setuptools.archive_util import unpack_archive
import shutil

from mock import patch, Mock
from setuptools_cmmi import process_cmmi


def test_cmmi_process():
    """Test CMMI process."""
    print "CMMI PROCESS!"

    rand_suffix = str(uuid.uuid1())

    temp_root_test_dest = os.getcwd() + "/setuptools_cmmi/tests/data/temp_test_dest-" \
                          + rand_suffix
    dest_dir = temp_root_test_dest + "/usr"
    temp_work_dir = os.getcwd() + "/setuptools_cmmi/tests/data/workdir-" + rand_suffix
    src_dist = os.getcwd() + "/setuptools_cmmi/tests/data/freetds-1.00.15.tar.gz"

    try:
        unpack_archive(src_dist, temp_work_dir)

        process_cmmi(dest_dir, temp_work_dir,
                     "--prefix={0} --disable-odbc --disable-apps --disable-server --disable-pool LDFLAGS='-Wl,-rpath,parts/usr/lib -Wl,-rpath,{0}/lib'"
                     .format(dest_dir), None)
    finally:
        if os.path.exists(temp_work_dir):
            shutil.rmtree(temp_work_dir)
        if os.path.exists(temp_root_test_dest):
            shutil.rmtree(temp_root_test_dest)
