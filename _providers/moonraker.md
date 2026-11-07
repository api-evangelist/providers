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
  href: https://artifacts.apis.io/moonraker/hosts/moonraker-hosts.yml
  title: ''
  type: Hosts
  url: hosts/moonraker-hosts.yml
- group: other
  href: https://artifacts.apis.io/moonraker/vendors/moonraker-vendors.yml
  title: ''
  type: Vendors
  url: vendors/moonraker-vendors.yml
- group: build
  href: https://artifacts.apis.io/moonraker/packages/moonraker-packages.yml
  title: ''
  type: SDKs
  url: packages/moonraker-packages.yml
- group: build
  href: https://artifacts.apis.io/moonraker/packages/moonraker-packages.yml
  title: ''
  type: Packages
  url: packages/moonraker-packages.yml
- group: auth
  href: https://artifacts.apis.io/moonraker/security/moonraker-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/moonraker-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://moonraker.readthedocs.io
- group: docs
  title: ''
  type: Documentation
  url: https://moonraker.readthedocs.io/en/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://moonraker.readthedocs.io/en/latest/external_api/introduction/
- group: start
  title: ''
  type: GettingStarted
  url: https://moonraker.readthedocs.io/en/latest/installation/
- group: operate
  title: ''
  type: Support
  url: https://github.com/Arksine/moonraker/issues
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Arksine
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Arksine/moonraker
coverage:
  checked: '2026-10-28'
  detail: Documentation provides HTML pages but no machine‑readable OpenAPI or other contract files.
  evidence:
  - status: 200
    url: https://moonraker.readthedocs.io/en/latest/external_api/introduction/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Moonraker is an open-source Python 3 based web server that provides a JSON‑RPC and RESTful API for controlling 3D printers running Klipper firmware. It enables client applications to manage printer objects, job queues, webcams, updates, and extensions via HTTP endpoints. The project is hosted on GitHub and documented on Read the Docs, offering installation guides, configuration details, and extensive API reference for developers.
layout: provider
modified: '2026-10-28'
name: Moonraker (Klipper)
nav: Providers
network: true
overview: 'Moonraker (Klipper) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, 3D Printing, Open Source, Python, and Klipper.


  Moonraker (Klipper)''s developer surface includes documentation, API reference, getting-started guide, support, and 8 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 44.6
    operational_transparency: 2.6
  previous_composite: 11.9
  provenance:
    conformance: unknown
    mcp: unknown
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
screenshot: https://apis.io/screenshots/moonraker/moonraker-2026-11-03T135841.png
security:
- kind: domain-security
  name: Moonraker Domain Security
  slug: moonraker-domain-security
  summary_line: TLSv1.3 · HSTS
slug: moonraker
tags:
- Company
- 3D Printing
- Open Source
- Python
- Klipper
website: https://moonraker.readthedocs.io
---
