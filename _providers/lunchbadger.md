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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/lunchbadger/hosts/lunchbadger-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lunchbadger-hosts.yml
- group: build
  href: https://artifacts.apis.io/lunchbadger/packages/lunchbadger-packages.yml
  title: ''
  type: SDKs
  url: packages/lunchbadger-packages.yml
- group: build
  href: https://artifacts.apis.io/lunchbadger/packages/lunchbadger-packages.yml
  title: ''
  type: Packages
  url: packages/lunchbadger-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LunchBadger
- group: auth
  href: https://artifacts.apis.io/lunchbadger/security/lunchbadger-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lunchbadger-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lunchbadger.com
coverage:
  checked: '2026-10-29'
  detail: API host returns no OpenAPI/Swagger spec despite probing common spec URLs
  evidence:
  - status: 530
    url: https://api.lunchbadger.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: LunchBadger is a technology company focused on providing a visual platform for designing, building, and managing microservice architectures and APIs. It offers tools for API modeling, documentation, and governance, aiming to streamline the development lifecycle for enterprises. The company was identified through the API Evangelist harvest backlog and is backed by Heavybit, reflecting its roots in the venture capital ecosystem. LunchBadger seeks to empower developers and architects with a low‑code environment to accelerate API‑first strategies and improve operational efficiency across complex software systems.
layout: provider
modified: '2026-10-29'
name: LunchBadger
nav: Providers
network: true
overview: LunchBadger is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API-Design, Low-Code, Microservices, and Enterprise.
random_paper: 23
score:
  band: minimal
  composite: 5.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Lunchbadger Domain Security
  slug: lunchbadger-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lunchbadger
tags:
- Company
- API-Design
- Low-Code
- Microservices
- Enterprise
website: https://www.lunchbadger.com
---
