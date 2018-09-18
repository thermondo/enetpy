import abc

__all__ = ('BaseAPIWrapper',)


class BaseAPIWrapper(abc.ABC):
    def __init__(self, wsdl_url, auth_token):
        self._wsdl_url = wsdl_url
        self._auth_token = auth_token

    @abc.abstractmethod
    def get_gas_grid_operator_for_address(
            self, zip_code, city, street, house_number,  _ignore_multiple=True
    ):
        """
        Return gas grid operator information for a given address.

        Args:
            zip_code (int or str): Zip code as int or string
            city (str): City name
            street (str): Street name
            house_number (int or str): House number as int or string
            _ignore_multiple (bool): If ``False`` raise error for multiple results.

        Returns:
            GasGridOperator: Most likely operator for the given address.

        Raises:
            zeep.exceptions.Fault:
                If no zip code is given.
                If zip code does not exist.
            MultipleResultsError: If multiple results are found for given address.

        """
        raise NotImplementedError
