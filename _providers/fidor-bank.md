---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'Fidor''s REST API for Customers, Accounts, Transfers, Transactions and Account Information, secured with OAuth2 (authorization-code flow). Now retired: the sandbox (*.sandbox.fidor.com) and production '
  name: Fidor Germany Banking API
  slug: fidor-germany-banking-api
artifact_total: 2
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/fidor/fidor_api/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/fidor/fidor_api/blob/master/LICENSE
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fidor
- group: build
  title: ''
  type: Packages
  url: packages/fidor-bank-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fidor-bank-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fidor-bank-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fidor-bank-lifecycle.yml
created: '2026-07-17'
description: 'Fidor Bank was a German digital challenger bank founded in Munich in 2009 and an early pioneer of Banking-as-a-Service and open banking through its fidorOS / bankOS middleware platform and public REST API, which covered Customers, Accounts, Transfers, Transactions and Account Information over an OAuth2 authorization-code flow. Fidor was acquired by France''s Groupe BPCE in 2016; following years of post-acquisition integration struggles the bank ceased business operations in mid-2023 and entered liquidation. Its developer portal (fidor.com) is now a parked domain and the sandbox and production API hosts are offline. The surviving first-party developer artifacts are the archived official Ruby client (RubyGems: fidor_api, by Fidor Solutions AG) and the github.com/fidor organization. This is a retired provider retained for historical reference.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fidor-bank.png
layout: provider
modified: '2026-07-19'
name: Fidor Bank
nav: Providers
network: true
overview: 'Fidor Bank publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Banking, Banking as a Service, and Open Banking.


  Fidor Bank''s developer surface includes authentication and 6 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 7.5
  delta: -3.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  previous_composite: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fidor-bank/refs/heads/main/screenshots/fidor-bank-2026-07-25T214428.png
security:
- kind: authentication
  name: Fidor Bank Authentication
  slug: fidor-bank-authentication
  summary_line: oauth2 · 1 scheme
slug: fidor-bank
tags:
- Company
- Fintech
- Banking
- Banking as a Service
- Open Banking
- Digital Bank
- Neobank
- Germany
- Retired
---
