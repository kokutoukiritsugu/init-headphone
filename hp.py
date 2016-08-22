import ctypes
import sys

nDLL = ctypes.WinDLL('hp.dll')

Set_effect = nDLL['Set_effect']
InitHeadphone = nDLL['InitHeadphone']

Set_effect.restype = ctypes.c_int
InitHeadphone.restype = ctypes.c_int

if len(sys.argv) == 1:
    print("init headphone.")
    InitHeadphone()

if len(sys.argv) == 2:
    print("set effect: " + sys.argv[1])
    Set_effect(int(sys.argv[1]))
