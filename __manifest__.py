{
    'name': 'EkoSystem E-Commerce Base',
    'version': '19.0.1.0.0',
    'category': 'Website/Website',
    'summary': 'Kategorie, tagi i atrybuty produktów dla e-commerce',
    'description': """
EkoSystem E-Commerce Base
=========================
Moduł bazowy z danymi niezbędnymi do funkcjonowania sklepu e-commerce:
- Kategorie produktów (publiczne i wewnętrzne)
- Atrybuty produktów z wartościami
- Tagi produktów

Instaluj ten moduł ZAWSZE gdy korzystasz z e-commerce.
Dane demo (produkty, zasoby, grupy) są w osobnym module ekosystem_demo01.
    """,
    'author': 'Navigare Space Ltd',
    'website': 'https://navigare.space',
    'license': 'OPL-1',
    'depends': [
        'ekobookapp',
        'website_sale',
    ],
    'data': [
        'data/product_categories.xml',
        'data/product_category_booking_types.xml',
        'data/product_public_categories.xml',
        'data/product_attributes.xml',
        'data/product_tags.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
