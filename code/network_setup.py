import nest
import csv
import gzip
import pickle
import os

def process_and_cache_data_gzip(csv_file_path, cache_file_path='network_data_cache.pkl'):
    if os.path.exists(cache_file_path):
        print('Loading connections data from cache...\n')
        with open(cache_file_path, 'rb') as f:
            return pickle.load(f)
        
    print('Processing CSV file ...\n')
    neurons = {}
    connections = []
    
    with gzip.open(csv_file_path, 'rt', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pre_id = int(row['pre_root_id'])
            post_id = int(row['post_root_id'])
            syn_count = int(row['syn_count'])
            nt_type = row['nt_type']
            
            for neuron_id in (pre_id, post_id):
                if neuron_id not in neurons:
                    neurons[neuron_id] = nt_type
            
            connections.append([pre_id, post_id, syn_count, nt_type])
            
    data = {
        'neurons': neurons,
        'connections': connections
    }
    
    print('Saving processed data to cache...\n')
    with open(cache_file_path, 'wb') as f:
        pickle.dump(data, f)
        
    return data

def process_and_cache_data_csv(csv_file_path, cache_file_path='network_data_cache_test.pkl'):
    if os.path.exists(cache_file_path):
        print('Loading connections data from cache...\n')
        with open(cache_file_path, 'rb') as f:
            print('Upload completed\n')
            return pickle.load(f)
        
    print('Processing CSV file ...\n')
    neurons = {}
    connections = []
    
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pre_id = int(row['pre_root_id'])
            post_id = int(row['post_root_id'])
            syn_count = int(row['syn_count'])
            nt_type = row['nt_type']
            
            for neuron_id in (pre_id, post_id):
                if neuron_id not in neurons:
                    neurons[neuron_id] = nt_type
            
            connections.append([pre_id, post_id, syn_count, nt_type])
            
    data = {
        'neurons': neurons,
        'connections': connections
    }
    
    print('Saving processed data to cache...\n')
    with open(cache_file_path, 'wb') as f:
        pickle.dump(data, f)
        
    return data

def setup_network(data):
    nest.ResetKernel()
    nest.SetKernelStatus({'resolution': 0.1})
    
    print('Creating neurons...\n')
    neurons = {}
    for neuron_id, nt_type in data['neurons'].items():
        if nt_type == 'GABA':
            neurons[neuron_id] = nest.Create('iaf_psc_alpha', 1, {'I_e': 0.0})
        else:
            neurons[neuron_id] = nest.Create('iaf_psc_alpha', 1, {'I_e': 0.0})
    
    print('Neurons creation completed\n')
    
    print('Creating connections...\n')
    for pre_id, post_id, syn_count, nt_type in data['connections']:
        weight = -5.0 if nt_type == 'GABA' else 5.0
        nest.Connect(neurons[pre_id], neurons[post_id], syn_spec={'weight': weight * syn_count, 'delay': 1.0})
    
    print('Connections creation completed\n')
    
    print('***Network Setup Complete***')
    print(f'Total number of neurons: {len(neurons)}')
    print(f'Total number of connections: {len(data['connections'])}')
        
    return neurons

def main(): 
    return
    csv_file_path = '../connectome_materials/connections.csv.gz'
    cache_file_path = 'network_data_cache.pkl'

    data = process_and_cache_data(csv_file_path, cache_file_path)
    neurons = setup_network(data)
    
    
    
    
if __name__ == '__main__':
    main()
        

