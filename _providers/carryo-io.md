---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Carryo Io Agentic Access
  operation_count: 5
  slug: carryo-io-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- baseURL: https://mcp.carryo.io
  baseurl_source: declared
  description: The Health API from Carryo — 1 operation(s) for health.
  name: Carryo Health API
  slug: carryo-io-health-api
- baseURL: https://mcp.carryo.io
  baseurl_source: declared
  description: The Mcp API from Carryo — 1 operation(s) for mcp.
  name: Carryo MCP API
  slug: carryo-io-mcp-api
- baseURL: https://mcp.carryo.io
  baseurl_source: declared
  description: The .well Known API from Carryo — 2 operation(s) for .well known.
  name: Carryo .well Known API
  slug: carryo-io-well-known-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/carryo-io/vocabulary/carryo-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/carryo-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/carryo-io/data-model/carryo-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/carryo-io-data-model.yml
- group: agent
  href: https://artifacts.apis.io/carryo-io/agentic-access/carryo-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/carryo-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/carryo-io/plans/carryo-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/carryo-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/carryo-io/rules/carryo-io-rules.yml
  title: ''
  type: Spectral
  url: rules/carryo-io-rules.yml
- group: design
  href: https://artifacts.apis.io/carryo-io/conventions/carryo-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/carryo-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/carryo-io/authentication/carryo-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/carryo-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/carryo-io/errors/carryo-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/carryo-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/carryo-io/conformance/carryo-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carryo-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/carryo-io/llms/carryo-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carryo-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/carryo-io/mcp/carryo-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/carryo-io-mcp.yml
- group: auth
  href: https://artifacts.apis.io/carryo-io/well-known/carryo-io-chatgpt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/carryo-io-chatgpt-security.txt
- group: agent
  href: https://artifacts.apis.io/carryo-io/well-known/carryo-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carryo-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/carryo-io/hosts/carryo-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carryo-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/carryo-io/vendors/carryo-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carryo-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carryo.io/terms
- group: operate
  title: ''
  type: Support
  url: https://carryo.io/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carryo.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://carryo.io/app/plans
- group: start
  title: ''
  type: Login
  url: https://carryo.io/sign-in
- group: docs
  title: ''
  type: APIReference
  url: https://carryo.io/llms.txt
- group: auth
  href: https://artifacts.apis.io/carryo-io/scopes/carryo-io-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/carryo-io-scopes.yml
- group: auth
  href: https://artifacts.apis.io/carryo-io/security/carryo-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carryo-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carryo.io/
- group: docs
  title: ''
  type: Documentation
  url: https://carryo.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://carryo.io/get-started
created: '2026-11-03'
description: Carryo enables publishing shareable websites generated by AI models such as ChatGPT and Claude. Users can start for free, manage multiple sites in a library, and customize domains. The platform focuses on AI‑driven content creation, offering tools for quick deployment and easy management of AI‑generated web pages.
image: https://carryo.io/og-carryo.jpg
json_schemas:
- name: HealthResponse
  property_count: 0
  slug: carryo-io-health-response
- name: JsonRpcRequest
  property_count: 0
  slug: carryo-io-json-rpc-request
- name: JsonRpcResponse
  property_count: 0
  slug: carryo-io-json-rpc-response
- name: ProtectedResourceMetadata
  property_count: 0
  slug: carryo-io-protected-resource-metadata
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.carryo.io requiring OAuth.
  name: Carryo MCP Server
  slug: carryo-io-mcp-yml
modified: '2026-11-03'
name: Carryo
nav: Providers
network: true
overview: 'Carryo publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Health API, MCP API, and .well Known API. Tagged areas include Artificial Intelligence, Website Publishing, Content Generation, Software-as-a-Service, and Low-Code.


  The Carryo catalog on APIs.io includes 1 Spectral governance ruleset.


  Carryo''s developer surface includes authentication, support, pricing, API reference, documentation, getting-started guide, and 20 more developer resources.'
plans:
- name: Carryo Io Plans Pricing
  plan_count: 2
  slug: carryo-io-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Carryo API Rules
  rule_count: 51
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 1
  slug: carryo-io-rules
scopes:
- name: Carryo Io Scopes
  scope_count: 3
  slug: carryo-io-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 59.8
    catalog_earned_first_party: 8.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 51.0
    developer_ergonomics: 28.6
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Carryo Io Authentication
  slug: carryo-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Carryo Io Domain Security
  slug: carryo-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: carryo-io
tags:
- Artificial Intelligence
- Website Publishing
- Content Generation
- Software-as-a-Service
- Low-Code
website: https://carryo.io/
---
