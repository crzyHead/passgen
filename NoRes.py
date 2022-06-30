import ctypes as ct

def NoRes(Tk): # function to remove Min/Max buttons:
    c = ct.windll.user32

    # Identifiers;
    gwl_style = -16

    ws_minimizebox = 131072
    ws_maximizebox = 65536

    swp_nozorder = 4
    swp_nomove = 2
    swp_nosize = 1
    swp_framechanged = 32

    hwnd = c.GetParent(Tk.winfo_id())

    old_style = c.GetWindowLongPtrW(hwnd, gwl_style) # Get the style;

    new_style = old_style & ~ ws_maximizebox & ~ ws_minimizebox # New style, without max/min buttons;

    c.SetWindowLongPtrW(hwnd, gwl_style, new_style) # Apply the new style;

    c.SetWindowPos(hwnd, 0, 0, 0, 0, 0, swp_nomove | swp_nosize | swp_nozorder | swp_framechanged) # Updates;