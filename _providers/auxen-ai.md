---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 45
  human_in_the_loop: 0
  name: Auxen Ai Agentic Access
  operation_count: 71
  slug: auxen-ai-agentic-access
  summary_line: 71 operations · 45 acting
api_count: 1
apis:
- baseURL: https://api.auxen.ai
  baseurl_source: declared
  description: The Billing API from Auxen — 4 operation(s) for billing.
  name: Auxen Billing API
  slug: auxen-ai-billing-api
- baseURL: https://api.auxen.ai
  baseurl_source: declared
  description: The Deployments API from Auxen — 8 operation(s) for deployments.
  name: Auxen Deployments API
  slug: auxen-ai-deployments-api
- baseURL: https://api.auxen.ai
  baseurl_source: declared
  description: The Deprecated API from Auxen — 10 operation(s) for deprecated.
  name: Auxen Deprecated API
  slug: auxen-ai-deprecated-api
- baseURL: https://api.auxen.ai
  baseurl_source: declared
  description: The Inference API from Auxen — 2 operation(s) for inference.
  name: Auxen Inference API
  slug: auxen-ai-inference-api
- baseURL: https://api.auxen.ai
  baseurl_source: declared
  description: The Models API from Auxen — 2 operation(s) for models.
  name: Auxen Models API
  slug: auxen-ai-models-api
- baseURL: https://api.auxen.ai
  baseurl_source: declared
  description: The Pay with USDC API from Auxen — 6 operation(s) for pay with usdc.
  name: Auxen Pay with USDC API
  slug: auxen-ai-pay-with-usdc-api
- baseURL: https://api.auxen.ai
  baseurl_source: declared
  description: The Scheduling API from Auxen — 3 operation(s) for scheduling.
  name: Auxen Scheduling API
  slug: auxen-ai-scheduling-api
- baseURL: https://api.auxen.ai
  baseurl_source: declared
  description: The Webhooks API from Auxen — 4 operation(s) for webhooks.
  name: Auxen Webhooks API
  slug: auxen-ai-webhooks-api
- baseURL: https://api.auxen.ai
  baseurl_source: declared
  description: The Workers API from Auxen — 16 operation(s) for workers.
  name: Auxen Workers API
  slug: auxen-ai-workers-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/auxen-ai/agentic-access/auxen-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/auxen-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/auxen-ai/rate-limits/auxen-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/auxen-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/auxen-ai/plans/auxen-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/auxen-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/auxen-ai/rules/auxen-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/auxen-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/auxen-ai/json-ld/auxen-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/auxen-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/auxen-ai/vocabulary/auxen-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/auxen-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/auxen-ai/data-model/auxen-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/auxen-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/auxen-ai/authentication/auxen-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/auxen-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/auxen-ai/lifecycle/auxen-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/auxen-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/auxen-ai/errors/auxen-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/auxen-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/auxen-ai/conformance/auxen-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/auxen-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/auxen-ai/llms/auxen-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/auxen-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/auxen-ai/a2a/auxen-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/auxen-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/auxen-ai/well-known/auxen-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/auxen-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/auxen-ai/hosts/auxen-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auxen-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/auxen-ai/vendors/auxen-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/auxen-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://auxen.ai/security
- group: start
  title: ''
  type: Login
  url: https://auxen.ai/login
- group: auth
  href: https://artifacts.apis.io/auxen-ai/security/auxen-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auxen-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://auxen.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://auxen.ai/docs/agents
- group: docs
  title: ''
  type: APIReference
  url: https://api.auxen.ai/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://auxen.ai/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://auxen.ai/builders#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://auxen.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://auxen.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/auxen-ai
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://auxen.ai/openapi.json
  - status: null
    url: https://api.auxen.ai/openapi.json
  - status: 401
    url: https://api.auxen.ai/mcp
  - status: 200
    url: https://auxen.ai/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: Auxen provides an AI‑powered platform that lets users hire autonomous AI workers to monitor websites, track price changes, watch status pages, and perform automated actions. Users define jobs with a brief, schedule, and budget; the workers run on schedule, read only allowed sites, and report results via email, Slack, or other integrations. The service is billed per minute of AI compute and offers a free test run.
image: https://auxen.ai/favicon.ico
json_schemas:
- name: Deployment
  property_count: 19
  slug: auxen-ai-deployment
- name: Meta
  property_count: 2
  slug: auxen-ai-meta
- name: Model
  property_count: 20
  slug: auxen-ai-model
jsonld:
- class_count: 9
  name: Auxen Ai Context
  property_count: 43
  slug: auxen-ai-context
layout: provider
modified: '2026-11-02'
name: Auxen
nav: Providers
network: true
overview: 'Auxen publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing API, Deployments API, Deprecated API, and 6 more. Tagged areas include Artificial Intelligence, Automation, Platform, Workers, and Productivity.


  The Auxen catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Auxen''s developer surface includes authentication, documentation, API reference, support, pricing, and 22 more developer resources.'
plans:
- name: Auxen Ai Plans Pricing
  plan_count: 2
  slug: auxen-ai-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Auxen Ai Rate Limits
  slug: auxen-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Auxen API Rules
  rule_count: 51
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 5
  slug: auxen-ai-rules
scopes:
- name: Auxen Ai Scopes
  scope_count: 0
  slug: auxen-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 34
    catalog_earned: 78.8
    catalog_earned_first_party: 16.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.2
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 62.0
    developer_ergonomics: 22.6
    discoverability: 66.1
    operational_transparency: 28.9
  previous_composite: 51.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
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
  name: Auxen Ai Authentication
  slug: auxen-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Auxen Ai Domain Security
  slug: auxen-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: auxen-ai
tags:
- Artificial Intelligence
- Automation
- Platform
- Workers
- Productivity
website: https://auxen.ai/
---
