

import tkinter
import threading
import time
import math

# This function was borrowed from https://stackoverflow.com/a/34374437
def rotate(point, angle, origin=(0.0, 0.0)):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy

# We use this to exit the background thread when mainloop() ends
exit_flag = False
triangle_center = (90, 90)
triangle_points = [(55, 85), (155, 85), (105, 180), (55, 85)]

def flatten(maybe_list):
  flat_list = []
  if isinstance(maybe_list, list):
    for x in maybe_list:
      for y in flatten(x):
        flat_list.append(y)
  else:
    flat_list.append(maybe_list)
  return flat_list

def update_canvas_thread(canvas):
  global exit_flag
  global triangle_points

  while not exit_flag:
    time.sleep(0.25)
    # rotate points by 25 degrees
    new_triangle_points = []
    for point in triangle_points:
      point = rotate(point, math.radians(25), origin=triangle_center)
      new_triangle_points.append(point)

    triangle_points = new_triangle_points

    # Clear the canvas
    canvas.delete("all")
    
    # Draw a line on the canvas
    canvas.create_line(flatten(triangle_points))


root = tkinter.Tk()

canvas = tkinter.Canvas(root, width=400, height=400)
canvas.create_line( flatten(triangle_points) )
canvas.pack()

# We spawn a thread before entering mainloop()
# to update the canvas every 1/4 second
bg_thread = threading.Thread(target=update_canvas_thread, args=(canvas,))
bg_thread.start()

root.geometry("400x250+300+300")
root.mainloop()

exit_flag = True

bg_thread.join()

