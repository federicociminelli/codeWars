'''
Each exclamation mark weight is 2; Each question mark weight is 3. Put two string left and right to the balance, Are they balanced?
If the left side is more heavy, return "Left"; If the right side is more heavy, return "Right"; If they are balanced, return "Balance".
'''

def balance(left, right):   
    lc = (left.count('!')*2) +( left.count('?')*3)
    rc = (right.count('!')*2) +( right.count('?')*3)
    if lc < rc:
        return 'Right'
    elif lc == rc:
        return 'Balance'
    return 'Left'
