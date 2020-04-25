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
from unittest import mock
from unittest.mock import MagicMock

from app.actions.updateProgress.AbstractUpdateProgressObservable import AbstractUpdateProgressObservable
from app.actions.updateProgress.ProgressTracker import ProgressTracker


class ProgressTrackerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.mockUpdateProgressObservable = MagicMock()

    def test_whenOperationCompletesSuccessfully_shouldTriggerStartAndUpdateAndFinished(self):
        def doSomeOperation(updateProgressObservable: AbstractUpdateProgressObservable) -> None:
            with ProgressTracker(updateProgressObservable):
                something = "some operation"
                return something

        doSomeOperation(self.mockUpdateProgressObservable)

        self.assertAllOperationsTrigger()

    def test_whenOperationFailsMidwayThroughExecution_shouldTriggerStartAndUpdateAndFinished(self):
        def doSomeOperationAndFail(updateProgressObservable: AbstractUpdateProgressObservable) -> None:
            with ProgressTracker(updateProgressObservable):
                something = "Things didn't go so well"
                raise BaseException(something)

        with self.assertRaises(BaseException):
            doSomeOperationAndFail(self.mockUpdateProgressObservable)

        self.assertAllOperationsTrigger()

    def test_whenOperationUpdatesDuringOperationAndCompletesSuccessfully_shouldTriggerStartAndUpdateAndFinished(self):
        def doSomeOperation(updateProgressObservable: AbstractUpdateProgressObservable) -> None:
            with ProgressTracker(updateProgressObservable) as tracker:
                something = "some operation"
                tracker.updateProgress(50)
                return something

        doSomeOperation(self.mockUpdateProgressObservable)

        self.assertAllOperationsTrigger([mock.call(50)])

    def assertAllOperationsTrigger(self, additionalCalls=[]):
        self.mockUpdateProgressObservable.start.assert_called_once()
        self.mockUpdateProgressObservable.updateProgress.assert_has_calls(
            [mock.call(0)] + additionalCalls + [mock.call(100)]
        )
        self.mockUpdateProgressObservable.finished.assert_called_once()
