"""Unit tests for the main entry point."""
import setuptools_cmmi

from mock import patch, Mock

@patch("setuptools_cmmi.process_cmmi")
def test_cmmi_entry_point(mock_process_cmmi):
    """Test entry point."""
    distribution = Mock()
    attr = 'cmmi'
    values = {
          'url': 'http://repo.in.zillow.net/content/groups/public/com/zillow/zpr/freetds/1.00.15/freetds-1.00.15.tar.gz',
          'config_options': '--prefix=$project_dir/lib/usr',
          'destination_dir': '$project_dir/lib/usr'
      }
    setuptools_cmmi.cmmi_entry_point(distribution, attr, values)

    # TODO: Add actual test stuff here
    mock_process_cmmi.assert_called_once()

