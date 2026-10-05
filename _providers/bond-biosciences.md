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
api_count: 1
apis:
- description: API documentation not publicly machine‑readable; website provides company information.
  name: Bond Biosciences API
  slug: bond-biosciences-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bond-biosciences/refs/heads/main/hosts/bond-biosciences-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bond-biosciences-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bond-biosciences/refs/heads/main/vendors/bond-biosciences-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bond-biosciences-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bond.bio/terms-of-use
- group: company
  title: ''
  type: Newsroom
  url: https://bond.bio/news
- group: other
  title: ''
  type: Leadership
  url: https://bond.bio/leadership
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bond-biosciences/refs/heads/main/security/bond-biosciences-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bond-biosciences-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bond.bio/
coverage:
  checked: '2026-10-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found on bond.bio or api.bond.bio.
  evidence:
  - status: 404
    url: https://bond.bio/openapi.json
  - status: 404
    url: https://bond.bio/openapi.json
  - status: 404
    url: https://bond.bio/swagger.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-02'
description: Bond Biosciences, Inc. is a privately held, clinical‑stage biopharmaceutical company focused on discovering and developing first‑in‑class non‑absorbed oral therapeutics that bind excess ions locally in the gastrointestinal tract to treat or prevent ion‑related human diseases. Their lead candidate, BBI‑001, aims to provide a safe, convenient solution for conditions such as hyperphosphatemia and hyperkalemia, leveraging a novel mechanism of action to improve patient outcomes.
image: http://static1.squarespace.com/static/60045b52399ee75bb3ff31e2/t/60270719db0e8560d0e7d00d/1618406397224/bond-biosciences-social-sharing-logo-600x600.png?format=1500w
layout: provider
modified: '2026-10-02'
name: Bond Biosciences
nav: Providers
network: true
overview: Bond Biosciences publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biopharma, Therapeutics, Ion‑related diseases, and Clinical Stage.
random_paper: 17
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 5
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
    discoverability: 60.7
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bond Biosciences Domain Security
  slug: bond-biosciences-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bond-biosciences
tags:
- Company
- Biopharma
- Therapeutics
- Ion‑related diseases
- Clinical Stage
website: https://bond.bio/
---
