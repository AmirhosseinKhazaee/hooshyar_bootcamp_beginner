import json

class Eye:
    def __init__(self, sample):
        self.sample = sample  
        self.facal_length = self.calc_facal_length(self.refractive_index)
        self.lens_power = self.calc_facal_length() 
    @property
    def sample(self):
        return self._sample  
    
    @sample.setter
    def sample(self, sample):
        is_dict = type(sample) == dict
        if not is_dict :
            print(f"Wrong data type ! : {type(sample).__name__} => dict")
        else:
            neccesary_data= ["refractive_error", "object_distance_cm", "refractive_index"]
            has_neccesary_data = all(key in sample for key in neccesary_data) 
            garbage_data = [garbage for garbage in sample if garbage not in neccesary_data]
            if has_neccesary_data:
                self._sample = sample  
                self.refractive_error = sample["refractive_error"]
                self.object_distance_cm = sample["object_distance_cm"]
                self.refractive_index = sample["refractive_index"]
            else:
                missing_informations = [missed for missed in neccesary_data if missed not in sample]
                for miss_info in missing_informations:
                    print(f'{miss_info.replace("_" , " ").capitalize()} is missed !')
                if garbage_data:
                    for garbage in garbage_data:
                        print(f'garbage / unneccesary data : {garbage}')

    def calc_facal_length(self,di = 2):
        facal = 1/((1/self.object_distance_cm) + (1/di))
        return facal
    
    def calc_lens_power_diopters(self):
        power = 100 / self.facal_length
        return power
    
    def calc_radius_of_curvature_m(self):   
        radius = ((self.refractive_index -1) **2 )/self.lens_power
        return radius


try:
    results = {}
    data = {}
    with open("exercise2\\data.json","r") as file:
        data = json.load(file)
    for i,sample in enumerate(data,1):       
        eye = Eye(sample["input"])
        refractive_error = eye.refractive_error
        facal_length = round(eye.calc_facal_length(),2)
        power = round(eye.calc_lens_power_diopters(),2)
        radius = round(eye.calc_radius_of_curvature_m(),4)
        results[f'Sample {i}'] ={ 
        "lens_power_diopters": power,
        "focal_length_cm": facal_length,
        "radius_of_curvature_m" : radius 
        }
        result = f""" Sample {i} Results:
            Type : {refractive_error.capitalize()}
            Power : {power} D
            Radius : {radius} M
            Facal Length : {facal_length} Cm"""
        print(result)

except Exception as error:
    print(f"error : {error}")
    
with open("exercise2/result.json", "w") as file:
    json.dump(results, file, indent=4)