---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Barnbridge Agentic Access
  operation_count: 48
  slug: barnbridge-agentic-access
  summary_line: 48 operations
api_count: 5
apis:
- description: BarnBridge DAO proposals, voting, and treasury
  name: BarnBridge Governance API
  slug: barnbridge-governance-api
- description: Price-volatility pools with upside exposure and downside protection
  name: BarnBridge SMART Alpha API
  slug: barnbridge-smart-alpha-api
- description: Automated token-ratio rebalancing tranches
  name: BarnBridge SMART Exposure API
  slug: barnbridge-smart-exposure-api
- description: Structured-product yield pools with senior/junior tranches
  name: BarnBridge SMART Yield API
  slug: barnbridge-smart-yield-api
- description: Staking-actions analytics and charts
  name: BarnBridge Yield Farming API
  slug: barnbridge-yield-farming-api
artifact_total: 15
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/barnbridge-agentic-access.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/barnbridge/refs/heads/main/json-ld/context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/barnbridge/refs/heads/main/json-schema/smart-yield-pool.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/barnbridge/refs/heads/main/json-schema/governance-proposal.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/barnbridge/refs/heads/main/json-schema/smart-alpha-pool.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/barnbridge/refs/heads/main/json-schema/smart-exposure-tranche.json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BarnBridge
- group: company
  title: ''
  type: Website
  url: https://barnbridge.com
- group: other
  title: ''
  type: Application
  url: https://app.barnbridge.com
- group: docs
  title: ''
  type: Documentation
  url: https://barnbridge.gitbook.io/docs
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/FfEhsVk
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/barn_bridge
- group: operate
  title: ''
  type: Forums
  url: https://forum.barnbridge.com
- group: other
  title: ''
  type: Whitepaper
  url: https://github.com/BarnBridge/BarnBridge-Whitepaper
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/barnbridge/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/barnbridge/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/barnbridge/refs/heads/main/finops/finops.yml
created: '2026-06-14'
description: BarnBridge is a risk tokenization DeFi protocol that allows users to hedge yield sensitivity and price volatility by transforming debt pools into structured products with varying risk and return characteristics. It offers SMART Yield bonds with junior and senior tranches, SMART Alpha for price volatility management, SMART Exposure for automated rebalancing, and yield farming analytics via a REST API.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/barnbridge.png
json_schemas:
- name: GovernanceProposal
  property_count: 9
  slug: governance-proposal
- name: SmartAlphaPool
  property_count: 14
  slug: smart-alpha-pool
- name: SmartExposureTranche
  property_count: 11
  slug: smart-exposure-tranche
- name: SmartYieldPool
  property_count: 14
  slug: smart-yield-pool
jsonld:
- class_count: 87
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-06-14'
name: BarnBridge
nav: Providers
network: true
overview: 'BarnBridge publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Governance API, SMART Alpha API, SMART Exposure API, and 2 more. Tagged areas include DeFi, Risk Tokenization, Yield, Blockchain, and Ethereum.


  The BarnBridge catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BarnBridge''s developer surface includes documentation and 16 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 20
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: BarnBridge API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: barnbridge-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 55.0
    developer_ergonomics: 8.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 5.3
  previous_composite: 40.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/barnbridge/refs/heads/main/screenshots/barnbridge-2026-06-20T173007.png
slug: barnbridge
tags:
- DeFi
- Risk Tokenization
- Yield
- Blockchain
- Ethereum
- SMART Yield
- Structured Products
- Tranches
website: https://barnbridge.com
---
