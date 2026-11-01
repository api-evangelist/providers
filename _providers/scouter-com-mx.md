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
- group: agent
  href: https://artifacts.apis.io/scouter-com-mx/llms/scouter-com-mx-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scouter-com-mx-llms.txt
- group: other
  href: https://artifacts.apis.io/scouter-com-mx/hosts/scouter-com-mx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scouter-com-mx-hosts.yml
- group: other
  href: https://artifacts.apis.io/scouter-com-mx/vendors/scouter-com-mx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/scouter-com-mx-vendors.yml
- group: auth
  href: https://artifacts.apis.io/scouter-com-mx/security/scouter-com-mx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scouter-com-mx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wearescouter.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://wearescouter.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Scouter is a Mexican technology company offering a platform for field service management, asset tracking, and IoT solutions. Their services include real‑time monitoring, predictive maintenance, and mobile workforce coordination for enterprises across Latin America. Scouter aims to improve operational efficiency through data‑driven insights and customizable dashboards, supporting integration with various hardware sensors and enterprise systems.
image: https://pub-bb2e103a32db4e198524a2e9ed8f35b4.r2.dev/e68c34d3-f0f6-4771-a0ab-24b1f3744ef1/id-preview-ecc13c05--cf961fa6-6101-46c6-9a0b-622b064e7ca8.lovable.app-1771288857979.png
layout: provider
modified: '2026-10-25'
name: Scouter
nav: Providers
network: true
overview: Scouter is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Field Service, IoT, Asset Tracking, and Predictive Maintenance.
random_paper: 19
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - mexico
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
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
  name: Scouter Com Mx Domain Security
  slug: scouter-com-mx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: scouter-com-mx
tags:
- Company
- Field Service
- IoT
- Asset Tracking
- Predictive Maintenance
website: https://wearescouter.com
---
