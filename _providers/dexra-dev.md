---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Solana DeFi intelligence API providing account, watches, tools and other data.
  name: Dexra API
  slug: dexra-api
- baseURL: https://api.dexra.dev
  baseurl_source: declared
  description: 'Solana DeFi intelligence for agents and bots: one call, one verdict. Send your API key as a bearer token, or pay per call over x402 without one. Docs: /docs on the cabinet site.'
  name: Dexra Api API
  slug: dexra-api-api
artifact_total: 7
asyncapis:
- description: ''
  name: Dexra Dev Webhooks
  slug: dexra-dev-webhooks
common:
- group: design
  href: https://artifacts.apis.io/dexra-dev/rules/dexra-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/dexra-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/dexra-dev/json-ld/dexra-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dexra-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/dexra-dev/vocabulary/dexra-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dexra-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dexra-dev/conformance/dexra-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dexra-dev-conformance.yml
- group: design
  href: https://artifacts.apis.io/dexra-dev/asyncapi/dexra-dev-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/dexra-dev-webhooks.yml
- group: design
  href: https://artifacts.apis.io/dexra-dev/data-model/dexra-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dexra-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/dexra-dev/errors/dexra-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dexra-dev-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/dexra-dev/llms/dexra-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dexra-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/dexra-dev/mcp/dexra-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dexra-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dexra-dev/well-known/dexra-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dexra-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/dexra-dev/hosts/dexra-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dexra-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/dexra-dev/vendors/dexra-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dexra-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/dexra-dev/packages/dexra-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/dexra-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/dexra-dev/packages/dexra-dev-packages.yml
  title: ''
  type: Packages
  url: packages/dexra-dev-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://dexra.dev/status
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dexra-dev
- group: start
  title: ''
  type: SignUp
  url: https://dexra.dev/signup
- group: start
  title: ''
  type: GettingStarted
  url: https://dexra.dev/docs/index
- group: docs
  title: ''
  type: APIReference
  url: https://dexra.dev/llms.txt
- group: auth
  href: https://artifacts.apis.io/dexra-dev/security/dexra-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dexra-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dexra.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://dexra.dev/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://dexra.dev/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dexra.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dexra.dev/privacy
created: '2026-11-05'
description: Dexra provides deep Solana due diligence for AI agents and trading bots, offering comprehensive checks on token launches, holders, wallets, pools, and swaps. The platform aggregates on-chain data into a single MCP or REST call, enabling automated risk assessment and integration for developers building trading bots or AI-driven finance tools.
image: https://dexra.dev/favicon.svg
jsonld:
- class_count: 1
  name: Dexra Dev Context
  property_count: 2
  slug: dexra-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.dexra.dev requiring an API key.
  name: Dexra MCP Server
  slug: dexra-dev-mcp-yml
modified: '2026-11-05'
name: Dexra
nav: Providers
network: true
overview: 'Dexra publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Api API, and 1 more. Tagged areas include Blockchain, Artificial Intelligence, Finance, Data, and Solana.


  The Dexra catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Dexra''s developer surface includes signup flow, getting-started guide, API reference, documentation, pricing, and 20 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Dexra API Rules
  rule_count: 59
  severity_counts:
    error: 56
    hint: 0
    info: 2
    warn: 1
  slug: dexra-dev-rules
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 45.5
    developer_ergonomics: 35.7
    discoverability: 65.0
    operational_transparency: 28.9
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dexra Dev Domain Security
  slug: dexra-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dexra-dev
tags:
- Blockchain
- Artificial Intelligence
- Finance
- Data
- Solana
website: https://dexra.dev/
---
