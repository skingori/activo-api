valid_asset_category_data = {
        "name": "Headset",
        "attributes": [
            {
                "label": "brand", "is_required": True,
                "input_control": "text", "choices": "null"
             },
            {
                "label": "color", "is_required": True,
                "input_control": "dropdown", "choices": "blue,red,black"
             }
        ]
}

invalid_asset_category_data = {
        "name": "Headset",
        "attributes": [
            {
                "labe": "brand", "is_required": True,
                "input_control": "text", "choices": "null"
             },
            {
                "label": "color", "is_required": True,
                "input_control": "dropdown", "choices": "blue,red,black"
             }
        ]
}