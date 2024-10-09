{
	#  Informacion general
	'name': 'Seguimiento de ordenes de producción',
	'version': '16.0',
	'summary': 'Seguimiento ordenes de producción',
    'price': 150.0,
    'currency': 'USD',
	'description': 'Permite visualizar el seguimiento de las ordenes de producción, desde el módulo de ventas',
	'category': 'other',

	# Author
	'author': 'Josué Wilfredo Henríquez Arevalo',
	'website': 'https://www.odoo.com',
	'license': 'Other proprietary',

	#  Depends
	'depends': ['base', 'sale', 'stock', 'account', 'mrp'],
	'external_dependencies': {},
	'data': [
        'view/view_ordenes_seguimiento.xml'

            ],

	#  Others
	'installable': True,
	'auto_install': False,

}
