import rotatescreen
import time
srn = rotatescreen.get_primary_display()
for i in range(10):
    time.sleep(1)
    srn.rotate_to(i * 90 % 360)

