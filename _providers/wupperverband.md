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
  href: https://artifacts.apis.io/wupperverband/hosts/wupperverband-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wupperverband-hosts.yml
- group: auth
  href: https://artifacts.apis.io/wupperverband/security/wupperverband-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wupperverband-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.wupperverband.de
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: http://www.wupperverband.de
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: Wupperverband is a public-law corporation (Körperschaft des öffentlichen Rechts) responsible for water management, flood protection, and environmental stewardship in the Wupper river basin in Germany. It oversees water supply, wastewater treatment, dam and reservoir operations, and implements climate adaptation projects. The organization provides data and services related to water quality, flood forecasting, and infrastructure, serving municipalities, businesses, and the public with sustainable water resource management.
image: https://www.wupperverband.de/internet/web.nsf/id/4A510A16A0BB335EC125847700304305/$file/logo.png
layout: provider
modified: '2026-10-23'
name: Wupperverband
nav: Providers
network: true
overview: Wupperverband is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Water Management, Flood Protection, Environmental Services, and Germany.
random_paper: 21
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
  name: Wupperverband Domain Security
  slug: wupperverband-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wupperverband
tags:
- Company
- Water Management
- Flood Protection
- Environmental Services
- Germany
website: http://www.wupperverband.de
---
