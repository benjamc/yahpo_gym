_yahpo_default_dict = {
    'basedir': "/home/flo/LRZ Sync+Share/multifidelity_data",
    'config_id': "",
    'surrogate': "model.onnx",
    'dataset': "data.csv",
    'config_space': "config_space.json",
    'y_names' : [],
    'cont_names': [],
    'cat_names': [],
    'fidelity_params': [],
    'runtime_name': ""
}

class Configuration():
    def __init__(self, config_dict):
        config = _yahpo_default_dict.copy()
        config.update(config_dict)
        self.config = config
        # Set properties
        self.config_id = self.config["config_id"]
        self.y_names = self.config["y_names"]
        self.cat_names = self.config["cat_names"]
        self.cont_names = self.config["cont_names"]
        self.fidelity_params = self.config["fidelity_params"]
        
    def get_path(self, key):
        return f"{self.config_path}/{self.config[key]}"
    
    @property
    def config_path(self):
        return f"{self.config['basedir']}/{self.config['config_id']}"
     
    def __repr__(self): 
        return f"Configuration: ({self.config['config_id']})"

    def __str__(self):
        return self.config.__str__()

class ConfigDict():
    def __init__(self):
        self.configs = {}
    def update(self, config):
        self.configs.update(config)
    
    def get_item(self, key):
        return Configuration(self.configs[key])

    def __repr__(self):
        return self.configs.__repr__()
    
    def __str__(self):
        return self.configs.__str__()


def cfg(config_id = None):
    if config_id is not None:
        return config_dict.get_item(config_id)
    else:
        return config_dict

config_dict = ConfigDict()

if __name__ == '__main__':
    print(cfg())