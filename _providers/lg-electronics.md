---
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
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: LG ThinQ provides smart home and IoT services integrating LG appliances and devices.
  name: LG ThinQ
  slug: lg-thinq
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/lg-electronics/llms/lg-electronics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lg-electronics-llms.txt
- group: other
  href: https://artifacts.apis.io/lg-electronics/hosts/lg-electronics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lg-electronics-hosts.yml
- group: other
  href: https://artifacts.apis.io/lg-electronics/vendors/lg-electronics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lg-electronics-vendors.yml
- group: auth
  href: https://artifacts.apis.io/lg-electronics/security/lg-electronics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lg-electronics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lg.com/
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract files were found on LG's documented hosts.
  evidence:
  - status: 404
    url: https://api.lg.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: LG ThinQ, a division of LG Electronics, offers a suite of smart home and IoT solutions under the ThinQ brand. It integrates appliances, televisions, and mobile devices through a unified platform, enabling users to control and monitor their environment via voice assistants and mobile apps. The company focuses on AI-driven features, energy efficiency, and seamless connectivity across its product ecosystem, serving consumers worldwide with innovative technology and support services.
layout: provider
modified: '2026-10-28'
name: LG ThinQ
nav: Providers
network: true
overview: LG ThinQ is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SmartHome, IoT, ConsumerElectronics, and AI.
random_paper: 19
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Lg Electronics Domain Security
  slug: lg-electronics-domain-security
  summary_line: TLSv1.2 · DMARC
slug: lg-electronics
tags:
- Company
- SmartHome
- IoT
- ConsumerElectronics
- AI
website: https://lg.com/
---
