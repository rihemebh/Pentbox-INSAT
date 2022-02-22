
import requests
from requests_kerberos import HTTPKerberosAuth
r = requests.get("http://example.org", auth=HTTPKerberosAuth())
