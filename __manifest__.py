
{
    'name': 'Odoo Whatsapp Connector',
    'version': '16.0.0.1.0',
    'category': 'Extra Tools',
    'summary': """Odoo Whatsapp Connector For Sales, Invoice, and Floating button in Website""",
    'description': """Added options for sending Whatsapp messages and Mails in systray bar,sale order, invoices, 
    website portal view and share the access url of documents using share option available in each records through 
    Whatsapp web..""",
    'author': '...',
    'depends': ['sale', 'account','sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/selection_messages_views.xml',
        'views/portal_whatsapp_view.xml',
        'views/sale_order_inherited.xml',
        'views/account_move_inherited.xml',
        'views/website_inherited.xml',
        'wizard/wh_message_wizard.xml',
        'wizard/portal_share_inherited.xml',
    ],
    'assets': {
        'web.assets_backend': [
            "whatsapp_odoo/static/src/js/whatsapp_button.js",
            "whatsapp_odoo/static/src/js/mail_button.js",
            'whatsapp_odoo/static/src/xml/whatsapp_button.xml',
            'whatsapp_odoo/static/src/xml/mail_button.xml',
        ],
        'web.assets_frontend': [
            "whatsapp_odoo/static/src/js/whatsapp_modal.js",
            "whatsapp_odoo/static/src/js/whatsapp_icon_website.js",
            "whatsapp_odoo/static/src/css/whatsapp.css"
        ],
    },
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
