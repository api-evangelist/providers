---
aid: givebutter
name: Givebutter
description: The Givebutter API is organized around REST and provides a stateless interface for interacting with your Givebutter account. The Givebutter API supports JSON, and all requests return and require a valid JSON object.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Donations
  - Fundraising
  - Nonprofits
created: '2025-01-07'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/givebutter/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: givebutter:givebutter
    name: Givebutter
    description: The Givebutter API is organized around REST and provides a stateless interface for interacting with your Givebutter account. The Givebutter API supports JSON, and all requests return and require a valid JSON object. The API uses Bearer token authentication with API keys and provides endpoints for campaigns, contacts, transactions, funds, households, tickets, discount codes, webhooks, payouts, recurring plans, and pledges.
    humanURL: https://docs.givebutter.com/reference/reference-getting-started
    baseURL: https://api.givebutter.com/v1
    tags:
      - Donations
      - Fundraising
      - Nonprofits
    properties:
      - type: Documentation
        url: https://docs.givebutter.com/reference/reference-getting-started
      - type: Authentication
        url: https://docs.givebutter.com/reference/authentication
      - type: Webhooks
        url: https://docs.givebutter.com/reference/webhooks
common:
  - type: Website
    url: https://givebutter.com/
  - type: Documentation
    url: https://docs.givebutter.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
