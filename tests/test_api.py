import pytest
from zeep.exceptions import Fault

from enet import types


class TestAPIWrapper:
    def test_get_gas_grid_operator_for_address__success(self, api):
        operator = api.get_gas_grid_operator_for_address(
            '10115', 'Berlin', 'Brunnenstr.', 153
        )

        assert operator == types.GasGridOperator(
            vnbg_nr=107851,
            title='NBB Netzgesellschaft Berlin-Brandenburg mbH & Co. KG',
            email='netzzugang@nbb-netzgesellschaft.de',
            contact_name='Herr Cornelius Baumann',
            phone_number='030/81876-1382',
            fax_number='',
            gas_type='H-Gas'
        )

    def test_get_gas_grid_operator_for_address__no_result(self, api):
        with pytest.raises(Fault) as e:
            api.get_gas_grid_operator_for_address(
                '00000', 'Berlin', 'nowhere', 0
            )
        assert e.value.message == "SOAP Fault 'InputError' (10101) occured: PLZ ist ungültig"

    def test_get_gas_grid_operator_for_address__no_plz(self, api):
        with pytest.raises(Fault) as e:
            api.get_gas_grid_operator_for_address(
                '', 'Berlin', '', 0,
            )
        assert e.value.message == (
            "SOAP Fault 'InputError' (10101) occured: PLZ wurde nicht eingegeben."
        )
