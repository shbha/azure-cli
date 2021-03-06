# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from datetime import datetime
from decimal import Decimal
from azure.cli.core.util import CLIError


def get_decimal_type():
    def decimal_type(string):
        try:
            return Decimal(string)
        except ValueError:
            raise ValueError("the value passed cannot be converted to decimal")
    return decimal_type


def get_datetime_type():
    """ Validates UTC datetime. Examples of accepted forms:
    2017-12-31T01:11:59Z,2017-12-31T01:11Z or 2017-12-31T01Z or 2017-12-31 """
    def datetime_type(string):
        """ Validates UTC datetime. Examples of accepted forms:
        2017-12-31T01:11:59Z,2017-12-31T01:11Z or 2017-12-31T01Z or 2017-12-31 """
        accepted_date_formats = ['%Y-%m-%dT%H:%M:%SZ', '%Y-%m-%dT%H:%MZ',
                                 '%Y-%m-%dT%HZ', '%Y-%m-%d']
        for form in accepted_date_formats:
            try:
                return datetime.strptime(string, form)
            except ValueError:
                continue
        raise ValueError("Input '{}' not valid. Valid example: 2017-02-11T23:59:59Z".format(string))
    return datetime_type


def validate_both_start_end_dates(namespace):
    """Validates the existence of both start and end dates in the parameter or neither"""
    if bool(namespace.start_date) != bool(namespace.end_date):
        raise CLIError("usage error: Both --start-date and --end-date need to be supplied or neither.")


def validate_reservations_summaries(namespace):
    """lowercase the data grain for comparison"""
    data_grain = namespace.grain.lower()
    if data_grain != 'daily' and data_grain != 'monthly':
        raise CLIError("usage error: --grain  can be either daily or monthly.")
    if data_grain == 'daily' and (not namespace.start_date or not namespace.end_date):
        raise CLIError("usage error: Both --start-date and --end-date need to be supplied for daily grain.")


def validate_budget_parameters(namespace):
    """lowercase the time grain for comparison"""

    budgetcategory = namespace.category.lower()
    if budgetcategory != 'cost' and budgetcategory != 'usage':
        raise CLIError("usage error: --parameters.category must be set to either cost or usage")

    time_grain = namespace.time_grain.lower().strip()

    if time_grain != 'annually' and time_grain != 'quarterly' and time_grain != 'monthly':
        raise CLIError("usage error: --parameters.time_grain can be 'Annually', 'Quarterly', or 'Monthly'.")

    if namespace.amount < 0:
        raise CLIError("usage error: --parameters.amount must be greater than 0")
