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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ambrosiabiosciences/refs/heads/main/hosts/ambrosiabiosciences-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ambrosiabiosciences-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ambrosiabiosciences/refs/heads/main/vendors/ambrosiabiosciences-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ambrosiabiosciences-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ambrosiabiosciences/refs/heads/main/security/ambrosiabiosciences-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ambrosiabiosciences-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ambrosiabiosciences.com
coverage:
  checked: 2026-09-24
  detail: No public API documentation or machine-readable contract was found for Ambrosiabiosciences.
  evidence:
  - status: 200
    url: https://ambrosiabiosciences.com
  reason: not-a-software-company
  state: none
created: '2026-09-24'
description: Ambrosia Biosciences is a drug discovery company that develops orally delivered, small‑molecule therapies for obesity and other metabolic disorders. The company leverages structure‑based discovery, cryo‑EM structural biology, biophysical assays, and AI‑powered design to target Class B GPCRs. Its integrated U.S. chemistry and biology labs support rapid progression from hit identification to IND filing.
layout: provider
modified: '2026-09-24'
name: Ambrosiabiosciences
nav: Providers
network: true
overview: Ambrosiabiosciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Drug Discovery, Metabolic Disorders, Small Molecule Therapeutics, GPCR, and Biotechnology.
random_paper: 3
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 3.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ambrosiabiosciences Domain Security
  slug: ambrosiabiosciences-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: ambrosiabiosciences
tags:
- Drug Discovery
- Metabolic Disorders
- Small Molecule Therapeutics
- GPCR
- Biotechnology
website: https://ambrosiabiosciences.com
---
