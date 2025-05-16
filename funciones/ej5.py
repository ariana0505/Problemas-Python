def _area_of_circle(radius: float) -> float:
    return radius ** 2

def _volume_of_cylinder(radius: float, height: float) -> str:
    area_circle = _area_of_circle(radius)
    volume = area_circle * height
    return f"Volume is {volume}π"

  