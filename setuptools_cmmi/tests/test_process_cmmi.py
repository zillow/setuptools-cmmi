"""Unit tests for the main entry point."""
import os

from mock import patch, Mock
from setuptools_cmmi import process_cmmi


def test_cmmi_process():
    """Test CMMI process."""
    print "CMMI PROCESS!"

    dest_dir = os.getcwd() + "/setuptools_cmmi/tests/data/temp_test_dest/usr"
    temp_work_dir = os.getcwd() + "/setuptools_cmmi/tests/data/workdir"

    process_cmmi(dest_dir, temp_work_dir,
                 "--prefix={0} --disable-odbc --disable-apps --disable-server --disable-pool LDFLAGS='-Wl,-rpath,parts/usr/lib -Wl,-rpath,{0}/lib'"
                 .format(dest_dir), None)
