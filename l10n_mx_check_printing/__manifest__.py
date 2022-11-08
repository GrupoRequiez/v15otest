{
    'name': 'MX Check Printing',
    'version': '14.0.1.0.0',
    'author': 'Vauxoo',
    'category': 'Localization',
    'license': 'LGPL-3',
    'summary': 'Print MX Checks',
    'depends': ['l10n_mx', 'account_check_printing'],
    'data': [
        'data/mx_check_printing.xml',
        'report/print_check.xml',
        'report/print_check_generic.xml',
        'report/print_check_bbva_bancomer.xml',
        'report/print_check_banamex.xml',
        'report/print_check_hsbc.xml',
        'report/print_check_santander.xml',
        'report/print_check_scotiabank.xml',
        'views/account_payment_view.xml',
        'views/account_journal_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
