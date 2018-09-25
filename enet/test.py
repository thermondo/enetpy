from .base import BaseAPIWrapper

from . import types
from zeep.exceptions import Fault


class FakeAPIWrapper(BaseAPIWrapper):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._storage = {}

    def get_gas_grid_operator_for_address(
            self, zip_code, city, street, house_number, _ignore_multiple=True
    ):
        if zip_code == '':
            raise Fault("SOAP Fault 'InputError' (10101) occured: PLZ wurde nicht eingegeben.")
        if int(zip_code) < 9000:
            raise Fault("SOAP Fault 'InputError' (10101) occured: PLZ ist ungültig")

        return types.GasGridOperator(
            vnbg_nr=107851,
            title='NBB Netzgesellschaft Berlin-Brandenburg mbH & Co. KG',
            email='netzzugang@nbb-netzgesellschaft.de',
            contact_name='Herr Cornelius Baumann',
            phone_number='030/81876-1382',
            fax_number='',
            gas_type='H-Gas'
        )
