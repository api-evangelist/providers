---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Stekker provides an API for electric vehicle owners to share charging revenue. Documentation is hosted at the developer portal but the spec is not publicly machine‑readable.
  name: Stekker API
  slug: stekker-api
artifact_total: 4
asyncapis:
- description: ''
  name: Stekker Webhooks
  slug: stekker-webhooks
common:
- group: design
  href: https://artifacts.apis.io/stekker/asyncapi/stekker-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/stekker-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/stekker/authentication/stekker-authentication.yml
  title: ''
  type: Authentication
  url: authentication/stekker-authentication.yml
- group: agent
  href: https://artifacts.apis.io/stekker/llms/stekker-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stekker-llms.txt
- group: other
  href: https://artifacts.apis.io/stekker/hosts/stekker-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stekker-hosts.yml
- group: other
  href: https://artifacts.apis.io/stekker/vendors/stekker-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stekker-vendors.yml
- group: build
  href: https://artifacts.apis.io/stekker/packages/stekker-packages.yml
  title: ''
  type: SDKs
  url: packages/stekker-packages.yml
- group: build
  href: https://artifacts.apis.io/stekker/packages/stekker-packages.yml
  title: ''
  type: Packages
  url: packages/stekker-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.stekker.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://stekker.com/nl/changelog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stekker
- group: auth
  href: https://artifacts.apis.io/stekker/security/stekker-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stekker-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stekker.com/
- group: docs
  title: ''
  type: Documentation
  url: https://stekker.com/nl/over-stekker/
- group: company
  title: ''
  type: Blog
  url: https://stekker.com/nl/blog/
- group: operate
  title: ''
  type: Support
  url: https://stekker.com/nl/support/
created: '2026-10-28'
description: Stekker is a Dutch platform that enables electric vehicle owners to earn revenue by sharing the electricity used to charge their cars. Users register, their charging sessions are recorded as Energy Revenue Entitlements (EREs), which Stekker monetises and distributes the earnings. The service supports multiple charger brands, offers transparent pricing, and provides a dashboard for tracking earnings and usage.
image: https://stekker.com/wp-content/uploads/2026/08/stekker-og-curve.png
layout: provider
modified: '2026-10-28'
name: Stekker
nav: Providers
network: true
overview: 'Stekker is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Electric Vehicles, Renewables, Marketplace, and Netherlands.


  The Stekker catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Stekker''s developer surface includes authentication, changelog, documentation, engineering blog, support, and 10 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 32.1
    discoverability: 64.3
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 28.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/stekker/stekker-2026-11-03T143811.png
security:
- kind: authentication
  name: Stekker Authentication
  slug: stekker-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Stekker Domain Security
  slug: stekker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stekker
tags:
- Energy
- Electric Vehicles
- Renewables
- Marketplace
- Netherlands
website: https://stekker.com/
---
