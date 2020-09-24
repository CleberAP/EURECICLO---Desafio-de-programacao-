# Define Gallon

class Container():

    def __init__(self, capacity=0.0, container_type=None, content=None, measure=None, registry=None, material=None, brand=None):
        self.registry = registry        # container registry
        self.type = container_type      # container type
        self.capacity = capacity        # storage capacity
        self.measure = measure          # unit of measurement
        self.material = material        # container material type
        self.content = content          # Records the type of content stored
        self.brand = brand              # container brand

    # GETTERS
    def get_registry(self):
        return self.registry

    def get_type(self):
        return self.type
    
    def get_capacity(self):
        return self.capacity

    def get_measure(self):
        return self.measure

    def get_material(self):
        return self.material

    def get_content(self):
        return self.content

    def get_brand(self):
        return self.brand
    
    # SETTERS
    def set_registry(self, registry):
        self.registry = registry

    def set_type(self, container_type):
        self.type = container_type
        
    def set_capacity(self, value):
        self.capacity = value

    def set_measure(self, measure):
        self.measure = measure

    def set_material(self, material):
        self.material= material

    def set_content(self, content):
        self.content = content

    def set_brand(self, brand):
        self.brand = brand

    # OTHER METHODS
    def get_info(self):

        response = "registry:"

        if self.registry is not None:
            response = ' '.join([response, self.registry])
        else:
            response = ' '.join([response, 'Without registry'])

        if self.type is not None:
            response = ' - tipo: '.join([response, self.type])
        else:
            response = ' - '.join([response, 'undefined container'])

        if self.capacity > 0:
            response = ' - capacity: '.join([response, str(self.capacity)])
            if self.measure is not None:
                response = ''.join([response, self.measure])
        else:
            response = ' - '.join([response, 'undefined capacity'])

        if self.content is not None:
            response = ' - content: '.join([response, self.content])

        if self.brand is not None:
            response = ' - brand: '.join([response, self.brand])
            
        if self.material is not None:
            response = ' - material: '.join([response, self.material])

        return response

    def get_info_dict(self):

        dict_info = {}
        dict_info['registry'] = self.registry if not None else 'Without registry'
        dict_info['type'] = self.type if self.type is not None else 'undefine container'
        dict_info['capacity'] = str(self.capacity).replace('.',',') # Convert dot to comma
        dict_info['measure'] = self.measure
        dict_info['content'] = self.content
        dict_info['brand'] = self.brand
        dict_info['material'] = self.material

        return dict_info

