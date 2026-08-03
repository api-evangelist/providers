---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Basis Agentic Access
  operation_count: 31
  slug: basis-agentic-access
  summary_line: 31 operations
api_count: 1
apis:
- description: The Analytics API from Basis — 31 operation(s) for analytics.
  name: Basis Analytics API
  slug: basis-analytics-api
artifact_total: 27
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/basis-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/basis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/basis-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://basis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://basis.com/technology/enterprise-api
- group: company
  title: ''
  type: Blog
  url: https://basis.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://basis.com/technology/enterprise-api
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/basis-technologies
- group: other
  title: ''
  type: X
  url: https://twitter.com/basisglobaltech
- group: commercial
  title: ''
  type: Plans
  url: plans/basis-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/basis-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/basis-finops.yml
created: '2026-06-13'
description: Basis is an advertising automation platform providing REST APIs for programmatic DSP campaign management, audience targeting, publisher management, reporting, and omnichannel media buying automation across display, video, audio, native, connected TV, and site-direct channels.
examples:
- key_count: 1
  name: Basis Api Examples
  slug: basis-api-examples
finops:
- name: Basis Finops
  service_category: ''
  slug: basis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/basis.png
json_schemas:
- name: Agency Get
  property_count: 1
  slug: agency-get
- name: Brands Get
  property_count: 2
  slug: brands-get
- name: Campaigns Addons Get
  property_count: 2
  slug: campaigns-addons-get
- name: Campaigns Get
  property_count: 3
  slug: campaigns-get
- name: Campaigns Line_Items Get
  property_count: 3
  slug: campaigns-line_items-get
- name: Clients Get
  property_count: 2
  slug: clients-get
- name: Conversions Get
  property_count: 2
  slug: conversions-get
- name: Creatives Get
  property_count: 2
  slug: creatives-get
- name: Delivery_Sources Get
  property_count: 2
  slug: delivery_sources-get
- name: Groups Get
  property_count: 2
  slug: groups-get
- name: Kpis Get
  property_count: 2
  slug: kpis-get
- name: Me Get
  property_count: 1
  slug: me-get
- name: Properties Get
  property_count: 3
  slug: properties-get
- name: Stats Get
  property_count: 2
  slug: stats-get
- name: Tactics Get
  property_count: 2
  slug: tactics-get
- name: Vendors Get
  property_count: 2
  slug: vendors-get
- name: Verticals Get
  property_count: 2
  slug: verticals-get
jsonld:
- class_count: 18
  name: Basis Context
  property_count: 9
  slug: basis-context
layout: provider
modified: '2026-06-13'
name: Basis
nav: Providers
network: true
overview: 'Basis publishes 1 API on the [APIs.io](https://apis.io/) network: Analytics API. Tagged areas include Programmatic Advertising, DSP, Media Buying, Campaign Management, and Audience Targeting.


  The Basis catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Basis'' developer surface includes authentication, documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Basis Plans Pricing
  plan_count: 1
  slug: basis-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 0
  name: Basis Rate Limits
  slug: basis-rate-limits
rules:
- name: Basis API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: basis-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.9
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 40.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/basis/refs/heads/main/screenshots/basis-2026-06-20T173036.png
security:
- kind: authentication
  name: Basis Authentication
  slug: basis-authentication
  summary_line: http/unknown · 2 schemes
- kind: domain-security
  name: Basis Domain Security
  slug: basis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: basis
tags:
- Programmatic Advertising
- DSP
- Media Buying
- Campaign Management
- Audience Targeting
- AdTech
website: https://basis.com/
---
