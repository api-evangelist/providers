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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-08-19'
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
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BarnBridge Governance API
  slug: open-barnbridge-governance-api
- collection_type: open
  name: BarnBridge Governance SMART Alpha API
  slug: open-barnbridge-smart-alpha-api
- collection_type: open
  name: BarnBridge Governance SMART Exposure API
  slug: open-barnbridge-smart-exposure-api
- collection_type: open
  name: BarnBridge Governance SMART Yield API
  slug: open-barnbridge-smart-yield-api
- collection_type: open
  name: BarnBridge Governance Yield Farming API
  slug: open-barnbridge-yield-farming-api
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
random_paper: 146
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: BarnBridge API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: barnbridge-jsonschema-spectral-rules
score:
  band: thin
  composite: 30.6
  delta: -6.8
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 52.0
    developer_ergonomics: 14.3
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 2.6
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
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
