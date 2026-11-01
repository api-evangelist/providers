---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 54
  human_in_the_loop: 2
  name: 0Latency Ai Agentic Access
  operation_count: 104
  slug: 0latency-ai-agentic-access
  summary_line: 104 operations · 54 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.0latency.ai
  baseurl_source: declared
  description: The Admin API from 0latency-ai — 4 operation(s) for admin.
  name: 0latency-ai Admin API
  slug: 0latency-ai-admin-api
- baseURL: https://api.0latency.ai
  baseurl_source: declared
  description: The Api Keys API from 0latency-ai — 1 operation(s) for api keys.
  name: 0latency-ai Api Keys API
  slug: 0latency-ai-api-keys-api
- baseURL: https://api.0latency.ai
  baseurl_source: declared
  description: The auth API from 0latency-ai — 8 operation(s) for auth.
  name: 0latency-ai Auth API
  slug: 0latency-ai-auth-api
- baseURL: https://api.0latency.ai
  baseurl_source: declared
  description: The billing API from 0latency-ai — 4 operation(s) for billing.
  name: 0latency-ai Billing API
  slug: 0latency-ai-billing-api
- baseURL: https://api.0latency.ai
  baseurl_source: declared
  description: The Criteria API from 0latency-ai — 2 operation(s) for criteria.
  name: 0latency-ai Criteria API
  slug: 0latency-ai-criteria-api
- baseURL: https://api.0latency.ai
  baseurl_source: declared
  description: The Dashboard API from 0latency-ai — 1 operation(s) for dashboard.
  name: 0latency-ai Dashboard API
  slug: 0latency-ai-dashboard-api
- baseURL: https://api.0latency.ai
  baseurl_source: declared
  description: The Extract API from 0latency-ai — 2 operation(s) for extract.
  name: 0latency-ai Extract API
  slug: 0latency-ai-extract-api
- baseURL: https://api.0latency.ai
  baseurl_source: declared
  description: The Graph API from 0latency-ai — 4 operation(s) for graph.
  name: 0latency-ai Graph API
  slug: 0latency-ai-graph-api
- baseURL: https://api.0latency.ai
  baseurl_source: declared
  description: The Health API from 0latency-ai — 1 operation(s) for health.
  name: 0latency-ai Health API
  slug: 0latency-ai-health-api
- baseURL: https://api.0latency.ai
  baseurl_source: declared
  description: The Memories API from 0latency-ai — 10 operation(s) for memories.
  name: 0latency-ai Memories API
  slug: 0latency-ai-memories-api
- baseURL: https://api.0latency.ai
  baseurl_source: declared
  description: The Org API from 0latency-ai — 3 operation(s) for org.
  name: 0latency-ai Org API
  slug: 0latency-ai-org-api
- baseURL: https://api.0latency.ai
  baseurl_source: declared
  description: The Recall API from 0latency-ai — 1 operation(s) for recall.
  name: 0latency-ai Recall API
  slug: 0latency-ai-recall-api
- baseURL: https://api.0latency.ai
  baseurl_source: declared
  description: The Schemas API from 0latency-ai — 2 operation(s) for schemas.
  name: 0latency-ai Schemas API
  slug: 0latency-ai-schemas-api
- baseURL: https://api.0latency.ai
  baseurl_source: declared
  description: The Tenant Info API from 0latency-ai — 1 operation(s) for tenant info.
  name: 0latency-ai Tenant Info API
  slug: 0latency-ai-tenant-info-api
- baseURL: https://api.0latency.ai
  baseurl_source: declared
  description: The Usage API from 0latency-ai — 1 operation(s) for usage.
  name: 0latency-ai Usage API
  slug: 0latency-ai-usage-api
- baseURL: https://api.0latency.ai
  baseurl_source: declared
  description: The Webhooks API from 0latency-ai — 2 operation(s) for webhooks.
  name: 0latency-ai Webhooks API
  slug: 0latency-ai-webhooks-api
artifact_total: 31
common:
- group: agent
  href: https://artifacts.apis.io/0latency-ai/agentic-access/0latency-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/0latency-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/0latency-ai/rate-limits/0latency-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/0latency-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/0latency-ai/plans/0latency-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/0latency-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/0latency-ai/rules/0latency-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/0latency-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/0latency-ai/json-ld/0latency-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/0latency-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/0latency-ai/vocabulary/0latency-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/0latency-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/0latency-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/0latency-ai/data-model/0latency-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/0latency-ai-data-model.yml
- group: build
  href: https://artifacts.apis.io/0latency-ai/cli/0latency-ai-cli.yml
  title: ''
  type: CLI
  url: cli/0latency-ai-cli.yml
- group: auth
  href: https://artifacts.apis.io/0latency-ai/authentication/0latency-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/0latency-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/0latency-ai/errors/0latency-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/0latency-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/0latency-ai/conformance/0latency-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/0latency-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/0latency-ai/llms/0latency-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/0latency-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/0latency-ai/well-known/0latency-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/0latency-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/0latency-ai/hosts/0latency-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/0latency-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/0latency-ai/vendors/0latency-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/0latency-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/0latency-ai/packages/0latency-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/0latency-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/0latency-ai/packages/0latency-ai-packages.yml
  title: ''
  type: Packages
  url: packages/0latency-ai-packages.yml
- group: auth
  href: https://artifacts.apis.io/0latency-ai/security/0latency-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/0latency-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://0latency.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://0latency.ai/docs.html
- group: docs
  title: ''
  type: APIReference
  url: https://0latency.ai/docs.html
- group: start
  title: ''
  type: GettingStarted
  url: https://0latency.ai/docs.html
- group: operate
  title: ''
  type: Support
  url: https://0latency.ai/support.html
- group: company
  title: ''
  type: Blog
  url: https://0latency.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/0latency-ai
- group: operate
  title: ''
  type: Roadmap
  url: https://0latency.ai/roadmap.html
- group: commercial
  title: ''
  type: Pricing
  url: https://0latency.ai/pricing.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://0latency.ai/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://0latency.ai/privacy.html
- group: start
  title: ''
  type: SignUp
  url: https://0latency.ai/login.html
created: '2026-10-30'
description: 0Latency provides a persistent memory layer API for AI agents, enabling structured, auditable, and synthesizable memory across sessions. It offers a context layer supporting rapid recall, provenance tracking, and multi‑agent orchestration, with tiered plans from free to enterprise. Integrates with LangChain, CrewAI, AutoGen, and more via simple HTTP API and webhooks.
image: https://0latency.ai/logos/0latency-icon-256.png
json_schemas:
- name: CreateTenantResponse
  property_count: 7
  slug: 0latency-ai-create-tenant-response
- name: CriteriaRequest
  property_count: 5
  slug: 0latency-ai-criteria-request
- name: ExtractRequest
  property_count: 5
  slug: 0latency-ai-extract-request
- name: HealthResponse
  property_count: 6
  slug: 0latency-ai-health-response
- name: OrgMemoryRequest
  property_count: 7
  slug: 0latency-ai-org-memory-request
- name: SubscriptionResponse
  property_count: 7
  slug: 0latency-ai-subscription-response
jsonld:
- class_count: 28
  name: 0Latency Ai Context
  property_count: 66
  slug: 0latency-ai-context
layout: provider
modified: '2026-10-30'
name: 0latency-ai
nav: Providers
network: true
overview: '0latency-ai publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Api Keys API, Auth API, and 13 more. Tagged areas include Company, AI, Memory, Agent, and Platform.


  The 0latency-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  0latency-ai''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 24 more developer resources.'
plans:
- name: 0Latency Ai Plans Pricing
  plan_count: 4
  slug: 0latency-ai-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: 0Latency Ai Rate Limits
  slug: 0latency-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: 0latency-ai API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: 0latency-ai-rules
scopes:
- name: 0Latency Ai Scopes
  scope_count: 0
  slug: 0latency-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 65.4
  coverage:
    artifact_dirs: 29
    catalog_earned: 99.3
    catalog_earned_first_party: 0.0
    catalog_gap: 15.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 53.7
    developer_ergonomics: 68.3
    discoverability: 66.1
    operational_transparency: 38.9
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
  name: 0Latency Ai Authentication
  slug: 0latency-ai-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: 0Latency Ai Domain Security
  slug: 0latency-ai-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: authentication
  slug: 0latency-ai-authentication
slug: 0latency-ai
tags:
- Company
- AI
- Memory
- Agent
- Platform
- API
website: https://0latency.ai/
---
