/* -*- c++ -*- */
/* 
 * Copyright 2019 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "decimador_cc_impl.h"

namespace gr {
  namespace Pruebas {

    decimador_cc::sptr
    decimador_cc::make(int decim)
    {
      return gnuradio::get_initial_sptr
        (new decimador_cc_impl(decim));
    }

    /*
     * The private constructor
     */
    decimador_cc_impl::decimador_cc_impl(int decim)
      : gr::sync_decimator("decimador_cc",
              gr::io_signature::make(1, 1, sizeof(gr_complex)),
              gr::io_signature::make(1, 1, sizeof(gr_complex)), decim),
	d_decimation(decim)
    {}

    /*
     * Our virtual destructor.
     */
    decimador_cc_impl::~decimador_cc_impl()
    {
    }

    int
    decimador_cc_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const gr_complex *in = (const gr_complex *) input_items[0];
      gr_complex *out = (gr_complex *) output_items[0];
      gr_complex origin = gr_complex(0,0);

      // Do <+signal processing+>
      for(int i = 0; i < noutput_items; i++)
      {
	    out[i] = in[2*i+1];
      }
      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace Pruebas */
} /* namespace gr */

