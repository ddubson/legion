from typing import Union

from PyQt5.QtWidgets import QAction, QTextEdit, QTableView, QTabWidget, QHeaderView, QAbstractButton


def bindTriggerAction(viewComponent: QAction, action: any) -> None:
    viewComponent.triggered.connect(action)


def bindSelectionChangedAction(viewComponent: QTextEdit, action: any) -> None:
    viewComponent.selectionChanged.connect(action)


def bindClickAction(viewComponent: Union[QTableView, QAbstractButton], action: any) -> None:
    viewComponent.clicked.connect(action)


def bindDoubleClickAction(viewComponent: QTableView, action: any) -> None:
    viewComponent.doubleClicked.connect(action)


def bindCurrentChangedAction(viewComponent: QTabWidget, action: any) -> None:
    viewComponent.currentChanged.connect(action)


def bindCustomContextMenuRequestAction(viewComponent: QTableView, action: any) -> None:
    viewComponent.customContextMenuRequested.connect(action)


def bindSectionResizeAction(viewComponent: QHeaderView, action: any) -> None:
    viewComponent.sectionResized.connect(action)
