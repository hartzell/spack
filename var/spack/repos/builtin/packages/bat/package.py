# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Bat(Package):
    """A cat(1) clone with wings."""

    homepage = "https://github.com/sharkdp/bat"
    url      = "https://github.com/sharkdp/bat/archive/v0.10.0.tar.gz"

    version('0.10.0', sha256='54dd396e8f20d44c6032a32339f45eab46a69b6134e74a704f8d4a27c18ddc3e')

    depends_on('rust')

    def install(self, spec, prefix):
        cargo = which('cargo')
        cargo('install', '--root', prefix, '--path', '.')
