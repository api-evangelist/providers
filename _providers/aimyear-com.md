---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/aimyear-com/hosts/aimyear-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aimyear-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aimyear-com/vendors/aimyear-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aimyear-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aimyear.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aimyear.com/privacy.html
- group: auth
  href: https://artifacts.apis.io/aimyear-com/security/aimyear-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aimyear-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aimyear.com/
- group: company
  title: ''
  type: Blog
  url: https://aimyear.com/blog.html
- group: commercial
  title: ''
  type: Pricing
  url: https://aimyear.com/#pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://aimyear.com/guide.html
coverage:
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found on discovered API hosts.
  evidence:
  - status: 404
    url: https://api.aimyear.com/openapi.json
  - status: 404
    url: https://api.aimyear.com/openapi.yaml
  - status: 404
    url: https://api.aimyear.com/swagger.json
  - status: 404
    url: https://api.aimyear.com/v1/openapi.json
  - status: 404
    url: https://api.aimyear.com/api-docs
  - status: 404
    url: https://api.aimyear.com/docs
  - status: 404
    url: https://api.aimyear.com/redoc
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AimYear provides an AI‑agent‑integrated goal‑tracking platform that helps founders break down yearly objectives into daily actionable steps. The free tier offers basic tracking, while Pro plans add advanced analytics and priority support. It runs inside popular AI agents like Claude, enabling seamless workflow integration. AimYear aims to turn ambitious visions into measurable progress, fostering accountability and transparent time‑spending records.
layout: provider
modified: '2026-11-01'
name: AimYear
nav: Providers
network: true
overview: 'AimYear is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Productivity, Artificial Intelligence, Goal Tracking, Startups, and Free Tier.


  AimYear''s developer surface includes engineering blog, pricing, getting-started guide, and 6 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 13.3
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aimyear Com Domain Security
  slug: aimyear-com-domain-security
  summary_line: TLSv1.3
slug: aimyear-com
tags:
- Productivity
- Artificial Intelligence
- Goal Tracking
- Startups
- Free Tier
website: https://aimyear.com/
---
