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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Fundraiseup Agentic Access
  operation_count: 14
  slug: fundraiseup-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 5
apis:
- description: One-time and recurring donations, including offline and ACH donations.
  name: Fundraise Up Donations API
  slug: fundraiseup-donations-api
- description: Secure access-link generation for the self-service Donor Portal.
  name: Fundraise Up Donor Portal API
  slug: fundraiseup-donor-portal-api
- description: Audit-log events across donations, recurring plans, tributes, and supporters.
  name: Fundraise Up Events API
  slug: fundraiseup-events-api
- description: Recurring donation plans modeling a supporter's ongoing giving.
  name: Fundraise Up Recurring Plans API
  slug: fundraiseup-recurring-plans-api
- description: Donor records (Fundraise Up calls donors "supporters").
  name: Fundraise Up Supporters API
  slug: fundraiseup-supporters-api
artifact_total: 12
collections:
- collection_type: open
  name: Fundraise Up REST API
  slug: open-fundraiseup
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fundraiseup-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fundraiseup-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fundraiseup-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fundraiseup
- group: company
  title: ''
  type: Website
  url: https://fundraiseup.com
- group: docs
  title: ''
  type: Documentation
  url: https://fundraiseup.com/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/fundraiseup-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fundraiseup-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fundraiseup-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://fundraiseup.com/blog/
created: '2026-07-05'
description: Fundraise Up is an online donation and fundraising platform for nonprofits that optimizes the digital giving experience to increase conversion and recurring revenue. Its REST API gives programmatic access to fundraising data - donations, recurring plans, supporters (donors), and an events audit log - so organizations can process offline and non-digital donations through their Fundraise Up account, combine them with online giving, and sync everything to CRMs, BI tools, and data warehouses. The API is resource-oriented, uses JSON-encoded request bodies, and authenticates with an API key over HTTP Bearer. Base URL is https://api.fundraiseup.com/v1.
finops:
- name: Fundraiseup Finops
  service_category: Fundraising and Payments
  slug: fundraiseup-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fundraiseup.png
layout: provider
modified: '2026-07-05'
name: Fundraise Up
nav: Providers
network: true
overview: 'Fundraise Up publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Donations API, Donor Portal API, Events API, and 2 more. Tagged areas include Fundraising, Donations, Nonprofit, Payments, and Recurring Giving.


  Fundraise Up''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Fundraiseup Plans Pricing
  plan_count: 2
  slug: fundraiseup-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Fundraiseup Rate Limits
  slug: fundraiseup-rate-limits
score:
  band: thin
  composite: 34.8
  delta: -1.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 61.2
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.3
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Fundraiseup Authentication
  slug: fundraiseup-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fundraiseup Domain Security
  slug: fundraiseup-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: fundraiseup
tags:
- Fundraising
- Donations
- Nonprofit
- Payments
- Recurring Giving
- Donor Management
website: https://fundraiseup.com
---
