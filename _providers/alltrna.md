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
  href: https://raw.githubusercontent.com/api-evangelist/alltrna/refs/heads/main/hosts/alltrna-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alltrna-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alltrna/refs/heads/main/vendors/alltrna-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alltrna-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alltrna.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alltrna.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.alltrna.com/newsroom
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alltrna/refs/heads/main/security/alltrna-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alltrna-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alltrna.com/
created: '2026-09-24'
description: Alltrna develops engineered transfer RNA (tRNA) medicines that correct premature termination (stop) codons and restore full‑length protein production. The company applies its tRNA platform to create universal genetic medicines for thousands of diseases caused by shared genetic mutations, focusing on rare and genetic disorders. It targets patients with nonsense mutations and other genetic diseases requiring protein restoration.
layout: provider
modified: '2026-09-24'
name: Alltrna
nav: Providers
network: true
overview: Alltrna is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include tRNA therapeutics, Genetic Medicine, Rare Disease, and Platform.
random_paper: 2
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 37.5
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alltrna Domain Security
  slug: alltrna-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alltrna
tags:
- tRNA therapeutics
- Genetic Medicine
- Rare Disease
- Platform
website: https://www.alltrna.com/
---
