---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 26
  human_in_the_loop: 2
  name: Sochain Com Agentic Access
  operation_count: 100
  slug: sochain-com-agentic-access
  summary_line: 100 operations · 26 acting · 2 human-in-the-loop
api_count: 2
apis:
- description: Balances, transactions, blocks, mempool, prices and charts for Bitcoin, Litecoin, Dogecoin, Zcash and testnets.
  name: SoChain API
  slug: sochain-api
artifact_total: 21
asyncapis:
- description: ''
  name: Sochain Com Webhooks
  slug: sochain-com-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/sochain-com/rate-limits/sochain-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sochain-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/sochain-com/plans/sochain-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sochain-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/sochain-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/sochain-com/asyncapi/sochain-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/sochain-com-webhooks.yml
- group: build
  href: https://artifacts.apis.io/sochain-com/cli/sochain-com-cli.yml
  title: ''
  type: CLI
  url: cli/sochain-com-cli.yml
- group: operate
  href: https://artifacts.apis.io/sochain-com/changelog/sochain-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sochain-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/sochain-com/security/sochain-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/sochain-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sochain-com/authentication/sochain-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sochain-com-authentication.yml
- group: operate
  href: https://artifacts.apis.io/sochain-com/lifecycle/sochain-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/sochain-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/sochain-com/lifecycle/sochain-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sochain-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/sochain-com/conformance/sochain-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sochain-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sochain-com/llms/sochain-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sochain-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/sochain-com/mcp/sochain-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sochain-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/sochain-com/well-known/sochain-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sochain-com-security.txt
- group: auth
  href: https://artifacts.apis.io/sochain-com/well-known/sochain-com-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sochain-com-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/sochain-com/well-known/sochain-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sochain-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/sochain-com/hosts/sochain-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sochain-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/sochain-com/vendors/sochain-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sochain-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sochain.com/terms
- group: operate
  title: ''
  type: Support
  url: https://sochain.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sochain.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sochain.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://sochain.com/pricing
- group: start
  title: ''
  type: Login
  url: https://sochain.com/signin
- group: operate
  title: ''
  type: ChangeLog
  url: https://sochain.com/docs/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://sochain.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://dev.sochain.com/
- group: docs
  title: ''
  type: APIReference
  url: https://sochain.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/sochain-com/security/sochain-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sochain-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sochain-com/security/sochain-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sochain-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sochain.com/
created: '2026-10-31'
description: SoChain provides a blockchain explorer and API for Bitcoin, Litecoin, Dogecoin, and Zcash. Users can look up addresses, transactions, and blocks in real time, and developers can integrate blockchain data into applications via the SoChain API. The service offers comprehensive data access across multiple cryptocurrencies, supporting both web interfaces and programmatic access for building financial tools, analytics, and AI agents.
image: https://sochain.com/og/home.png
json_schemas:
- name: AccountInfo
  property_count: 5
  slug: sochain-com-account-info
- name: Block
  property_count: 33
  slug: sochain-com-block
- name: BucketSummary
  property_count: 16
  slug: sochain-com-bucket-summary
- name: NetworkInfo
  property_count: 4
  slug: sochain-com-network-info
- name: Transaction
  property_count: 23
  slug: sochain-com-transaction
- name: TransactionStatus
  property_count: 10
  slug: sochain-com-transaction-status
jsonld:
- class_count: 64
  name: Sochain Com Context
  property_count: 203
  slug: sochain-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at sochain.com.
  name: sochain-com MCP Server
  slug: sochain-com-mcp-yml
modified: '2026-10-31'
name: sochain-com
nav: Providers
network: true
overview: 'sochain-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain, Explorer, Bitcoin, Litecoin, and Dogecoin.


  The sochain-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  sochain-com''s developer surface includes CLI, changelog, authentication, support, pricing, getting-started guide, documentation, and 24 more developer resources.'
plans:
- name: Sochain Com Plans Pricing
  plan_count: 5
  slug: sochain-com-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Sochain Com Rate Limits
  slug: sochain-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: sochain-com API Rules
  rule_count: 16
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 4
  slug: sochain-com-rules
scopes:
- name: Sochain Com Scopes
  scope_count: 0
  slug: sochain-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 54.1
  coverage:
    artifact_dirs: 31
    catalog_earned: 72.5
    catalog_earned_first_party: 20.0
    catalog_gap: 42.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 59.1
    developer_ergonomics: 42.1
    discoverability: 65.0
    operational_transparency: 63.2
  previous_composite: 64.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sochain-com/sochain-com-2026-11-03T143439.png
security:
- kind: authentication
  name: Sochain Com Authentication
  slug: sochain-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Sochain Com Domain Security
  slug: sochain-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Sochain Com Vulnerability Disclosure
  slug: sochain-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: address-transactions
  slug: sochain-com-address-transactions
- name: balance-lookup
  slug: sochain-com-balance-lookup
- name: transaction-details
  slug: sochain-com-transaction-details
slug: sochain-com
tags:
- Blockchain
- Explorer
- Bitcoin
- Litecoin
- Dogecoin
- Zcash
website: https://sochain.com/
---
