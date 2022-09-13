import math
cos_angles = [math.cos(math.radians(int(input("Angle: ")))) for _ in range(int(input("How many angles?: ")))]
times = [float(input("time: ")) for _ in range(int(input("How many times?: ")))]
times_cos_angles = [time*cos_angle for time,cos_angle in zip(times,cos_angles)]
for index, time_cos_angles in enumerate(times_cos_angles): print(f"t cos \u03F4 {index+1}: {time_cos_angles}")
