import pandas as pd
import pickle
import os

def process_and_cache_data(classification_file, cache_file):
    if os.path.exists(cache_file):
        print('Loading classification data from cache...\n')
        with open(cache_file, 'rb') as f:
            print('Upload completed\n')
            return pickle.load(f)
        
    print('Processing data...\n')
    
    #Load and process neuron info
    neuroInfo = pd.read_csv(classification_file)
    
    #Process different neuron types
    Optic_neurons_Right = neuroInfo[(neuroInfo['super_class'] == 'optic') & (neuroInfo['side'] == 'right')]
    Sensory_neurons_Right = neuroInfo[(neuroInfo['super_class'] == 'sensory') & (neuroInfo['side'] == 'right')]
    
    #Retina field
    R1_6_Right_Info = Sensory_neurons_Right[Sensory_neurons_Right['cell_type'] == 'R1-6'][['root_id']]
    R7_8_Right_Info = Sensory_neurons_Right[Sensory_neurons_Right['cell_type'].isin(['R7', 'R8'])][['root_id']]
    ocellar_retinula_Right_Info = Sensory_neurons_Right[Sensory_neurons_Right['cell_type'] == 'ocellar_retinula_cell'][['root_id']]
    
    #Lamina
    L1_5_Right_Info = Optic_neurons_Right[Optic_neurons_Right['sub_class'] == 'L1-5'][['root_id']]
    T1_3_Right_Info = Optic_neurons_Right[Optic_neurons_Right['sub_class'].isin(['T1', 'T2', 'T3'])][['root_id']]
    Am_Right_Info = Optic_neurons_Right[Optic_neurons_Right['sub_class'] == 'Am'][['root_id']]
    C2_3_Right_Info = Optic_neurons_Right[Optic_neurons_Right['sub_class'].isin(['C2', 'C3'])][['root_id']]
    
    #Prepare data for caching
    data = {
        'R1_6_Right_Info': R1_6_Right_Info,
        'R7_8_Right_Info': R7_8_Right_Info,
        'ocellar_retinula_Right_Info': ocellar_retinula_Right_Info,
        'L1_5_Right_Info': L1_5_Right_Info,
        'T1_3_Right_Info': T1_3_Right_Info,
        'Am_Right_Info': Am_Right_Info,
        'C2_3_Right_Info': C2_3_Right_Info
        
    }
    
    print('Saving processed data to cache...\n')
    with open(cache_file, 'wb') as f:
        pickle.dump(data, f)
        
    return data


def main():
    classification_file = '../connectome_materials/classification.csv.gz'
    cache_file = 'processed_neuron_classification.pkl'

    data = process_and_cache_data(classification_file, cache_file)
    
    return data

if __name__ == '__main__':
    main()
    