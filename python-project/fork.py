#!/usr/bin/python3

import os,sys

#fork()関数を呼び出す 
#コードを実行しているプロセスが「親プロセス」となり
#全く同じ状態のコピーとして「子プロセス」が生成される
ret = os.fork() 



if ret > 0:
    print("子プロセス: プロセスID={}, 親プロセスのプロセスID={}"
          .format(os.getpid(), ret))   
    exit()

elif ret == 0:
    print("親プロセス: プロセスID={}, 子プロセスのプロセスID={}" 
        .format(os.getpid(), os.getppid()))  
    exit()


