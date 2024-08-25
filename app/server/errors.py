

class UserNotFoundError(Exception):
    """Raised when a user is not found in the database."""
    pass

class FileTypeNotACsv(Exception):
    """Passed File type isn't a csv"""
    pass