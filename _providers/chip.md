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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/chip/a2a/chip-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/chip-a2a.yml
- group: agent
  href: https://artifacts.apis.io/chip/well-known/chip-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chip-well-known.yml
- group: other
  href: https://artifacts.apis.io/chip/hosts/chip-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chip-hosts.yml
- group: other
  href: https://artifacts.apis.io/chip/vendors/chip-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chip-vendors.yml
- group: auth
  href: https://artifacts.apis.io/chip/security/chip-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chip-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.chip-in.asia/login
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chip-in.asia
- group: docs
  title: ''
  type: APIReference
  url: https://docs.chip-in.asia/chip-collect/overview/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.chip-in.asia/chip-collect/overview/quickstart
- group: operate
  title: ''
  type: Support
  url: https://portal.chip-in.asia/collect/developers/api-keys
- group: company
  title: ''
  type: Blog
  url: https://blog.chip-in.asia
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CHIPAsia
created: '2026-10-08'
description: Chip provides a payment gateway API that enables businesses to accept payments online through various integrations and plugins. It offers a suite of endpoints for collecting payments, managing customers, handling webhooks, and accessing transaction data. The platform supports multiple SDKs and plugins for popular e‑commerce solutions, aiming to simplify payment processing for developers and merchants.
layout: provider
modified: '2026-10-08'
name: Chip
nav: Providers
network: true
overview: 'Chip is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Chip''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 8 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 35.7
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  previous_composite: 11.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/chip/chip-2026-11-03T124050.png
security:
- kind: domain-security
  name: Chip Domain Security
  slug: chip-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chip
tags:
- Company
website: https://www.nasdaqprivatemarket.com/
---
