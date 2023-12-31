import json

data = '''{
    "results": [
        {
            "address_components": [
                {
                    "long_name": "Lagos",
                    "short_name": "Lagos",
                    "types": [
                        "locality",
                        "political"
                    ]
                },
                {
                    "long_name": "Lagos",
                    "short_name": "LA",
                    "types": [
                        "administrative_area_level_1",
                        "political"
                    ]
                },
                {
                    "long_name": "Nigeria",
                    "short_name": "NG",
                    "types": [
                        "country",
                        "political"
                    ]
                }
            ],
            "formatted_address": "Lagos, Nigeria",
            "geometry": {
                "bounds": {
                    "northeast": {
                        "lat": 6.7027591,
                        "lng": 3.4696459
                    },
                    "southwest": {
                        "lat": 6.393351099999999,
                        "lng": 3.0982732
                    }
                },
                "location": {
                    "lat": 6.5243793,
                    "lng": 3.3792057
                },
                "location_type": "APPROXIMATE",
                "viewport": {
                    "northeast": {
                        "lat": 6.7027591,
                        "lng": 3.564808
                    },
                    "southwest": {
                        "lat": 6.393351099999999,
                        "lng": 3.0982732
                    }
                }
            },
            "place_id": "ChIJwYCC5iqLOxARy9nDZ6OHntw",
            "types": [
                "locality",
                "political"
            ]
        }
    ],
    "status": "OK"
}
'''
info = json.loads(data)

if info['status'] == 'OK':
    print('Im good to go!')

