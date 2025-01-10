import geojson

print("Mulai eksekusi")

# Data dalam format Python dictionary
data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [107.6, -6.9]
            },
            "properties": {
                "name": "Bandung",
                "description": "Kota Kembang"
            }
        }
    ]
}

print("Data geojson siap")

# Konversi dictionary ke format GeoJSON
geojson_data = geojson.dumps(data, indent=4)

print("Data geojson dikonversi")

# Menyimpan hasil ke file
with open("data.geojson", "w") as file:
    file.write(geojson_data)

print("File GeoJSON berhasil dibuat dengan nama 'data.geojson'")
