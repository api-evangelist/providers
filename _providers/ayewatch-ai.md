---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: AyeWatch REST API for monitoring topics and receiving webhook events.
  name: AyeWatch API
  slug: ayewatch-api
- description: 'Ayewatch API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Ayewatch API
  slug: ayewatch-ai-api
artifact_total: 16
common:
- group: operate
  href: https://artifacts.apis.io/ayewatch-ai/rate-limits/ayewatch-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ayewatch-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ayewatch-ai/plans/ayewatch-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ayewatch-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ayewatch-ai/rules/ayewatch-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/ayewatch-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/ayewatch-ai/json-ld/ayewatch-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ayewatch-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/ayewatch-ai/vocabulary/ayewatch-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ayewatch-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ayewatch-ai/data-model/ayewatch-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ayewatch-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/ayewatch-ai/conventions/ayewatch-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ayewatch-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/ayewatch-ai/authentication/ayewatch-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ayewatch-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/ayewatch-ai/errors/ayewatch-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ayewatch-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ayewatch-ai/conformance/ayewatch-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ayewatch-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ayewatch-ai/llms/ayewatch-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ayewatch-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/ayewatch-ai/mcp/ayewatch-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ayewatch-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ayewatch-ai/well-known/ayewatch-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ayewatch-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/ayewatch-ai/hosts/ayewatch-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ayewatch-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/ayewatch-ai/vendors/ayewatch-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ayewatch-ai-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://ayewatch.ai/settings/webhooks
- group: auth
  href: https://artifacts.apis.io/ayewatch-ai/security/ayewatch-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ayewatch-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ayewatch.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ayewatch.ai/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://ayewatch.ai/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://ayewatch.ai/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://ayewatch.ai/documentation#quick-start
- group: operate
  title: ''
  type: Support
  url: https://ayewatch.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://ayewatch.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://ayewatch.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ayewatch.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ayewatch.ai/privacy
coverage:
  checked: '2026-11-02'
  detail: Documentation is public HTML but no OpenAPI or other machine-readable spec is published.
  evidence:
  - status: 200
    url: https://ayewatch.ai/documentation
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Ayewatch is your real-time AI companion that monitors the internet for any topic you care about and alerts you the moment something new happens. Stay ahead with instant updates, cross‑platform access (web & mobile), and an effortless dashboard to track news, trends, and research subjects.
image: https://ayewatch.ai/theeatcvherlogoplain.png
json_schemas:
- name: GetApiV1TopicsResponse
  property_count: 2
  slug: ayewatch-ai-get-api-v1-topics-response
- name: GetApiV1WebhookResponse
  property_count: 6
  slug: ayewatch-ai-get-api-v1-webhook-response
- name: PostApiV1TopicsResponse
  property_count: 1
  slug: ayewatch-ai-post-api-v1-topics-response
- name: PostApiV1WebhookRotateSecretResponse
  property_count: 6
  slug: ayewatch-ai-post-api-v1-webhook-rotate-secret-response
- name: PutApiV1WebhookRequest
  property_count: 1
  slug: ayewatch-ai-put-api-v1-webhook-request
- name: PutApiV1WebhookResponse
  property_count: 1
  slug: ayewatch-ai-put-api-v1-webhook-response
jsonld:
- class_count: 7
  name: Ayewatch Ai Context
  property_count: 12
  slug: ayewatch-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at ayewatch.ai.
  name: Ayewatch MCP Server
  slug: ayewatch-ai-mcp-yml
modified: '2026-11-02'
name: Ayewatch
nav: Providers
network: true
overview: 'Ayewatch is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Monitoring, Real-Time, Webhook, and Dashboards.


  The Ayewatch catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ayewatch''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 20 more developer resources.'
plans:
- name: Ayewatch Ai Plans Pricing
  plan_count: 3
  slug: ayewatch-ai-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 1
  name: Ayewatch Ai Rate Limits
  slug: ayewatch-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Ayewatch API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: ayewatch-ai-rules
scopes:
- name: Ayewatch Ai Scopes
  scope_count: 0
  slug: ayewatch-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 77.8
    catalog_earned_first_party: 20.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 34.5
    discoverability: 56.7
    operational_transparency: 25.0
  previous_composite: 44.8
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
  name: Ayewatch Ai Authentication
  slug: ayewatch-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ayewatch Ai Domain Security
  slug: ayewatch-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ayewatch-ai
tags:
- Artificial Intelligence
- Monitoring
- Real-Time
- Webhook
- Dashboards
- News
website: https://ayewatch.ai/
---
