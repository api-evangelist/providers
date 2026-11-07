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
  href: https://artifacts.apis.io/lat-lon-gmbh/llms/lat-lon-gmbh-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lat-lon-gmbh-llms.txt
- group: agent
  href: https://artifacts.apis.io/lat-lon-gmbh/well-known/lat-lon-gmbh-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lat-lon-gmbh-well-known.yml
- group: other
  href: https://artifacts.apis.io/lat-lon-gmbh/hosts/lat-lon-gmbh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lat-lon-gmbh-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://support.lat-lon.de/help
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lat-lon
- group: auth
  href: https://artifacts.apis.io/lat-lon-gmbh/security/lat-lon-gmbh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lat-lon-gmbh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lat-lon.de
- group: docs
  title: ''
  type: Documentation
  url: https://lat-lon.de/open-source/
- group: company
  title: ''
  type: About
  url: https://lat-lon.de/unternehmen/about/
- group: operate
  title: ''
  type: Contact
  url: https://lat-lon.de/kontakt/
coverage:
  checked: '2026-10-23'
  detail: Provider docs are rendered as HTML with no machine‑readable OpenAPI spec discovered.
  evidence:
  - status: 200
    url: https://lat-lon.de/open-source/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: lat/lon GmbH provides services in spatial and modern internet-based information systems based on open‑source software. The team combines expertise in geography, geoinformatics and computer science, offering consulting, development and support for geodata infrastructures. They contribute to open‑source projects such as xPlanBox and the OSGeo deegree framework, and are members of FOSSGIS, OGC and the Open Source Business Alliance.
image: https://lat-lon.de/wp-content/uploads/2025/01/latlon_Logo.jpg
layout: provider
modified: '2026-10-23'
name: lat/lon GmbH
nav: Providers
network: true
overview: 'lat/lon GmbH is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, GIS, Open Source, Consulting, and Geodata.


  lat/lon GmbH''s developer surface includes support, documentation, and 8 more developer resources.'
random_paper: 2
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
  delta: -1.8
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 55.4
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 8.6
  provenance:
    mcp: unknown
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
screenshot: https://apis.io/screenshots/lat-lon-gmbh/lat-lon-gmbh-2026-11-03T134656.png
security:
- kind: domain-security
  name: Lat Lon Gmbh Domain Security
  slug: lat-lon-gmbh-domain-security
  summary_line: TLSv1.3
slug: lat-lon-gmbh
tags:
- Company
- GIS
- Open Source
- Consulting
- Geodata
website: https://lat-lon.de
---
