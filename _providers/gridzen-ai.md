---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Gridzen Ai Agentic Access
  operation_count: 3
  slug: gridzen-ai-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- baseURL: https://gridzen.ai/developers/api/
  baseurl_source: declared
  description: The health API from gridzen-ai — 1 operation(s) for health.
  name: gridzen-ai Health API
  slug: gridzen-ai-health-api
- baseURL: https://gridzen.ai/developers/api/
  baseurl_source: declared
  description: The trust-decisions API from gridzen-ai — 2 operation(s) for trust-decisions.
  name: gridzen-ai Trust Decisions API
  slug: gridzen-ai-trust-decisions-api
artifact_total: 12
asyncapis:
- description: ''
  name: Gridzen Ai Webhooks
  slug: gridzen-ai-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/gridzen-ai/agentic-access/gridzen-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gridzen-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/gridzen-ai/plans/gridzen-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gridzen-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/gridzen-ai/rules/gridzen-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/gridzen-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/gridzen-ai/json-ld/gridzen-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gridzen-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/gridzen-ai/vocabulary/gridzen-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gridzen-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/gridzen-ai/asyncapi/gridzen-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/gridzen-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/gridzen-ai/data-model/gridzen-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gridzen-ai-data-model.yml
- group: build
  href: https://artifacts.apis.io/gridzen-ai/cli/gridzen-ai-cli.yml
  title: ''
  type: CLI
  url: cli/gridzen-ai-cli.yml
- group: auth
  href: https://artifacts.apis.io/gridzen-ai/authentication/gridzen-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gridzen-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/gridzen-ai/errors/gridzen-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gridzen-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gridzen-ai/conformance/gridzen-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gridzen-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gridzen-ai/llms/gridzen-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gridzen-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/gridzen-ai/well-known/gridzen-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gridzen-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/gridzen-ai/hosts/gridzen-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gridzen-ai-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://gridzen.ai/security/
- group: start
  title: ''
  type: Sandbox
  url: https://gridzen.ai/console/?lang=en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gridzen.ai/privacy/
- group: start
  title: ''
  type: GettingStarted
  url: https://gridzen.ai/developers/quickstart.html
- group: docs
  title: ''
  type: APIReference
  url: https://gridzen.ai/developers/?lang=en
- group: auth
  href: https://artifacts.apis.io/gridzen-ai/security/gridzen-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gridzen-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gridzen.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://gridzen.ai/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://gridzen.ai/pricing/
created: '2026-10-30'
description: GridZen AI is an emerging artificial intelligence platform focused on providing advanced grid optimization solutions for renewable energy management. The company leverages machine learning to predict energy demand, balance supply across distributed resources, and enhance grid stability for utilities and large-scale energy producers. Their services include real-time analytics, forecasting tools, and integration APIs that enable seamless data exchange between grid operators and AI-driven optimization engines. GridZen AI aims to accelerate the transition to sustainable energy by improving efficiency and reducing operational costs.
image: https://gridzen.ai/assets/og/og-default.png
json_schemas:
- name: DecisionRequest
  property_count: 4
  slug: gridzen-ai-decision-request
- name: DecisionResponse
  property_count: 9
  slug: gridzen-ai-decision-response
- name: DecisionTrace
  property_count: 9
  slug: gridzen-ai-decision-trace
jsonld:
- class_count: 10
  name: Gridzen Ai Context
  property_count: 36
  slug: gridzen-ai-context
layout: provider
modified: '2026-10-30'
name: gridzen-ai
nav: Providers
network: true
overview: 'gridzen-ai publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Health API and Trust Decisions API. Tagged areas include Company, AI, Energy, Grid, and Optimization.


  The gridzen-ai catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  gridzen-ai''s developer surface includes CLI, authentication, sandbox, getting-started guide, API reference, documentation, pricing, and 16 more developer resources.'
plans:
- name: Gridzen Ai Plans Pricing
  plan_count: 8
  slug: gridzen-ai-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: gridzen-ai API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: gridzen-ai-rules
score:
  band: strong
  composite: 54.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 88.5
    catalog_earned_first_party: 0.0
    catalog_gap: 26.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 49.5
    contract_governance: 79.1
    contract_quality: 58.6
    developer_ergonomics: 54.8
    discoverability: 66.1
    operational_transparency: 18.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Gridzen Ai Authentication
  slug: gridzen-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Gridzen Ai Domain Security
  slug: gridzen-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: gridzen-ai
tags:
- Company
- AI
- Energy
- Grid
- Optimization
website: https://gridzen.ai/
---
