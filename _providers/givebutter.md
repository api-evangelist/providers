---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Givebutter Agentic Access
  operation_count: 27
  slug: givebutter-agentic-access
  summary_line: 27 operations · 11 acting
api_count: 10
apis:
- description: The Givebutter API is organized around REST and provides a stateless interface for interacting with your Givebutter account. The Givebutter API supports JSON, and all requests return and require a val
  name: Givebutter
  slug: givebutter
- description: The Campaigns API from Givebutter — 4 operation(s) for campaigns.
  name: Givebutter Campaigns API
  slug: givebutter-campaigns-api
- description: The Contacts API from Givebutter — 2 operation(s) for contacts.
  name: Givebutter Contacts API
  slug: givebutter-contacts-api
- description: The Discount Codes API from Givebutter — 1 operation(s) for discount codes.
  name: Givebutter Discount Codes API
  slug: givebutter-discount-codes-api
- description: The Funds API from Givebutter — 2 operation(s) for funds.
  name: Givebutter Funds API
  slug: givebutter-funds-api
- description: The Payouts API from Givebutter — 1 operation(s) for payouts.
  name: Givebutter Payouts API
  slug: givebutter-payouts-api
- description: The Plans API from Givebutter — 1 operation(s) for plans.
  name: Givebutter Plans API
  slug: givebutter-plans-api
- description: The Tickets API from Givebutter — 2 operation(s) for tickets.
  name: Givebutter Tickets API
  slug: givebutter-tickets-api
- description: The Transactions API from Givebutter — 2 operation(s) for transactions.
  name: Givebutter Transactions API
  slug: givebutter-transactions-api
- description: The Webhooks API from Givebutter — 2 operation(s) for webhooks.
  name: Givebutter Webhooks API
  slug: givebutter-webhooks-api
artifact_total: 17
collections:
- collection_type: open
  name: Givebutter API
  slug: open-givebutter
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/givebutter-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/givebutter-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/givebutter-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/givebutter
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/givebutter
- group: company
  title: ''
  type: Website
  url: https://givebutter.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.givebutter.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.givebutter.com/llms.txt
created: '2025-01-07'
description: The Givebutter API is organized around REST and provides a stateless interface for interacting with your Givebutter account. The Givebutter API supports JSON, and all requests return and require a valid JSON object.
finops:
- name: Givebutter Finops
  service_category: API
  slug: givebutter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/givebutter.png
layout: provider
modified: '2026-04-28'
name: Givebutter
nav: Providers
network: true
overview: 'Givebutter publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Contacts API, Discount Codes API, and 6 more. Tagged areas include Donations, Fundraising, and Nonprofits.


  Givebutter''s developer surface includes authentication, documentation, and 6 more developer resources.'
plans:
- name: Givebutter Plans Pricing
  plan_count: 3
  slug: givebutter-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Givebutter Rate Limits
  slug: givebutter-rate-limits
score:
  band: thin
  composite: 34.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.3
    developer_ergonomics: 19.6
    discoverability: 55.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/givebutter/refs/heads/main/screenshots/givebutter-2026-06-20T181853.png
security:
- kind: authentication
  name: Givebutter Authentication
  slug: givebutter-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Givebutter Domain Security
  slug: givebutter-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: givebutter
tags:
- Donations
- Fundraising
- Nonprofits
website: https://givebutter.com/
---
