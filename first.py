def site_to_ip(site_id: str) -> str:
    """given a site id, return the site net addr
    >>> site_to_ip("1234")
    '11.12.34.0'
    >>> site_to_ip('5678')
    '11.56.78.0'
    """
    net_octet_list = ["11", "", "", "0"]
    first_half = site_id[:2]
    second_half = site_id[2:]
    net_octet_list[1] = first_half
    net_octet_list[2] = second_half
    return ".".join(net_octet_list)


def ip_to_site(site_net_addr: str) -> str:
    """given a site net addr, return the site id
    >>> ip_to_site("11.12.34.0")
    '1234'
    """
    octets = site_net_addr.split(".")
    # figure out how to take the result of the str.split() method
    # above and return the portion that represents the site id
    # there are a few different ways to do this:
    # it is possible to use a plus sign '+' to add strings together (concatenate)
    # i.e. 'Hello' + 'World' would become 'HelloWorld'
    # or
    # https://docs.python.org/3/library/stdtypes.html#str.join
    # you'll also need to figure out how to reference elements in an array
    # in a similar way as site_to_ip
    # test the same was as above in the repl with:
    # >>> import doctest
    # >>> import first
    # >>> doctest.testmod(first)
    pass
