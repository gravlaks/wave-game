from enum import Enum, unique

@unique
class Pose(Enum):
    facing_right = 1
    facing_left = -1

