---
aid: hostbill
name: HostBill
description: HostBill is a comprehensive billing and automation software for web hosting providers, domain registrars, and online service companies. HostBill provides an Admin API that enables custom applications to call HostBill functions remotely via HTTP protocol or from HostBill modules.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - Billing
  - Domain Registration
  - Web Hosting
url: https://raw.githubusercontent.com/api-evangelist/hostbill/refs/heads/main/apis.yml
created: '2025-02-09'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: hostbill:hostbill-admin-api
    name: HostBill Admin API
    description: The HostBill Admin API enables custom applications to call HostBill functions remotely via HTTP protocol, providing access to client management, invoicing, service provisioning, billing operations, ticket handling, and plugin integrations including DNS, IPAM, Proxmox, and VMManager.
    humanURL: https://api2.hostbillapp.com/
    baseURL: https://yourinstance.hostbillapp.com/api2.php
    tags:
      - Accounts
      - Billing
      - Clients
      - Domains
      - Invoices
      - Orders
      - Services
      - Tickets
      - Web Hosting
    properties:
      - type: Documentation
        url: https://api2.hostbillapp.com/
      - type: Authentication
        url: https://api2.hostbillapp.com/
common:
  - type: Website
    url: https://hostbillapp.com/
  - type: Documentation
    url: https://hostbillapp.com/features/
  - type: Support
    url: https://hostbillapp.com/support/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
