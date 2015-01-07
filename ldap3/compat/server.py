"""
"""

# Created on 2014.03.10
#
# Author: Giovanni Cannata
#
# Copyright 2015 Giovanni Cannata
#
# This file is part of ldap3.
#
# ldap3 is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ldap3 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with ldap3 in the COPYING and COPYING.LESSER files.
# If not, see <http://www.gnu.org/licenses/>.

from ldap3.core.server import Server as newServer


# noinspection PyPep8Naming
class Server(newServer):
    def __init__(self, host, port=389, useSsl=False, allowedReferralHosts=None, getInfo=None, tls=None):
        newServer.__init__(self, host, port, useSsl, allowedReferralHosts, getInfo, tls)
