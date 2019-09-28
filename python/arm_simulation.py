#!/usr/bin/env python3
import ServoMotor as motor
import TouchSensor as ts
import Sound

from time import sleep
import random

motor.reset()

ROTATION_STEP_SIZE = -12
ROTATION_SPEED = 20
LEARNING_RATE_ALPHA = 0.5
DISCOUNT_FACTOR_GAMMA = 0.5

stateFrom = 0
stateTo = 1
numEpochs = 200
numRecords = 20
records = [0] * numRecords

state = [
  -ROTATION_STEP_SIZE,
  0 * ROTATION_STEP_SIZE,
  1 * ROTATION_STEP_SIZE,
  2 * ROTATION_STEP_SIZE,
  3 * ROTATION_STEP_SIZE,
  4 * ROTATION_STEP_SIZE,
  5 * ROTATION_STEP_SIZE,
  6 * ROTATION_STEP_SIZE,
  7 * ROTATION_STEP_SIZE
]

Q = [[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]]

stateCount = len(state)

def getRandomState():
  index = random.randint(0, stateCount - 1)
  return index

def performAction():
  reward = 0
  targetAngle = state[stateTo] - state[stateFrom]
  
  motor.run_to_abs_pos(position_sp=targetAngle, speed_sp=700)
  time.sleep(0.4)
  ts.motorPosition = motor.position

  if ts.is_pressed:
      Sound.beep()
      reward = 1

  records.pop()
  records.insert(0, reward)
  precision = records.count(1) / numRecords
  print("Precision: " + str(precision))

  return reward

for i in range(numEpochs):
  for j in range(10):
    stateTo = getRandomState()
    maxReward = Q[stateFrom][stateTo]

    for k in range(stateCount):
        if Q[stateTo][k] > maxReward:
            maxReward = Q[stateTo][k]

    reward = performAction()
    Q[stateFrom][stateTo] = (1 - LEARNING_RATE_ALPHA) * Q[stateFrom][stateTo] + LEARNING_RATE_ALPHA * (reward + (DISCOUNT_FACTOR_GAMMA * maxReward))
    stateFrom = stateTo

  stateTo = getRandomState()
  performAction()
  stateFrom = stateTo

  lcd.clear()
  lcd.draw.text((10, 20), str(precision * 100) + "%", font=fonts.load('luBS24'))
  lcd.update()