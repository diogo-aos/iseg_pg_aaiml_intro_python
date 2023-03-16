def read_csv(fn: str) -> list:
    # csv = comma separated values
    data = []
    with open(fn) as f:
        for i,line in enumerate(f):
            if i != 0: # ignore first line with column names
                try:
                    # split lines by comma
                    v1,v2 = line.split(',')
                    v1,v2 = float(v1), float(v2)
                    data.append((v1,v2))
                except:
                    print(f"error in line {i}, ignored")
                
    return data

