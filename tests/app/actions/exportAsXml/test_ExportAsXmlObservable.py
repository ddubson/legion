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
from unittest.mock import MagicMock

from app.actions.exportSessionAsXml.AbstractExportAsXmlObserver import AbstractExportAsXmlObserver
from app.actions.exportSessionAsXml.ExportAsXmlObservable import ExportAsXmlObservable


class MockObserver(AbstractExportAsXmlObserver):
    xmlExported = False

    def onExportedSuccessfully(self) -> None:
        self.xmlExported = True


class ExportAsXmlObservableTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mockShell = MagicMock()
        self.exportAsXmlObservable = ExportAsXmlObservable(self.mockShell)
        self.mockObserver = MockObserver()
        self.exportAsXmlObservable.attach(self.mockObserver)

    def test_exportAsXml_InvokesExportAsXmlActionAndNotifiesObserversAboutResult(self):
        self.exportAsXmlObservable.exportAsXml("some-file")
        self.mockShell.writeFile.assert_called_once_with("some-file", unittest.mock.ANY)
        self.assertTrue(self.mockObserver.xmlExported)
