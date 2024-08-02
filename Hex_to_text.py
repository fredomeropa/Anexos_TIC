import pmt
from gnuradio import gr

class hex_to_text(gr.basic_block):
    def __init__(self):
        gr.basic_block.__init__(self,
            name="Hex to Text",
            in_sig=None,
            out_sig=None)
        self.message_port_register_in(pmt.intern("in"))
        self.set_msg_handler(pmt.intern("in"), self.handle_msg)
        self.message_port_register_out(pmt.intern("out"))

    def handle_msg(self, msg):
        if pmt.is_pair(msg):
            data = pmt.cdr(msg)
            if pmt.is_u8vector(data):
                bytes_data = bytes(pmt.u8vector_elements(data))
                text = self.bytes_to_clean_text(bytes_data)
                self.message_port_pub(pmt.intern("out"), pmt.intern(text))

    def bytes_to_clean_text(self, bytes_data):
        try:
            text = bytes_data.decode('utf-8', errors='ignore')
            # Filtrar caracteres no deseados
            filtered_text = ''.join([c for c in text if c.isprintable()])
            # Eliminar cualquier prefijo no deseado
            if "Hola mundo" in filtered_text:
                start_index = filtered_text.find("Hola mundo")
                filtered_text = filtered_text[start_index:]
            return filtered_text
        except Exception as e:
            print(f"Error decoding message: {e}")
            return ""

def main():
    return hex_to_text()
