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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: HTTP API Query offers from user intent with Offer Query, read known Offer details with OfferInfo, or look up Offer cards you were served with the Offer Instance API; both use a Live API Key. Use Locat
  name: AON API
  slug: aon-api
- baseURL: https://api.aon.pro
  baseurl_source: declared
  description: 'AON API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AON API
  slug: aon-pro-api
artifact_total: 16
common:
- group: operate
  href: https://artifacts.apis.io/aon-pro/rate-limits/aon-pro-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aon-pro-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/aon-pro/rules/aon-pro-rules.yml
  title: ''
  type: Spectral
  url: rules/aon-pro-rules.yml
- group: design
  href: https://artifacts.apis.io/aon-pro/json-ld/aon-pro-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aon-pro-context.jsonld
- group: design
  href: https://artifacts.apis.io/aon-pro/vocabulary/aon-pro-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aon-pro-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aon-pro/data-model/aon-pro-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aon-pro-data-model.yml
- group: design
  href: https://artifacts.apis.io/aon-pro/components/aon-pro-components.yml
  title: ''
  type: Components
  url: components/aon-pro-components.yml
- group: build
  href: https://artifacts.apis.io/aon-pro/cli/aon-pro-cli.yml
  title: ''
  type: CLI
  url: cli/aon-pro-cli.yml
- group: operate
  href: https://artifacts.apis.io/aon-pro/changelog/aon-pro-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aon-pro-changelog.yml
- group: start
  href: https://artifacts.apis.io/aon-pro/sandbox/aon-pro-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/aon-pro-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/aon-pro/authentication/aon-pro-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aon-pro-authentication.yml
- group: design
  href: https://artifacts.apis.io/aon-pro/conformance/aon-pro-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aon-pro-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aon-pro/llms/aon-pro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aon-pro-llms.txt
- group: agent
  href: https://artifacts.apis.io/aon-pro/mcp/aon-pro-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aon-pro-mcp.yml
- group: other
  href: https://artifacts.apis.io/aon-pro/hosts/aon-pro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aon-pro-hosts.yml
- group: other
  href: https://artifacts.apis.io/aon-pro/vendors/aon-pro-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aon-pro-vendors.yml
- group: build
  href: https://artifacts.apis.io/aon-pro/packages/aon-pro-packages.yml
  title: ''
  type: SDKs
  url: packages/aon-pro-packages.yml
- group: build
  href: https://artifacts.apis.io/aon-pro/packages/aon-pro-packages.yml
  title: ''
  type: Packages
  url: packages/aon-pro-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.aon.pro/changelog
- group: auth
  href: https://artifacts.apis.io/aon-pro/security/aon-pro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aon-pro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aon.pro/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.aon.pro/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aon.pro/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aon.pro/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aon.pro/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.aon.pro/faq
- group: start
  title: ''
  type: SignUp
  url: https://auth.aon.pro/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aon.pro/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aon.pro/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agentoffernetwork
coverage:
  checked: '2026-11-01'
  detail: Docs provide a Base URL but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://docs.aon.pro/api.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AON – Agent Offer Network for AI‑Native Commerce provides a structured offer layer that connects AI product builders with merchant offers. It enables AI agents to monetize user intent through real‑time offer discovery, attribution, and outcome‑based commission models. Publishers can integrate via REST, SDKs, or MCP, gaining control over presentation while preserving revenue tracking. The platform supports various verticals such as travel, retail, and gaming, offering customizable UI components and detailed reporting. AON is a product of VertexFlow, aiming to simplify monetization for autonomous AI applications.
image: https://www.aon.pro/aon-logo-wordmark.png
json_schemas:
- name: GetV1PostbackPartneridResponse
  property_count: 9
  slug: aon-pro-get-v1-postback-partnerid-response
- name: GetV1PublicPlacementsPlacementidSetupResponse
  property_count: 6
  slug: aon-pro-get-v1-public-placements-placementid-setup-response
- name: PostV1DeveloperReportsOffersBatchRequest
  property_count: 3
  slug: aon-pro-post-v1-developer-reports-offers-batch-request
- name: PostV1DeveloperReportsOffersBatchResponse
  property_count: 13
  slug: aon-pro-post-v1-developer-reports-offers-batch-response
- name: PostV1OffersQueryRequest
  property_count: 6
  slug: aon-pro-post-v1-offers-query-request
- name: PostV2DeveloperReportsOffersBatchResponse
  property_count: 4
  slug: aon-pro-post-v2-developer-reports-offers-batch-response
jsonld:
- class_count: 15
  name: Aon Pro Context
  property_count: 47
  slug: aon-pro-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.aon.pro.
  name: AON MCP Server
  slug: aon-pro-mcp-yml
modified: '2026-11-01'
name: AON
nav: Providers
network: true
overview: 'AON is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Commerce, Monetization, OfferNetwork, and Platform.


  The AON catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AON''s developer surface includes CLI, changelog, sandbox, authentication, documentation, API reference, getting-started guide, and 22 more developer resources.'
plans:
- name: Aon Pro Plans Pricing
  plan_count: 0
  slug: aon-pro-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Aon Pro Rate Limits
  slug: aon-pro-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: AON API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 2
  slug: aon-pro-rules
scopes:
- name: Aon Pro Scopes
  scope_count: 0
  slug: aon-pro-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.9
  coverage:
    artifact_dirs: 28
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.6
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 25.3
    developer_ergonomics: 54.8
    discoverability: 65.0
    operational_transparency: 31.6
  previous_composite: 45.5
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
  name: Aon Pro Authentication
  slug: aon-pro-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aon Pro Domain Security
  slug: aon-pro-domain-security
  summary_line: TLSv1.3
slug: aon-pro
tags:
- Artificial Intelligence
- Commerce
- Monetization
- OfferNetwork
- Platform
website: https://aon.pro/
---
