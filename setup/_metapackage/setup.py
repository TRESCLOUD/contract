import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-contract",
    description="Meta package for oca-contract Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-agreement',
        'odoo12-addon-agreement_legal',
        'odoo12-addon-agreement_maintenance',
        'odoo12-addon-agreement_mrp',
        'odoo12-addon-agreement_repair',
        'odoo12-addon-agreement_sale',
        'odoo12-addon-agreement_serviceprofile',
        'odoo12-addon-agreement_stock',
        'odoo12-addon-contract',
        'odoo12-addon-contract_sale',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
