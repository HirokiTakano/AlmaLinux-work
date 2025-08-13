#!/usr/bin/python3

import signal

#SIGINTシグナルを無視する迷惑プログラム

#特定のシグナル(signal.SIGINT)に対して、ハンドラ(SIG_IGN)を設定
signal.signal(signal.SIGINT,signal.SIG_IGN)
while True:
    pass
