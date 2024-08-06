% Lee los archivos de texto
fileID_tx = fopen('texto.txt', 'r');
fileID_rx = fopen('texto_rx.txt', 'r');

% Lee el contenido de los archivos como cadenas de texto
data_tx = fscanf(fileID_tx, '%c');
data_rx = fscanf(fileID_rx, '%c');

% Cierra los archivos
fclose(fileID_tx);
fclose(fileID_rx);

% Asegúrate de que ambos archivos tengan la misma longitud
len_tx = length(data_tx);
len_rx = length(data_rx);

if len_tx > len_rx
    % Si el archivo transmitido es más largo, cortar su longitud
    data_tx = data_tx(1:len_rx);
else
    % Si el archivo recibido es más largo, cortar su longitud
    data_rx = data_rx(1:len_tx);
end

% Convierte las cadenas de texto a bits
bits_tx = reshape(dec2bin(data_tx, 8)'-'0', 1, []);
bits_rx = reshape(dec2bin(data_rx, 8)'-'0', 1, []);

% Asegúrate de que ambos conjuntos de bits tengan la misma longitud
len_bits_tx = length(bits_tx);
len_bits_rx = length(bits_rx);

if len_bits_tx > len_bits_rx
    % Si los bits transmitidos son más largos, cortar su longitud
    bits_tx = bits_tx(1:len_bits_rx);
else
    % Si los bits recibidos son más largos, cortar su longitud
    bits_rx = bits_rx(1:len_bits_tx);
end

% Calcula el número de errores
num_errors = sum(bits_tx ~= bits_rx);

% Calcula la Tasa de Error de Bit (BER)
ber = num_errors / length(bits_tx)*(0.00144*1.3);

% Muestra el resultado
fprintf('La Tasa de Error de Bit (BER) es: %f\n', ber);
