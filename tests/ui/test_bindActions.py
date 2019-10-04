import unittest
from unittest.mock import patch, MagicMock

from ui.bindActions import bindTriggerAction, bindSelectionChangedAction, bindClickAction, bindCurrentChangedAction, \
    bindDoubleClickAction, bindSectionResizeAction, bindCustomContextMenuRequestAction


class BindActionsTests(unittest.TestCase):
    @patch("PyQt5.QtWidgets.QAction")
    def setUp(self, someViewComponentSpy) -> None:
        self.someViewComponentSpy = someViewComponentSpy
        self.someAction = "some-action"

    def test_bindTriggerAction_WhenGivenViewComponentAndAction_AttachesTriggeredActionToComp(self):
        bindTriggerAction(self.someViewComponentSpy, self.someAction)
        self.someViewComponentSpy.triggered.connect.assert_called_once_with(self.someAction)

    def test_bindSelectionChangedAction_WhenGivenViewComponentAndAction_AttachesSelectionChangedActionToComp(self):
        bindSelectionChangedAction(self.someViewComponentSpy, self.someAction)
        self.someViewComponentSpy.selectionChanged.connect.assert_called_once_with(self.someAction)

    def test_bindClickAction_WhenGivenViewComponentAndAction_AttachesClickActionToComp(self):
        bindClickAction(self.someViewComponentSpy, self.someAction)
        self.someViewComponentSpy.clicked.connect.assert_called_once_with(self.someAction)

    def test_bindDoubleClickAction_WhenGivenViewComponentAndAction_AttachesDoubleClickActionToComp(self):
        bindDoubleClickAction(self.someViewComponentSpy, self.someAction)
        self.someViewComponentSpy.doubleClicked.connect.assert_called_once_with(self.someAction)

    def test_bindCurrentChangedAction_WhenGivenViewComponentAndAction_AttachesCurrentChangedActionToComp(self):
        bindCurrentChangedAction(self.someViewComponentSpy, self.someAction)
        self.someViewComponentSpy.currentChanged.connect.assert_called_once_with(self.someAction)

    def test_bindSectionResizeAction_WhenGivenViewComponentAndAction_AttachesSectionResizeActionToComp(self):
        bindSectionResizeAction(self.someViewComponentSpy, self.someAction)
        self.someViewComponentSpy.sectionResized.connect.assert_called_once_with(self.someAction)

    def test_bindCustomContextMenuRequestAction_WhenGivenViewComponentAndAction_AttachesCustomContextActionToComp(self):
        bindCustomContextMenuRequestAction(self.someViewComponentSpy, self.someAction)
        self.someViewComponentSpy.customContextMenuRequested.connect.assert_called_once_with(self.someAction)

