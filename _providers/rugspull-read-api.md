---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 57.4
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Rugspull Read Api Agentic Access
  operation_count: 9
  slug: rugspull-read-api-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- description: Nine GET-only endpoints providing service health, chain config, indexer status, discovery cache, indexed events, event-derived market data, sparklines, and immutable metadata objects. Backed by a publ
  name: Rugspull Read API
  slug: rugspull-read-api
artifact_total: 7
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rugspull-read-api-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rugspull-read-api-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rugspull-read-api-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/pqchase/rugspull/blob/main/docs/INTEGRATION.md
- group: docs
  title: ''
  type: APIReference
  url: https://rugspull.com/api-reference
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/pqchase/rugspull/blob/main/docs/INTEGRATION.md
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/pqchase/rugspull/blob/main/docs/INTEGRATION.md#read-the-public-cache
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pqchase/rugspull
- group: operate
  title: ''
  type: Support
  url: https://github.com/pqchase/rugspull/issues
- group: build
  title: ''
  type: Postman
  url: collections/rugspull-read-api.postman_collection.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rugspull-read-api-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rugspull-read-api-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/rugspull-read-api-api-catalog.json
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/rugspull-read-api-security.txt
- group: auth
  title: ''
  type: Security
  url: security/rugspull-read-api-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rugspull-read-api-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rugspull-read-api-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/rugspull-read-api-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rugspull-read-api-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rugspull-read-api-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rugspull-read-api-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rugspull-read-api-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/rugspull-read-api-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rugspull-read-api-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/rugspull-read-api-plans-pricing.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rugspull-read-api-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/rugspull-read-api-examples.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/rugspull-read-api-read-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-19'
description: A read-only, GET-only discovery-cache REST API for Rugspull, a self-described high-risk parody DeFi protocol on BNB Smart Chain (chain id 56). Exposes rebuildable discovery/indexed-event data with no write, settlement, or transaction-proxy operations; on-chain BSC contracts remain the source of financial truth. Unauthenticated, free, best-effort, with no published rate limits or SLA.
image: https://rugspull.com/assets/og-mechanism.png
layout: provider
modified: '2026-08-11'
name: Rugspull Read API
nav: Providers
network: true
overview: 'Rugspull Read API publishes 1 API on the [APIs.io](https://apis.io/) network: Rugspull Read API. Tagged areas include bnb-smart-chain, bsc, wbnb, read-only, and openapi.


  Rugspull Read API''s developer surface includes documentation, API reference, getting-started guide, support, authentication, changelog, code examples, and 22 more developer resources.'
plans:
- name: Rugspull Read Api Plans Pricing
  plan_count: 0
  slug: rugspull-read-api-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 0
  name: Rugspull Read Api Rate Limits
  slug: rugspull-read-api-rate-limits
score:
  band: thin
  composite: 35.6
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 32.3
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 31.6
  previous_composite: 35.6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Rugspull Read Api Authentication
  slug: rugspull-read-api-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Rugspull Read Api Domain Security
  slug: rugspull-read-api-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Rugspull Read Api Vulnerability Disclosure
  slug: rugspull-read-api-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: rugspull-read-api
tags:
- bnb-smart-chain
- bsc
- wbnb
- read-only
- openapi
- high-risk
- discovery-cache
- defi
- web3
- crypto-market-data
- indexer
---
