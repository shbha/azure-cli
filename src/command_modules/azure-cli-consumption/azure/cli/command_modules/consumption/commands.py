# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from ._transformers import (transform_usage_list_output,
                            transform_reservation_summaries_list_output,
                            transform_reservation_details_list_output,
                            transform_pricesheet_show_output,
                            transform_marketplace_list_output,
                            transform_budget_list_output,
                            transform_budget_show_output,
                            transform_budget_create_update_output)
from ._client_factory import (usage_details_mgmt_client_factory,
                              reservations_summaries_mgmt_client_factory,
                              reservations_details_mgmt_client_factory,
                              pricesheet_mgmt_client_factory,
                              marketplace_mgmt_client_factory,
                              budget_mgmt_client_factory)
from ._validators import (validate_both_start_end_dates,
                          validate_reservations_summaries,
                          validate_budget_parameters)
from ._exception_handler import consumption_exception_handler


def load_command_table(self, _):
    with self.command_group('consumption usage') as g:
        g.custom_command('list', 'cli_consumption_list_usage', transform=transform_usage_list_output,
                         exception_handler=consumption_exception_handler, validator=validate_both_start_end_dates, client_factory=usage_details_mgmt_client_factory)

    with self.command_group('consumption reservations summaries') as s:
        s.custom_command('list', 'cli_consumption_list_reservations_summaries', transform=transform_reservation_summaries_list_output,
                         exception_handler=consumption_exception_handler, validator=validate_reservations_summaries, client_factory=reservations_summaries_mgmt_client_factory)

    with self.command_group('consumption reservations details') as d:
        d.custom_command('list', 'cli_consumption_list_reservations_details', transform=transform_reservation_details_list_output,
                         exception_handler=consumption_exception_handler, client_factory=reservations_details_mgmt_client_factory)

    with self.command_group('consumption pricesheet') as p:
        p.custom_command('show', 'cli_consumption_list_pricesheet_show', transform=transform_pricesheet_show_output,
                         exception_handler=consumption_exception_handler, client_factory=pricesheet_mgmt_client_factory)

    with self.command_group('consumption marketplace') as p:
        p.custom_command('list', 'cli_consumption_list_marketplace', transform=transform_marketplace_list_output,
                         exception_handler=consumption_exception_handler, validator=validate_both_start_end_dates, client_factory=marketplace_mgmt_client_factory)

    with self.command_group('consumption budget') as p:
        p.custom_command('list', 'cli_consumption_list_budgets', transform=transform_budget_list_output,
                         exception_handler=consumption_exception_handler, validator=None, client_factory=budget_mgmt_client_factory)

        p.custom_command('show', 'cli_consumption_show_budget', transform=transform_budget_show_output,
                         exception_handler=consumption_exception_handler, validator=None, client_factory=budget_mgmt_client_factory)

        p.custom_command('create', 'cli_consumption_create_budget', transform=transform_budget_create_update_output,
                         exception_handler=consumption_exception_handler, validator=validate_budget_parameters, client_factory=budget_mgmt_client_factory)

        p.custom_command('update', 'cli_consumption_update_budget', transform=transform_budget_create_update_output,
                         exception_handler=consumption_exception_handler, validator=validate_budget_parameters, client_factory=budget_mgmt_client_factory)

        p.custom_command('delete', 'cli_consumption_delete_budget', transform=None,
                         exception_handler=consumption_exception_handler, client_factory=budget_mgmt_client_factory)
