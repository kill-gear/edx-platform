"""
  Constants and strings for the course-enrollment app
"""

# Captures strings composed of alphanumeric characters a-f and dashes.
PROGRAM_UUID_PATTERN = r'(?P<program_uuid>[A-Fa-f0-9-]+)'
MAX_ENROLLMENT_RECORDS = 25

# The name of the key that identifies students for POST/PATCH requests
REQUEST_STUDENT_KEY = 'external_user_key'

class CourseEnrollmentResponseStatuses(object):
    """
    Class to group response statuses returned by the course enrollment endpoint
    """
    ACTIVE = "active"
    INACTIVE = "inactive"
    DUPLICATED = "duplicated"
    INVALID_STATUS = "invalid-status"
    CONFLICT = "conflict"
    ILLEGAL_OPERATION = "illegal-operation"
    NOT_IN_PROGRAM = "not-in-program"
    INTERNAL_ERROR = "internal-error"

    ERROR_STATUSES = (
        DUPLICATED,
        INVALID_STATUS,
        CONFLICT,
        ILLEGAL_OPERATION,
        NOT_IN_PROGRAM,
        INTERNAL_ERROR,
    )
