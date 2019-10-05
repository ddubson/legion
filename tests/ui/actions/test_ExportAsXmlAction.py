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
from unittest.mock import MagicMock, patch


class ExportAsXmlActionTest(unittest.TestCase):
    @patch("PyQt5.QtWidgets.QFileDialog")
    def setUp(self, fileDialog) -> None:
        self.fileDialog = fileDialog
        self.fileDialog.getSaveFileName.return_value = ("some-file.xml", "")
        from ui.actions.ExportAsXmlAction import ExportAsXmlAction
        self.mainAppWindow = MagicMock()
        self.exportAsXmlObservable = MagicMock()
        self.exportAsXmlAction = ExportAsXmlAction(self.mainAppWindow, self.exportAsXmlObservable)

    def test_exportAsXml(self):
        self.exportAsXmlAction.exportAsXml()

        self.fileDialog.getSaveFileName.assert_called_once()
        self.exportAsXmlObservable.exportAsXml.assert_called_once_with("some-file.xml")
