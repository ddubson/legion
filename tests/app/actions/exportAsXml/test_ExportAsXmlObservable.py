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

from app.actions.exportSessionAsXml.AbstractExportAsXmlObserver import AbstractExportAsXmlObserver
from app.actions.exportSessionAsXml.ExportAsXmlObservable import ExportAsXmlObservable


class MockObserver(AbstractExportAsXmlObserver):
    fileNameThatWasSet = None
    xmlExported = False

    def onFileNameSet(self, fileName: str) -> None:
        self.fileNameThatWasSet = fileName

    def onXmlExportReceive(self, xmlPayload: str) -> None:
        self.xmlExported = True


class ExportAsXmlObservableTest(unittest.TestCase):
    def setUp(self) -> None:
        self.exportAsXmlObservable = ExportAsXmlObservable()
        self.mockObserver = MockObserver()
        self.exportAsXmlObservable.attach(self.mockObserver)

    def test_fileNameSetAs_WhenProvidedAFileName_NotifiesObserversAboutFileNameForExport(self):
        self.exportAsXmlObservable.fileNameSetAs("some-file")
        self.assertEqual("some-file", self.mockObserver.fileNameThatWasSet)

    def test_exportAsXml_InvokesExportAsXmlActionAndNotifiesObserversAboutResult(self):
        self.exportAsXmlObservable.exportAsXml()
        self.assertTrue(self.mockObserver.xmlExported)
