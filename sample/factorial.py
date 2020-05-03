# Template Repository for testing
# Copyright (C) 2020 Ezekiel Bernal

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""This is a factorial code"""

#Next is imports

__author__ = 'Ezekiel Bernal'
__version__ = '0.0.1'

#Next is Global Variable

class something(object):

	def __init__(self,text):
		self.text = text

	def x(self,text):
		print(f'{text}')

def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1);