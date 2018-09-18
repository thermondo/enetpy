import logging

from zeep import Client

from . import types, exceptions, base

logger = logging.getLogger('enet')


class LiveAPIWrapper(base.BaseAPIWrapper):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__client = None

    @property
    def _client(self):
        """Load lazily the SOAP client so that we don't do it when the GGO result is cached."""
        if self.__client is None:
            self.__client = Client(wsdl=self._wsdl_url)
            self.__client.set_default_soapheaders({'AuthHeader': self._auth_token})
        return self.__client

    def get_gas_grid_operator_for_address(
            self, zip_code, city, street, house_number, _ignore_multiple=True
    ):
        data = {
            'PLZ': zip_code,
            'Ort': city,
            'Strasse': street,
            'Hausnummer': house_number,
        }
        result = self._client.service.NetzbetreiberGas(request=data)[0]

        try:
            return types.GasGridOperator(
                vnbg_nr=result['VNBG_Nr'],
                title=result['Netzbetreibername'],
                contact_name=result['Netzbetreiber_Ansprechpartner'] or '',
                phone_number=result['Netzbetreiber_Telefon'] or '',
                fax_number=result['Netzbetreiber_Fax'] or '',
                email=result['Netzbetreiber_Email'].replace('mailto:', '') or '',
                gas_type=result['Marktgebiete']['Marktgebiet'][0]['Name'][:5]
            )
        except (KeyError, IndexError) as e:
            raise exceptions.UnexpectedResponse(
                "Unexpected response %r for: %r" % (result, data)
            ) from e
