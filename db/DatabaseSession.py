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
from sqlalchemy.orm import scoped_session

from db.SqliteDbAdapter import Database


class DatabaseSession:
    def __init__(self, db: Database):
        self.db = db

    def __enter__(self) -> scoped_session:
        # ensure that while this thread is running, no one else can write to the DB
        self.db.dbsemaphore.acquire()
        return self.db.session

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.db.dbsemaphore.release()
