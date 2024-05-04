#!/usr/bin/python3
"""pack and deploy static files"""

import os
from datetime import datetime
from fabric.api import local, env, put, run

env.user = 'ubuntu'
env.hosts = ['3.85.175.13', '54.237.33.168']


def do_pack():
    """pack static files"""
    if local("mkdir -p versions").failed:
        return None
    path = f"versions/web_static_{datetime.now().strftime('%Y%m%d%H%M%S')}.tgz"
    if local(f"tar -cvzf {path} web_static").failed:
        return None
    return path


def do_deploy(archive_path):
    """deploy static files"""
    if not os.path.exists(archive_path):
        return False
    if put(archive_path, '/tmp/').failed:
        return False

    basename = os.path.basename(archive_path)
    remote_path = f"/data/web_static/releases/{basename[:-4]}"
    if run(f"mkdir -p {remote_path}").failed:
        return False

    if run(f"tar -xzf /tmp/{basename} -C {remote_path}").failed:
        return False

    if run(f"rm /tmp/{basename}").failed:
        return False

    if run(f"mv {remote_path}/web_static/* {remote_path}/").failed:
        return False

    if run(f"rm -rf {remote_path}/web_static").failed:
        return False

    if run("rm -rf /data/web_static/current").failed:
        return False

    if run(f"ln -s {remote_path} /data/web_static/current").failed:
        return False

    return True


def deploy():
    """pack and deploy"""
    arc_path = do_pack()
    if arc_path is None:
        return False
    return do_deploy(arc_path)
