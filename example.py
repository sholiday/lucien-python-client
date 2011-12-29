#!/usr/bin/env python
# encoding: utf-8
"""
example.py

Created by Stephen Holiday on 2011-12-27.
Copyright (c) 2011 Stephen Holiday. All rights reserved.
"""

import sys
import os

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
 
from lucien import Lucien
from lucien.ttypes import *

def main():
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Lucien.Client(protocol)
    transport.open()
    
    client.put("hey","there", "{'hey':'there'}")
    print client.get("hey","there")


if __name__ == '__main__':
	main()

