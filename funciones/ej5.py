def _area_of_circle(radius:float):
    area = radius**2
    return f"{area}π"

def _volume_of_cylinder(radius:float, height: float):
    area_cicle = _area_of_circle(radius)
    area_cicle = area_cicle.split("π")[0]
    volume = area_cicle * height
    return f"Volume is {volume}"


