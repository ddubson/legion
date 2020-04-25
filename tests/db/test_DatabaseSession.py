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
from unittest import TestCase
from unittest.mock import MagicMock

from db.DatabaseSession import DatabaseSession
from db.SqliteDbAdapter import Database


class DatabaseSessionTest(TestCase):
    def setUp(self) -> None:
        self.mockDb = MagicMock()

    def test_givenADbSession_shouldAcquireASemaphoreAndReleaseItDuringTheLifetimeOfSession(self):
        def someDbOperation(db: Database) -> None:
            with DatabaseSession(db):
                something = "Doing some operation"
                return something

        someDbOperation(self.mockDb)

        self.mockDb.dbsemaphore.acquire.assert_called_once()
        self.mockDb.dbsemaphore.release.assert_called_once()

    def test_givenADbSession_whenDbOperationPerformed_shouldAcquireASemaphoreAndCallOperationAndReleaseSemaphore(self):
        def someDbOperation(db: Database) -> None:
            with DatabaseSession(db) as session:
                something = "Doing some operation"
                session.commit()
                return something

        someDbOperation(self.mockDb)

        self.mockDb.dbsemaphore.acquire.assert_called_once()
        self.mockDb.session.commit.assert_called_once()
        self.mockDb.dbsemaphore.release.assert_called_once()

    def test_givenADbSession_whenOperationRaisesError_shouldAcquireASemaphoreAndReleaseIt(self):
        def someDbOperation(db: Database) -> None:
            with DatabaseSession(db):
                something = "Doing some operation"
                raise BaseException(something)

        with self.assertRaises(BaseException):
            someDbOperation(self.mockDb)

        self.mockDb.dbsemaphore.acquire.assert_called_once()
        self.mockDb.dbsemaphore.release.assert_called_once()
