#   Copyright 2008 Aaron Barnes
#
#   This file is part of the FreeEMS project.
#
#   FreeEMS software is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   FreeEMS software is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with any FreeEMS software.  If not, see <http://www.gnu.org/licenses/>.
#
#   We ask that if you make any changes to this file you send them upstream to us at admin@diyefi.org

# Handle configuration saving/loading
import ConfigParser


# Get config parser
# Defaults are stored in config.ini (in same directory as code)
# User overrided settings are found in data/my_config.ini
def getParser():

    config = ConfigParser.RawConfigParser()
    config.read(['config.default.ini', 'data/my_config.ini'])
    
    return config


# Load option from config file
def load(section, option):

    # Get defaults and user settings
    parser = getParser()
    return parser.get(section, option)


# Load option but return as a boolean value
def loadBool(section, option):

    parser = getParser()
    return parser.getboolean(section, option)