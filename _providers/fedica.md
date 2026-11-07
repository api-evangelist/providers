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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/fedica/well-known/fedica-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fedica-well-known.yml
- group: other
  href: https://artifacts.apis.io/fedica/hosts/fedica-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fedica-hosts.yml
- group: other
  href: https://artifacts.apis.io/fedica/vendors/fedica-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fedica-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://fedica.com/auth/login
- group: company
  title: ''
  type: Blog
  url: https://fedica.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.fedica.com/
- group: auth
  href: https://artifacts.apis.io/fedica/security/fedica-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fedica-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fedica.com/
coverage:
  checked: '2026-10-26'
  detail: No OpenAPI or other machine‑readable contract was found; attempts at common spec URLs returned 404.
  evidence:
  - status: 404
    url: https://fedica.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Fedica provides a social media analytics platform that schedules posts across 15 social platforms and delivers deep audience insights, including demographics down to city level, location, bot detection, and engagement analytics. It helps brands understand who their audience is and optimize content strategy with comprehensive metrics and reporting.
image: https://fedica.com/c/images/static/brand.png
layout: provider
modified: '2026-10-26'
name: Fedica
nav: Providers
network: true
overview: 'Fedica is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social Media, Analytics, Marketing, and Software-as-a-Service.


  Fedica''s developer surface includes engineering blog, documentation, and 6 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 9.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/fedica/fedica-2026-11-03T131922.png
security:
- kind: domain-security
  name: Fedica Domain Security
  slug: fedica-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: fedica
tags:
- Company
- Social Media
- Analytics
- Marketing
- Software-as-a-Service
website: https://fedica.com/
---
