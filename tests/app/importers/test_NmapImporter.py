"""
LEGION (https://govanguard.io)
Copyright (c) 2020 GoVanguard

    This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
    License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
    version.

    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
    warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
    details.

    You should have received a copy of the GNU General Public License along with this program.
    If not, see <http://www.gnu.org/licenses/>.

Author(s): Dmitriy Dubson (d.dubson@gmail.com)
"""

import unittest
from os.path import join, dirname
from unittest import mock
from unittest.mock import MagicMock, patch


class NmapImporterTests(unittest.TestCase):
    @patch('utilities.stenoLogging.get_logger')
    def test_givenAValidXmlNmapReport_SavesHostsSuccessfully(self, getLogger):
        from app.importers.NmapImporter import NmapImporter
        updateProgressObservable = MagicMock()
        hostRepository = MagicMock()
        mockDb = MagicMock()
        mockFilename = join(dirname(__file__), "../../parsers/nmap-fixtures/valid-nmap-report.xml")
        importer = NmapImporter(updateProgressObservable, hostRepository)
        importer.setDB(mockDb)
        importer.setFilename(mockFilename)

        importer.run()

        mockDb.session.commit.assert_called()

