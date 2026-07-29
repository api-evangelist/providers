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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Slice Agentic Access
  operation_count: 10
  slug: slice-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 2
apis:
- description: Create, retrieve, update, and cancel orders against a Slice shop.
  name: Slice Orders API
  slug: slice-orders-api
- description: Discover pizzerias (shops) in the Slice network.
  name: Slice Shops API
  slug: slice-shops-api
artifact_total: 12
collections:
- collection_type: open
  name: Slice Public API
  slug: open-slice-public-api-v1
- collection_type: open
  name: Slice Public API
  slug: open-slice-public-api-v2
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/slice-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/slice-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/slice-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://slicelife.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.slicelife.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.slicelife.com/docs/Getting-started.md
- group: commercial
  title: ''
  type: Pricing
  url: https://slice.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://slicelife.com/pages/support
- group: operate
  title: API Support
  type: Contact
  url: mailto:api-support@slicelife.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/slicelife
- group: commercial
  title: ''
  type: Plans
  url: plans/slice-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/slice-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/slice-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/slice-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/slice-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.slicelife.com/feed/
created: '2026-06-02'
description: Slice is an online ordering and management platform built specifically for independent local pizzerias, giving small shops digital ordering, marketing, loyalty, and back-office tools that compete with large delivery marketplaces at a low flat per-order fee. For technology partners, Slice publishes a Slice Public API documented on a Stoplight developer portal, exposing pizzeria-oriented resources such as shops and orders over a RESTful HTTP interface in two versions (v1 and v2). The platform serves pizzeria owners and the partners that integrate ordering, POS, and operations into the Slice network across thousands of locations.
finops:
- name: Slice Finops
  service_category: ''
  slug: slice-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/slice.png
jsonld:
- class_count: 4
  name: Slice Context
  property_count: 4
  slug: slice-context
layout: provider
modified: '2026-06-03'
name: Slice
nav: Providers
network: true
overview: 'Slice publishes 2 APIs on the [APIs.io](https://apis.io/) network: Orders API and Shops API. Tagged areas include Restaurant, Pizza, Online Ordering, Local Commerce, and Menus.


  The Slice catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Slice''s developer surface includes authentication, documentation, getting-started guide, pricing, support, engineering blog, and 10 more developer resources.'
plans:
- name: Slice Plans Pricing
  plan_count: 3
  slug: slice-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 2
  name: Slice Rate Limits
  slug: slice-rate-limits
rules:
- name: Slice API Rules
  rule_count: 14
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 11
  slug: slice-rules
score:
  band: developing
  composite: 44.9
  delta: -3.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 57.6
    developer_ergonomics: 37.0
    discoverability: 59.3
    governance: 31.3
    operational_transparency: 26.3
  previous_composite: 48.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/slice/refs/heads/main/screenshots/slice-2026-06-20T194029.png
security:
- kind: authentication
  name: Slice Authentication
  slug: slice-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Slice Domain Security
  slug: slice-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: slice
tags:
- Restaurant
- Pizza
- Online Ordering
- Local Commerce
- Menus
- Orders
website: https://slicelife.com/
---
