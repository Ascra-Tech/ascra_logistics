import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_items():
    filters = {}  # Define your filters here
    item_barcode = frappe.local.form_dict.get('item_barcode', '')
    qr_rack = frappe.local.form_dict.get('qr_rack', '')
    if item_barcode :
        filters['custom_barcode'] = item_barcode
    if qr_rack :
        filters['custom_rack_name'] = qr_rack

    items = frappe.get_all('Item', fields=[
        'name',
        'item_code',
        'item_group',
        'stock_uom',
        'custom_barcode',
        'custom_rack_name',
    ], filters=filters, order_by='name asc')
    
    # Don't use frappe.response directly, return a dictionary instead
    if not items:
        return {
            'status': 'success',
            'message': 'No items found.',
            'data': []
        }
    else:
        return {
            'status': 'success',
            'message': 'Items fetched successfully.',
            'data': items
        }