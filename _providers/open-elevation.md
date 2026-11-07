---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides worldwide elevation data via a simple GET endpoint. Free tier allows limited requests per IP; paid plans increase limits and throughput.
  name: Elevation API
  slug: elevation-api
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/open-elevation/rate-limits/open-elevation-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/open-elevation-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/open-elevation/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/open-elevation/hosts/open-elevation-hosts.yml
  title: ''
  type: Hosts
  url: hosts/open-elevation-hosts.yml
- group: other
  href: https://artifacts.apis.io/open-elevation/vendors/open-elevation-vendors.yml
  title: ''
  type: Vendors
  url: vendors/open-elevation-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Jorl17/open-elevation/blob/master/docs/host-your-own.md
- group: auth
  href: https://artifacts.apis.io/open-elevation/security/open-elevation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/open-elevation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://open-elevation.com/
coverage:
  checked: '2026-10-28'
  detail: Open‑Elevation provides a public GET endpoint at https://api.open-elevation.com/api/v1/lookup but no machine‑readable OpenAPI or other spec is published.
  evidence:
  - status: 404
    url: https://api.open-elevation.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Open-Elevation provides a free, open-source elevation API that offers worldwide elevation data derived from NASA/USGS SRTM datasets. Users can query elevations via simple HTTP GET requests without needing an API key for modest usage, while paid plans grant higher limits and faster throughput. The service is hosted publicly at open-elevation.com and also offers self-hosted Docker images for private deployments. It aims to be an easy-to-use alternative to commercial elevation services.
image: https://open-elevation.com/images/logo.svg
layout: provider
modified: '2026-10-28'
name: Open-Elevation
nav: Providers
network: true
overview: 'Open-Elevation is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Elevation, Geospatial, Open Source, and Free.


  Open-Elevation''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Open Elevation Plans Pricing
  plan_count: 4
  slug: open-elevation-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Open Elevation Rate Limits
  slug: open-elevation-rate-limits
scopes:
- name: Open Elevation Scopes
  scope_count: 0
  slug: open-elevation-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.5
    discoverability: 66.1
    operational_transparency: 23.7
  previous_composite: 33.1
  provenance:
    conformance: unknown
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/open-elevation/open-elevation-2026-11-03T140627.png
security:
- kind: authentication
  name: Open Elevation Authentication
  slug: open-elevation-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Open Elevation Domain Security
  slug: open-elevation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: open-elevation
tags:
- Company
- Elevation
- Geospatial
- Open Source
- Free
website: https://open-elevation.com/
---
