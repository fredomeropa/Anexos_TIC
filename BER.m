clear all;
close all;
clc

% Apertura y lectura de archivos
file_tx = fopen('Datos.txt');  % Archivo de transmisión
file_rx = fopen('Datos_RX.txt'); % Archivo de recepción

% Lectura del contenido de los archivos
text_tx = fscanf(file_tx, '%c'); % Lee el archivo de transmisión
text_rx = fscanf(file_rx, '%c'); % Lee el archivo de recepción

% Conversión de texto a binario
[bits_tx, bin_tx] = txt2bin(text_tx); % txt2bin es una función definida
[bits_rx, bin_rx] = txt2bin(text_rx);

% Alineación de longitud de bits
len_tx = length(bits_tx);
len_rx = length(bits_rx);

if len_tx < len_rx
    bits_rx = bits_rx(1:len_tx); % Ajuste de longitud
else 
    bits_rx(len_rx+1:len_tx) = 0; % Relleno con ceros si es necesario
end

% Cálculo de BER
[num_errors, bit_error_rate] = biterr(bits_tx, bits_rx); 

% Cierre de archivos
fclose(file_tx);
fclose(file_rx);

