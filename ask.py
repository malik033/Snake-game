import numpy as np
import matplotlib.pyplot as plt

# Function to generate ASK signal
def ask_modulation(data, M, fc=2, fs=100, T=1):
    if M not in [2, 4, 8]:
        raise ValueError("Only 2, 4, or 8-ASK are supported")
    
    bits_per_symbol = int(np.log2(M))
    
    # Check if length of data is a multiple of bits_per_symbol
    if len(data) % bits_per_symbol != 0:
        raise ValueError(f"The length of the data should be a multiple of {bits_per_symbol} for {M}-ASK")
    
    # Reshape the data into groups of bits_per_symbol
    data_symbols = np.reshape(data, (-1, bits_per_symbol))
    
    # Convert binary symbols to decimal values
    decimal_data = np.array([int(''.join(map(str, symbol)), 2) for symbol in data_symbols])
    
    # ASK amplitude mapping
    amplitudes = np.arange(-(M-1), M, 2)
    
    # Map the decimal data to corresponding ASK amplitudes
    ask_signal = amplitudes[decimal_data]
    
    # Time vector for one symbol
    t = np.arange(0, T, 1/fs)
    
    # Generate the ASK modulated signal
    modulated_signal = np.array([])
    for amp in ask_signal:
        carrier = amp * np.cos(2 * np.pi * fc * t)
        modulated_signal = np.concatenate([modulated_signal, carrier])
    
    return modulated_signal, ask_signal

# Input binary data (example)
data = np.array([1, 0, 1, 1, 0, 1, 0, 0])

# Select ASK modulation type (2, 4, or 8)
M = int(input('Enter the type of ASK modulation (2, 4, or 8): '))

# Generate ASK modulated signal
modulated_signal, ask_signal = ask_modulation(data, M)

# Plotting the modulated signal
plt.figure(figsize=(10, 4))
plt.plot(modulated_signal)
plt.title(f'{M}-ASK Modulated Signal')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

# Plotting the input binary data
plt.figure(figsize=(10, 2))
plt.stem(data, use_line_collection=True)
plt.title('Input Binary Data')
plt.xlabel('Bit Index')
plt.ylabel('Binary Value')
plt.grid(True)
plt.show()
