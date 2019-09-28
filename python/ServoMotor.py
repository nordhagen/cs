from time import sleep

range = 0
position = 0

# A range of 0 means overflowing 360 rotation
def init(range = 0):
  range = min(max(range, 0), 360)

def sanitizeSpeed(speed = 20):
  return max(-100, min(100, speed))

def sanitizeAngle(angle):
  if range == 0:
    angle = angle % 360
    if angle < 0:
      angle = 360 + angle
  else:
    print(angle, range)
    angle = min(max(angle, 0), range)
    print(angle, range)

  return angle

def reset:
  position = 0

def run_to_abs_pos(angle, speed):
  global position

  if not angle:
    print('Invalid angle argument:' + str(angle))
    return
  
  speed = sanitizeSpeed(speed)
  angle = sanitizeAngle(angle)

  if angle == position:
    print('Motor ' + str(port) + ' stopped at position ' + str(position))
    return position
  
  print('Motor ' + str(port) + ' moving to position ' + str(angle) + ' at speed ' + str(speed))
  step = speed * 10 / 1000

  while True:
    if verbose:
      print('  Position: ' + str(position))
    
    position += step
    delta = abs(position - angle)

    if delta <= 0.2:
      position = angle
      print('Motor ' + str(port) + ' stopped at position ' + str(position))
      return position
    
    sleep(0.001)