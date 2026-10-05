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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/applied-stemcell/refs/heads/main/hosts/applied-stemcell-hosts.yml
  title: ''
  type: Hosts
  url: hosts/applied-stemcell-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/applied-stemcell/refs/heads/main/vendors/applied-stemcell-vendors.yml
  title: ''
  type: Vendors
  url: vendors/applied-stemcell-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appliedstemcell.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://appliedstemcell.com/news/
- group: start
  title: ''
  type: Login
  url: https://appliedstemcell.com/login/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/applied-stemcell/refs/heads/main/security/applied-stemcell-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/applied-stemcell-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appliedstemcell.com
created: '2026-09-25'
description: Applied StemCell provides genome engineering platforms and services, including the TARGATT™ large knock‑in technology, CRISPR/Cas9, Mad7 gene editing, and iPSC‑based drug discovery. The company offers kits, cell lines, and cGMP manufacturing to accelerate research and therapeutic development.
image: https://appliedstemcell.com/wp-content/uploads/2025/03/ASClogo_sqStacked.jpg?wsr
layout: provider
modified: '2026-09-25'
name: Applied StemCell
nav: Providers
network: true
overview: Applied StemCell is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Genome Engineering, CRISPR, iPSC, and Cell Therapy.
random_paper: 9
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Applied Stemcell Domain Security
  slug: applied-stemcell-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: applied-stemcell
tags:
- Biotechnology
- Genome Engineering
- CRISPR
- iPSC
- Cell Therapy
website: https://appliedstemcell.com
---
