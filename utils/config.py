import os

def get_paremeters():
    parameters = {
        'DATA_PATH': os.path.join('data/'),
        'no_sequences': 50,
        'start_folder': 1,
        'sequence_length': 30,
        'num_epochs': 150,
        'batch_size': 8
    }
    return parameters