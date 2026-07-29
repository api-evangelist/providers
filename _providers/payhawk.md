---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: RESTful API for programmatic access to Payhawk spend management features including expenses, corporate cards, transactions, employees, custom fields, fund accounts, bank statements, and webhook subscr
  name: Payhawk API
  slug: payhawk-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/payhawk-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/payhawk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/payhawk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://payhawk.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.payhawk.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://payhawk.com/help/payhawk-for-developers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/payhawk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/payhawk
- group: other
  title: ''
  type: X
  url: https://x.com/payhawk
- group: company
  title: ''
  type: Blog
  url: https://payhawk.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://payhawk.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.payhawk.com
- group: commercial
  title: ''
  type: Plans
  url: plans/payhawk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/payhawk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/payhawk-finops.yml
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/payhawk-context.jsonld
created: 2026-06-12
description: Payhawk is a spend management platform that enables finance teams to issue corporate cards, capture and manage expenses, process invoices, enforce budget controls, and integrate with ERP and accounting systems. The platform serves businesses across Europe, the US, and the UK in over 32 countries. Payhawk exposes a RESTful Developer API at https://api.payhawk.io/api/v3 that allows custom integrations over expenses, transactions, cards, employees, custom fields, fund accounts, and bank statements. The API is authenticated via API key, supports real-time webhooks for event-driven automation, and is rate-limited to 15 requests per second. The API is free to use for all Payhawk account holders, with no separate developer tier required.
finops:
- name: Payhawk Finops
  service_category: ''
  slug: payhawk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/payhawk.png
jsonld:
- class_count: 12
  name: Payhawk Context
  property_count: 0
  slug: payhawk-context
layout: provider
modified: 2026-06-12
name: Payhawk
nav: Providers
network: true
overview: 'Payhawk publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Spend Management, Corporate Cards, Expense Management, Invoice Management, and Budget Controls.


  The Payhawk catalog on APIs.io includes 1 JSON-LD context.


  Payhawk''s developer surface includes documentation, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Payhawk Plans Pricing
  plan_count: 3
  slug: payhawk-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 1
  name: Payhawk Rate Limits
  slug: payhawk-rate-limits
score:
  band: thin
  composite: 30.2
  delta: -2.9
  facets:
    commercial_clarity: 57.9
    contract_quality: 12.9
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 33.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/payhawk/refs/heads/main/screenshots/payhawk-2026-06-20T191457.png
security:
- kind: domain-security
  name: Payhawk Domain Security
  slug: payhawk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Payhawk Vulnerability Disclosure
  slug: payhawk-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Payhawk Trust Center
  slug: payhawk-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR, CSA STAR
slug: payhawk
tags:
- Spend Management
- Corporate Cards
- Expense Management
- Invoice Management
- Budget Controls
- ERP Integration
- Accounts Payable
- FinTech
- Finance Automation
- Webhooks
website: https://payhawk.com
---
