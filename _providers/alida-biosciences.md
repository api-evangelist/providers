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
  href: https://raw.githubusercontent.com/api-evangelist/alida-biosciences/refs/heads/main/hosts/alida-biosciences-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alida-biosciences-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.alidabio.com/news/alidabio-launches-epiplex-platform-to-advance-epitranscriptomic-research-business-wire-feb-5-2025/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alidabio
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alida-biosciences/refs/heads/main/security/alida-biosciences-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alida-biosciences-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alidabio.com/
- group: company
  title: ''
  type: Blog
  url: https://www.alidabio.com/blog-post/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alidabio.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alidabio.com/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://www.alidabio.com/contact-us/
coverage:
  checked: '2026-10-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found at the API host (api.alidabio.com) despite probing common spec endpoints.
  evidence:
  - status: 0
    url: https://api.alidabio.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-24'
description: Alida Biosciences (operating as AlidaBio) is a San Diego‑based biotechnology company founded in 2020 that develops innovative platforms for analyzing RNA modifications. Their EpiPlex™ platform enables high‑throughput profiling of m6A, inosine, pseudouridine and RNA expression in a single workflow, supporting research, diagnostics and therapeutic discovery. The company aims to unlock the epitranscriptomic layer of gene regulation to advance precision medicine.
layout: provider
modified: '2026-09-24'
name: Alida Biosciences
nav: Providers
network: true
overview: 'Alida Biosciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, RNA, Epitranscriptomics, and San-Diego.


  Alida Biosciences'' developer surface includes engineering blog and 8 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 9.5
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 46.4
    operational_transparency: 5.3
  previous_composite: 0.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alida Biosciences Domain Security
  slug: alida-biosciences-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alida-biosciences
tags:
- Company
- Biotechnology
- RNA
- Epitranscriptomics
- San-Diego
website: https://www.alidabio.com/
---
