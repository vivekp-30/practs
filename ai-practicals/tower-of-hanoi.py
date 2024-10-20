def moveTower(height, fromPole, toPole, withPole):
  if height >= 1:
    moveTower(height-1, fromPole, withPole, toPole) # Move tower from 'fromPole' to 'withPole'
    moveDisk(fromPole, toPole) # Move disk from 'fromPole' to 'toPole'
    moveTower(height-1, withPole, toPole, fromPole) # Move tower from 'withPole' to  'toPole'
def moveDisk(fp, tp):
 print("Moving disk from", fp, "to", tp)
# Test with height 3 and poles A, B, C
moveTower(3, "A", "B", "C")
