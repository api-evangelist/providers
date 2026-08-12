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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Donately Agentic Access
  operation_count: 22
  slug: donately-agentic-access
  summary_line: 22 operations · 10 acting
api_count: 6
apis:
- description: The organizations a token has access to.
  name: Donately Accounts API
  slug: donately-accounts-api
- description: Fundraising pages with goals and settings.
  name: Donately Campaigns API
  slug: donately-campaigns-api
- description: One-time and recurring gifts.
  name: Donately Donations API
  slug: donately-donations-api
- description: Peer-to-peer fundraising pages under a campaign.
  name: Donately Fundraisers API
  slug: donately-fundraisers-api
- description: Donors and contacts.
  name: Donately People API
  slug: donately-people-api
- description: Recurring donation schedules.
  name: Donately Subscriptions API
  slug: donately-subscriptions-api
artifact_total: 13
collections:
- collection_type: open
  name: Donately API
  slug: open-donately
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/donately-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/donately-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/donately-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/donately
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/donately
- group: company
  title: ''
  type: Website
  url: https://www.donately.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.donately.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/donately-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/donately-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/donately-finops.yml
created: '2026-07-05'
description: Donately is an online donation and fundraising platform for nonprofits, churches, and businesses, offering embeddable donation forms, campaign and peer-to-peer fundraising pages, recurring giving, and donor management. Its REST API (base https://api.donately.com/v2, version 2019-03-15) exposes accounts, campaigns, donations, recurring subscriptions, people (donors), fundraisers, forms, and webhooks, authenticated with an API token via HTTP Basic Auth. Donately charges a platform fee (4%, 2%, or 0% prepaid) on top of Stripe/PayPal payment processing.
finops:
- name: Donately Finops
  service_category: Fundraising and Payments
  slug: donately-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/donately.png
layout: provider
modified: '2026-07-05'
name: Donately
nav: Providers
network: true
overview: 'Donately publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Campaigns API, Donations API, and 3 more. Tagged areas include Fundraising, Donations, Nonprofit, Payments, and Donor Management.


  Donately''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Donately Plans Pricing
  plan_count: 3
  slug: donately-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 2
  name: Donately Rate Limits
  slug: donately-rate-limits
score:
  band: thin
  composite: 35.1
  delta: -0.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 35.6
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
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/donately/refs/heads/main/screenshots/donately-2026-07-25T212248.png
security:
- kind: authentication
  name: Donately Authentication
  slug: donately-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Donately Domain Security
  slug: donately-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: donately
tags:
- Fundraising
- Donations
- Nonprofit
- Payments
- Donor Management
- Recurring Giving
website: https://www.donately.com
---
