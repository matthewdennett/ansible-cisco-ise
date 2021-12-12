#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: trustsec_vn_bulk_delete
short_description: Resource module for Trustsec Vn Bulk Delete
description:
- Manage operation create of the resource Trustsec Vn Bulk Delete.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Trustsec Vn Bulk Delete's payload.
    elements: str
    type: list
requirements:
- ciscoisesdk >= 1.3.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Trustsec Vn Bulk Delete reference
  description: Complete reference of the Trustsec Vn Bulk Delete object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.trustsec_vn_bulk_delete:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string"
    }
"""
