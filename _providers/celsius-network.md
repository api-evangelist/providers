---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.7
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Celsius Network Agentic Access
  operation_count: 24
  slug: celsius-network-agentic-access
  summary_line: 24 operations · 7 acting
api_count: 1
apis:
- description: 'The partner-facing wallet and earning API for the Celsius Network platform, also called the Wallet API. 21 paths and 24 operations across four tags — Wallet (balances, accrued interest, transactions, '
  name: Celsius Partner API
  slug: partner-api
artifact_total: 5
collections:
- collection_type: postman
  name: Celsius API
  slug: postman-celsius-network-partner-api
common:
- group: company
  title: ''
  type: Website
  url: https://celsius.network/
- group: docs
  title: ''
  type: Documentation
  url: https://www.postman.com/labs-celsiusnet-decents/celsius-public/documentation/tsw6j4r/celsius-api
- group: docs
  title: ''
  type: APIReference
  url: https://documenter.getpostman.com/view/4207695/Rzn6v2mZ
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/labs-celsiusnet-decents/workspace/celsius-public/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CelsiusNetwork
- group: operate
  title: ''
  type: Support
  url: https://celsiusdistribution.stretto.com/support/solutions
- group: start
  title: ''
  type: Login
  url: https://claimsportal.celsius.network
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://celsius.network/static/privacy-policy.pdf
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/celsius-network-partner-api-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/celsius-network-partner-api-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/celsius-network-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/celsius-network-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/celsius-network-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/celsius-network-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/celsius-network-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/celsius-network-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/celsius-network-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/celsius-network-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://celsius.network/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/celsius-network-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/celsius-network-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/celsius-network-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/celsius-network-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/celsius-network-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/celsius-network-domain-security.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/celsius-network_stock/
created: '2026-08-02'
description: 'Celsius Network LLC was a global cryptocurrency lending, custody and yield platform, founded in 2017, that let retail and institutional customers earn interest on crypto deposits, borrow US dollars and stablecoins against their holdings, and — through the Celsius Partner API — let third-party partners embed that earning power directly into their own applications. The Partner (Wallet) API exposed per-coin balances, accrued interest, transaction history, deposit addresses, withdrawals, KYC verification and utility reference data across three partnership models: Omnibus Integration, Omnibus Treasury, and Segmented Integration, where the partner created and managed a Celsius wallet for each of its own end users. Celsius froze withdrawals on 2022-06-12, filed for Chapter 11 bankruptcy on 2022-07-13, had its plan of reorganization confirmed on 2023-11-09, emerged on 2024-01-31 and shut down its mobile and web applications on 2024-02-29 as part of the wind-down of its business operations.
  The Partner API and the developer portal are retired and their hosts no longer resolve. The reorganized bitcoin-mining business was spun out as Ionic Digital, a separate company that listed on Nasdaq under IOND on 2026-07-28. This profile preserves the API contract as a historical record, derived entirely from first-party artifacts that are still publicly resolvable.'
image: https://celsius.network/_next/static/media/blue_logo.6966df1d.svg
layout: provider
modified: '2026-08-02'
name: Celsius Network
nav: Providers
network: true
overview: 'Celsius Network publishes 1 API on the [APIs.io](https://apis.io/) network: Celsius Partner API. Tagged areas include Company, Cryptocurrency, Digital Assets, Financial Services, and Lending.


  Celsius Network''s developer surface includes documentation, API reference, support, authentication, changelog, sandbox, and 21 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 43.6
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 68.2
    developer_ergonomics: 49.5
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 43.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 32.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Celsius Network Authentication
  slug: celsius-network-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Celsius Network Domain Security
  slug: celsius-network-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: celsius-network
tags:
- Company
- Cryptocurrency
- Digital Assets
- Financial Services
- Lending
- Custody
- Wallet
- Interest
- KYC
- Retired
website: https://celsius.network/
---
