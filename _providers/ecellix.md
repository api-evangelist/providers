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
  href: https://artifacts.apis.io/ecellix/hosts/ecellix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ecellix-hosts.yml
- group: other
  href: https://artifacts.apis.io/ecellix/vendors/ecellix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ecellix-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ecellix/security/ecellix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ecellix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ecellix.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://ecellix.com/
  - status: 403
    url: https://forgeglobal.com/ecellix_stock/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Ecellix develops eCell™ high silicon-content anode technology, offering a drop-in replacement for graphite anodes that delivers over three times the capacity of typical graphite. Founded in 2018, the company focuses on configurable energy density and power for battery applications, positioning itself within the advanced materials and energy storage sector. While detailed corporate website information is limited, the company is listed on investment platforms such as Forge Global, highlighting its role in the technology hardware market and its ongoing funding activities.
image: https://ecellix.com/wp-content/uploads/2023/01/ecellix-logo.png
layout: provider
modified: '2026-10-24'
name: Ecellix
nav: Providers
network: true
overview: Ecellix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Battery, Materials, Technology, and Company.
random_paper: 22
score:
  band: minimal
  composite: 3.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 3.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ecellix/ecellix-2026-11-03T131253.png
security:
- kind: domain-security
  name: Ecellix Domain Security
  slug: ecellix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ecellix
tags:
- Energy
- Battery
- Materials
- Technology
- Company
website: https://ecellix.com/
---
