{
    'name': 'Hospital Management System',
    'version': '1.0',
    'summary': 'Manage patients and hospital data',
    'author': 'You',
    'category': 'Healthcare',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/hms_department_views.xml',
        'views/hms_doctor_views.xml',
        'views/base_menu.xml',
        'views/hms_patient_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': True,
}
