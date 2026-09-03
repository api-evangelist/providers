---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cybavo-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/cybavo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cybavo-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cybavo-llms.txt
- group: company
  title: ''
  type: Website
  url: https://cybavo.com
created: '2026-07-17'
description: CYBAVO was a digital asset security company (founded 2018, Taipei/Singapore) providing institutional-grade cryptocurrency custody and wallet infrastructure. Its flagship CYBAVO Vault delivered MPC-based (Multi-Party Computation) custody with a policy/workflow engine, REST API, and client SDKs, alongside the CYBAVO Wallet App SDK for embedding secure private-key storage into mobile apps. Circle Internet Financial acquired CYBAVO in June 2022; the team and technology became the foundation of Circle Web3 Services and Circle Programmable Wallets. The cybavo.com developer surface has since been wound down (redirects to circle.com), but the first-party @cybavo Wallet/Auth SDKs remain published on npm and are maintained under Circle's circlefin GitHub organization.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cybavo.png
layout: provider
modified: '2026-07-18'
name: CYBAVO
nav: Providers
network: true
overview: CYBAVO is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Digital Asset Security, Wallets, and Custody.
random_paper: 14
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cybavo/refs/heads/main/screenshots/cybavo-2026-07-25T211020.png
security:
- kind: domain-security
  name: Cybavo Domain Security
  slug: cybavo-domain-security
  summary_line: DNSSEC · DMARC
slug: cybavo
tags:
- Company
- Cryptocurrency
- Digital Asset Security
- Wallets
- Custody
- MPC
- Blockchain
- SDK
website: https://cybavo.com
---
