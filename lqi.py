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

class display_lqi_value(gr.sync_block):
    """
    docstring for block display_lqi_value
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="display_lqi_value",
            in_sig=[],
            out_sig=[])
	self.message_port_register_in(pmt.intern("in")) 
	self.message_port_register_out(pmt.intern("out")) 
	self.set_msg_handler(pmt.intern("in"), self.print_LQI) #Funcion print_LQI


    def print_LQI(self, msg_pmt):
	# Extraer el valor de LQI
	key0 = pmt.intern("lqi")
        msg_lqi = pmt.car(msg_pmt)
	v_lqi = pmt.dict_ref(msg_lqi, key0, pmt.PMT_NIL)
	if(pmt.eq(v_lqi, pmt.PMT_NIL)):
		vLQI = 0
	else:
		vLQI = pmt.to_long(v_lqi)
	msg = [ord(c) for c in str(vLQI)]
	msg.append(10) # Insertar salto de linea
	# Crea un PMT vacio
	send_pmt = pmt.make_u8vector(len(msg), ord(' '))
	# Copia caracteres a u8vector
	for i in range(len(msg)):
	    pmt.u8vector_set(send_pmt, i, msg[i])
	# Envia mensaje
	self.message_port_pub(pmt.intern('out'), pmt.cons(pmt.PMT_NIL, send_pmt))


