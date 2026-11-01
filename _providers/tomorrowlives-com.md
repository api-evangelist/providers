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
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 64
  human_in_the_loop: 4
  name: Tomorrowlives Com Agentic Access
  operation_count: 72
  slug: tomorrowlives-com-agentic-access
  summary_line: 72 operations · 64 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://tomorrowlives.com
  baseurl_source: declared
  description: Sign up, name the owner, buy a pass or a unit pack, read the meter and the notices.
  name: tomorrowlives-com Account API
  slug: tomorrowlives-com-account-api
- baseURL: https://tomorrowlives.com
  baseurl_source: declared
  description: Queued jobs, their files and cancelling them.
  name: tomorrowlives-com Jobs API
  slug: tomorrowlives-com-jobs-api
- baseURL: https://tomorrowlives.com
  baseurl_source: declared
  description: Research instruments (https://tomorrowlives.com/lab). The pull engine measures whether one agent follows another beyond chance and labels the result.
  name: tomorrowlives-com Lab API
  slug: tomorrowlives-com-lab-api
- baseURL: https://tomorrowlives.com
  baseurl_source: declared
  description: The same verbs as MCP tools.
  name: tomorrowlives-com MCP API
  slug: tomorrowlives-com-mcp-api
- baseURL: https://tomorrowlives.com
  baseurl_source: declared
  description: 'The seven engines that make an asset: print designs, materials, forms, characters, terrain, voice and video. The same request returns the same bytes.'
  name: tomorrowlives-com Production engines API
  slug: tomorrowlives-com-production-engines-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/tomorrowlives-com/agentic-access/tomorrowlives-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tomorrowlives-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/tomorrowlives-com/plans/tomorrowlives-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tomorrowlives-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/tomorrowlives-com/rules/tomorrowlives-com-rules.yml
  title: ''
  type: Spectral
  url: rules/tomorrowlives-com-rules.yml
- group: design
  href: https://artifacts.apis.io/tomorrowlives-com/json-ld/tomorrowlives-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tomorrowlives-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/tomorrowlives-com/vocabulary/tomorrowlives-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tomorrowlives-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/tomorrowlives-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/tomorrowlives-com/data-model/tomorrowlives-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tomorrowlives-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/tomorrowlives-com/authentication/tomorrowlives-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tomorrowlives-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/tomorrowlives-com/errors/tomorrowlives-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tomorrowlives-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tomorrowlives-com/conformance/tomorrowlives-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tomorrowlives-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tomorrowlives-com/llms/tomorrowlives-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tomorrowlives-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/tomorrowlives-com/well-known/tomorrowlives-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tomorrowlives-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/tomorrowlives-com/hosts/tomorrowlives-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tomorrowlives-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/tomorrowlives-com/vendors/tomorrowlives-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tomorrowlives-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tomorrowlives.com/account/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tomorrowlives.com/account/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://tomorrowlives.com/lab/pull/pricing
- group: auth
  href: https://artifacts.apis.io/tomorrowlives-com/security/tomorrowlives-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tomorrowlives-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tomorrowlives.com/
- group: docs
  title: ''
  type: Documentation
  url: https://tomorrowlives.com/lab
- group: docs
  title: ''
  type: APIReference
  url: https://tomorrowlives.com/api/agents/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://tomorrowlives.com/engines
- group: company
  title: ''
  type: Blog
  url: https://tomorrowlives.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://tomorrowlives.com/account/login
created: '2026-10-31'
description: Tomorrow Lives Studio offers a suite of generative AI engines that produce printable designs, textures, characters, terrain, voice, forms, and short videos. These engines are accessible via a REST API and MCP, allowing software agents to request assets on demand. The platform operates on a pay‑per‑use model with a 30‑day pass and provides documentation, a developer portal, and an open OpenAPI specification.
image: https://tomorrowlives.com/engines/og-engines.jpg
json_schemas:
- name: Job
  property_count: 6
  slug: tomorrowlives-com-job
- name: JobState
  property_count: 0
  slug: tomorrowlives-com-job-state
- name: JobStatus
  property_count: 15
  slug: tomorrowlives-com-job-status
- name: QueuedJob
  property_count: 8
  slug: tomorrowlives-com-queued-job
- name: Signup
  property_count: 5
  slug: tomorrowlives-com-signup
- name: Subscription
  property_count: 0
  slug: tomorrowlives-com-subscription
jsonld:
- class_count: 7
  name: Tomorrowlives Com Context
  property_count: 31
  slug: tomorrowlives-com-context
layout: provider
modified: '2026-10-31'
name: tomorrowlives-com
nav: Providers
network: true
overview: 'tomorrowlives-com publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Jobs API, Lab API, and 2 more. Tagged areas include AI, Generative, Engines, API, and Creative.


  The tomorrowlives-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  tomorrowlives-com''s developer surface includes authentication, pricing, documentation, API reference, getting-started guide, engineering blog, signup flow, and 17 more developer resources.'
plans:
- name: Tomorrowlives Com Plans Pricing
  plan_count: 3
  slug: tomorrowlives-com-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Tomorrowlives Com Rate Limits
  slug: tomorrowlives-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: tomorrowlives-com API Rules
  rule_count: 17
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 4
  slug: tomorrowlives-com-rules
score:
  band: strong
  composite: 57.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 88.5
    catalog_earned_first_party: 0.0
    catalog_gap: 26.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 61.9
    developer_ergonomics: 49.3
    discoverability: 66.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Tomorrowlives Com Authentication
  slug: tomorrowlives-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Tomorrowlives Com Domain Security
  slug: tomorrowlives-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: art-render
  slug: tomorrowlives-com-art-render
slug: tomorrowlives-com
tags:
- AI
- Generative
- Engines
- API
- Creative
website: https://tomorrowlives.com/
---
