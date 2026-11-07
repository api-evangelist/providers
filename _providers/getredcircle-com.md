---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: RedCircle API provides podcast advertising management endpoints. Documentation is referenced on the main site but no machine‑readable spec was found.
  name: RedCircle API
  slug: redcircle-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/getredcircle-com/plans/getredcircle-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/getredcircle-com-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/getredcircle-com/hosts/getredcircle-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getredcircle-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/getredcircle-com/vendors/getredcircle-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getredcircle-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/getredcircle-com/security/getredcircle-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getredcircle-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getredcircle.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://redcircle.com/
- group: docs
  title: ''
  type: Documentation
  url: https://redcircle.com/
- group: company
  title: ''
  type: Blog
  url: https://redcircle.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://redcircle.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://redcircle.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://redcircle.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://support.redcircle.com
coverage:
  checked: '2026-10-25'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract was found on any discovered API host.
  evidence:
  - status: timeout
    url: https://api.getredcircle.com/openapi.json
  - status: 404
    url: https://api.redcircle.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: RedCircle is a podcast advertising platform that connects brands with podcasters to create authentic host‑read ads. Founded in 2018, the company offers a self‑serve ad platform, creative services, and detailed performance metrics. It serves over 1 billion ad impressions across 10 k+ partnered podcasters, handling everything from campaign setup to reporting. RedCircle aims to simplify podcast advertising for brands while ensuring creators are fairly compensated.
image: https://redcircle.com/redcircle-meta-image.png
layout: provider
modified: '2026-10-25'
name: RedCircle
nav: Providers
network: true
overview: 'RedCircle is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Podcast Advertising, Marketing, Media, Technology, and Company.


  RedCircle''s developer surface includes documentation, engineering blog, pricing, support, and 8 more developer resources.'
plans:
- name: Getredcircle Com Plans Pricing
  plan_count: 4
  slug: getredcircle-com-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.9
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 23.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Getredcircle Com Domain Security
  slug: getredcircle-com-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: getredcircle-com
tags:
- Podcast Advertising
- Marketing
- Media
- Technology
- Company
website: https://www.getredcircle.com/
---
