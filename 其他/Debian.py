# -*- encoding: utf-8 -*-
"""
@File    :   apt.py
@Time    :   2022-09-05 09:17
@Author  :   坐公交也用券
@Version :   1.0
@Contact :   faith01238@hotmail.com
@Homepage : https://liumou.site
@Desc    :   当前文件作用
"""
from os import getenv, path

from model.apt import Apt
from model.cmd import Cmd
from model.install_pac_list import pac_list
from model.pip import Pip
from model.docker import Docker


class DebianInit:
    def __init__(self, passwd, debug=False):
        """
        chushihua
        :param passwd:
        """
        self.debug = debug
        self.passwd = passwd
        self.home = getenv('HOME')
        self.apt = Apt(passwd, debug=debug)
        self.cmd = Cmd(passwd, debug=debug)
        self.res = False
        self.pips = Pip(debug=debug)
        self.docker = Docker(passwd)

    def zh_cn(self):
        txt = '''export GTK_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"
'''
        file = path.join(self.home, '.xprofile')
        with open(file=file, mode='w', encoding='utf8') as z:
            z.write(txt)

    def add_paths(self):
        self.res = self.cmd.add_path(paths=path.join(self.home, '.local/bin'))

    def pip(self):
        """

        :return:
        """
        self.pips.config()
        self.pips.update()
        self.pips.install()

    def install(self):
        """

        :return:
        """
        for i in pac_list:
            self.apt.install(pac=i)

    def install_google(self):
        """

        :return:
        """
        file = path.join(self.home, 'google-chrome-stable_current_amd64.deb')
        cmd = "wget -c https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O %s" % file
        if self.cmd.shell(command=cmd, name='Download google-chrome-stable'):
            self.apt.local_install_f(file=file)

    def start(self):
        self.zh_cn()
        self.apt.update()
        self.install()
        self.pip()
        self.install_google()
        self.docker.start()
        print("请执行下面的命令 : \nsource ~/.xprofile")
        if self.res:
            print("source ~/.bashrc")


if __name__ == "__main__":
    up = DebianInit(passwd='1')
    up.start()
