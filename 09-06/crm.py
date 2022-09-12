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
        processed_leads = [{k: str(lead.split()[i]) for i, k in enumerate(PROCESSED_LEAD_KEYS)} for lead in leads]
        return [enrich_leads(key=k, value=v) for p_lead in processed_leads for k, v in p_lead]

    return None


def enrich_leads(key: str, value: str) -> None:
    """Match the key and process the value with the correct method"""
    match key:
        case 'first_name':
            value.replace(' ', '')
        case 'last_name':
            value.lower()
        case 'email':
            print(f'Importing {value}') if 'gmail' or 'hotmail' in value else print('Custom mail server.')
        case 'twitter':
            value.replace('@', '')
        case 'website':
            value.replace('https://', '')




class Lead:
    touchpoints = []
    company_size = ''
    _company_website = ''
    days_since_last_post = 0
    discount = 1

    def get_lead_score(self):
        return 1 if self.recent_blog_post() else 0

    def recent_blog_post(self):
        return self.days_since_last_post < 5

    def get_lifetime_value(self, product):
        mrr = product.base_price() * self.discount
        return mrr * 12


class Customer:
    company_size = ''
    lead = Lead()
    company_website = ''

    def __init__(self, lead):
        self.company_size = lead.company_size
        self.company_website = lead._company_website
        self.lead = lead


class CRMImportEntry:
    """Entry imported from our legacy CRM."""

    def __init__(self):
        imported_data = {
            'name': {
                'first': 'John',
                'last': 'Smith'
            },
            'company': 'ACME',
            'deals': [13435, 33456]
        }

        self.first_name = imported_data.get('name', dict(first='', last='')).get('first', '')
        self.last_name = imported_data.get('name', dict(first='', last='')).get('last', '')
        self.num_deals = len(imported_data.get('deals', []))


def convert_lead(lead):
    if lead.company_size == 'smb':
        send_smb_funnel()
    elif lead.company_size == 'mid_market':
        send_mid_market_funnel()
    elif lead.company_size == 'enterprise':
        log_manual_sales_follow_up()
    else:
        print('Wrong lead company type!')


def send_smb_funnel(services=''):
    client = services.email.client('transactional', region='eu-ireland')
    response = client.send_email(
        destination='test@gmail.com',
        message={
            'body': {'Text': {'Hello small business!'}},
            'subject': {'Text': {'Buy our stuff!'}}
        },
        source='refactoring@course.com'
    )
    print(response)


def send_mid_market_funnel(services=''):
    client = services.email.client('transactional', region='eu-ireland')
    response = client.send_email(
        destination='test@gmail.com',
        message={
            'body': {'Text': {'Hello medium sized business!'}},
            'subject': {'Text': {'Buy our stuff!'}}
        },
        source='refactoring@course.com'
    )
    print(response)


def log_manual_sales_follow_up(services=''):
    client = services.email.client('transactional', region='eu-ireland')
    response = client.send_email(
        destination='internal.sales@course.com',
        message={
            'body': {'Text': {'Go say hello to this business!'}},
            'subject': {'Text': {'Buy our stuff!'}}
        },
        source='refactoring@course.com'
    )
    print(response)


def prioritize_lead(lead):
    if (lead.company_size > 100) and \
            (lead.company_website.endswith(' .com')) and \
            (lead.company_size < 0) and (len(lead.touchpoints)) == 0:
        lead.priority = 100
