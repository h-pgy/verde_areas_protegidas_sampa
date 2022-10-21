from .utils.file_path import solve_dir, solve_path


ORIGINAL_DATA_FOLDER = solve_dir('original_data')
SHP_FOLDER = solve_dir(solve_path('shp_files', ORIGINAL_DATA_FOLDER))
ZIP_FOLDER = solve_dir(solve_path('shp_zips', ORIGINAL_DATA_FOLDER))

URIS_CAMADAS = {
        'unidades_de_conservacao' : r'09_Verde%20e%20Recursos%20Naturais%5C%5CUnidades%20de%20Conserva%E7%E3o%5C%5CShapefile%5C%5CSIRGAS_SHP_unidadeconservacao',
        'parques_municipais' : r'09_Verde e Recursos Naturais\\Parques Municipais\\Shapefile\\SIRGAS_SHP_parquemunicipal',
        'terras_indigenas' : r'13_Legisla%E7%E3o%20Urbana%5C%5CTerras%20Ind%EDgenas%5C%5CShapefile%5C%5CSIRGAS_SHP_terraindigena',
        'rmsp' : r'01_Limites%20Administrativos%5C%5CMunic%EDpios%20do%20ESP%5C%5CShapefile%5C%5CSIRGAS_limites_municipios_estado_sao_paulo'
        }

