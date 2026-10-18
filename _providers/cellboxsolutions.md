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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Cellbox Solutions' logistics platform (no public documentation found)
  name: Cellbox Solutions API
  slug: cellbox-solutions-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cellboxsolutions/refs/heads/main/hosts/cellboxsolutions-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cellboxsolutions-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cellbox-solutions.com/terms-and-conditions
- group: company
  title: ''
  type: Newsroom
  url: https://cellbox-solutions.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cellboxsolutions/refs/heads/main/security/cellboxsolutions-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cellboxsolutions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cellbox-solutions.com
coverage:
  checked: '2026-10-07'
  detail: Main website loads content via JavaScript, preventing automated spec discovery.
  evidence:
  - status: 200
    url: https://cellbox-solutions.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: Cellbox Solutions develops innovative logistics solutions for the global bio‑medical industry, focusing on portable CO₂ incubators and temperature‑controlled transport systems that keep living cells and biological samples viable during shipment. Their flagship products enable safe, regulated transport for cell and gene therapy, drug discovery, and pre‑clinical research, integrating hardware, software, and logistics expertise to support the warm‑chain logistics needs of modern life‑science workflows.
image: https://cellbox-solutions.com/media/site/74aed02430-1692692040/co2-transportable-incubator-cellbox-flight-cdi-cellbox-solutions.jpg
layout: provider
modified: '2026-10-07'
name: Cellboxsolutions
nav: Providers
network: true
overview: Cellboxsolutions is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Bio-Medical, Logistics, Cell Transport, and CO2 Incubator.
random_paper: 15
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cellboxsolutions Domain Security
  slug: cellboxsolutions-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cellboxsolutions
tags:
- Company
- Bio-Medical
- Logistics
- Cell Transport
- CO2 Incubator
- Life Sciences
website: https://cellbox-solutions.com
---
