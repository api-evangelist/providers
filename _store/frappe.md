---
aid: frappe
name: Frappe
description: Frappe is a fully featured, low-code web framework written in Python and JavaScript that powers ERPNext, the open-source ERP for accounting, inventory, payroll, and operations. The Frappe REST API auto-exposes every DocType for CRUD plus whitelisted Python method calls.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-06'
modified: '2026-04-28'
position: Consumer
tags:
  - Open Source
  - ERP
  - Accounting
  - Inventory
  - Payroll
  - Low Code
url: https://raw.githubusercontent.com/api-evangelist/frappe/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: frappe:rest-api
    name: Frappe Framework REST API
    description: Auto-generated REST API exposing every Frappe DocType for CRUD, filtered list queries, and whitelisted Python method calls. Powers Frappe and ERPNext integrations.
    humanURL: https://docs.frappe.io/framework/user/en/api/rest
    tags:
      - REST
      - DocTypes
      - CRUD
      - Methods
    properties:
      - type: Documentation
        url: https://docs.frappe.io/framework/user/en/api/rest
      - type: Documentation
        name: Frappe Framework Docs
        url: https://docs.frappe.io/framework/user/en/introduction
      - type: Capabilities
        url: https://raw.githubusercontent.com/api-evangelist/frappe/refs/heads/main/capabilities/frappe-rest-capabilities.yml
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/frappe/refs/heads/main/rules/frappe-rest-rules.yml
      - type: SourceCode
        url: https://github.com/frappe/frappe
common:
  - type: Website
    url: https://frappe.io/
  - type: Documentation
    url: https://docs.frappe.io/
  - type: GitHub Organization
    url: https://github.com/frappe
  - type: SourceCode
    name: Frappe Framework
    url: https://github.com/frappe/frappe
  - type: SourceCode
    name: ERPNext
    url: https://github.com/frappe/erpnext
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
