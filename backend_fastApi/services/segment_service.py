import json

from sqlalchemy import text
from database import engine


SCORE_COLUMNS = {
    "pl": "score_test_pl",
    "vul": "score_test_vul",
    "vc": "score_test_vc"
}


def get_segments(vehicle: str):

    if vehicle not in SCORE_COLUMNS:
        raise ValueError("Type de véhicule invalide")

    score_column = SCORE_COLUMNS[vehicle]

    query = text(f"""
        SELECT
            id,
            source_objectid,
            road_number,
            shape_length,
            {score_column} AS score,

            ST_AsGeoJSON(
                ST_Transform(geom, 4326)
            ) AS geometry

        FROM road_segments_test
        ORDER BY id;
    """)

    with engine.connect() as connexion:

        result = connexion.execute(query)

        rows = result.mappings().all()

    features = []

    for row in rows:

        feature = {
            "type": "Feature",

            "properties": {
                "id": row["id"],
                "road_number": row["road_number"],
                "shape_length": row["shape_length"],
                "score": row["score"],
                "vehicle": vehicle
            },

            "geometry": json.loads(row["geometry"])
        }

        features.append(feature)

    return {
        "type": "FeatureCollection",
        "features": features
    }