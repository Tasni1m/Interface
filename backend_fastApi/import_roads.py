import json
from pathlib import Path

from sqlalchemy import text

from database import engine


# Chemin vers le fichier GeoJSON
geojson_path = (
    Path(__file__).parent.parent
    / "data"
    / "raw"
    / "DGC_OFROU_RTE_PRINCIPALE.geojson"
)


# 1. Lire le fichier GeoJSON
with open(geojson_path, "r", encoding="utf-8") as fichier:
    data = json.load(fichier)


features = data["features"]

print("Nombre de tronçons trouvés :", len(features))


# 2. Insérer les tronçons dans PostGIS
with engine.begin() as connexion:

    for feature in features:

        properties = feature["properties"]
        geometry = feature["geometry"]

        requete = text("""
            INSERT INTO road_segments_test (
                source_objectid,
                road_number,
                shape_length,
                geom
            )
            VALUES (
                :objectid,
                :road_number,
                :shape_length,

                ST_Transform(
                    ST_SetSRID(
                        ST_GeomFromGeoJSON(:geometry),
                        4326
                    ),
                    2056
                )
            )
        """)

        connexion.execute(
            requete,
            {
                "objectid": properties["OBJECTID"],
                "road_number": properties["NUM_RTE_PRINCIPALE"],
                "shape_length": properties["SHAPE_LEN"],
                "geometry": json.dumps(geometry)
            }
        )


print("Import terminé.")