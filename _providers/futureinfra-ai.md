---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.5
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: FutureInfra REST API documentation covering authentication, server creation, firewall, and payment.
  name: FutureInfra API
  slug: futureinfra-api
- baseURL: https://api.futureinfra.ai
  baseurl_source: declared
  description: 'FutureInfra API as documented publicly: 44 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: FutureInfra API
  slug: futureinfra-ai-api
artifact_total: 16
common:
- group: commercial
  href: https://artifacts.apis.io/futureinfra-ai/plans/futureinfra-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/futureinfra-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/futureinfra-ai/rules/futureinfra-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/futureinfra-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/futureinfra-ai/json-ld/futureinfra-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/futureinfra-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/futureinfra-ai/vocabulary/futureinfra-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/futureinfra-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/futureinfra-ai/data-model/futureinfra-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/futureinfra-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/futureinfra-ai/authentication/futureinfra-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/futureinfra-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/futureinfra-ai/errors/futureinfra-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/futureinfra-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/futureinfra-ai/conformance/futureinfra-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/futureinfra-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/futureinfra-ai/llms/futureinfra-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/futureinfra-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/futureinfra-ai/mcp/futureinfra-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/futureinfra-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/futureinfra-ai/mcp/futureinfra-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/futureinfra-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/futureinfra-ai/well-known/futureinfra-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/futureinfra-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/futureinfra-ai/hosts/futureinfra-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/futureinfra-ai-hosts.yml
- group: start
  title: ''
  type: Sandbox
  url: https://futureinfra.ai/console/?signup=1&utm_source=site&utm_medium=header
- group: auth
  href: https://artifacts.apis.io/futureinfra-ai/security/futureinfra-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/futureinfra-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://futureinfra.ai
- group: docs
  title: ''
  type: Documentation
  url: https://futureinfra.ai/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://futureinfra.ai/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://futureinfra.ai/docs/
- group: operate
  title: ''
  type: Support
  url: https://futureinfra.ai/support/
- group: company
  title: ''
  type: Blog
  url: https://futureinfra.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://futureinfra.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://futureinfra.ai/console/?signup=1
- group: commercial
  title: ''
  type: TermsOfService
  url: https://futureinfra.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://futureinfra.ai/privacy/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://futureinfra.ai/console/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/futureinfra
coverage:
  checked: '2026-10-28'
  detail: Documentation provides API overview but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL files are available.
  evidence:
  - status: 404
    url: https://futureinfra.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: 'FutureInfra (Korean: 퓨쳐인프라) is a Korean cloud infrastructure and AI service provider offering virtual machines, container‑based applications, block storage, CDN, domain registration, DNS hosting, and AI model APIs for image, video and speech generation. All services are accessed through a single API key and a prepaid wallet, with pricing per‑use and monthly plans. The platform targets developers and “vibe coders” who prefer minimal configuration.'
image: https://futureinfra.ai/assets/icon-512.png
json_schemas:
- name: GetV1AiVoicesResponse
  property_count: 13
  slug: futureinfra-ai-get-v1-ai-voices-response
- name: GetV1GenModelsResponse
  property_count: 4
  slug: futureinfra-ai-get-v1-gen-models-response
- name: GetV1ProxyResponse
  property_count: 3
  slug: futureinfra-ai-get-v1-proxy-response
- name: PostV1BrainSaveRequest
  property_count: 3
  slug: futureinfra-ai-post-v1-brain-save-request
- name: PostV1ScrapeMyActorsRequest
  property_count: 8
  slug: futureinfra-ai-post-v1-scrape-my-actors-request
- name: PostV1ScrapeRunsBatchRequest
  property_count: 1
  slug: futureinfra-ai-post-v1-scrape-runs-batch-request
jsonld:
- class_count: 37
  name: Futureinfra Ai Context
  property_count: 77
  slug: futureinfra-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at futureinfra.ai requiring OAuth.
  name: FutureInfra MCP Server
  slug: futureinfra-ai-mcp-yml
modified: '2026-10-28'
name: FutureInfra
nav: Providers
network: true
overview: 'FutureInfra is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud, Infrastructure, AI, Korean, and Platform.


  The FutureInfra catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FutureInfra''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, support, engineering blog, and 20 more developer resources.'
plans:
- name: Futureinfra Ai Plans Pricing
  plan_count: 11
  slug: futureinfra-ai-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Futureinfra Ai Rate Limits
  slug: futureinfra-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: FutureInfra API Rules
  rule_count: 13
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 3
  slug: futureinfra-ai-rules
scopes:
- name: Futureinfra Ai Scopes
  scope_count: 0
  slug: futureinfra-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 24.9
    developer_ergonomics: 64.3
    discoverability: 56.7
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 14
      marker_coverage: 100.0
      total: 14
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Futureinfra Ai Authentication
  slug: futureinfra-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Futureinfra Ai Domain Security
  slug: futureinfra-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: futureinfra-ai
tags:
- Cloud
- Infrastructure
- AI
- Korean
- Platform
website: https://futureinfra.ai
---
