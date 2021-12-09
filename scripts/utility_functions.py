import pandas as pd
from IPython import get_ipython
ipython = get_ipython()


def goto_project_folder(use_colab):
    # Import with EPFL google drive!
    if use_colab:
        from google.colab import drive
        drive.mount('/content/drive', force_remount=True)
        ipython.magic('%cd /content/drive/Shareddrives/ADA-project')
        
def downgrade_pandas(use_colab):
    if use_colab:
        ipython.magic('!pip install pandas==1.0.5')
        print(pd.__version__)

def load_mini_version_of_data(path_to_file, chunksize, nb_chunks):
    """
    Returns a mini dataframe from of a bz2 compressed json file.
    :path_to_file   file path as string
    :chunksize      size to iterate
    :nb_chunks      how many chunks
    :return         pandas.DataFrame with chunksize*nb_chunks of rows
    """
    
    curr_chunk = 0
    chunk_list = []
    
    if use_colab:
        for chunk in pd.read_json(path_to_file, lines=True, compression='bz2', chunksize=chunksize):
            if curr_chunk == nb_chunks:
                break
            curr_chunk = curr_chunk + 1
            chunk_list.append(chunk)
    else:
        with pd.read_json(path_to_file, lines=True, compression='bz2', chunksize=chunksize) as df_reader:
            for chunk in df_reader:
                if curr_chunk == nb_chunks:
                    break 
                curr_chunk = curr_chunk + 1
                chunk_list.append(chunk)
    
    df = pd.concat(chunk_list)
    return df

def convert_to_1Dseries(series):
    """
    Converts a 2D pandas series containing lists into a 1D pandas series.
    :series     2D pandas.Series
    :return     1D pandas.Series
    """
    return pd.Series([x for _list in series for x in _list])

def process_data_in_chunks(path_to_file, process_chunk, add_function, result):
    """
    """
    if use_colab:
        for chunk in pd.read_json(path_to_file, lines=True, compression='bz2', chunksize=100000):
            tmp = process_chunk(chunk)
            result = add_function(result, tmp)
    else:
        with pd.read_json(path_to_file, lines=True, compression='bz2', chunksize=100000) as df_reader:
            for chunk in df_reader:
                tmp = process_chunk(chunk)
                result = add_function(result, tmp)
    return result