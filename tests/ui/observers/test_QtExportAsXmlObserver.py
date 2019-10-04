"""
LEGION (https://govanguard.io)
Copyright (c) 2018 GoVanguard

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
from unittest.mock import patch, MagicMock


class QtExportAsXmlObserverTest(unittest.TestCase):
    @patch("PyQt5.QtWidgets.QFileDialog")
    def setUp(self, fileDialog) -> None:
        from ui.observers.QtExportAsXmlObserver import QtExportAsXmlObserver
        self.fileDialog = fileDialog
        self.fileDialog.getSaveFileName.return_value = ("some-file", "")
        self.mainAppWindow = MagicMock()
        self.qtExportAsXmlObserver = QtExportAsXmlObserver(self.mainAppWindow)

    def test_onXmlExportReceive_PromptsForSaveXml(self):
        self.qtExportAsXmlObserver.onXmlExportReceive("some-xml")
        self.fileDialog.getSaveFileName.assert_called_once()
