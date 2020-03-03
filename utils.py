from math import copysign

# Utils

sign = lambda x: int(copysign(1, x)) if x != 0 else 0
