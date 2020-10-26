from glm import vec3

def lerp(v1, v2, delta):
    return (v1 * (1.0 - delta)) + (v2 * delta)

delta = (19.0 - 4.0) / 20.0

print("i = 0")
p1_0 = vec3(15, 5, 2)
p2_0 = vec3(10, 2, 2)
p3_0 = vec3(5, 7, 2)
p4_0 = vec3(0, 0, 2)
print("    p1_0: ", p1_0)
print("    p2_0: ", p2_0)
print("    p3_0: ", p3_0)
print("    p4_0: ", p4_0)

print("i = 1")
p1_1 = lerp(p1_0, p2_0, delta)
p2_1 = lerp(p2_0, p3_0, delta)
p3_1 = lerp(p3_0, p4_0, delta)
print("    p1_1: ", p1_1)
print("    p2_1: ", p2_1)
print("    p3_1: ", p3_1)

print("i = 2")
p1_2 = lerp(p1_1, p2_1, delta)
p2_2 = lerp(p2_1, p3_1, delta)
print("    p1_2: ", p1_2)
print("    p2_2: ", p2_2)

print("i = 3")
p1_3 = lerp(p1_2, p2_2, delta)
print("    p1_3: ", p1_3)