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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/polish-geological-institute-national-research-institute/hosts/polish-geological-institute-national-research-institute-hosts.yml
  title: ''
  type: Hosts
  url: hosts/polish-geological-institute-national-research-institute-hosts.yml
- group: other
  href: https://artifacts.apis.io/polish-geological-institute-national-research-institute/vendors/polish-geological-institute-national-research-institute-vendors.yml
  title: ''
  type: Vendors
  url: vendors/polish-geological-institute-national-research-institute-vendors.yml
- group: auth
  href: https://artifacts.apis.io/polish-geological-institute-national-research-institute/security/polish-geological-institute-national-research-institute-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/polish-geological-institute-national-research-institute-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pgi.gov.pl/
coverage:
  checked: '2026-10-29'
  detail: The provider's website returns only a JavaScript shell with no machine‑readable documentation.
  evidence:
  - status: 200
    url: http://www.pgi.gov.pl/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: The Polish Geological Institute – National Research Institute (PGI) is Poland’s leading state‑run organization for geological research, monitoring, and resource assessment. It conducts scientific studies, provides expert advice on mineral resources, groundwater, and environmental protection, and publishes data and reports for government, industry, and the public. The institute operates a network of laboratories, field stations, and a comprehensive digital library, supporting sustainable development and safety in the mining and construction sectors.
layout: provider
modified: '2026-10-28'
name: Polish Geological Institute - National Research Institute
nav: Providers
network: true
overview: Polish Geological Institute - National Research Institute is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Geology, Research, Poland, and Government.
random_paper: 11
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Polish Geological Institute National Research Institute Domain Security
  slug: polish-geological-institute-national-research-institute-domain-security
  summary_line: TLSv1.3 · DMARC
slug: polish-geological-institute-national-research-institute
tags:
- Company
- Geology
- Research
- Poland
- Government
website: https://www.pgi.gov.pl/
---
