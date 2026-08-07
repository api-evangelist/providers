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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Tithely Agentic Access
  operation_count: 11
  slug: tithely-agentic-access
  summary_line: 11 operations · 8 acting
api_count: 6
apis:
- description: Authentication and login.
  name: Tithe.ly Accounts API
  slug: tithely-accounts-api
- description: Send templated transactional email.
  name: Tithe.ly Mail API
  slug: tithely-mail-api
- description: Look up churches/organizations.
  name: Tithe.ly Organizations API
  slug: tithely-organizations-api
- description: Giving funds a donation is allocated to.
  name: Tithe.ly Payment Categories API
  slug: tithely-payment-categories-api
- description: V1 tokenized payment methods and charges.
  name: Tithe.ly Payments API
  slug: tithely-payments-api
- description: Create donation transactions.
  name: Tithe.ly Transactions API
  slug: tithely-transactions-api
artifact_total: 13
collections:
- collection_type: open
  name: Tithe.ly API
  slug: open-tithely
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tithely-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tithely-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tithely-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tithely
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tithe-ly
- group: company
  title: ''
  type: Website
  url: https://get.tithe.ly/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tithe.ly/reference/introduction
- group: commercial
  title: ''
  type: Plans
  url: plans/tithely-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tithely-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tithely-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://get.tithe.ly/blog/rss.xml
created: '2026-07-03'
description: Tithe.ly is a church technology platform for online and mobile giving, church management (ChMS), branded church apps, websites, events, and messaging. Its developer API lets churches and approved partners create donations, tokenize cards and bank accounts for PCI-safe payments, charge one-time and recurring gifts, manage giving funds (payment categories), and look up organizations. API access is gated - it is granted by request to organizations that use (or are moving to) Tithe.ly, and approved requesters receive public and private API keys by email. There are two documented generations - a V1 payments/tokenization API (Tithely.js plus charge endpoints) and a V2 REST API (organizations, transactions, funds, and mail).
finops:
- name: Tithely Finops
  service_category: Payments and Fundraising
  slug: tithely-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tithely.png
layout: provider
modified: '2026-07-03'
name: Tithe.ly
nav: Providers
network: true
overview: 'Tithe.ly publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Mail API, Organizations API, and 3 more. Tagged areas include Church Giving, Donations, Fundraising, Payments, and Nonprofit.


  Tithe.ly''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Tithely Plans Pricing
  plan_count: 4
  slug: tithely-plans-pricing
random_paper: 93
rate_limits:
- limit_count: 3
  name: Tithely Rate Limits
  slug: tithely-rate-limits
score:
  band: thin
  composite: 36.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 62.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Tithely Authentication
  slug: tithely-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tithely Domain Security
  slug: tithely-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tithely
tags:
- Church Giving
- Donations
- Fundraising
- Payments
- Nonprofit
- ChMS
- Faith
website: https://get.tithe.ly/
---
