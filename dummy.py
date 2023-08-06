"""
Dummy - Python library for dummy and dummy lovers.

This is a Python docstring, we can use Markdown syntax here because
our API documentation library understands it (mkdocstrings).

    # Import Dummy
    import dummy

    # Call its only function
    get_random_ingredients(kind=["cheeses"])

"""

class MainDummyClass(object):
    """This class docstring shows how to use sphinx and rst syntax"""
    
    pass


def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]
