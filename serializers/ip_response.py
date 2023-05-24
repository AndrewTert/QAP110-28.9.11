from pydantic import BaseModel, validator


class IPResponse(BaseModel):
    ip: str
    network: str
    version: str
    city: str
    region: str
    region_code: str
    country: str
    country_name: str
    country_code: str
    country_code_iso3: str
    country_capital: str
    country_tld: str
    continent_code: str
    in_eu: bool
    postal: str
    latitude: float
    longitude: float
    timezone: str
    utc_offset: str
    country_calling_code: str
    currency: str
    currency_name: str
    languages: str
    country_area: float
    country_population: int
    asn: str
    org: str

    @validator('country')
    def country_length(cls, value):
        if len(value) != 2:
            raise ValueError('Field "country" must be 2 chars')
        return value

    @validator('country_code')
    def country_code_length(cls, value):
        if len(value) != 2:
            raise ValueError('Field "country_code" must be 2 chars')
        return value

    @validator('country_code_iso3')
    def country_code_iso_length(cls, value):
        if len(value) != 3:
            raise ValueError('Field "country" must be 3 chars')
        return value

    @validator('version', 'asn')
    def validator_alphanumeric(cls, v):
        assert v.isalnum(), f'{v} must be alphanumeric'
        return v

    @validator('region', 'region_code', 'country', 'currency', 'currency_name')
    def validator_alpha(cls, v):
        assert v.isalpha(), f'{v} must contain only text symbols'
        return v

    @validator('utc_offset')
    def validator_utc_offset(cls, v):
        sign = v[:1]
        num = v[1:]
        assert num.isdigit() and len(num) == 4 and (
                sign == '+' or sign == '-'), f'{v} must be in format: +HHMM or -HHMM, where HHMM digits'
        return v

    @validator('country_calling_code')
    def validator_country_calling_code(cls, v):
        sign = v[:1]
        num = v[1:]
        assert num.isdigit() and sign == '+', f'{v} must be in format: +T..., where T... some digits'
        return v
