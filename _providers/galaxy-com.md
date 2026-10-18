---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.3
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Galaxy Com Agentic Access
  operation_count: 30
  slug: galaxy-com-agentic-access
  summary_line: 30 operations · 21 acting
api_count: 4
apis:
- description: The Ethereum API from Galaxy — 16 operation(s) for ethereum.
  name: Galaxy Ethereum API
  slug: galaxy-com-ethereum-api
- description: The Staking API responses will adhere to standard HTTP response conventions. Importantly, the staking platform performs business validations on all POST request messages to ensure that each request co
  name: Galaxy Solana API
  slug: galaxy-com-solana-api
artifact_total: 21
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/galaxy-com/refs/heads/main/agentic-access/galaxy-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/galaxy-com-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/galaxy-com/refs/heads/main/rules/galaxy-com-rules.yml
  title: ''
  type: Spectral
  url: rules/galaxy-com-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/galaxy-com/refs/heads/main/json-ld/galaxy-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/galaxy-com-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/galaxy-com/refs/heads/main/vocabulary/galaxy-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/galaxy-com-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/galaxy-com/refs/heads/main/data-model/galaxy-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/galaxy-com-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/galaxy-com/refs/heads/main/conventions/galaxy-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/galaxy-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/galaxy-com/refs/heads/main/conventions/galaxy-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/galaxy-com-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/galaxy-com/refs/heads/main/sandbox/galaxy-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/galaxy-com-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/galaxy-com/refs/heads/main/errors/galaxy-com-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/galaxy-com-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/galaxy-com/refs/heads/main/errors/galaxy-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/galaxy-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/galaxy-com/refs/heads/main/conformance/galaxy-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/galaxy-com-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/galaxy-com/refs/heads/main/well-known/galaxy-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/galaxy-com-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/galaxy-com/refs/heads/main/hosts/galaxy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/galaxy-com-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/galaxy-com/refs/heads/main/vendors/galaxy-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/galaxy-com-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/galaxy-com/refs/heads/main/authentication/galaxy-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/galaxy-com-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/galaxy-com/refs/heads/main/security/galaxy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/galaxy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.galaxy.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.galaxy.com/apis
- group: docs
  title: ''
  type: Documentation
  url: https://docs.staking.galaxy.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/galaxy-com/refs/heads/main/llms/galaxy-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/galaxy-com-llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://www.galaxy.com/get-started
- group: start
  title: ''
  type: Login
  url: https://www.galaxy.com/logins
- group: company
  title: ''
  type: Newsroom
  url: https://www.galaxy.com/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.galaxy.com/leadership
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.galaxy.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.galaxy.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.galaxy.com/insights
- group: other
  title: ''
  type: X
  url: https://twitter.com/GalaxyHQ
created: '2026-10-13'
description: Galaxy (Galaxy Digital) is a digital assets and data center infrastructure company offering institutional trading, lending, derivatives, prime services (GalaxyOne), custody, staking, tokenization, asset management and investment banking. Its APIs page lists OTC Trading, Prime Services (GalaxyOne Institutional) and Staking APIs; the Staking API is publicly documented at docs.staking.galaxy.com for Ethereum validator and Solana delegation operations, while the OTC, Prime and DeFi docs sit on access-controlled GitBook spaces.
image: https://images.ctfassets.net/f2k4wquz44by/463x5RWiljKDUDreKR2jBr/b63f3a1e75664639bb120e02663c68fc/galaxy.com.png?w=1200&h=675&fit=fill&q=60&fm=jpg&fl=progressive
json_schemas:
- name: DelegatorInfoListRequest
  property_count: 5
  slug: galaxy-com-delegator-info-list-request
- name: DelegatorInfoListResponse
  property_count: 4
  slug: galaxy-com-delegator-info-list-response
- name: DelegatorInfoResponse
  property_count: 7
  slug: galaxy-com-delegator-info-response
- name: DelegatorRewardsInfoResponse
  property_count: 6
  slug: galaxy-com-delegator-rewards-info-response
- name: Staking Response
  property_count: 9
  slug: galaxy-com-deposit-data-response
- name: Rewards Request
  property_count: 6
  slug: galaxy-com-eth-epoch-level-info-request
- name: SolValidatorInfoResponse
  property_count: 7
  slug: galaxy-com-sol-validator-info-response
- name: SOLDelegatorRewardsRequest
  property_count: 5
  slug: galaxy-com-soldelegator-rewards-request
- name: Staking Request
  property_count: 10
  slug: galaxy-com-staking-request
- name: Staking Response
  property_count: 9
  slug: galaxy-com-staking-response
- name: Validator Exit Request
  property_count: 7
  slug: galaxy-com-validator-exit-request
- name: Validator Info
  property_count: 19
  slug: galaxy-com-validator-info-response
jsonld:
- class_count: 78
  name: Galaxy Com Context
  property_count: 140
  slug: galaxy-com-context
layout: provider
modified: '2026-10-14'
name: Galaxy
nav: Providers
network: true
overview: 'Galaxy publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Ethereum API and Solana API. Tagged areas include Company, Cryptocurrency, Digital Assets, Staking, and Ethereum.


  The Galaxy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Galaxy''s developer surface includes sandbox, authentication, documentation, getting-started guide, engineering blog, and 23 more developer resources.'
plans:
- name: Galaxy Com Plans Pricing
  plan_count: 0
  slug: galaxy-com-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Galaxy Com Rate Limits
  slug: galaxy-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Galaxy API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: galaxy-com-rules
score:
  band: developing
  composite: 42.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 19.7
    contract_quality: 58.3
    developer_ergonomics: 52.4
    discoverability: 73.2
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Galaxy Com Authentication
  slug: galaxy-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Galaxy Com Domain Security
  slug: galaxy-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: galaxy-com
tags:
- Company
- Cryptocurrency
- Digital Assets
- Staking
- Ethereum
- Solana
- Trading
- Custody
- Financial Services
website: https://www.galaxy.com
---
