---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - rate-limits
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Public web services for geocoding, reverse geocoding, address parsing, nearby search, and POI data.
  name: Gisgraphy API
  slug: gisgraphy-api-2
- description: 'Gisgraphy API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Gisgraphy API
  slug: gisgraphy-api
artifact_total: 8
common:
- group: operate
  href: https://artifacts.apis.io/gisgraphy/rate-limits/gisgraphy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gisgraphy-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/gisgraphy/plans/gisgraphy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gisgraphy-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/gisgraphy/rules/gisgraphy-rules.yml
  title: ''
  type: Spectral
  url: rules/gisgraphy-rules.yml
- group: design
  href: https://artifacts.apis.io/gisgraphy/vocabulary/gisgraphy-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gisgraphy-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/gisgraphy/conformance/gisgraphy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gisgraphy-conformance.yml
- group: other
  href: https://artifacts.apis.io/gisgraphy/hosts/gisgraphy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gisgraphy-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gisgraphy.com/terms.php
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gisgraphy.com/privacy.php
- group: auth
  href: https://artifacts.apis.io/gisgraphy/security/gisgraphy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gisgraphy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gisgraphy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.gisgraphy.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://www.gisgraphy.com/webservices/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.gisgraphy.com/documentation/user-guide.php
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gisgraphy
coverage:
  checked: '2026-10-28'
  detail: The public web services are documented, but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec is published.
  evidence:
  - status: 404
    url: https://services.gisgraphy.com/geocoding/?address=paris&format=json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Gisgraphy provides open‑source geocoding and location services, offering web APIs for geocoding, reverse geocoding, address parsing, nearby place search, autocompletion, and access to extensive address and POI databases derived from Geonames and OpenStreetMap. The platform can be self‑hosted or accessed via free public web services, supporting developers building mapping, logistics, travel, and location‑aware applications.
image: https://www.gisgraphy.com/images/logos/logo_48.png
layout: provider
modified: '2026-10-28'
name: Gisgraphy
nav: Providers
network: true
overview: 'Gisgraphy is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Geocoding, Geolocation, Open Source, and Maps.


  The Gisgraphy catalog on APIs.io includes 1 Spectral governance ruleset.


  Gisgraphy''s developer surface includes documentation, API reference, getting-started guide, and 11 more developer resources.'
plans:
- name: Gisgraphy Plans Pricing
  plan_count: 5
  slug: gisgraphy-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Gisgraphy Rate Limits
  slug: gisgraphy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Gisgraphy API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: gisgraphy-rules
scopes:
- name: Gisgraphy Scopes
  scope_count: 0
  slug: gisgraphy-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 61.8
    catalog_earned_first_party: 24.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 34.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 33.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/gisgraphy/gisgraphy-2026-11-03T132824.png
security:
- kind: authentication
  name: Gisgraphy Authentication
  slug: gisgraphy-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Gisgraphy Domain Security
  slug: gisgraphy-domain-security
  summary_line: TLSv1.3
slug: gisgraphy
tags:
- Company
- Geocoding
- Geolocation
- Open Source
- Maps
website: https://gisgraphy.com/
---
