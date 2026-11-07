---
access_model:
  confidence: high
  label: Paid (free trial)
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: REST API for the WaterrAI meeting platform – create scenarios, run AI meetings, fetch transcripts and analyses.
  name: WaterrAI API
  slug: waterrai-api
- baseURL: https://api.waterr.ai/v1
  baseurl_source: declared
  description: REST API for the WaterrAI meeting platform — create scenarios, spin up AI-driven meetings, fetch transcripts and analyses.
  name: WaterrAI API API
  slug: waterrai-api-api
artifact_total: 15
asyncapis:
- description: ''
  name: Waterr Ai Webhooks
  slug: waterr-ai-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/waterr-ai/rate-limits/waterr-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/waterr-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/waterr-ai/plans/waterr-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/waterr-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/waterr-ai/rules/waterr-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/waterr-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/waterr-ai/json-ld/waterr-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/waterr-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/waterr-ai/vocabulary/waterr-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/waterr-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/waterr-ai/asyncapi/waterr-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/waterr-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/waterr-ai/data-model/waterr-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/waterr-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/waterr-ai/changelog/waterr-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/waterr-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/waterr-ai/conventions/waterr-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/waterr-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/waterr-ai/authentication/waterr-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/waterr-ai-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.waterr.ai/api-reference/versioning.md
- group: design
  href: https://artifacts.apis.io/waterr-ai/lifecycle/waterr-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/waterr-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/waterr-ai/errors/waterr-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/waterr-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/waterr-ai/conformance/waterr-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/waterr-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/waterr-ai/llms/waterr-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/waterr-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/waterr-ai/a2a/waterr-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/waterr-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/waterr-ai/well-known/waterr-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/waterr-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/waterr-ai/hosts/waterr-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/waterr-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/waterr-ai/vendors/waterr-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/waterr-ai-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://waterr.ai/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://waterr.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.waterr.ai/security/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/waterrai
- group: company
  title: ''
  type: Blog
  url: https://waterr.ai/blog
- group: auth
  href: https://artifacts.apis.io/waterr-ai/security/waterr-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/waterr-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://waterr.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.waterr.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.waterr.ai/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.waterr.ai/api-reference/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://waterr.ai/pricing
created: '2026-10-31'
description: Waterr AI provides an AI‑driven meeting platform that runs video calls on behalf of users. It can conduct interviews, discovery sessions, role‑play sales calls, and intake meetings, returning a recording, transcript and a rubric‑scored analysis. The service offers a unified API for authentication, SDKs, webhooks and rate‑limit management, enabling developers to integrate AI meeting agents into their applications.
image: https://waterr.ai/og-image-v2.png
json_schemas:
- name: Avatar
  property_count: 17
  slug: waterr-ai-avatar
- name: CustomFunction
  property_count: 16
  slug: waterr-ai-custom-function
- name: Guardrail
  property_count: 8
  slug: waterr-ai-guardrail
- name: MemoryContainer
  property_count: 7
  slug: waterr-ai-memory-container
- name: Memory
  property_count: 9
  slug: waterr-ai-memory
- name: Skill
  property_count: 10
  slug: waterr-ai-skill
jsonld:
- class_count: 17
  name: Waterr Ai Context
  property_count: 105
  slug: waterr-ai-context
layout: provider
modified: '2026-10-31'
name: waterr-ai
nav: Providers
network: true
overview: 'waterr-ai publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including WaterrAI API API, and 1 more. Tagged areas include Company, Artificial Intelligence, Meetings, Video, and Automation.


  The waterr-ai catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  waterr-ai''s developer surface includes changelog, authentication, engineering blog, documentation, API reference, getting-started guide, pricing, and 23 more developer resources.'
plans:
- name: Waterr Ai Plans Pricing
  plan_count: 5
  slug: waterr-ai-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Waterr Ai Rate Limits
  slug: waterr-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: waterr-ai API Rules
  rule_count: 58
  severity_counts:
    error: 48
    hint: 0
    info: 3
    warn: 7
  slug: waterr-ai-rules
score:
  band: developing
  composite: 48.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.8
  facets:
    access_clarity: 51.3
    contract_governance: 22.0
    contract_quality: 64.3
    developer_ergonomics: 27.4
    discoverability: 66.1
    operational_transparency: 51.3
  previous_composite: 57.5
  provenance:
    conformance: derived
    mcp: derived
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
security:
- kind: authentication
  name: Waterr Ai Authentication
  slug: waterr-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Waterr Ai Domain Security
  slug: waterr-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: waterr-ai
tags:
- Company
- Artificial Intelligence
- Meetings
- Video
- Automation
website: https://waterr.ai/
---
