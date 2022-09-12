from typing import AnyStr

PROCESSED_LEAD_KEYS = ['first_name', 'last_name', 'email', 'company', 'twitter', 'website']


def read_this_file(filename) -> list[AnyStr]:
    """Open and read a file"""
    with open(filename, 'rb') as f:
        return f.readlines()


def import_leads(leads_file: str) -> list[dict] or None:
    """
    Read the file
    If the file can be read properly: Process, enrich and return the leads
    """
    leads = read_this_file(leads_file)

    if leads:
        processed_leads = [{k: lead.split()[i].decode('utf-8') for i, k in enumerate(PROCESSED_LEAD_KEYS)} for lead in leads]
        processed_leads = [enrich_leads(p_lead) for p_lead in processed_leads]
        return processed_leads

    return None


def enrich_leads(p_lead: dict) -> dict:
    """Match the key and process the value with the correct method"""
    for key, value in p_lead.items():
        match key:
            case 'first_name':
                value.replace(' ', '')
            case 'last_name':
                value.lower()
            case 'email':
                if 'gmail' in value or 'hotmail' in value:
                    print(f'Importing {value}')
                else:
                    print('Custom mail server.')
            case 'twitter':
                value.replace('@', '')
            case 'website':
                value.replace('https://', '')

    return p_lead


print(import_leads('leads.txt'))


class Company:
    def __init__(self, size: str, services: str, source: str) -> None:
        self._company_size = size
        self._services = services
        self._source = source

    @property
    def company_size(self) -> str:
        return self._company_size

    @company_size.setter
    def company_size(self, size: str) -> None:
        self._company_size = size

    @property
    def services(self) -> str:
        return self._services

    @services.setter
    def services(self, service: str) -> None:
        self._services = service

    @property
    def source(self) -> str:
        return self._source

    @source.setter
    def source(self, source: str) -> None:
        self._source = source

    def send_funnel(self,
                    service_type: str,
                    region: str,
                    destination: str,
                    message_body: str,
                    message_subject: str) -> None:
        client = self.services.email.client(service_type, region=region)

        response = client.send_email(
            destination=destination,
            message={
                'body': {'Text': {message_body}},
                'subject': {'Text': {message_subject}}
            },
            source=self.source
        )

        print(response)


if __name__ == '__main__':
    smb = Company(size='smb', services='', source='refactoring@course.com')
    mid_market = Company(size='mid_market', services='', source='refactoring@course.com')
    enterprise = Company(size='enterprise', services='', source='refactoring@course.com')

    smb.send_funnel(
        service_type='transactional',
        region='eu-ireland',
        destination='test@gmail.com',
        message_body='Hello small business!',
        message_subject='Buy our stuff!'
    )
    mid_market.send_funnel(
        service_type='transactional',
        region='eu-ireland',
        destination='test@gmail.com',
        message_body='Hello medium sized business!',
        message_subject='Buy our stuff!'
    )
    enterprise.send_funnel(
        service_type='transactional',
        region='eu-ireland',
        destination='internal.sales@course.com',
        message_body='Go say hello to this business!',
        message_subject='Buy our stuff!',
    )
