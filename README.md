# enetpy

Python wrapper for the ene't Marktpartner API

### Setup

Install the package:

```bash
pip install enetpy
```

Make sure to set the authentication token in your production environment.

```bash
export ENET_AUTH_TOKEN='****'
```

#### Testing

The API wrapper comes with a testing stub. To use it set your test environment to:

```bash
export ENET_TESTING_STUB=1
```

### Usage

```python
>>> from enet import api
>>> api.get_gas_grid_operator_for_address(
...     zip_code='10115',
...     city='Berlin',
...     street='Brunnenstr.',
...     house_number='153'
... )
GasGridOperator(vnbg_nr=107851, title='NBB Netzgesellschaft Berlin-Brandenburg mbH & Co. KG', email='netzzugang@nbb-netzgesellschaft.de', contact_name='Herr Cornelius Baumann', phone_number='030/81876-1382', fax_number='', gas_type='H-Gas')
```
