def map_by_year(json_data):
    mapper = {}
    for obj in json_data:
        if str(obj['year']) in mapper.keys():
            mapper[str(obj['year'])].append({
                obj['state']: obj['value']
            })
        else:
            mapper[str(obj['year'])] = []
            mapper[str(obj['year'])].append({
                obj['state']: obj['value']
            })
    return mapper
