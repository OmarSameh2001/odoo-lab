{
    'name': 'Hospital Management System',
    'version': '1.0',
    'summary': 'Manage patients and hospital data',
    'author': 'You',
    'category': 'Healthcare',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/hms_patient_views.xml',
    ],
    'installable': True,
    'application': True,
}
