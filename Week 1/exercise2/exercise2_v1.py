# zarib shekast made
sample = {
        "refractive_error": "myopia",
        "object_distance_cm": 50,
        "refractive_index": 1.5
}
# refrective_error = sample["refrective_error"]
error_type = sample["refractive_error"]
object_distance = sample["object_distance_cm"]
refrective_index = sample["refractive_index"]
def calc_facal_length(d0,di =2):
     facal = 1/((1/d0) + (1/di))
     return facal
def lens_power_diopters(facal_length):
    power = 100 / facal_length
    return power
def calc_radius_of_curvature_m(refractive_index,power):   
     radius = ((refractive_index -1) **2 )/power
     return radius
facal_length = round(calc_facal_length(object_distance),2)
power = round(lens_power_diopters(facal_length),2)
radius = round(calc_radius_of_curvature_m(refrective_index,power),4)
print(f"""Results:
    Type : {error_type.capitalize()}
    Power : {power} D
    Radius : {radius} M
    Facal Length : {facal_length} Cm""")
