# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class FdFind(Package):
    """A simple, fast and user-friendly alternative to 'find'."""

    homepage = "https://github.com/sharkdp/fd"
    url      = "https://github.com/sharkdp/fd/archive/v7.3.0.tar.gz"

    version('7.3.0', sha256='fbd48cc83c90a0ab09fc3bbe865708a3a528876a99f8304a17d07af7fb378170')

    depends_on('rust')

    def install(self, spec, prefix):
        cargo = which('cargo')
        cargo('install', '--root', prefix, '--path', '.')
