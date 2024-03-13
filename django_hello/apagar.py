import sys

if sys.platform.startswith('linux'):
    print("O ambiente é Linux.")
elif sys.platform.startswith('darwin'):
    print("O ambiente é macOS (Unix-like).")
elif sys.platform.startswith('win'):
    print("O ambiente é Windows.")
else:
    print("O ambiente não é Linux, macOS ou Windows.")