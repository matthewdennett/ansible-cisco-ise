#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: trustsec_vn
short_description: Resource module for Trustsec Vn
description:
- Manage operations create, update and delete of the resource Trustsec Vn.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  additionalAttributes:
    description: JSON String of additional attributes for the Virtual Network.
    type: str
  id:
    description: Identifier of the Virtual Network.
    type: str
  lastUpdate:
    description: Timestamp for the last update of the Virtual Network.
    type: str
  name:
    description: Name of the Virtual Network.
    type: str
requirements:
- ciscoisesdk >= 1.2.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Trustsec Vn reference
  description: Complete reference of the Trustsec Vn object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.trustsec_vn:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    additionalAttributes: string
    id: string
    lastUpdate: string
    name: string

- name: Update by id
  cisco.ise.trustsec_vn:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    additionalAttributes: string
    id: string
    lastUpdate: string
    name: string

- name: Delete by id
  cisco.ise.trustsec_vn:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

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
        "additionalAttributes": "string",
        "id": "string",
        "lastUpdate": "string",
        "name": "string"
      }
    ]

ise_update_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: "1.1.0"
  type: dict
  sample: >
    {
      "code": 0,
      "message": "string"
    }
"""
