"""
Given a list of IDs, which contains many duplicate integers (pairs) and one unique integer, find the unique integer.
The IDs are not guaranteed to be sorted or sequential.
"""

def unique_id_find(id_list):
    unique_id = 0
    for id in id_list:
        unique_id ^= id
    
    return unique_id


    
