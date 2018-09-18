from collections import namedtuple

__all__ = ('GasGridOperator',)

GasGridOperator = namedtuple(
    'GasGridOperator', [
        'vnbg_nr',
        'title',
        'email',
        'contact_name',
        'phone_number',
        'fax_number',
        'gas_type',
    ])
