---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Zeffy Agentic Access
  operation_count: 6
  slug: zeffy-agentic-access
  summary_line: 6 operations
api_count: 4
apis:
- description: Outbound webhooks configured under Settings then Integrations. When a payment is completed, Zeffy sends an HTTP POST with the full payment details to the organization's configured URL, enabling thank-
  name: Zeffy Webhooks
  slug: zeffy-webhooks
- description: Donation forms, events, and other campaign types.
  name: Zeffy Campaigns API
  slug: zeffy-campaigns-api
- description: An organization's donors and supporters.
  name: Zeffy Contacts API
  slug: zeffy-contacts-api
- description: An organization's transactions and donations.
  name: Zeffy Payments API
  slug: zeffy-payments-api
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zeffy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zeffy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zeffy-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zeffy
- group: company
  title: ''
  type: Website
  url: https://www.zeffy.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.zeffy.com/integration/api
- group: commercial
  title: ''
  type: Plans
  url: plans/zeffy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zeffy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zeffy-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.zeffy.com/blog
created: '2026-07-05'
description: Zeffy is a 100% free fundraising platform for nonprofits - donation forms, event ticketing, peer-to-peer campaigns, memberships, e-commerce, and donor management - with no platform, transaction, or credit-card fees, funded entirely by optional tips from donors. Zeffy exposes a free public REST API that gives organization admins read-only access to their Payments, Contacts, and Campaigns data (base https://api.zeffy.com/api/v1), authenticated with a per-organization API key sent as a Bearer token, plus outbound webhooks that POST payment details to a configured URL when a payment is completed. Zeffy also integrates via Zapier, QuickBooks, and WordPress.
finops:
- name: Zeffy Finops
  service_category: Fundraising and Payments
  slug: zeffy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zeffy.png
layout: provider
modified: '2026-07-05'
name: Zeffy
nav: Providers
network: true
overview: 'Zeffy publishes 3 APIs on the [APIs.io](https://apis.io/) network: Campaigns API, Contacts API, and Payments API. Tagged areas include Fundraising, Nonprofit, Donations, Payments, and Donor Management.


  Zeffy''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Zeffy Plans Pricing
  plan_count: 1
  slug: zeffy-plans-pricing
random_paper: 84
rate_limits:
- limit_count: 1
  name: Zeffy Rate Limits
  slug: zeffy-rate-limits
score:
  band: thin
  composite: 33.1
  delta: -0.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 61.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 33.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Zeffy Authentication
  slug: zeffy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zeffy Domain Security
  slug: zeffy-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: zeffy
tags:
- Fundraising
- Nonprofit
- Donations
- Payments
- Donor Management
- Free
- Webhooks
website: https://www.zeffy.com
---
