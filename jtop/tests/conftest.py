# -*- coding: UTF-8 -*-
# This file is part of the jetson_stats package (https://github.com/rbonghi/jetson_stats or http://rnext.it).
# Copyright (c) 2020 Raffaello Bonghi.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os
import logging
import pytest
from ..service import JtopServer
# Create logger
logger = logging.getLogger(__name__)


def remove_tests():
    if os.path.isfile('/tmp/jetson_model'):
        os.remove('/tmp/jetson_model')
    if os.path.isfile('/tmp/jetson_clocks_test'):
        os.remove('/tmp/jetson_clocks_test')
    if os.path.isfile('/tmp/nvp_model_test'):
        os.remove('/tmp/nvp_model_test')


@pytest.fixture(scope="package")
def jtop_server():
    logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')
    # Clean test files
    remove_tests()
    print("Initialize jtop service")
    jtop_server = JtopServer(fan_path=['tests/fan/'])
    jtop_server.start(force=True)
    yield jtop_server
    jtop_server.close()
    print("Close jtop service")
    # Clean test files
    remove_tests()


@pytest.fixture(scope="package")
def jtop_server_nothing():
    logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')
    # Clean test files
    remove_tests()
    print("Initialize jtop service")
    jtop_server = JtopServer(fan_path=[], jetson_clocks_path=[], tegrastats_path=[])
    jtop_server.start(force=True)
    yield jtop_server
    status = jtop_server.close()
    print("Close jtop service {}".format(status))
    # Clean test files
    remove_tests()
# EOF
