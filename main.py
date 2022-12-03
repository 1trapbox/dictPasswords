def fread(fn :str, mode :str = 'rb', encoding = None):
    with open(fn, mode, encoding = encoding) as f:
        return f.read()

def fwrite(fn :str, data :object, mode :str = 'wb', encoding = None):
    with open(fn, mode, encoding = encoding) as f:
        f.write(data)

def splitInHalf(in_fn, out_fn_1, out_fn_2):
    data = fread(in_fn, mode = 'r').split()
    data_size = len(data)

    file_data_1 = '\n'.join(data[0:data_size // 2]).encode()
    file_data_2 = '\n'.join(data[data_size // 2:]).encode()

    fwrite(out_fn_1, file_data_1)
    fwrite(out_fn_2, file_data_2)





