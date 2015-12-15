# internal exceptions
class QualysException(Exception):
    '''
    Top level qualysapi exception event
    '''


class QualysAuthenticationException(QualysException):
    '''
    Raised for authentication exceptions in Qualys
    '''


class NoConnectionError(QualysException):
    '''
    Raised for calls that require a valid connection to Qualys but didn't get
    one.
    '''


class ParsingBufferException(QualysException):
    '''
    Raised for API calls using a parsing buffer in which the buffer had an
    exception of some kind.
    '''