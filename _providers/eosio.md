---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Eosio Agentic Access
  operation_count: 10
  slug: eosio-agentic-access
  summary_line: 10 operations · 9 acting
api_count: 13
apis:
- description: The history_api_plugin exposes endpoints under /v1/history for retrieving historical actions, transactions, key accounts, and controlled accounts. On modern Antelope deployments this is typically repl
  name: EOSIO Nodeos History API
  slug: nodeos-history-api
- description: The producer_api_plugin exposes endpoints under /v1/producer for controlling block production on a node, including pause, resume, schedule snapshots, and manage protocol features. Restricted to operat
  name: EOSIO Nodeos Producer API
  slug: nodeos-producer-api
- description: The net_api_plugin exposes endpoints under /v1/net for inspecting and managing peer-to-peer connections of an Antelope node, including connections, status, connect, and disconnect operations.
  name: EOSIO Nodeos Net API
  slug: nodeos-net-api
- description: The Get Abi API from EOSIO — 1 operation(s) for get abi.
  name: EOSIO Get Abi API
  slug: eosio-get-abi-api
- description: The Get Account API from EOSIO — 1 operation(s) for get account.
  name: EOSIO Get Account API
  slug: eosio-get-account-api
- description: The Get Block API from EOSIO — 1 operation(s) for get block.
  name: EOSIO Get Block API
  slug: eosio-get-block-api
- description: The Get Code API from EOSIO — 1 operation(s) for get code.
  name: EOSIO Get Code API
  slug: eosio-get-code-api
- description: The Get Currency Balance API from EOSIO — 1 operation(s) for get currency balance.
  name: EOSIO Get Currency Balance API
  slug: eosio-get-currency-balance-api
- description: The Get Info API from EOSIO — 1 operation(s) for get info.
  name: EOSIO Get Info API
  slug: eosio-get-info-api
- description: The Get Required Keys API from EOSIO — 1 operation(s) for get required keys.
  name: EOSIO Get Required Keys API
  slug: eosio-get-required-keys-api
- description: The Get Table Rows API from EOSIO — 1 operation(s) for get table rows.
  name: EOSIO Get Table Rows API
  slug: eosio-get-table-rows-api
- description: The Push Transaction API from EOSIO — 1 operation(s) for push transaction.
  name: EOSIO Push Transaction API
  slug: eosio-push-transaction-api
- description: The Send Transaction API from EOSIO — 1 operation(s) for send transaction.
  name: EOSIO Send Transaction API
  slug: eosio-send-transaction-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: EOSIO / Antelope Nodeos Chain Get Abi API
  slug: open-eosio-get-abi-api
- collection_type: open
  name: EOSIO / Antelope Nodeos Chain Get Abi Get Account API
  slug: open-eosio-get-account-api
- collection_type: open
  name: EOSIO / Antelope Nodeos Chain Get Abi Get Block API
  slug: open-eosio-get-block-api
- collection_type: open
  name: EOSIO / Antelope Nodeos Chain Get Abi Get Code API
  slug: open-eosio-get-code-api
- collection_type: open
  name: EOSIO / Antelope Nodeos Chain Get Abi Get Currency Balance API
  slug: open-eosio-get-currency-balance-api
- collection_type: open
  name: EOSIO / Antelope Nodeos Chain Get Abi Get Info API
  slug: open-eosio-get-info-api
- collection_type: open
  name: EOSIO / Antelope Nodeos Chain Get Abi Get Required Keys API
  slug: open-eosio-get-required-keys-api
- collection_type: open
  name: EOSIO / Antelope Nodeos Chain Get Abi Get Table Rows API
  slug: open-eosio-get-table-rows-api
- collection_type: open
  name: EOSIO / Antelope Nodeos Chain API
  slug: open-eosio-nodeos-chain-api
- collection_type: open
  name: EOSIO / Antelope Nodeos Chain Get Abi Push Transaction API
  slug: open-eosio-push-transaction-api
- collection_type: open
  name: EOSIO / Antelope Nodeos Chain Get Abi Send Transaction API
  slug: open-eosio-send-transaction-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/AntelopeIO/leap/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/AntelopeIO/leap/blob/main/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eosio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eosio-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eosio
- group: company
  title: ''
  type: Website
  url: https://eosnetwork.com/
- group: start
  title: ''
  type: Portal
  url: https://developers.eos.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.eos.io/welcome/latest/getting-started-guide/index
- group: learn
  title: ''
  type: Tutorials
  url: https://developers.eos.io/welcome/latest/tutorials/index
- group: docs
  title: ''
  type: Documentation
  url: https://developers.eos.io/welcome/latest/reference/index
- group: operate
  title: ''
  type: FAQ
  url: https://developers.eos.io/welcome/latest/faq/index
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AntelopeIO
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/AntelopeIO/leap
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/AntelopeIO/leap/releases
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://eos.io/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://eos.io/legal/terms-of-use/
created: '2025-02-08'
description: EOSIO, now known as the Antelope protocol, is a free, open-source blockchain software protocol that provides developers and entrepreneurs with a platform on which to build, deploy, and run high-performing blockchain applications. Reference node software (nodeos) exposes HTTP/JSON RPC plugins for chain reads, history queries, transaction submission, and producer operations.
finops:
- name: Eosio Finops
  service_category: Blockchain Infrastructure
  slug: eosio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eosio.png
layout: provider
modified: '2026-05-19'
name: EOSIO
nav: Providers
network: true
overview: 'EOSIO publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Get Abi API, Get Account API, Get Block API, and 7 more. Tagged areas include Antelope, Blockchain, and EOS.


  EOSIO''s developer surface includes developer portal, getting-started guide, documentation, FAQ, changelog, and 11 more developer resources.'
plans:
- name: Eosio Plans Pricing
  plan_count: 2
  slug: eosio-plans-pricing
random_paper: 96
rate_limits:
- limit_count: 3
  name: Eosio Rate Limits
  slug: eosio-rate-limits
score:
  band: thin
  composite: 33.6
  delta: -1.2
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 48.7
    developer_ergonomics: 26.2
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 34.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Eosio Domain Security
  slug: eosio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: eosio
tags:
- Antelope
- Blockchain
- EOS
website: https://eosnetwork.com/
---
