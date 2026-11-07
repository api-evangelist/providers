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
  href: https://artifacts.apis.io/fermata-discovery/hosts/fermata-discovery-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fermata-discovery-hosts.yml
- group: auth
  href: https://artifacts.apis.io/fermata-discovery/security/fermata-discovery-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fermata-discovery-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fermatadiscovery.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.fermatadiscovery.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fermatadiscovery.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.fermatadiscovery.com/about-fermata/
- group: operate
  title: ''
  type: Contact
  url: https://www.fermatadiscovery.com/contact/
coverage:
  detail: No developer program or API documentation is publicly available.
  evidence:
  - status: 200
    url: https://www.fermatadiscovery.com/docs
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Fermata Discovery provides an AI‑assisted investigation and diligence platform that ingests diverse data sources, automates document processing, and visualizes connections among people, organizations, events, and locations. Their VIXN solution serves use cases in corrections intelligence, law enforcement, risk diligence, and investigative services, offering streamlined case management and advanced analytics to accelerate insight generation.
layout: provider
modified: '2026-10-25'
name: Fermata Discovery
nav: Providers
network: true
overview: 'Fermata Discovery is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Fermata Discovery''s developer surface includes documentation, getting-started guide, and 5 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 35.7
    operational_transparency: 0.0
  previous_composite: 8.4
  provenance:
    mcp: derived
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
screenshot: https://apis.io/screenshots/fermata-discovery/fermata-discovery-2026-11-03T131932.png
security:
- kind: domain-security
  name: Fermata Discovery Domain Security
  slug: fermata-discovery-domain-security
  summary_line: TLSv1.2 · DMARC
slug: fermata-discovery
tags:
- Company
website: https://www.fermatadiscovery.com
---
