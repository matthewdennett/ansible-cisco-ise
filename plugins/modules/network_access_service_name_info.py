#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_access_service_name_info
short_description: Information module for Network Access Service Name
description:
- Get all Network Access Service Name.
- Returns list of Allowed Protocols and Server Sequences for Network Access.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options: {}
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
seealso:
- name: Cisco ISE documentation for Network Access - Service Names
  description: Complete reference of the Network Access - Service Names API.
  link: https://developer.cisco.com/docs/identity-services-engine/v1/#!policy-openapi
notes:
  - SDK Method used are
    network_access_service_names.NetworkAccessServiceNames.get_network_access_service_names,

  - Paths used are
    get /network-access/service-names,

"""

EXAMPLES = r"""
- name: Get all Network Access Service Name
  cisco.ise.network_access_service_name_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
  register: result

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "id": "string",
        "isLocalAuthorization": true,
        "name": "string",
        "serviceType": "string"
      }
    ]
"""
