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
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 54.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Aitopia Ai Agentic Access
  operation_count: 12
  slug: aitopia-ai-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api-live.aitopia.ai
  baseurl_source: declared
  description: The Account API from AITOPIA — 1 operation(s) for account.
  name: AITOPIA Account API
  slug: aitopia-ai-account-api
- baseURL: https://api-live.aitopia.ai
  baseurl_source: declared
  description: The Batch API from AITOPIA — 1 operation(s) for batch.
  name: AITOPIA Batch API
  slug: aitopia-ai-batch-api
- baseURL: https://api-live.aitopia.ai
  baseurl_source: declared
  description: The Edit API from AITOPIA — 1 operation(s) for edit.
  name: AITOPIA Edit API
  slug: aitopia-ai-edit-api
- baseURL: https://api-live.aitopia.ai
  baseurl_source: declared
  description: The Models API from AITOPIA — 2 operation(s) for models.
  name: AITOPIA Models API
  slug: aitopia-ai-models-api
- baseURL: https://api-live.aitopia.ai
  baseurl_source: declared
  description: The Openapi.json API from AITOPIA — 1 operation(s) for openapi.json.
  name: AITOPIA Openapi.json API
  slug: aitopia-ai-openapi-json-api
- baseURL: https://api-live.aitopia.ai
  baseurl_source: declared
  description: The Requests API from AITOPIA — 3 operation(s) for requests.
  name: AITOPIA Requests API
  slug: aitopia-ai-requests-api
- baseURL: https://api-live.aitopia.ai
  baseurl_source: declared
  description: The Uploads API from AITOPIA — 2 operation(s) for uploads.
  name: AITOPIA Uploads API
  slug: aitopia-ai-uploads-api
artifact_total: 26
asyncapis:
- description: ''
  name: Aitopia Ai Webhooks
  slug: aitopia-ai-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/aitopia-ai/agentic-access/aitopia-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aitopia-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/aitopia-ai/rate-limits/aitopia-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aitopia-ai-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/aitopia-ai/rules/aitopia-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/aitopia-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/aitopia-ai/json-ld/aitopia-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aitopia-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/aitopia-ai/vocabulary/aitopia-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aitopia-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aitopia-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aitopia-ai/asyncapi/aitopia-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/aitopia-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/aitopia-ai/data-model/aitopia-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aitopia-ai-data-model.yml
- group: build
  href: https://artifacts.apis.io/aitopia-ai/cli/aitopia-ai-cli.yml
  title: ''
  type: CLI
  url: cli/aitopia-ai-cli.yml
- group: design
  href: https://artifacts.apis.io/aitopia-ai/conventions/aitopia-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aitopia-ai-conventions.yml
- group: start
  href: https://artifacts.apis.io/aitopia-ai/sandbox/aitopia-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/aitopia-ai-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/aitopia-ai/authentication/aitopia-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aitopia-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/aitopia-ai/errors/aitopia-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aitopia-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aitopia-ai/conformance/aitopia-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aitopia-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aitopia-ai/llms/aitopia-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aitopia-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/aitopia-ai/mcp/aitopia-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aitopia-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/aitopia-ai/well-known/aitopia-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aitopia-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/aitopia-ai/hosts/aitopia-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aitopia-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/aitopia-ai/vendors/aitopia-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aitopia-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/aitopia-ai/packages/aitopia-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/aitopia-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/aitopia-ai/packages/aitopia-ai-packages.yml
  title: ''
  type: Packages
  url: packages/aitopia-ai-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aitopia.ai/quickstart/
- group: auth
  href: https://artifacts.apis.io/aitopia-ai/security/aitopia-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aitopia-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aitopia.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://aitopia.ai/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://aitopia.ai/mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://aitopia.ai/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aitopia.ai/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://aitopia.ai/login
created: '2026-11-01'
description: AITOPIA is an AI app store offering a marketplace of AI agents, models, and tools for image, video, and content creation. The platform lets users generate media, run AI workflows, and integrate agents via its MCP API. With over 3 million users, AITOPIA provides a catalog of agents across categories such as image generation, video production, marketing, and productivity, and offers pricing plans, a creator program, and community features.
image: https://aitopia.ai/Logo.svg
json_schemas:
- name: BatchItem
  property_count: 5
  slug: aitopia-ai-batch-item
- name: Cancel
  property_count: 3
  slug: aitopia-ai-cancel
- name: DryRun
  property_count: 10
  slug: aitopia-ai-dry-run
- name: Model
  property_count: 8
  slug: aitopia-ai-model
- name: Price
  property_count: 4
  slug: aitopia-ai-price
- name: Request
  property_count: 13
  slug: aitopia-ai-request
jsonld:
- class_count: 11
  name: Aitopia Ai Context
  property_count: 49
  slug: aitopia-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at scotty.aitopia.ai.
  name: AITOPIA MCP Server
  slug: aitopia-ai-mcp-yml
modified: '2026-11-01'
name: AITOPIA
nav: Providers
network: true
overview: 'AITOPIA publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Batch API, Edit API, and 4 more. Tagged areas include Artificial Intelligence, Marketplace, App Store, Image Generation, and Video Generation.


  The AITOPIA catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  AITOPIA''s developer surface includes CLI, sandbox, authentication, getting-started guide, documentation, API reference, pricing, and 22 more developer resources.'
plans:
- name: Aitopia Ai Plans Pricing
  plan_count: 0
  slug: aitopia-ai-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Aitopia Ai Rate Limits
  slug: aitopia-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: AITOPIA API Rules
  rule_count: 15
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 5
  slug: aitopia-ai-rules
scopes:
- name: Aitopia Ai Scopes
  scope_count: 0
  slug: aitopia-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 30
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 67.0
    developer_ergonomics: 54.0
    discoverability: 65.0
    operational_transparency: 39.5
  previous_composite: 53.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 26.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aitopia Ai Authentication
  slug: aitopia-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aitopia Ai Domain Security
  slug: aitopia-ai-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: get-request-status
  slug: aitopia-ai-get-request-status
- name: list-models
  slug: aitopia-ai-list-models
- name: run-model
  slug: aitopia-ai-run-model
slug: aitopia-ai
tags:
- Artificial Intelligence
- Marketplace
- App Store
- Image Generation
- Video Generation
- Agents
website: https://aitopia.ai/
---
