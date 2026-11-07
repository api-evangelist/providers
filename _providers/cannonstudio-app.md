---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
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
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Cannon Studio AI video production platform
  name: Cannon Studio API
  slug: cannon-studio-api
- description: 'Cannon Studio API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Cannon Studio API
  slug: cannonstudio-app-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/cannonstudio-app/plans/cannonstudio-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cannonstudio-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cannonstudio-app/rules/cannonstudio-app-rules.yml
  title: ''
  type: Spectral
  url: rules/cannonstudio-app-rules.yml
- group: design
  href: https://artifacts.apis.io/cannonstudio-app/json-ld/cannonstudio-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cannonstudio-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/cannonstudio-app/vocabulary/cannonstudio-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cannonstudio-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cannonstudio-app/data-model/cannonstudio-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cannonstudio-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/cannonstudio-app/conventions/cannonstudio-app-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/cannonstudio-app-conventions.yml
- group: design
  href: https://artifacts.apis.io/cannonstudio-app/conventions/cannonstudio-app-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cannonstudio-app-conventions.yml
- group: auth
  href: https://artifacts.apis.io/cannonstudio-app/authentication/cannonstudio-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cannonstudio-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/cannonstudio-app/conformance/cannonstudio-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cannonstudio-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cannonstudio-app/llms/cannonstudio-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cannonstudio-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/cannonstudio-app/mcp/cannonstudio-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cannonstudio-app-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cannonstudio-app/well-known/cannonstudio-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cannonstudio-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/cannonstudio-app/hosts/cannonstudio-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cannonstudio-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/cannonstudio-app/vendors/cannonstudio-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cannonstudio-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cannonstudio.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cannonstudio.app/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cannonstudio.app/pricing
- group: start
  title: ''
  type: Login
  url: https://www.cannonstudio.app/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.cannonstudio.app/guides
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.cannonstudio.app/developers
- group: company
  title: ''
  type: Blog
  url: https://www.cannonstudio.app/blog/creator-flow
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cannonstudio.app/developers/docs/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://www.cannonstudio.app/developers/docs/reference/status
- group: auth
  href: https://artifacts.apis.io/cannonstudio-app/security/cannonstudio-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cannonstudio-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cannonstudio.app/
coverage:
  checked: '2026-11-04'
  detail: Documentation is public but no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL spec was found.
  evidence:
  - status: 200
    url: https://www.cannonstudio.app/developers/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Cannon Studio is an AI video production studio offering tools for ads, UGC, commercials, shorts, episodic content, TV shows, and films. It provides reusable worlds, consistent characters, location continuity, and team collaboration, enabling creators to generate visual content efficiently with AI-driven workflows.
image: https://www.cannonstudio.app/cover.png
json_schemas:
- name: GetApiV1RequestsRequestidResponse
  property_count: 12
  slug: cannonstudio-app-get-api-v1-requests-requestid-response
- name: GetApiV1StatusResponse
  property_count: 8
  slug: cannonstudio-app-get-api-v1-status-response
- name: PostApiV1RequestsRequest
  property_count: 2
  slug: cannonstudio-app-post-api-v1-requests-request
- name: PostApiV1RequestsResponse
  property_count: 5
  slug: cannonstudio-app-post-api-v1-requests-response
jsonld:
- class_count: 4
  name: Cannonstudio App Context
  property_count: 22
  slug: cannonstudio-app-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.cannonstudio.app.
  name: Cannon Studio MCP Server
  slug: cannonstudio-app-mcp-yml
modified: '2026-11-04'
name: Cannon Studio
nav: Providers
network: true
overview: 'Cannon Studio is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Video Production, Advertising, Content Creation, and Multimedia.


  The Cannon Studio catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cannon Studio''s developer surface includes authentication, pricing, documentation, engineering blog, getting-started guide, API reference, and 19 more developer resources.'
plans:
- name: Cannonstudio App Plans Pricing
  plan_count: 5
  slug: cannonstudio-app-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Cannon Studio API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: cannonstudio-app-rules
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 22.4
    developer_ergonomics: 32.1
    discoverability: 56.7
    operational_transparency: 0.0
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
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cannonstudio App Authentication
  slug: cannonstudio-app-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cannonstudio App Domain Security
  slug: cannonstudio-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cannonstudio-app
tags:
- Artificial Intelligence
- Video Production
- Advertising
- Content Creation
- Multimedia
website: https://www.cannonstudio.app/
---
