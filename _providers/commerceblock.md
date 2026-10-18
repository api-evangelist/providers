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
api_count: 1
apis:
- description: API for Commerceblock platform
  name: Commerceblock API
  slug: commerceblock-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/commerceblock/refs/heads/main/hosts/commerceblock-hosts.yml
  title: ''
  type: Hosts
  url: hosts/commerceblock-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/commerceblock/refs/heads/main/vendors/commerceblock-vendors.yml
  title: ''
  type: Vendors
  url: vendors/commerceblock-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/commerceblock/refs/heads/main/security/commerceblock-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/commerceblock-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/commerceblock/refs/heads/main/security/commerceblock-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/commerceblock-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://commerceblock.com
coverage:
  checked: '2026-10-09'
  detail: Home page returns a JavaScript shell with no machine‑readable documentation.
  evidence:
  - status: 200
    url: https://commerceblock.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-09'
description: Commerceblock is a blockchain technology company focused on building public and hybrid blockchain infrastructure for the distribution, exchange, and storage of tokenized assets and securities. The company develops enterprise‑grade systems that combine the immutability and security of public blockchains with the operational flexibility of permissioned environments, targeting regulated financial markets. Their platform offers sidechains, attestation services, and tools for clients to create, manage, and trade digital securities on multiple public networks, aiming to enable compliant tokenization and decentralized finance solutions.
layout: provider
modified: '2026-10-09'
name: Commerceblock
nav: Providers
network: true
overview: Commerceblock is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain, Fintech, Tokenization, Distributed Ledger, and Securities.
random_paper: 2
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 11.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Commerceblock Domain Security
  slug: commerceblock-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Commerceblock Vulnerability Disclosure
  slug: commerceblock-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: commerceblock
tags:
- Blockchain
- Fintech
- Tokenization
- Distributed Ledger
- Securities
website: https://commerceblock.com
---
