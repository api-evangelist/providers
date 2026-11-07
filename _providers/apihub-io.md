---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Every public APIHub endpoint with parameters, request, and response examples.
  name: APIHub API
  slug: apihub-api
- baseURL: https://proxy.apihub.io
  baseurl_source: declared
  description: 'APIHub API as documented publicly: 257 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: APIHub API
  slug: apihub-io-api
artifact_total: 16
common:
- group: operate
  href: https://artifacts.apis.io/apihub-io/rate-limits/apihub-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apihub-io-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/apihub-io/rules/apihub-io-rules.yml
  title: ''
  type: Spectral
  url: rules/apihub-io-rules.yml
- group: design
  href: https://artifacts.apis.io/apihub-io/json-ld/apihub-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apihub-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/apihub-io/vocabulary/apihub-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apihub-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/apihub-io/data-model/apihub-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apihub-io-data-model.yml
- group: build
  href: https://artifacts.apis.io/apihub-io/cli/apihub-io-cli.yml
  title: ''
  type: CLI
  url: cli/apihub-io-cli.yml
- group: auth
  href: https://artifacts.apis.io/apihub-io/authentication/apihub-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apihub-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/apihub-io/lifecycle/apihub-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/apihub-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/apihub-io/errors/apihub-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apihub-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/apihub-io/conformance/apihub-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apihub-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apihub-io/llms/apihub-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apihub-io-llms.txt
- group: other
  href: https://artifacts.apis.io/apihub-io/a2a/apihub-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/apihub-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/apihub-io/mcp/apihub-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/apihub-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/apihub-io/hosts/apihub-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apihub-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/apihub-io/vendors/apihub-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apihub-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/apihub-io/packages/apihub-io-packages.yml
  title: ''
  type: SDKs
  url: packages/apihub-io-packages.yml
- group: build
  href: https://artifacts.apis.io/apihub-io/packages/apihub-io-packages.yml
  title: ''
  type: Packages
  url: packages/apihub-io-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://apihub.io/status
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.apihub.io/
- group: auth
  href: https://artifacts.apis.io/apihub-io/security/apihub-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apihub-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apihub.io/
- group: docs
  title: ''
  type: Documentation
  url: https://apihub.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://apihub.io/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://apihub.io/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://apihub.io/contact
- group: start
  title: ''
  type: SignUp
  url: https://apihub.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apihub.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apihub.io/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apihubio
coverage:
  checked: '2026-11-01'
  detail: API reference lists endpoints but no OpenAPI/AsyncAPI/GraphQL/WSDL contract is published.
  evidence:
  - status: 200
    url: https://apihub.io/docs/api-reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: APIHub is a marketplace where AI agents discover, pay for, and consume monitored APIs through a single endpoint. Powered by x402 and USDC on Base, it offers a unified MCP-native experience with per‑request pricing, no wallet required, and tools for agents to integrate APIs seamlessly. The platform provides documentation, SDKs, and a CLI for easy onboarding, enabling agents to call APIs via a proxy with a simple Bearer key.
image: https://apihub.io/icon.svg
json_schemas:
- name: GetSlugFetchResponse
  property_count: 6
  slug: apihub-io-get-slug-fetch-response
- name: GetV1WalletBalanceResponse
  property_count: 5
  slug: apihub-io-get-v1-wallet-balance-response
- name: PostExecuteResponse
  property_count: 5
  slug: apihub-io-post-execute-response
- name: PostExternalResponse
  property_count: 5
  slug: apihub-io-post-external-response
- name: PostV1RegisterRequest
  property_count: 4
  slug: apihub-io-post-v1-register-request
- name: PostV1RegisterResponse
  property_count: 5
  slug: apihub-io-post-v1-register-response
jsonld:
- class_count: 50
  name: Apihub Io Context
  property_count: 95
  slug: apihub-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.apihub.io.
  name: APIHub MCP Server
  slug: apihub-io-mcp-yml
modified: '2026-11-01'
name: APIHub
nav: Providers
network: true
overview: 'APIHub is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Marketplace, MCP, Artificial Intelligence, and Payments.


  The APIHub catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  APIHub''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, support, signup flow, and 22 more developer resources.'
plans:
- name: Apihub Io Plans Pricing
  plan_count: 0
  slug: apihub-io-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Apihub Io Rate Limits
  slug: apihub-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: APIHub API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: apihub-io-rules
scopes:
- name: Apihub Io Scopes
  scope_count: 0
  slug: apihub-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 30
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 47.6
    discoverability: 56.7
    operational_transparency: 42.1
  previous_composite: 44.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Apihub Io Authentication
  slug: apihub-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Apihub Io Domain Security
  slug: apihub-io-domain-security
  summary_line: TLSv1.3 · HSTS
slug: apihub-io
tags:
- Marketplace
- MCP
- Artificial Intelligence
- Payments
website: https://apihub.io/
---
