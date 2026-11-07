---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Animam Ai Agentic Access
  operation_count: 26
  slug: animam-ai-agentic-access
  summary_line: 26 operations · 18 acting
api_count: 1
apis:
- baseURL: https://api.animam.ai
  baseurl_source: declared
  description: Knowledge base CRUD.
  name: Animam.ai Corpus API
  slug: animam-ai-corpus-api
- baseURL: https://api.animam.ai
  baseurl_source: declared
  description: Conversation segments (audiences).
  name: Animam.ai Segments API
  slug: animam-ai-segments-api
- baseURL: https://api.animam.ai
  baseurl_source: declared
  description: Tenant settings, persona, MCP tools config.
  name: Animam.ai Tenants API
  slug: animam-ai-tenants-api
artifact_total: 19
common:
- group: auth
  href: https://artifacts.apis.io/animam-ai/well-known/animam-ai-modelcontextprotocol-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/animam-ai-modelcontextprotocol-security.txt
- group: docs
  title: ''
  type: Documentation
  url: https://docs.animam.ai/
- group: agent
  href: https://artifacts.apis.io/animam-ai/agentic-access/animam-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/animam-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/animam-ai/rate-limits/animam-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/animam-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/animam-ai/plans/animam-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/animam-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/animam-ai/rules/animam-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/animam-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/animam-ai/json-ld/animam-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/animam-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/animam-ai/vocabulary/animam-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/animam-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/animam-ai/data-model/animam-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/animam-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/animam-ai/components/animam-ai-components.yml
  title: ''
  type: Components
  url: components/animam-ai-components.yml
- group: design
  href: https://artifacts.apis.io/animam-ai/conventions/animam-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/animam-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/animam-ai/conventions/animam-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/animam-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/animam-ai/security/animam-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/animam-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/animam-ai/authentication/animam-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/animam-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/animam-ai/scopes/animam-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/animam-ai-scopes.yml
- group: design
  href: https://artifacts.apis.io/animam-ai/errors/animam-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/animam-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/animam-ai/conformance/animam-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/animam-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/animam-ai/llms/animam-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/animam-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/animam-ai/a2a/animam-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/animam-ai-a2a.yml
- group: build
  href: https://artifacts.apis.io/animam-ai/mcp/animam-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/animam-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/animam-ai/mcp/animam-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/animam-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/animam-ai/well-known/animam-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/animam-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/animam-ai/well-known/animam-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/animam-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/animam-ai/hosts/animam-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/animam-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/animam-ai/vendors/animam-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/animam-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/animam-ai/packages/animam-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/animam-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/animam-ai/packages/animam-ai-packages.yml
  title: ''
  type: Packages
  url: packages/animam-ai-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://animam.ai/trust
- group: start
  title: ''
  type: Login
  url: https://animam.ai/login
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.animam.ai/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://animam.ai/for-dev
- group: auth
  href: https://artifacts.apis.io/animam-ai/security/animam-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/animam-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/animam-ai/security/animam-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/animam-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://animam.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://animam.ai/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/animam
created: '2026-11-01'
description: Animam.ai provides an API‑first platform for deploying AI‑powered conversational agents at scale. It offers multi‑tenant, multi‑channel, white‑label agents with built‑in tools for contact forms, quote generation, meeting booking, and payment processing. The service includes a public REST API, an MCP server for model‑context protocol, a widget CDN, and voice integration via Vapi. Hosted in France, it is GDPR‑compliant and billed per bot with flat monthly pricing. Developers can use managed Claude models or bring their own keys (BYOK) across major providers.
image: https://animam.ai/logo/logo-horizontal.svg
json_schemas:
- name: CorpusEntry
  property_count: 12
  slug: animam-ai-corpus-entry
- name: CreateCorpusBody
  property_count: 10
  slug: animam-ai-create-corpus-body
- name: CreateSegmentBody
  property_count: 5
  slug: animam-ai-create-segment-body
- name: ListCorpusResponse
  property_count: 2
  slug: animam-ai-list-corpus-response
- name: SegmentDetail
  property_count: 7
  slug: animam-ai-segment-detail
- name: UpdateTenantBody
  property_count: 17
  slug: animam-ai-update-tenant-body
jsonld:
- class_count: 19
  name: Animam Ai Context
  property_count: 63
  slug: animam-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.animam.ai requiring OAuth.
  name: Animam.ai MCP Server
  slug: animam-ai-mcp-yml
modified: '2026-11-01'
name: Animam.ai
nav: Providers
network: true
overview: 'Animam.ai publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Corpus API, Segments API, and Tenants API. Tagged areas include Artificial Intelligence, Automation, Lead Generation, Chatbots, and Software-as-a-Service.


  The Animam.ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Animam.ai''s developer surface includes documentation, authentication, getting-started guide, API reference, pricing, and 31 more developer resources.'
plans:
- name: Animam Ai Plans Pricing
  plan_count: 4
  slug: animam-ai-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Animam Ai Rate Limits
  slug: animam-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: Animam.ai API Rules
  rule_count: 66
  severity_counts:
    error: 64
    hint: 0
    info: 1
    warn: 1
  slug: animam-ai-rules
scopes:
- name: Animam Ai Scopes
  scope_count: 7
  slug: animam-ai-scopes
  summary_line: 7 scopes
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 32
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 61.6
    developer_ergonomics: 33.3
    discoverability: 65.0
    operational_transparency: 34.2
  previous_composite: 55.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 32.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Animam Ai Authentication
  slug: animam-ai-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Animam Ai Domain Security
  slug: animam-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Animam Ai Vulnerability Disclosure
  slug: animam-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: animam-ai
tags:
- Artificial Intelligence
- Automation
- Lead Generation
- Chatbots
- Software-as-a-Service
website: https://animam.ai/
---
