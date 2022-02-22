import os
import logging
import datetime

#https://selvaganesh93.medium.com/python-impala-flask-integration-using-kerberos-authentication-part-1-212fe9321c4d
class Kdc:
    def __init__(self, username, keytabpath):
        self.username = username
        self.keytabpath = keytabpath
        os.system("wsl")

    def create_ticket(self):
        command = (
                "kinit "
                + self.username
                + "@xyz.domain.com"
                + " -k -t "
                + self.keytabpath
        )
        logging.info("Creating ticket ... %s", command)
        result = os.system(command)
        logging.info("Ticket created")
        return result

        def list_kerberos(self):
            command = "klist -kt " + self.keytabpath
            result = os.popen(command).read()
            return result