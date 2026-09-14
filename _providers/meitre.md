---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 1
apis:
- description: Partner integration API for accessing Meitre's restaurant reservations, availability, and guest data. Documentation is behind an authenticated developer portal at meitre-api.com; access is arranged vi
  name: Meitre Partner API
  slug: meitre-partner-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meitre-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://meitre.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://meitre-api.com/
- group: docs
  title: ''
  type: APIReference
  url: https://meitre-api.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.meitre.com/en/client-signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.meitre.com/terms-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.meitre.com/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/meitre-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/meitre-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/meitre-llms.txt
created: '2026-07-17'
description: Meitre is the leading online reservations, guest, and revenue management platform for the world's top restaurants, with a strong presence across Latin America. It provides a hardware-agnostic, white-label toolkit that lets restaurants manage reservations, availability, waitlists, and guest relationships from a single centralized system. Meitre's algorithms automatically manage table availability by analyzing the setup of each area of a restaurant and demand for each slot, and can require credit-card guarantees to virtually eliminate no-shows. Restaurants pay a fixed monthly fee (no commission), and Meitre exposes a partner integration API at meitre-api.com plus an MCP server for AI-powered natural-language restaurant booking.
image: https://meitre.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Meitre MCP Server
  slug: meitre-mcp-server
modified: '2026-07-20'
name: Meitre
nav: Providers
network: true
overview: 'Meitre publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant, Reservations, Hospitality, and Booking.


  Meitre''s developer surface includes API reference, signup flow, and 8 more developer resources.'
random_paper: 16
screenshot: https://raw.githubusercontent.com/api-evangelist/meitre/refs/heads/main/screenshots/meitre-2026-08-07T172434.png
security:
- kind: domain-security
  name: Meitre Domain Security
  slug: meitre-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: meitre
tags:
- Company
- Restaurant
- Reservations
- Hospitality
- Booking
- Guest Management
- Revenue Management
- Food and Beverage
- Latin America
website: https://meitre.com
---
