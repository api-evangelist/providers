---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: unknown
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 54.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 190
  human_in_the_loop: 2
  name: Relaystation Ai Agentic Access
  operation_count: 244
  slug: relaystation-ai-agentic-access
  summary_line: 244 operations · 190 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: Pay-per-call API platform for AI agents and developers.
  name: Relaystation API
  slug: relaystation-api
- baseURL: https://api.relaystation.ai
  baseurl_source: declared
  description: Pay-per-call API platform for AI agents and developers. Baton — a prepaid storage object configured along five groups (write behavior · capacity · sharing · lifecycle · trust); five named preconfigs (
  name: Relaystation Api API
  slug: relaystation-api-api
artifact_total: 15
asyncapis:
- description: ''
  name: Relaystation Ai Webhooks
  slug: relaystation-ai-webhooks
common:
- group: design
  href: https://artifacts.apis.io/relaystation-ai/rules/relaystation-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/relaystation-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/relaystation-ai/json-ld/relaystation-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/relaystation-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/relaystation-ai/vocabulary/relaystation-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/relaystation-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/relaystation-ai/conformance/relaystation-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/relaystation-ai-conformance.yml
- group: design
  href: https://artifacts.apis.io/relaystation-ai/asyncapi/relaystation-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/relaystation-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/relaystation-ai/data-model/relaystation-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/relaystation-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/relaystation-ai/conventions/relaystation-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/relaystation-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/relaystation-ai/conventions/relaystation-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/relaystation-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/relaystation-ai/authentication/relaystation-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/relaystation-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/relaystation-ai/errors/relaystation-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/relaystation-ai-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/relaystation-ai/llms/relaystation-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/relaystation-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/relaystation-ai/well-known/relaystation-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/relaystation-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/relaystation-ai/hosts/relaystation-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/relaystation-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/relaystation-ai/vendors/relaystation-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/relaystation-ai-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://relaystation.ai/solutions/developers
- group: auth
  href: https://artifacts.apis.io/relaystation-ai/security/relaystation-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/relaystation-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://relaystation.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://relaystation.ai/docs/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://relaystation.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://relaystation.ai/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://relaystation.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://relaystation.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://relaystation.ai/privacy
created: '2026-10-31'
description: RelayStation AI is an emerging technology company focused on providing advanced AI-driven relay services for real-time data transmission and processing across distributed networks. The platform enables developers and enterprises to integrate intelligent routing, transformation, and analytics capabilities into their applications, leveraging scalable cloud infrastructure and cutting‑edge machine learning models. RelayStation AI aims to simplify complex data workflows, improve latency, and enhance reliability for IoT, edge computing, and enterprise integration scenarios, positioning itself as a pivotal middleware solution in the evolving AI and data ecosystem.
image: https://relaystation.ai/og.png
json_schemas:
- name: TabularFormat
  property_count: 0
  slug: relaystation-ai-tabular-format
- name: V1Webhook
  property_count: 9
  slug: relaystation-ai-v1-webhook
- name: WebhookEventName
  property_count: 0
  slug: relaystation-ai-webhook-event-name
jsonld:
- class_count: 5
  name: Relaystation Ai Context
  property_count: 18
  slug: relaystation-ai-context
layout: provider
modified: '2026-10-31'
name: relaystation-ai
nav: Providers
network: true
overview: 'relaystation-ai publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Relaystation Api API, and 1 more. Tagged areas include Company, AI, Data-Relay, Real-time, and Cloud.


  The relaystation-ai catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  relaystation-ai''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, and 18 more developer resources.'
plans:
- name: Relaystation Ai Plans Pricing
  plan_count: 0
  slug: relaystation-ai-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Relaystation Ai Rate Limits
  slug: relaystation-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: relaystation-ai API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 2
  slug: relaystation-ai-rules
scopes:
- name: Relaystation Ai Scopes
  scope_count: 0
  slug: relaystation-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 52.2
  coverage:
    artifact_dirs: 30
    catalog_earned: 77.7
    catalog_earned_first_party: 0.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 79.1
    contract_quality: 64.9
    developer_ergonomics: 50.0
    discoverability: 66.1
    operational_transparency: 7.9
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
  name: Relaystation Ai Authentication
  slug: relaystation-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Relaystation Ai Domain Security
  slug: relaystation-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: ask-operator
  slug: relaystation-ai-ask_operator
slug: relaystation-ai
tags:
- Company
- AI
- Data-Relay
- Real-time
- Cloud
website: https://relaystation.ai/
---
