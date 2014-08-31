#will most likely ends up with an incomplete matrix.

"""
boxes: refers to a line/column of the resulting matrix
clues: the clues of the current line/column in correct order
clue_position: the position of the clue to process in the clue list
"""

def process_clue(boxes, clues, clue_position):

    window_start = 0
    window_end = len(clues)

#first pass: reduce the window width considering the other clues

    for i in range(0,len(clues)):
        if i < clue_position:            
            window_start += clues[i]+1
        elif i > clue_position:
            window_end += - (clues[i]+1)
        else:
            current_clue = clues[i]
            
#second pass: detect all white boxes in current window (i.e. resulting window
of first pass) and reduce the window width accordingly

    for i in range (window_start, window_end):
        if boxes[i].is_white():
            if i - window_start < current_clue:                
                window_start = i + 1
            elif window_end - i < current_clue:
                window_end = i
		overlap = 2 * current_clue - (window_end - window_start)
            
#in case the entire clue may be solved at once, fill all the boxes within the
window in black and fill the window extremities in white.

    if overlap == current_clue:
        for i in range (current_clue):
            boxes[window_start + i].fill_black()
            
# The current clue is entirely solved. Fill the extremities of the window to
# white.

            boxes[window_start - 1].fill_white()
            boxes[window_end].fill_white()
            
#in case there really is an overlap, fill the boxes within the overlap in
black. Otherwise do nothing
        
    elif overlap > 0:
	for i in range(current_clue - overlap, current_clue + overlap - 1):
            boxes[window_start + i].fill_black()
