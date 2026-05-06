---
aid: namesilo
name: NameSilo
description: NameSilo is a domain registrar and web services provider offering domain registration, hosting, email, and SSL solutions. NameSilo exposes a Domain API enabling programmatic domain search, registration, and management via HTTPS GET requests with XML or JSON responses, plus an MCP server for AI agents.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Domains
  - Domain Registrar
  - DNS
  - Hosting
  - SSL
  - Email
created: '2025-02-09'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/namesilo/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: namesilo:namesilo
    name: NameSilo Domain API
    description: The NameSilo Domain API allows developers to search, register, transfer, renew, and manage domains programmatically. All API calls use HTTPS GET requests and return XML or JSON. A sandbox environment is available for testing.
    humanURL: https://www.namesilo.com/
    tags:
      - Domains
      - Domain Registrar
      - DNS
    properties:
      - type: Documentation
        url: https://www.namesilo.com/api-reference
      - type: Reference
        url: https://www.namesilo.com/api-reference
      - type: MCP Server
        url: https://mcp.namesilo.com
common:
  - type: Website
    url: https://www.namesilo.com/
  - type: Documentation
    url: https://www.namesilo.com/api-reference
  - type: Sign Up
    url: https://www.namesilo.com/account/api-manager
  - type: Pricing
    url: https://www.namesilo.com/pricing
  - type: Support
    url: https://www.namesilo.com/support
  - type: Terms of Service
    url: https://www.namesilo.com/terms-and-conditions
  - type: Privacy Policy
    url: https://www.namesilo.com/privacy-policy
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
