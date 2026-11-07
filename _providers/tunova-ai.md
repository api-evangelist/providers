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
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Tunova Ai Agentic Access
  operation_count: 10
  slug: tunova-ai-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.tunova.ai
  baseurl_source: declared
  description: Create songs (async)
  name: tunova-ai Generation API
  slug: tunova-ai-generation-api
- baseURL: https://api.tunova.ai
  baseurl_source: declared
  description: Poll async jobs
  name: tunova-ai Jobs API
  slug: tunova-ai-jobs-api
- baseURL: https://api.tunova.ai
  baseurl_source: declared
  description: Lyrics, clips, limits
  name: tunova-ai Utility API
  slug: tunova-ai-utility-api
artifact_total: 19
asyncapis:
- description: ''
  name: Tunova Ai Webhooks
  slug: tunova-ai-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/tunova-ai/agentic-access/tunova-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tunova-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/tunova-ai/rate-limits/tunova-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tunova-ai-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/tunova-ai/rules/tunova-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/tunova-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/tunova-ai/json-ld/tunova-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tunova-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/tunova-ai/vocabulary/tunova-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tunova-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/tunova-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/tunova-ai/asyncapi/tunova-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/tunova-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/tunova-ai/data-model/tunova-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tunova-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/tunova-ai/changelog/tunova-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tunova-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/tunova-ai/conventions/tunova-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/tunova-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/tunova-ai/conventions/tunova-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tunova-ai-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://tunova.ai/security
- group: auth
  href: https://artifacts.apis.io/tunova-ai/authentication/tunova-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tunova-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/tunova-ai/lifecycle/tunova-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tunova-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/tunova-ai/errors/tunova-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tunova-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tunova-ai/conformance/tunova-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tunova-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tunova-ai/llms/tunova-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tunova-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/tunova-ai/mcp/tunova-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/tunova-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/tunova-ai/mcp/tunova-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tunova-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/tunova-ai/well-known/tunova-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tunova-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/tunova-ai/hosts/tunova-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tunova-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/tunova-ai/vendors/tunova-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tunova-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/tunova-ai/packages/tunova-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/tunova-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/tunova-ai/packages/tunova-ai-packages.yml
  title: ''
  type: Packages
  url: packages/tunova-ai-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://tunova.ai/status
- group: auth
  title: ''
  type: Security
  url: https://tunova.ai/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://tunova.ai/changelog
- group: auth
  href: https://artifacts.apis.io/tunova-ai/security/tunova-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tunova-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/tunova-ai/security/tunova-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tunova-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tunova.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.tunova.ai
- group: docs
  title: ''
  type: Documentation
  url: https://api.tunova.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.tunova.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://tunova.ai/quickstart
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tunova.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tunova.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/erliona
created: '2026-10-31'
description: Tunova provides a prepaid, token‑based REST and MCP API that enables developers to generate music using Suno's v5.5 models. It offers asynchronous job handling, HMAC‑signed webhooks, token pricing plans, and a quick‑start guide, positioning itself as an independent, fully managed service that abstracts Suno's API complexities.
image: https://tunova.ai/icon.svg
json_schemas:
- name: Balance
  property_count: 13
  slug: tunova-ai-balance
- name: Clip
  property_count: 8
  slug: tunova-ai-clip
- name: CustomGenerateRequest
  property_count: 7
  slug: tunova-ai-custom-generate-request
- name: GenerateRequest
  property_count: 5
  slug: tunova-ai-generate-request
- name: Job
  property_count: 10
  slug: tunova-ai-job
jsonld:
- class_count: 7
  name: Tunova Ai Context
  property_count: 39
  slug: tunova-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.tunova.ai requiring an API key.
  name: tunova-ai MCP Server
  slug: tunova-ai-mcp-yml
modified: '2026-10-31'
name: tunova-ai
nav: Providers
network: true
overview: 'tunova-ai publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Generation API, Jobs API, and Utility API. Tagged areas include Artificial Intelligence, Music, Audio, Suno, and TokenizedAPI.


  The tunova-ai catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  tunova-ai''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, and 32 more developer resources.'
plans:
- name: Tunova Ai Plans Pricing
  plan_count: 0
  slug: tunova-ai-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Tunova Ai Rate Limits
  slug: tunova-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: tunova-ai API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: tunova-ai-rules
score:
  band: developing
  composite: 49.5
  coverage:
    artifact_dirs: 29
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.7
  facets:
    access_clarity: 22.4
    contract_governance: 35.6
    contract_quality: 70.2
    developer_ergonomics: 44.5
    discoverability: 65.0
    operational_transparency: 52.6
  previous_composite: 60.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tunova-ai/tunova-ai-2026-11-03T145241.png
security:
- kind: authentication
  name: Tunova Ai Authentication
  slug: tunova-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Tunova Ai Domain Security
  slug: tunova-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Tunova Ai Trust Center
  slug: tunova-ai-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 1
skills:
- name: tunova-ai-generation-skill
  slug: tunova-ai-generation-skill
slug: tunova-ai
tags:
- Artificial Intelligence
- Music
- Audio
- Suno
- TokenizedAPI
- REST
- MCP
website: https://tunova.ai/
---
