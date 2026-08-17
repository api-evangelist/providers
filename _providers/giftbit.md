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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Giftbit Agentic Access
  operation_count: 16
  slug: giftbit-agentic-access
  summary_line: 16 operations · 7 acting
api_count: 9
apis:
- description: Browse available reward brands and catalogs
  name: Giftbit Brands API
  slug: giftbit-brands-api
- description: Create and manage email reward orders
  name: Giftbit Campaigns API
  slug: giftbit-campaigns-api
- description: Create direct link reward orders
  name: Giftbit Direct Links API
  slug: giftbit-direct-links-api
- description: Create in-app embedded reward orders
  name: Giftbit Embedded Rewards API
  slug: giftbit-embedded-rewards-api
- description: Manage account balance and credit card funding
  name: Giftbit Funds API
  slug: giftbit-funds-api
- description: Health check and authentication test
  name: Giftbit Ping API
  slug: giftbit-ping-api
- description: List supported geographical regions
  name: Giftbit Regions API
  slug: giftbit-regions-api
- description: List, retrieve, resend, or cancel individual rewards
  name: Giftbit Rewards API
  slug: giftbit-rewards-api
- description: Create shortlink reward orders
  name: Giftbit Shortlinks API
  slug: giftbit-shortlinks-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Giftbit Brands API
  slug: open-giftbit-brands-api
- collection_type: open
  name: Giftbit Brands Campaigns API
  slug: open-giftbit-campaigns-api
- collection_type: open
  name: Giftbit Brands Direct Links API
  slug: open-giftbit-direct-links-api
- collection_type: open
  name: Giftbit Brands Embedded Rewards API
  slug: open-giftbit-embedded-rewards-api
- collection_type: open
  name: Giftbit Brands Funds API
  slug: open-giftbit-funds-api
- collection_type: open
  name: Giftbit Brands Ping API
  slug: open-giftbit-ping-api
- collection_type: open
  name: Giftbit Brands Regions API
  slug: open-giftbit-regions-api
- collection_type: open
  name: Giftbit Brands Rewards API
  slug: open-giftbit-rewards-api
- collection_type: open
  name: Giftbit Brands Shortlinks API
  slug: open-giftbit-shortlinks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/giftbit-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/giftbit-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/giftbit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/giftbit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/giftbit-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.giftbit.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.giftbit.com/api-documentation
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Giftbit
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/giftbit
- group: company
  title: ''
  type: Blog
  url: https://www.giftbit.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.giftbit.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.giftbit.com/
- group: other
  title: ''
  type: X
  url: https://x.com/giftbit
- group: commercial
  title: ''
  type: Plans
  url: plans/giftbit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/giftbit-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/giftbit-finops.yml
created: '2026-06-13'
description: Giftbit is a gift card and digital reward platform with a REST API for distributing digital gift cards, managing reward campaigns, tracking redemptions, and accessing a marketplace of 1,500+ brand integrations across 40+ countries. The API enables businesses to send single-brand or multi-brand rewards via email delivery, shortlinks, direct links, or in-app embeds, with no platform subscription fees — paying only the face value of rewards sent.
examples:
- key_count: 5
  name: Create Email Order
  slug: create-email-order
- key_count: 3
  name: Create Embedded Reward
  slug: create-embedded-reward
- key_count: 3
  name: Funds Response
  slug: funds-response
- key_count: 3
  name: Reward Response
  slug: reward-response
finops:
- name: Giftbit Finops
  service_category: ''
  slug: giftbit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/giftbit.png
json_schemas:
- name: Campaign
  property_count: 8
  slug: campaign
- name: Contact
  property_count: 3
  slug: contact
- name: Reward
  property_count: 13
  slug: reward
jsonld:
- class_count: 5
  name: Giftbit Context
  property_count: 42
  slug: giftbit-context
layout: provider
modified: '2026-06-13'
name: Giftbit
nav: Providers
network: true
overview: 'Giftbit publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Brands API, Campaigns API, Direct Links API, and 6 more. Tagged areas include Gift Cards, Digital Rewards, Incentives, Payments, and Reward Distribution.


  The Giftbit catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Giftbit''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Giftbit Plans Pricing
  plan_count: 1
  slug: giftbit-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Giftbit Rate Limits
  slug: giftbit-rate-limits
rules:
- name: Giftbit API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: giftbit-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.8
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 70.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 47.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 43.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/giftbit/refs/heads/main/screenshots/giftbit-2026-06-20T181826.png
security:
- kind: authentication
  name: Giftbit Authentication
  slug: giftbit-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Giftbit Domain Security
  slug: giftbit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Giftbit Vulnerability Disclosure
  slug: giftbit-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Giftbit Trust Center
  slug: giftbit-trust-center
  summary_line: SOC 2, GDPR
slug: giftbit
tags:
- Gift Cards
- Digital Rewards
- Incentives
- Payments
- Reward Distribution
- Prepaid Cards
website: https://www.giftbit.com
---
