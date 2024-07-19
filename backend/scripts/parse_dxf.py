import ezdxf

def parse_dxf(file_path):
    doc = ezdxf.readfile(file_path)
    points = []
    
    for entity in doc.modelspace().query('LWPOLYLINE'):
        points.extend(entity.points)
    
    return points

# Example usage
# dxf_file = 'path/to/file.dxf'
# points = parse_dxf(dxf_file)
# print(points)
