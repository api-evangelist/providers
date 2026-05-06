---
aid: openprovider
name: Openprovider
description: 'Openprovider is a wholesaler of Internet services and products with a unique platform from which you can find and manage all the products you need: domains, new gTLDs, SSL certificates, licenses for Plesk and Virtuozzo, spam filters, and more.'
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Domains
  - DNS
  - Hosting
  - Reseller
  - SSL Certificates
  - TLDs
created: '2025-02-09'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/openprovider/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: openprovider:openprovider-api
    name: Openprovider API
    description: The Openprovider Reseller API provides programmatic access to domain registration and management, DNS, SSL certificate provisioning, hosting products, and customer/billing operations across the Openprovider wholesale platform.
    humanURL: https://docs.openprovider.com/doc/all
    baseURL: https://api.openprovider.eu/v1beta
    properties:
      - type: Documentation
        url: https://docs.openprovider.com/doc/all
      - type: Portal
        url: https://www.openprovider.com/
      - type: Support
        url: https://support.openprovider.eu/
    tags:
      - Domains
      - DNS
      - SSL Certificates
common:
  - type: Website
    url: https://www.openprovider.com/
  - type: Documentation
    url: https://docs.openprovider.com/
  - type: Support
    url: https://support.openprovider.eu/
  - type: Login
    url: https://cp.openprovider.eu/login.php
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
