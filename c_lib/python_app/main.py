import ctypes

# Load C library
fastlog = ctypes.CDLL("../c_lib/libfastlog.dylib")

# Define function input/output types
fastlog.count_chars.argtypes = [ctypes.c_char_p]
fastlog.count_chars.restype = ctypes.c_int

# Test string
text = b"FastLog Demo"

# Call C function
result = fastlog.count_chars(text)

print("Character Count:", result)