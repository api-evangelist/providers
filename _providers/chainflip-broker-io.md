---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Chainflip Broker Io Agentic Access
  operation_count: 19
  slug: chainflip-broker-io-agentic-access
  summary_line: 19 operations · 2 acting
api_count: 1
apis:
- baseURL: /
  baseurl_source: spec
  description: 'The assets you can swap: their ids, decimals, minimum swap amounts, USD prices and logos. No key needed.'
  name: Chainflip Broker as a Service Assets API
  slug: chainflip-broker-io-assets-api
- baseURL: /
  baseurl_source: spec
  description: The broker fees you have earned.
  name: Chainflip Broker as a Service Fees API
  slug: chainflip-broker-io-fees-api
- baseURL: /
  baseurl_source: spec
  description: The networks you can swap on, and their logos. No key needed.
  name: Chainflip Broker as a Service Networks API
  slug: chainflip-broker-io-networks-api
- baseURL: /
  baseurl_source: spec
  description: 'How to start: what works without a key, how to get one, the sandbox and a first call.'
  name: Chainflip Broker as a Service Onboarding API
  slug: chainflip-broker-io-onboarding-api
- baseURL: /
  baseurl_source: spec
  description: 'Quotes for a swap: the expected output, every fee, and Chainflip''s recommended slippage protection, retry window and live price protection. Ask for one before starting a swap.'
  name: Chainflip Broker as a Service Quote API
  slug: chainflip-broker-io-quote-api
- baseURL: /
  baseurl_source: spec
  description: 'A Chainflip broker JSON-RPC endpoint for the Chainflip SDK and other broker clients: point their broker URL at it and the deposit channels and vault swaps they open earn your commission.'
  name: Chainflip Broker as a Service Rpc API
  slug: chainflip-broker-io-rpc-api
- baseURL: /
  baseurl_source: spec
  description: Follow a swap, from waiting for the deposit to completed or failed, looked up by BaaS swap id, deposit channel or deposit transaction.
  name: Chainflip Broker as a Service Status API
  slug: chainflip-broker-io-status-api
- baseURL: /
  baseurl_source: spec
  description: 'Start a swap: open a deposit channel that the source asset is sent to.'
  name: Chainflip Broker as a Service Swap API
  slug: chainflip-broker-io-swap-api
- baseURL: /
  baseurl_source: spec
  description: 'The swaps made through your broker: a filterable list, and a feed of completed swaps for processing each one exactly once.'
  name: Chainflip Broker as a Service Swaps API
  slug: chainflip-broker-io-swaps-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/chainflip-broker-io/agentic-access/chainflip-broker-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/chainflip-broker-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/chainflip-broker-io/plans/chainflip-broker-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chainflip-broker-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/chainflip-broker-io/rules/chainflip-broker-io-rules.yml
  title: ''
  type: Spectral
  url: rules/chainflip-broker-io-rules.yml
- group: design
  href: https://artifacts.apis.io/chainflip-broker-io/json-ld/chainflip-broker-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/chainflip-broker-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/chainflip-broker-io/vocabulary/chainflip-broker-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chainflip-broker-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/chainflip-broker-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/chainflip-broker-io/data-model/chainflip-broker-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chainflip-broker-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/chainflip-broker-io/changelog/chainflip-broker-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/chainflip-broker-io-changelog.yml
- group: start
  href: https://artifacts.apis.io/chainflip-broker-io/sandbox/chainflip-broker-io-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/chainflip-broker-io-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/chainflip-broker-io/security/chainflip-broker-io-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/chainflip-broker-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/chainflip-broker-io/authentication/chainflip-broker-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chainflip-broker-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/chainflip-broker-io/errors/chainflip-broker-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/chainflip-broker-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/chainflip-broker-io/conformance/chainflip-broker-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chainflip-broker-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chainflip-broker-io/llms/chainflip-broker-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chainflip-broker-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/chainflip-broker-io/mcp/chainflip-broker-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/chainflip-broker-io-mcp.yml
- group: auth
  href: https://artifacts.apis.io/chainflip-broker-io/well-known/chainflip-broker-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chainflip-broker-io-security.txt
- group: agent
  href: https://artifacts.apis.io/chainflip-broker-io/well-known/chainflip-broker-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chainflip-broker-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/chainflip-broker-io/hosts/chainflip-broker-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chainflip-broker-io-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chainflip-broker.io/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.chainflip-broker.io/changelog/
- group: start
  title: ''
  type: SignUp
  url: https://chainflip-broker.io/register
- group: start
  title: ''
  type: GettingStarted
  url: https://chainflip-broker.io/onboarding
- group: auth
  href: https://artifacts.apis.io/chainflip-broker-io/security/chainflip-broker-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/chainflip-broker-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/chainflip-broker-io/security/chainflip-broker-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chainflip-broker-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chainflip-broker.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chainflip-broker.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.chainflip-broker.io/resources/api-documentation/
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.chainflip-broker.io/resources/pricing/
- group: operate
  title: ''
  type: Support
  url: https://docs.chainflip-broker.io/resources/contact/
created: '2026-11-03'
description: Chainflip Broker as a Service (BaaS) enables users to run a Chainflip broker without managing infrastructure. It offers fully managed broker infrastructure, commission protection, automatic updates, DCA swaps, boosted deposits, and a REST API plus MCP server for AI agents. Pricing includes a 0.05% operating fee per swap with optional broker fees. The platform targets DeFi participants seeking seamless cross-chain swaps and liquidity provisioning.
image: https://chainflip-broker.io/img/social-card.jpg
json_schemas:
- name: ChainflipBaas.Fees.FeesResponse
  property_count: 3
  slug: chainflip-broker-io-chainflip-baas-fees-fees-response
- name: ChainflipBaas.Infrastructure.Http.OnboardingDocument
  property_count: 9
  slug: chainflip-broker-io-chainflip-baas-infrastructure-http-onboarding-document
- name: ChainflipBaas.Quote.Quote
  property_count: 23
  slug: chainflip-broker-io-chainflip-baas-quote-quote
- name: ChainflipBaas.Status.StatusResponse
  property_count: 3
  slug: chainflip-broker-io-chainflip-baas-status-status-response
- name: ChainflipBaas.Swap.DepositAddress
  property_count: 10
  slug: chainflip-broker-io-chainflip-baas-swap-deposit-address
- name: ChainflipBaas.SwapsFeed.FeedStatusResponse
  property_count: 4
  slug: chainflip-broker-io-chainflip-baas-swaps-feed-feed-status-response
jsonld:
- class_count: 41
  name: Chainflip Broker Io Context
  property_count: 193
  slug: chainflip-broker-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at chainflip-broker.io.
  name: Chainflip Broker as a Service MCP Server
  slug: chainflip-broker-io-mcp-yml
modified: '2026-11-03'
name: Chainflip Broker as a Service
nav: Providers
network: true
overview: 'Chainflip Broker as a Service publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Assets API, Fees API, Networks API, and 6 more. Tagged areas include Finance, DeFi, Cryptocurrency, Brokerage, and Infrastructure.


  The Chainflip Broker as a Service catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Chainflip Broker as a Service''s developer surface includes changelog, sandbox, authentication, signup flow, getting-started guide, documentation, API reference, and 22 more developer resources.'
plans:
- name: Chainflip Broker Io Plans Pricing
  plan_count: 1
  slug: chainflip-broker-io-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Chainflip Broker as a Service API Rules
  rule_count: 60
  severity_counts:
    error: 50
    hint: 0
    info: 3
    warn: 7
  slug: chainflip-broker-io-rules
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 38.2
    contract_governance: 22.0
    contract_quality: 58.6
    developer_ergonomics: 42.1
    discoverability: 56.7
    operational_transparency: 18.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Chainflip Broker Io Authentication
  slug: chainflip-broker-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Chainflip Broker Io Domain Security
  slug: chainflip-broker-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Chainflip Broker Io Vulnerability Disclosure
  slug: chainflip-broker-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: chainflip-broker-io
tags:
- Finance
- DeFi
- Cryptocurrency
- Brokerage
- Infrastructure
- Company
website: https://chainflip-broker.io/
---
