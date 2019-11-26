class Contractors(object):

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @staticmethod
    def from_dict(source):
        # [START_EXCLUDE]
        contractors = Contractors(source[u'projectName'], source[u'projectEmail'])

        if u'projectName' in source:
            contractors.name = source[u'projectName']

        if u'projectEmail' in source:
            contractors.email = source[u'projectEmail']

        return contractors
        # [END_EXCLUDE]

    def to_dict(self):
        # [START_EXCLUDE]
        dest = {
            u'projectName': self.name,
            u'projectEmail': self.email
        }

        if self.name:
            dest[u'projectName'] = self.name

        if self.email:
            dest[u'projectEmail'] = self.email

        return dest
        # [END_EXCLUDE]

    def __repr__(self):
        return(
            u'Contractors(projectName={}, projectEmail={})'
            .format(self.name, self.email))

