#!/usr/bin/env python
# -*- coding: utf-8 -*-

__license__ = """
BASIS - Basic check sistem.

Author:
  Miguel Morillo Iruela | https://bitbucket.org/mmorillo

Project site: https://bitbucket.org/mmorillo

Copyright (c) 2013, Miguel Morillo Iruela.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3. Neither the name of copyright holders nor the names of its
   contributors may be used to endorse or promote products derived
   from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
''AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL COPYRIGHT HOLDERS OR CONTRIBUTORS
BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""

__all__ = [

    # Metadata
    "__author__",
    "__copyright__",
    "__credits__",
    "__email__",
    "__version__",

    # Banner
    "get_banner",
    "show_banner",
]


#----------------------------------------------------------------------
# Metadata

__author__ = "Miguel Morillo Iruela"
__copyright__ = "Copyright 2013-Miguel Morillo Iruela"
__credits__ = ["https://bitbucket.org/mmorillo"]
__email__ = "https://bitbucket.org/mmorillo"
__version__ = "0.1"


#----------------------------------------------------------------------
def get_banner():
    """
    :returns: The program banner.
    :rtype: str
    """
    banner_lines = [
        "Basis %s - BAsic System Information Sistem." % __version__,
        ##__copyright__,
        "Contact: " + __email__,
        "",
    ]
    for ppl in __credits__:
        banner_lines.append(ppl)
    width = max(len(line) for line in banner_lines)
    banner = "\n#-" + ("-" * width) + "-#\n"
    for line in banner_lines:
        banner += "| " + line + (" " * (width - len(line))) + " |\n"
    banner += "#-" + ("-" * width) + "-#\n"
    return banner


#----------------------------------------------------------------------
def show_banner():
    """
    Prints the program banner.
    """
    print get_banner()
