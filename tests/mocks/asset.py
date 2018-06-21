"""
A set of mock asset data for testing asset creation
"""
asset = {'tag': 'Fred\'s Macbook', 'serial': 'sbgdvt4528j8gg'}

no_tag = {'serial': 'sbgdvt4528j8hg'}

no_serial = {'tag': 'Jude\'s Macbook'}

non_existing_category = {
	'tag': 'Fred\'s Macbook',
	'serial': 'sbgdvt4528j8gg',
	'asset_category_id': '-LEiS7lgOu3VmeEBg5cUtt'
}

invalid_category_id = {
	'tag': 'Fred\'s Macbook',
	'serial': 'sbgdvt4528j8gg',
	'asset_category_id': 'LEiS7lgOu3VmeEBg5cU'
}
