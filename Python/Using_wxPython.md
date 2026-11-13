# Using wxPython

When dialogs are created in Python using the wxWidgets GUI toolkit and accessed from the KITModelViewer, the dialog initially lacks a relationship to the main application. This means that the dialog does not automatically come to the foreground, nor does it disappear when the application is minimized.
To achieve this standard behavior, use the following code. This sets the main window of the KITModelViewer as the parent window for the dialog created in Python.

<u>__Example code:__</u>
```
import ifcdb
import wx
import ctypes
from ctypes import wintypes

def set_mfc_owner(wx_dialog, mfc_hwnd):
    user32 = ctypes.windll.user32
    user32.SetWindowLongPtrW(wintypes.HWND(wx_dialog.GetHandle()), -8, ctypes.c_ssize_t(mfc_hwnd))
```

<u>__Usage__</u>
```
set_mfc_owner(dialog, document.parentWnd)
```
