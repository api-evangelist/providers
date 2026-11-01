---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 67.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 26
  human_in_the_loop: 2
  name: Sochain Com Agentic Access
  operation_count: 100
  slug: sochain-com-agentic-access
  summary_line: 100 operations · 26 acting · 2 human-in-the-loop
api_count: 2
apis:
- baseURL: https://sochain.com/api/v3
  baseurl_source: declared
  description: The Account API from sochain-com — 2 operation(s) for account.
  name: sochain-com Account API
  slug: sochain-com-account-api
- baseURL: https://sochain.com/api/v3
  baseurl_source: declared
  description: The Addresses API from sochain-com — 12 operation(s) for addresses.
  name: sochain-com Addresses API
  slug: sochain-com-addresses-api
- baseURL: https://sochain.com/api/v3
  baseurl_source: declared
  description: The Blocks API from sochain-com — 3 operation(s) for blocks.
  name: sochain-com Blocks API
  slug: sochain-com-blocks-api
- baseURL: https://sochain.com/api/v3
  baseurl_source: declared
  description: The Buckets API from sochain-com — 11 operation(s) for buckets.
  name: sochain-com Buckets API
  slug: sochain-com-buckets-api
- baseURL: https://sochain.com/api/v3
  baseurl_source: declared
  description: The Charts API from sochain-com — 1 operation(s) for charts.
  name: sochain-com Charts API
  slug: sochain-com-charts-api
- baseURL: https://sochain.com/api/v3
  baseurl_source: declared
  description: The Network & price API from sochain-com — 4 operation(s) for network & price.
  name: sochain-com Network & price API
  slug: sochain-com-network-price-api
- baseURL: https://sochain.com/api/v3
  baseurl_source: declared
  description: The SoChain API API from sochain-com — 1 operation(s) for sochain api.
  name: sochain-com SoChain API
  slug: sochain-com-sochain-api-api
- baseURL: https://sochain.com/api/v3
  baseurl_source: declared
  description: The Transactions API from sochain-com — 2 operation(s) for transactions.
  name: sochain-com Transactions API
  slug: sochain-com-transactions-api
- baseURL: https://sochain.com/api/v3
  baseurl_source: declared
  description: The Webhooks API from sochain-com — 6 operation(s) for webhooks.
  name: sochain-com Webhooks API
  slug: sochain-com-webhooks-api
artifact_total: 29
asyncapis:
- description: ''
  name: Sochain Com Webhooks
  slug: sochain-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/sochain-com/agentic-access/sochain-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sochain-com-agentic-access.yml
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
- group: design
  href: https://artifacts.apis.io/sochain-com/rules/sochain-com-rules.yml
  title: ''
  type: Spectral
  url: rules/sochain-com-rules.yml
- group: design
  href: https://artifacts.apis.io/sochain-com/json-ld/sochain-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sochain-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/sochain-com/vocabulary/sochain-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sochain-com-vocabulary.yml
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
- group: design
  href: https://artifacts.apis.io/sochain-com/data-model/sochain-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sochain-com-data-model.yml
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
- group: design
  href: https://artifacts.apis.io/sochain-com/conventions/sochain-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sochain-com-conventions.yml
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
- group: design
  href: https://artifacts.apis.io/sochain-com/errors/sochain-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sochain-com-problem-types.yml
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
- group: build
  href: https://artifacts.apis.io/sochain-com/mcp/sochain-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/sochain-com-tool-crosswalk.yml
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
- group: build
  href: https://artifacts.apis.io/sochain-com/packages/sochain-com-packages.yml
  title: ''
  type: SDKs
  url: packages/sochain-com-packages.yml
- group: build
  href: https://artifacts.apis.io/sochain-com/packages/sochain-com-packages.yml
  title: ''
  type: Packages
  url: packages/sochain-com-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sochain.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.sochain.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://sochain.com/docs/changelog
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
- group: docs
  title: ''
  type: Documentation
  url: https://sochain.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://sochain.com/api/v3/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://sochain.com/docs
- group: operate
  title: ''
  type: Support
  url: https://sochain.com/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BlockIo
- group: commercial
  title: ''
  type: Pricing
  url: https://sochain.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://sochain.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sochain.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sochain.com/privacy
created: '2026-10-31'
description: SoChain provides a blockchain explorer and a robust API for querying Bitcoin, Litecoin, Dogecoin, and Zcash networks. Users can retrieve address balances, transaction details, block information, and price data. The platform offers both free and paid plans, with rate limits and API keys for higher usage. Documentation includes quickstart guides, authentication details, and SDKs, enabling developers to integrate cryptocurrency data into applications, services, and AI agents.
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
overview: 'sochain-com publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Addresses API, Blocks API, and 6 more. Tagged areas include Company, Blockchain, Explorer, API, and Cryptocurrency.


  The sochain-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  sochain-com''s developer surface includes CLI, changelog, authentication, documentation, API reference, getting-started guide, support, and 34 more developer resources.'
plans:
- name: Sochain Com Plans Pricing
  plan_count: 5
  slug: sochain-com-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 6
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
  band: exemplar
  composite: 77.2
  coverage:
    artifact_dirs: 28
    catalog_earned: 99.3
    catalog_earned_first_party: 0.0
    catalog_gap: 15.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 67.2
    developer_ergonomics: 75.5
    discoverability: 65.0
    operational_transparency: 83.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Sochain Com Authentication
  slug: sochain-com-authentication
  summary_line: 2 schemes
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
- Company
- Blockchain
- Explorer
- API
- Cryptocurrency
- Finance
website: https://sochain.com/
---
