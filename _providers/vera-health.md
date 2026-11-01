---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 59.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Vera Health Agentic Access
  operation_count: 6
  slug: vera-health-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 2
apis:
- baseURL: https://www.verahealth.ai
  baseurl_source: declared
  description: The Chat API from Vera Health — 6 operation(s) for chat.
  name: Vera Health Chat API
  slug: vera-health-chat-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/vera-health/agentic-access/vera-health-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/vera-health-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/vera-health/rate-limits/vera-health-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vera-health-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/vera-health/rules/vera-health-rules.yml
  title: ''
  type: Spectral
  url: rules/vera-health-rules.yml
- group: design
  href: https://artifacts.apis.io/vera-health/json-ld/vera-health-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/vera-health-context.jsonld
- group: design
  href: https://artifacts.apis.io/vera-health/vocabulary/vera-health-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/vera-health-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/vera-health/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/vera-health/data-model/vera-health-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vera-health-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.verahealth.ai/
- group: auth
  href: https://artifacts.apis.io/vera-health/authentication/vera-health-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vera-health-authentication.yml
- group: design
  href: https://artifacts.apis.io/vera-health/errors/vera-health-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/vera-health-problem-types.yml
- group: design
  href: https://artifacts.apis.io/vera-health/conformance/vera-health-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vera-health-conformance.yml
- group: agent
  href: https://artifacts.apis.io/vera-health/llms/vera-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vera-health-llms.txt
- group: other
  href: https://artifacts.apis.io/vera-health/a2a/vera-health-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/vera-health-a2a.yml
- group: agent
  href: https://artifacts.apis.io/vera-health/well-known/vera-health-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vera-health-well-known.yml
- group: other
  href: https://artifacts.apis.io/vera-health/hosts/vera-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vera-health-hosts.yml
- group: other
  href: https://artifacts.apis.io/vera-health/vendors/vera-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vera-health-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.verahealth.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.verahealth.ai/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://verahealth.ai/news
- group: company
  title: ''
  type: Blog
  url: https://www.verahealth.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.verahealth.ai/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.verahealth.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.verahealth.ai/api-reference/v1/chat
- group: auth
  href: https://artifacts.apis.io/vera-health/security/vera-health-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/vera-health-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/vera-health/security/vera-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vera-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.verahealth.ai/home
created: '2026-10-29'
description: Vera Health provides AI‑driven clinical decision support, offering clinicians rapid access to medical knowledge, guidelines, drug references, calculators and peer‑reviewed sources. Backed by Gradient Ventures, the platform combines evidence‑based content with large language models to answer point‑of‑care questions, accelerate research and improve patient outcomes across specialties.
image: https://verahealth.ai/og_banner.png
json_schemas:
- name: AgentChatRequest
  property_count: 6
  slug: vera-health-agent-chat-request
- name: AgentChatResponse
  property_count: 6
  slug: vera-health-agent-chat-response
- name: ChatRequest
  property_count: 4
  slug: vera-health-chat-request
- name: ChatResponse
  property_count: 3
  slug: vera-health-chat-response
- name: QuotasResponse
  property_count: 1
  slug: vera-health-quotas-response
jsonld:
- class_count: 23
  name: Vera Health Context
  property_count: 65
  slug: vera-health-context
layout: provider
modified: '2026-10-29'
name: Vera Health
nav: Providers
network: true
overview: 'Vera Health publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Chat API. Tagged areas include Health, AI, Clinical Decision Support, Medical Knowledge, and Healthcare.


  The Vera Health catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Vera Health''s developer surface includes authentication, engineering blog, getting-started guide, documentation, API reference, and 21 more developer resources.'
plans:
- name: Vera Health Plans Pricing
  plan_count: 0
  slug: vera-health-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Vera Health Rate Limits
  slug: vera-health-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Vera Health API Rules
  rule_count: 18
  severity_counts:
    error: 15
    hint: 0
    info: 2
    warn: 1
  slug: vera-health-rules
scopes:
- name: Vera Health Scopes
  scope_count: 0
  slug: vera-health-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.2
  coverage:
    artifact_dirs: 31
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 69.3
    developer_ergonomics: 44.6
    discoverability: 67.9
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 34.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Vera Health Authentication
  slug: vera-health-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Vera Health Domain Security
  slug: vera-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Vera Health Trust Center
  slug: vera-health-trust-center
  summary_line: SOC 2, HIPAA, GDPR
skill_count: 1
skills:
- name: chat
  slug: vera-health-chat
slug: vera-health
tags:
- Health
- AI
- Clinical Decision Support
- Medical Knowledge
- Healthcare
website: https://www.verahealth.ai/home
---
