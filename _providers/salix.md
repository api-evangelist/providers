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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/salix/hosts/salix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/salix-hosts.yml
- group: other
  href: https://artifacts.apis.io/salix/vendors/salix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/salix-vendors.yml
- group: auth
  href: https://artifacts.apis.io/salix/security/salix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/salix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.salix.com/
created: '2026-10-26'
description: Salix Pharmaceuticals develops and markets gastrointestinal (GI) treatments. It provides proven therapeutic products for patients with GI diseases and supplies product information to healthcare professionals. The company also conducts research to advance its pipeline of GI specialty pharmaceuticals.
layout: provider
modified: '2026-10-26'
name: Salix
nav: Providers
network: true
overview: Salix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Pharmaceuticals, Gastrointestinal, Specialty Pharma, and Healthcare.
random_paper: 17
score:
  band: minimal
  composite: 2.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Salix Domain Security
  slug: salix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: salix
tags:
- Pharmaceuticals
- Gastrointestinal
- Specialty Pharma
- Healthcare
website: https://www.salix.com/
---
