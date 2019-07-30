#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

import inits
import logging
from logging import handlers
import globalvar as gl
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
import base64

global logger
global wb_logger
global CONF

def log_init(log_app_name, file_name):
    logger = logging.getLogger(log_app_name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(message)s')


    ch = logging.handlers.TimedRotatingFileHandler(
                    filename=file_name,
                    when='midnight',
                    backupCount=3
                    )
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)

    #控制台输出
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    #logger.addHandler(sh)

    return logger

def inThread(datagram, address):
    ip, port = address
    logger.info("ip:%s, port:%s, len(%d)", ip, port, len(datagram))
    info = base64.b64decode(datagram)
    wb_logger.info(info)

# Here's a UDP version of the simplest possible protocol
class EchoUDP(DatagramProtocol):
    def datagramReceived(self, datagram, address):
        reactor.callInThread(inThread, datagram, address)

def main():
    reactor.suggestThreadPoolSize(15)
    reactor.listenUDP(CONF['port'], EchoUDP())
    reactor.run()

if __name__ == '__main__':
    logger = gl.get_logger()
    CONF = gl.get_conf()
    wb_logger = log_init('RESULT', './result.log')
    main()