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
  href: https://artifacts.apis.io/survey-of-pakistan/hosts/survey-of-pakistan-hosts.yml
  title: ''
  type: Hosts
  url: hosts/survey-of-pakistan-hosts.yml
- group: auth
  href: https://artifacts.apis.io/survey-of-pakistan/security/survey-of-pakistan-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/survey-of-pakistan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.surveyofpakistan.gov.pk/
coverage:
  checked: '2026-10-28'
  detail: No machine‑readable API specification was found on the provider’s website.
  evidence:
  - status: 200
    url: https://www.surveyofpakistan.gov.pk/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Survey of Pakistan (SoP) is Pakistan's national survey and mapping organization providing accurate geospatial data for planning, development, and security of the nation. It serves government, semi-government, autonomous bodies, and both public and private sectors, contributing to national development projects through comprehensive surveying and mapping services.
layout: provider
modified: '2026-10-28'
name: Survey of Pakistan
nav: Providers
network: true
overview: Survey of Pakistan is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Geospatial, Mapping, Government, and Data.
random_paper: 0
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
  name: Survey Of Pakistan Domain Security
  slug: survey-of-pakistan-domain-security
  summary_line: TLSv1.3 · DMARC
slug: survey-of-pakistan
tags:
- Company
- Geospatial
- Mapping
- Government
- Data
website: https://www.surveyofpakistan.gov.pk/
---
