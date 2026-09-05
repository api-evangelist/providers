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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: REST API for cryptocurrency market data. JSON responses with Laravel-style pagination, HTTP Bearer auth, quota-based Free/Starter/Pro plans, and signed webhook deliveries. OpenAPI 3.0.3 contract.
  name: Bitculator Data API
  slug: bitculator-data-api
artifact_total: 7
asyncapis:
- description: ''
  name: Bitculator Webhooks
  slug: bitculator-webhooks
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitculator-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitculator-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/bitculator-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bitculator-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bitculator-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/bitculator-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bitculator-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/bitculator-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bitculator-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bitculator-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bitculator-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/bitculator-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bitculator-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bitculator-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bitculator-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bitculator-rate-limits.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bitculator
- group: commercial
  title: ''
  type: Pricing
  url: https://bitculator.com/en/crypto-api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bitculator.com/en/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bitculator.com/en/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://bitculator.com/en/contact
- group: start
  title: ''
  type: SignUp
  url: https://bitculator.com/en/register
created: '2026-07-05'
description: Modern cryptocurrency REST API providing programmatic read access to crypto market data including coins, prices, markets, exchanges, wallets, global market data, sentiment, indicators, liquidations, conversions, calculators, editorial content, alarms, and webhooks. Version 1.0.0 with 70+ endpoints across 15 groups.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bitculator.png
layout: provider
mcp_servers:
- description: 'Official hosted MCP server exposing the Bitculator Data API as 19 curated, read-only tools over Streamable HTTP. One key, one quota: every tool call counts as one Data API request against the plan''s m'
  name: Bitculator MCP Server
  slug: bitculator-mcp-server
modified: '2026-09-03'
name: Bitculator
nav: Providers
network: true
overview: 'Bitculator publishes 1 API on the [APIs.io](https://apis.io/) network: Data API. Tagged areas include Cryptocurrency, crypto-market-data, Blockchain, Finance, and Fintech.


  The Bitculator catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bitculator''s developer surface includes authentication, pricing, support, signup flow, and 19 more developer resources.'
plans:
- name: Bitculator Plans Pricing
  plan_count: 3
  slug: bitculator-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 6
  name: Bitculator Rate Limits
  slug: bitculator-rate-limits
score:
  band: developing
  composite: 49.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 47.0
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 44.7
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 49.3
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitculator/refs/heads/main/screenshots/bitculator-2026-07-25T203141.png
security:
- kind: authentication
  name: Bitculator Authentication
  slug: bitculator-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bitculator Domain Security
  slug: bitculator-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bitculator
tags:
- Cryptocurrency
- crypto-market-data
- Blockchain
- Finance
- Fintech
- Web3
- Trading
- Exchange Data
- Wallets
- Sentiment
- Indicators
---
