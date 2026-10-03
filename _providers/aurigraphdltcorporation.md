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
api_count: 1
apis:
- description: Aurigraph - Decentralized Ledger Technology
  name: Aurigraph API
  slug: aurigraph-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aurigraphdltcorporation/refs/heads/main/hosts/aurigraphdltcorporation-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aurigraphdltcorporation-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.aurigraph.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aurigraphdltcorporation/refs/heads/main/security/aurigraphdltcorporation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aurigraphdltcorporation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aurigraph.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aurigraph.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aurigraph.io/terms
- group: operate
  title: ''
  type: Support
  url: https://www.aurigraph.io/investors
- group: start
  title: ''
  type: GettingStarted
  url: https://www.aurigraph.io/investors
coverage:
  checked: 2026-09-26
  detail: Docs pages return HTML shells with no machine‑readable spec despite HTTP 200
  evidence:
  - status: 200
    url: https://www.aurigraph.io/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Aurigraph DLT Corporation is a blockchain-focused company offering decentralized ledger technology solutions. It provides a platform for building, deploying, and managing distributed applications, with services ranging from tokenization to smart contract execution. The company emphasizes security, scalability, and regulatory compliance, targeting enterprises seeking to integrate DLT into their operations.
layout: provider
modified: '2026-09-26'
name: Aurigraphdltcorporation
nav: Providers
network: true
overview: 'Aurigraphdltcorporation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain, DLT, Decentralized, Enterprise, and Platform.


  Aurigraphdltcorporation''s developer surface includes documentation, support, getting-started guide, and 5 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 53.6
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
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aurigraphdltcorporation Domain Security
  slug: aurigraphdltcorporation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aurigraphdltcorporation
tags:
- Blockchain
- DLT
- Decentralized
- Enterprise
- Platform
- Company
website: https://www.aurigraph.io
---
