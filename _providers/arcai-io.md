---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: MCP server providing token risk scans, AI reports, live signals, and whale flow data.
  name: ARC AI MCP
  slug: arc-ai-mcp
- description: 'ARC AI API as documented publicly: 10 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: ARC AI API
  slug: arcai-io-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/arcai-io/rules/arcai-io-rules.yml
  title: ''
  type: Spectral
  url: rules/arcai-io-rules.yml
- group: design
  href: https://artifacts.apis.io/arcai-io/json-ld/arcai-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/arcai-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/arcai-io/vocabulary/arcai-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/arcai-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/arcai-io/data-model/arcai-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/arcai-io-data-model.yml
- group: auth
  href: https://artifacts.apis.io/arcai-io/security/arcai-io-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/arcai-io-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/arcai-io/conformance/arcai-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arcai-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/arcai-io/llms/arcai-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arcai-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/arcai-io/mcp/arcai-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arcai-io-mcp.yml
- group: auth
  href: https://artifacts.apis.io/arcai-io/well-known/arcai-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arcai-io-security.txt
- group: agent
  href: https://artifacts.apis.io/arcai-io/well-known/arcai-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arcai-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/arcai-io/hosts/arcai-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arcai-io-hosts.yml
- group: build
  href: https://artifacts.apis.io/arcai-io/packages/arcai-io-packages.yml
  title: ''
  type: SDKs
  url: packages/arcai-io-packages.yml
- group: build
  href: https://artifacts.apis.io/arcai-io/packages/arcai-io-packages.yml
  title: ''
  type: Packages
  url: packages/arcai-io-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://app.arcai.io/support
- group: operate
  title: ''
  type: StatusPage
  url: https://arcai.io/status
- group: company
  title: ''
  type: Newsroom
  url: https://arcai.io/news
- group: auth
  href: https://artifacts.apis.io/arcai-io/security/arcai-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/arcai-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/arcai-io/security/arcai-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arcai-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arcai.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://arcai.io/developers
- group: docs
  title: ''
  type: Documentation
  url: https://arcai.io/developers
- group: docs
  title: ''
  type: APIReference
  url: https://arcai.io/developers
- group: company
  title: ''
  type: Blog
  url: https://arcai.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://arcai.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arcai.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arcai.io/privacy
- group: start
  title: ''
  type: SignUp
  url: https://arcai.io/dashboard/api
created: '2026-11-01'
description: ARC AI is an AI‑native crypto intelligence platform that provides real‑time token risk scans, automated whale tracking with on‑chain proof, and AI‑agent signals graded in public. The service offers a free public REST API and MCP server for AI agents to analyze tokens, monitor wallets, track new launches, and surface alpha signals 24/7 on Solana. It aims to deliver transparent, automated market intelligence for crypto projects.
image: https://arcai.io/logo/arcai-logo-512.png
json_schemas:
- name: PostApiAnalyzeRequest
  property_count: 3
  slug: arcai-io-post-api-analyze-request
- name: PostApiAnalyzeResponse
  property_count: 7
  slug: arcai-io-post-api-analyze-response
- name: PostApiFeedRequest
  property_count: 3
  slug: arcai-io-post-api-feed-request
jsonld:
- class_count: 3
  name: Arcai Io Context
  property_count: 10
  slug: arcai-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at arcai.io; 9 tools listed.
  name: ARC AI MCP Server
  slug: arcai-io-mcp-yml
modified: '2026-11-01'
name: ARC AI
nav: Providers
network: true
overview: 'ARC AI is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Cryptocurrency, Artificial Intelligence, Intelligence, and Blockchain.


  The ARC AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ARC AI''s developer surface includes support, documentation, API reference, engineering blog, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Arcai Io Plans Pricing
  plan_count: 0
  slug: arcai-io-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Arcai Io Rate Limits
  slug: arcai-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: ARC AI API Rules
  rule_count: 49
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 2
  slug: arcai-io-rules
scopes:
- name: Arcai Io Scopes
  scope_count: 0
  slug: arcai-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.4
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 23.1
    developer_ergonomics: 23.8
    discoverability: 57.5
    operational_transparency: 18.4
  previous_composite: 37.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arcai Io Authentication
  slug: arcai-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Arcai Io Domain Security
  slug: arcai-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arcai Io Vulnerability Disclosure
  slug: arcai-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: arcai-io
tags:
- Finance
- Cryptocurrency
- Artificial Intelligence
- Intelligence
- Blockchain
website: https://arcai.io/
---
