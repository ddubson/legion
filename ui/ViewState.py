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


# Defines the state of the UI at any given moment
# Defaults are the initial state of the UI
class ViewState:
    # Indicator if any changes have happened since last save (default: False [no changes])
    dirty: bool = False
    # Indicator if 'Save As..' dialog should be used (default: True)
    firstSave = True
    # Indicator of which tabs should be displayed for each host (default: empty dictionary)
    hostTabs = dict()
