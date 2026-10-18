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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ica-gruppen/refs/heads/main/hosts/ica-gruppen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ica-gruppen-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ica-gruppen/refs/heads/main/vendors/ica-gruppen-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ica-gruppen-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ica-gruppen/refs/heads/main/security/ica-gruppen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ica-gruppen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.icagruppen.se/
- group: docs
  title: ''
  type: Documentation
  url: https://www.icagruppen.se/om-ica-gruppen/
- group: company
  title: ''
  type: Press
  url: https://www.icagruppen.se/press
coverage:
  checked: '2026-10-15'
  detail: No OpenAPI or other machine-readable contract found on api.icagruppen.se or related hosts.
  evidence:
  - status: 0
    url: https://api.icagruppen.se/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: ICA Gruppen is a leading Swedish retail and service conglomerate operating supermarkets, pharmacies, banks, and real estate. It focuses on sustainable growth, digital innovation, and customer convenience across Scandinavia, offering a wide range of products and services while emphasizing environmental responsibility and community engagement.
image: https://www.icagruppen.se/globalassets/02.-om-ica-gruppen/om-ica-gruppen-1200x800.jpg
layout: provider
modified: '2026-10-14'
name: ICA Gruppen
nav: Providers
network: true
overview: 'ICA Gruppen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Services, Sweden, and Sustainability.


  ICA Gruppen''s developer surface includes documentation and 5 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ica Gruppen Domain Security
  slug: ica-gruppen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ica-gruppen
tags:
- Company
- Retail
- Services
- Sweden
- Sustainability
website: https://www.icagruppen.se/
---
