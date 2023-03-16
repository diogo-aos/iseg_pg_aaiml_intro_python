def read_csv(fn: str) -> list:
    # csv = comma separated values
    data = []
    with open(fn) as f:
        for line in f:
            # split lines by comma
            v1,v2 = line.split(',')
            v1,v2 = float(v1), float(v2)
            data.append((v1,v2))
    return data

