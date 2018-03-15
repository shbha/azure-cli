# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=too-many-statements
from ._validators import get_datetime_type
from ._validators import get_decimal_type


def load_arguments(self, _):
    with self.argument_context('consumption usage') as c:
        c.argument('top', options_list=['--top', '-t'], type=int, help='maximum number of items to return. Accepted range for this value is 1 - 1000')
        c.argument('include_additional_properties', options_list=['--include-additional-properties', '-a'], action='store_true', help='include additional properties in the usages')
        c.argument('include_meter_details', options_list=['--include-meter-details', '-m'], action='store_true', help='include meter details in the usages')
        c.argument('start_date', options_list=['--start-date', '-s'], type=get_datetime_type(), help='start date (in UTC Y-m-d) of the usages. Both start date and end date need to be supplied or neither')
        c.argument('end_date', options_list=['--end-date', '-e'], type=get_datetime_type(), help='end date (in UTC Y-m-d) of the usages. Both start date and end date need to be supplied or neither')
        c.argument('billing_period_name', options_list=['--billing-period-name', '-p'], help='name of a specific billing period to get the usage details that associate with')

    with self.argument_context('consumption reservations') as rs:
        rs.argument('reservation_order_id', options_list=['--reservation-order-id', '-r'], help='Reservation order id')
        rs.argument('start_date', options_list=['--start-date', '-s'], type=get_datetime_type(), help='start date (in UTC Y-m-d) of the reservation summaries. Only needed for daily grain and both start date and end date need to be supplied or neither')
        rs.argument('end_date', options_list=['--end-date', '-e'], type=get_datetime_type(), help='end date (in UTC Y-m-d) of the reservation summaries. Only needed for daily grain and both start date and end date need to be supplied or neither')
        rs.argument('reservation_id', options_list=['--reservation-id', '-i'], help='Reservation id')

    with self.argument_context('consumption reservations summaries list') as rs:
        rs.argument('grain', options_list=['--grain', '-g'], type=str, help='Reservation summaries grain. Possible values are daily or monthly')

    with self.argument_context('consumption pricesheet show') as cps:
        cps.argument('top', options_list=['--top', '-t'], type=int, help='maximum number of items to return. Accepted range for this value is 1 - 1000')
        cps.argument('include_meter_details', options_list=['--include-meter-details', '-m'], action='store_true', help='include meter details in the price sheet')
        cps.argument('billing_period_name', options_list=['--billing-period-name', '-p'], help='name of a specific billing period to get the price sheet')

    with self.argument_context('consumption marketplace list') as cmp:
        cmp.argument('billing_period_name', options_list=['--billing-period-name', '-p'], help='name of a specific billing period to get the marketplace')
        cmp.argument('top', options_list=['--top', '-t'], type=int, help='maximum number of items to return. Accepted range for this value is 1 - 1000')
        cmp.argument('start_date', options_list=['--start-date', '-s'], type=get_datetime_type(), help='start date (in UTC Y-m-d) of the usages. Both start date and end date need to be supplied or neither')
        cmp.argument('end_date', options_list=['--end-date', '-e'], type=get_datetime_type(), help='end date (in UTC Y-m-d) of the usages. Both start date and end date need to be supplied or neither')

    with self.argument_context('consumption budget') as cb:
        cb.argument('resource_group_name', options_list=['--resource-group-name', '-r'], type=str, help='specific resource group name of a budget')
        cb.argument('budget_name', options_list=['--budget-name', '-b'], type=str, help='budget name of a budget')
        cb.argument('category', options_list=['--category', '-c'], type=str, help='category can be cost or usage')
        cb.argument('amount', options_list=['--amount', '-a'], type=get_decimal_type(), help='amount of a budget')
        cb.argument('time_grain', options_list=['--time_grain', '-t'], type=str, help='time grain can be monthly, quarterly, or annually')
        cb.argument('start_date', options_list=['--start_date', '-s'], type=get_datetime_type(), help='start date of time period of a budget')
        cb.argument('end_date', options_list=['--end_date', '-e'], type=get_datetime_type(), help='end date of time period of a budget')
        cb.argument('resource_groups', options_list=['--resource-groups', '-g'], nargs='+', help='resource groups specified as a filter')
        cb.argument('resources', options_list=['--resources', '-u'], nargs='+', help='resource(s) specified as a filter')
        cb.argument('meters', options_list=['--meters', '-m'], nargs='+', help='meter(s) specified as a filter')
        cb.argument('notifications', options_list=['--notifications', '-n'], nargs='+', help='notifications used to send a budget')

    with self.argument_context('consumption budget update') as cbu:
        cbu.argument('e_tag', options_list=['--e_tag', '-x'], type=str, help='etag required when updating existing budget')
