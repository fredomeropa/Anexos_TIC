#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2019 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import string
import pmt
import struct
from gnuradio import gr
from gnuradio import digital

class pmt_symbol_to_pdu(gr.sync_block):
    """
    docstring for block pmt_symbol_to_pdu
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="pmt_symbol_to_pdu",
            in_sig=[],
            out_sig=[])
	self.message_port_register_in(pmt.intern("in")) 
	self.message_port_register_out(pmt.intern("out")) 
	self.set_msg_handler(pmt.intern("in"), self.make_PDU) #Funcion make_PDU


    def make_PDU(self, msg_pmt):
	# Toma Pmt Symbol a String y luego a lista
        msg_pmt = pmt.symbol_to_string(msg_pmt)
	msg = [ord(c) for c in msg_pmt]
	# Crea un PMT vacio
	send_pmt = pmt.make_u8vector(len(msg), ord(' '))
	# Copia caracteres a u8vector
	for i in range(len(msg)):
	    pmt.u8vector_set(send_pmt, i, msg[i])
	# Envia mensaje
	self.message_port_pub(pmt.intern('out'), pmt.cons(pmt.PMT_NIL, send_pmt))


