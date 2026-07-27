---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Ezee Agentic Access
  operation_count: 2
  slug: ezee-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 2
apis:
- description: The Inventory and Rates API from eZee Technosys — 1 operation(s) for inventory and rates.
  name: eZee Technosys Inventory and Rates API
  slug: ezee-inventory-and-rates-api
- description: The PMS Connectivity API from eZee Technosys — 1 operation(s) for pms connectivity.
  name: eZee Technosys PMS Connectivity API
  slug: ezee-pms-connectivity-api
artifact_total: 10
collections:
- collection_type: open
  name: eZee Technosys YCS Connectivity API
  slug: open-ezee
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ezee-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ezee-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ezee-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ezee-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ezee-technosys-pvt-ltd-/
- group: company
  title: ''
  type: Website
  url: https://www.ezeetechnosys.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.ezeetechnosys.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/ezee-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ezee-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ezee-finops.yml
created: '2026-06-21'
description: eZee Technosys is a hospitality technology company offering eZee Absolute (cloud hotel PMS), eZee Centrix (channel manager), eZee Reservation (booking engine), and eZee Optimus (restaurant POS). Its YCS Connectivity Portal exposes a partner-gated HTTP API for PMS connectivity, channel manager, booking engine, and POS integrations so third-party systems can sync reservations, room inventory, rates, restrictions, and guest data. eZee is now part of Yanolja Cloud (Yanolja Cloud Solution).
finops:
- name: Ezee Finops
  service_category: Hospitality Software
  slug: ezee-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ezee.png
layout: provider
modified: '2026-06-21'
name: eZee Technosys
nav: Providers
network: true
overview: 'eZee Technosys publishes 2 APIs on the [APIs.io](https://apis.io/) network: Inventory and Rates API and PMS Connectivity API. Tagged areas include Hospitality, Hotel, PMS, Channel Manager, and Reservations.


  eZee Technosys'' developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Ezee Plans Pricing
  plan_count: 2
  slug: ezee-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Ezee Rate Limits
  slug: ezee-rate-limits
score:
  band: thin
  composite: 37.0
  delta: 3.3
  facets:
    commercial_clarity: 36.8
    contract_quality: 54.9
    developer_ergonomics: 19.6
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 33.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ezee/refs/heads/main/screenshots/ezee-2026-07-25T214046.png
security:
- kind: authentication
  name: Ezee Authentication
  slug: ezee-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ezee Domain Security
  slug: ezee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ezee Trust Center
  slug: ezee-trust-center
  summary_line: PCI DSS, GDPR
slug: ezee
tags:
- Hospitality
- Hotel
- PMS
- Channel Manager
- Reservations
website: https://www.ezeetechnosys.com
---
