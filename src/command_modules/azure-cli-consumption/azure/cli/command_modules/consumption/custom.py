# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long

def cli_consumption_list_usage(client, top=None, include_additional_properties=False, include_meter_details=False, start_date=None, end_date=None):
    if include_additional_properties and include_meter_details:
        expand = 'properties/additionalProperties,properties/meterDetails'
    elif include_additional_properties:
        expand = 'properties/additionalProperties'
    elif include_meter_details:
        expand = 'properties/meterDetails'
    else:
        expand = None

    filter_from = None
    filter_to = None
    filter_expression = None
    if start_date and end_date:
        filter_from = "properties/usageEnd ge \'{}\'".format(start_date.strftime("%Y-%m-%dT%H:%M:%SZ"))
        filter_to = "properties/usageEnd le \'{}\'".format(end_date.strftime("%Y-%m-%dT%H:%M:%SZ"))
        filter_expression = "{} and {}".format(filter_from, filter_to)
    if top:
        pages = client.list(expand=expand, filter=filter_expression, top=top)
        return list(pages.advance_page())
    return list(client.list(expand=expand, filter=filter_expression))


def cli_consumption_list_usage_by_billing_period(client, billing_period_name=None, top=None, include_additional_properties=False, include_meter_details=False, start_date=None, end_date=None):
    if include_additional_properties and include_meter_details:
        expand = 'properties/additionalProperties,properties/meterDetails'
    elif include_additional_properties:
        expand = 'properties/additionalProperties'
    elif include_meter_details:
        expand = 'properties/meterDetails'
    else:
        expand = None

    filter_from = None
    filter_to = None
    filter_expression = None
    if start_date and end_date:
        filter_from = "properties/usageEnd ge \'{}\'".format(start_date.strftime("%Y-%m-%dT%H:%M:%SZ"))
        filter_to = "properties/usageEnd le \'{}\'".format(end_date.strftime("%Y-%m-%dT%H:%M:%SZ"))
        filter_expression = "{} and {}".format(filter_from, filter_to)
    if top:
        pages = client.list_by_billing_period(billing_period_name, expand=expand, filter=filter_expression, top=top)
        return list(pages.advance_page())
    return list(client.list_by_billing_period(billing_period_name, expand=expand, filter=filter_expression))


def cli_consumption_list_reservations_summaries(client, grain, reservationorderid, start_date=None, end_date=None):
    filter_from = None
    filter_to = None
    filter_expression = None
    if start_date and end_date:
        filter_from = "properties/UsageDate ge {}".format(start_date.strftime("%Y-%m-%dT%H:%M:%SZ"))
        filter_to = "properties/UsageDate le {}".format(end_date.strftime("%Y-%m-%dT%H:%M:%SZ"))
        filter_expression = "{} and {}".format(filter_from, filter_to)
        return list(client.list_by_reservation_order(reservationorderid, grain=grain, filter=filter_expression))

    return list(client.list_by_reservation_order(reservationorderid, grain=grain))


def cli_consumption_list_reservations_summaries_reservation_id(client, grain, reservationorderid, reservationid=None, start_date=None, end_date=None):
    filter_from = None
    filter_to = None
    filter_expression = None
    if start_date and end_date:
        filter_from = "properties/UsageDate ge {}".format(start_date.strftime("%Y-%m-%dT%H:%M:%SZ"))
        filter_to = "properties/UsageDate le {}".format(end_date.strftime("%Y-%m-%dT%H:%M:%SZ"))
        filter_expression = "{} and {}".format(filter_from, filter_to)
        return list(client.list_by_reservation_order_and_reservation(reservationorderid, reservationid, grain=grain, filter=filter_expression))

    return list(client.list_by_reservation_order_and_reservation(reservationorderid, reservationid, grain=grain))


def cli_consumption_list_reservations_details(client, reservationorderid, start_date, end_date):
    filter_from = None
    filter_to = None
    filter_expression = None
    filter_from = "properties/UsageDate ge {}".format(start_date.strftime("%Y-%m-%dT%H:%M:%SZ"))
    filter_to = "properties/UsageDate le {}".format(end_date.strftime("%Y-%m-%dT%H:%M:%SZ"))
    filter_expression = "{} and {}".format(filter_from, filter_to)
    return list(client.list_by_reservation_order(reservationorderid, filter=filter_expression))


def cli_consumption_list_reservations_details_by_reservation_id(client, reservationorderid, start_date, end_date, reservationid=None):
    filter_from = None
    filter_to = None
    filter_expression = None
    filter_from = "properties/UsageDate ge {}".format(start_date.strftime("%Y-%m-%dT%H:%M:%SZ"))
    filter_to = "properties/UsageDate le {}".format(end_date.strftime("%Y-%m-%dT%H:%M:%SZ"))
    filter_expression = "{} and {}".format(filter_from, filter_to)
    return list(client.list_by_reservation_order_and_reservation(reservationorderid, reservationid, filter=filter_expression))


def cli_consumption_list_pricesheet_get(client, include_additional_properties=False, include_meter_details=False):
    if include_additional_properties and include_meter_details:
        expand_properties = 'properties/additionalProperties,properties/meterDetails'
    elif include_additional_properties:
        expand_properties = 'properties/additionalProperties'
    elif include_meter_details:
        expand_properties = 'properties/meterDetails'
    else:
        expand_properties = None

    return client.get(expand=expand_properties)


def cli_consumption_list_pricesheet_by_billing_period_get(client, billing_period_name, include_additional_properties=False, include_meter_details=False):
    if include_additional_properties and include_meter_details:
        expand_properties = 'properties/additionalProperties,properties/meterDetails'
    elif include_additional_properties:
        expand_properties = 'properties/additionalProperties'
    elif include_meter_details:
        expand_properties = 'properties/meterDetails'
    else:
        expand_properties = None

    return client.get_by_billing_period(billing_period_name, expand=expand_properties)
