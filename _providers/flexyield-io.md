---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: unknown
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Flexyield Io Agentic Access
  operation_count: 18
  slug: flexyield-io-agentic-access
  summary_line: 18 operations · 6 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://flexyield.io
  baseurl_source: declared
  description: The Agents API from flexyield-io — 1 operation(s) for agents.
  name: flexyield-io Agents API
  slug: flexyield-io-agents-api
- baseURL: https://flexyield.io
  baseurl_source: declared
  description: The Data API from flexyield-io — 2 operation(s) for data.
  name: flexyield-io Data API
  slug: flexyield-io-data-api
- baseURL: https://flexyield.io
  baseurl_source: declared
  description: The Keys API from flexyield-io — 3 operation(s) for keys.
  name: flexyield-io Keys API
  slug: flexyield-io-keys-api
- baseURL: https://flexyield.io
  baseurl_source: declared
  description: The Rpc API from flexyield-io — 1 operation(s) for rpc.
  name: flexyield-io Rpc API
  slug: flexyield-io-rpc-api
- baseURL: https://flexyield.io
  baseurl_source: declared
  description: The Statements API from flexyield-io — 2 operation(s) for statements.
  name: flexyield-io Statements API
  slug: flexyield-io-statements-api
- baseURL: https://flexyield.io
  baseurl_source: declared
  description: The Toolbox API from flexyield-io — 7 operation(s) for toolbox.
  name: flexyield-io Toolbox API
  slug: flexyield-io-toolbox-api
- baseURL: https://flexyield.io
  baseurl_source: declared
  description: The X402 API from flexyield-io — 2 operation(s) for x402.
  name: flexyield-io X402 API
  slug: flexyield-io-x402-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/flexyield-io/agentic-access/flexyield-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/flexyield-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/flexyield-io/plans/flexyield-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flexyield-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/flexyield-io/rules/flexyield-io-rules.yml
  title: ''
  type: Spectral
  url: rules/flexyield-io-rules.yml
- group: design
  href: https://artifacts.apis.io/flexyield-io/json-ld/flexyield-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/flexyield-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/flexyield-io/vocabulary/flexyield-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/flexyield-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/flexyield-io/data-model/flexyield-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/flexyield-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/flexyield-io/changelog/flexyield-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/flexyield-io-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://flexyield.io/terms
- group: build
  href: https://artifacts.apis.io/flexyield-io/errors/flexyield-io-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/flexyield-io-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/flexyield-io/errors/flexyield-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/flexyield-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/flexyield-io/conformance/flexyield-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/flexyield-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/flexyield-io/llms/flexyield-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flexyield-io-llms.txt
- group: other
  href: https://artifacts.apis.io/flexyield-io/a2a/flexyield-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/flexyield-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/flexyield-io/mcp/flexyield-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/flexyield-io-mcp.yml
- group: auth
  href: https://artifacts.apis.io/flexyield-io/well-known/flexyield-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/flexyield-io-security.txt
- group: auth
  href: https://artifacts.apis.io/flexyield-io/well-known/flexyield-io-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/flexyield-io-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/flexyield-io/well-known/flexyield-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/flexyield-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/flexyield-io/hosts/flexyield-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flexyield-io-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://flexyield.io/status
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.flexyield.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://flexyield.io/changelog
- group: auth
  href: https://artifacts.apis.io/flexyield-io/authentication/flexyield-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/flexyield-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/flexyield-io/security/flexyield-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/flexyield-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/flexyield-io/security/flexyield-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flexyield-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flexyield.io/
- group: docs
  title: ''
  type: Documentation
  url: https://flexyield.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://flexyield.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://flexyield.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://flexyield.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flexyield.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flexyield.io/privacy
- group: operate
  title: ''
  type: Roadmap
  url: https://flexyield.io/roadmap
- group: operate
  title: ''
  type: Support
  url: https://flexyield.io/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/1909-Works/flexyield-io
created: '2026-10-30'
description: FlexYield provides a unified API gateway that aggregates JSON-RPC traffic across multiple blockchain providers, offering automatic failover, a single billing meter, and support for several major chains including Ethereum, Base, Arbitrum, Optimism, Polygon, and Solana. Users can start for free without a wallet or crypto, access a toolbox of utilities, and view real-time uptime and performance metrics. The platform aims to simplify blockchain integration by consolidating endpoints, reducing complexity, and delivering transparent pricing.
image: https://flexyield.io/og.png
json_schemas:
- name: JsonRpcRequest
  property_count: 4
  slug: flexyield-io-json-rpc-request
- name: JsonRpcResponse
  property_count: 4
  slug: flexyield-io-json-rpc-response
jsonld:
- class_count: 3
  name: Flexyield Io Context
  property_count: 6
  slug: flexyield-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at flexyield.io.
  name: flexyield-io MCP Server
  slug: flexyield-io-mcp-yml
modified: '2026-10-30'
name: flexyield-io
nav: Providers
network: true
overview: 'flexyield-io publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Data API, Keys API, and 4 more. Tagged areas include Blockchain, API Gateway, Unified Billing, Multi-Chain, and Free Tier.


  The flexyield-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  flexyield-io''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, support, and 27 more developer resources.'
plans:
- name: Flexyield Io Plans Pricing
  plan_count: 6
  slug: flexyield-io-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: flexyield-io API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 2
  slug: flexyield-io-rules
score:
  band: strong
  composite: 61.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 82.5
    catalog_earned_first_party: 0.0
    catalog_gap: 32.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 79.1
    contract_quality: 52.9
    developer_ergonomics: 54.8
    discoverability: 65.0
    operational_transparency: 52.6
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Flexyield Io Authentication
  slug: flexyield-io-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Flexyield Io Domain Security
  slug: flexyield-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Flexyield Io Vulnerability Disclosure
  slug: flexyield-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: flexyield-io
tags:
- Blockchain
- API Gateway
- Unified Billing
- Multi-Chain
- Free Tier
website: https://flexyield.io/
---
