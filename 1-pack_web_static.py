#!/usr/bin/python3
"""pack static files"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """pack static files"""
    if local("mkdir -p versions").failed:
        return None
    path = f"versions/web_static_{datetime.now().strftime('%Y%m%d%H%M%S')}.tgz"
    if local(f"tar -cvzf {path} web_static").failed:
        return None
    return path
