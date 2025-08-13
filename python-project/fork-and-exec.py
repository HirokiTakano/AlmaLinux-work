#!/usr/bin/python3

import os,sys

ret = os.fork()

#retが0の場合、つまり子プロセスの戻り値が0の場合
#getpidは自分自身のプロセスID(子プロセスID), getppidは自身から見た親のプロセスID
if ret == 0:
    print("[子プロセスの場合]親プロセスIDは{},子プロセスIDは{}"
          .format(os.getppid(), os.getpid())) 
    os.execve("/bin/echo", ["echo", "pid={} からこんにちは"
                            .format(os.getpid())], {})

#retが0以上の場合、つまり親プロセスの戻り値が子プロセスの場合
#getpidは自身のプロセスID(親プロセスID),retは戻り値であるret
if ret > 0:
    print("[親プロセスの場合]親プロセスIDは{},子プロセスIDは{}"
          .format(os.getpid(), ret)) 
