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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: 'REST API for managing corporate cards, expense claims, vendor invoices, wallet summaries, settlements, bank fees, members, suppliers, cost centers, analytical fields, and webhook subscriptions within '
  name: Spendesk Public API
  slug: spendesk-public-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spendesk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spendesk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.spendesk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.spendesk.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Spendesk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spendesk
- group: other
  title: ''
  type: X
  url: https://twitter.com/Spendesk
- group: company
  title: ''
  type: Blog
  url: https://www.spendesk.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.spendesk.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.spendesk.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/spendesk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spendesk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/spendesk-finops.yml
- group: company
  title: ''
  type: BlogFeed
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/spendesk-context.jsonld
created: 2026-06-12
description: Spendesk is an AI-powered spend management and procurement platform serving over 200,000 users across Europe. Its public REST API enables partners and customers to integrate programmatic card issuance, transaction retrieval, expense claims processing, vendor and invoice management, and accounting exports into their own tools and workflows. Authentication is supported via API keys (for customers) and OAuth2 (for partners building native integrations). API access requires a Premium or Enterprise subscription plan, and the developer portal at developer.spendesk.com provides reference documentation, changelogs, a Postman collection, and webhook administration.
finops:
- name: Spendesk Finops
  service_category: ''
  slug: spendesk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spendesk.png
jsonld:
- class_count: 9
  name: Spendesk Context
  property_count: 10
  slug: spendesk-context
layout: provider
modified: 2026-06-12
name: Spendesk
nav: Providers
network: true
overview: 'Spendesk publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Spend Management, Corporate Cards, Expense Management, Invoices, and Procurement.


  The Spendesk catalog on APIs.io includes 1 JSON-LD context.


  Spendesk''s developer surface includes documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Spendesk Plans Pricing
  plan_count: 3
  slug: spendesk-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 3
  name: Spendesk Rate Limits
  slug: spendesk-rate-limits
score:
  band: thin
  composite: 34.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 20.8
    developer_ergonomics: 10.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 34.0
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spendesk/refs/heads/main/screenshots/spendesk-2026-06-20T194306.png
security:
- kind: domain-security
  name: Spendesk Domain Security
  slug: spendesk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Spendesk Vulnerability Disclosure
  slug: spendesk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: spendesk
tags:
- Spend Management
- Corporate Cards
- Expense Management
- Invoices
- Procurement
- FinTech
- Accounting
- Payments
website: https://www.spendesk.com/
---
