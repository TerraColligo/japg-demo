# -*- coding: utf-8 -*-

{
    'name': 'Nomina Electrónica para México CFDI v1.2 EE',
    'summary': 'Agrega funcionalidades para timbrar la nómina electrónica en México para la versión EE.',
    'description': '''
    Nomina CFDI Module
    ''',
    'author': 'IT Admin',
    'version': '12.9',
    'category': 'Employees',
    'depends': [
        'base', 'hr', 'hr_payroll'
    ],
    'data': [
        'data/sequence_data.xml',
        'data/cron.xml',
        'views/hr_employee_view.xml',
        'views/hr_contract_view.xml',
        'views/hr_salary_view.xml',
        'views/hr_payroll_payslip_view.xml',
        'views/tablas_cfdi_view.xml',
        'views/res_company_view.xml',
        'report/report_payslip.xml',
        'views/res_bank_view.xml',
        'data/mail_template_data.xml',
        'security/ir.model.access.csv',
        'data/res.bank.csv',
        'views/menu.xml',
        'views/horas_extras_view.xml',
        'wizard/wizard_liquidacion_view.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'AGPL-3',
}
