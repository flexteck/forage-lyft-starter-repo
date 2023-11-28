def calculate_service_date(last_srviced_yr, years_to_add):
    """calculates service date"""
    result = last_srviced_yr.replace(year=last_srviced_yr + years_to_add)
    return result
