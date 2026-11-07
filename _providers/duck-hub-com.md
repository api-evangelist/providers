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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 37
  human_in_the_loop: 37
  name: Duck Hub Com Agentic Access
  operation_count: 62
  slug: duck-hub-com-agentic-access
  summary_line: 62 operations · 37 acting · 37 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.duck-hub.com
  baseurl_source: declared
  description: The IntegrationsPublic API from Duckhub — 40 operation(s) for integrationspublic.
  name: Duckhub Integrations Public API
  slug: duck-hub-com-integrationspublic-api
- baseURL: https://api.duck-hub.com
  baseurl_source: declared
  description: The Open API API from Duckhub — 1 operation(s) for open api.
  name: Duckhub Open API
  slug: duck-hub-com-open-api-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/duck-hub-com/agentic-access/duck-hub-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/duck-hub-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/duck-hub-com/rate-limits/duck-hub-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/duck-hub-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/duck-hub-com/rules/duck-hub-com-rules.yml
  title: ''
  type: Spectral
  url: rules/duck-hub-com-rules.yml
- group: design
  href: https://artifacts.apis.io/duck-hub-com/json-ld/duck-hub-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/duck-hub-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/duck-hub-com/vocabulary/duck-hub-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/duck-hub-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/duck-hub-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/duck-hub-com/data-model/duck-hub-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/duck-hub-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/duck-hub-com/authentication/duck-hub-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/duck-hub-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/duck-hub-com/lifecycle/duck-hub-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/duck-hub-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/duck-hub-com/errors/duck-hub-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/duck-hub-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/duck-hub-com/conformance/duck-hub-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/duck-hub-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/duck-hub-com/llms/duck-hub-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/duck-hub-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/duck-hub-com/well-known/duck-hub-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/duck-hub-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/duck-hub-com/hosts/duck-hub-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/duck-hub-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/duck-hub-com/vendors/duck-hub-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/duck-hub-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.duck-hub.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.duck-hub.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.duck-hub.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.duck-hub.com/reference
- group: docs
  title: ''
  type: Documentation
  url: https://docs.duck-hub.com/
- group: auth
  href: https://artifacts.apis.io/duck-hub-com/security/duck-hub-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/duck-hub-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.duck-hub.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.duck-hub.com/v1/openapi.json
  - status: 401
    url: https://api.duck-hub.com/mcp
  - status: 200
    url: https://duck-hub.com/
  reason: partner-login
  state: gated
created: '2026-11-06'
description: Duckhub provides an AI‑powered QR menu platform for restaurants, enabling owners to create digital menus in minutes, integrate ChatGPT or Claude for automatic dish descriptions, translate into multiple languages, and sell with zero commission. The service offers a free forever plan and a range of paid features, positioning itself as a no‑fee, AI‑enhanced solution for modern eateries.
image: https://www.duck-hub.com/opengraph-image-pwu6ef?f4baad62cae91e2e
json_schemas:
- name: CleanupDto
  property_count: 4
  slug: duck-hub-com-cleanup-dto
- name: CleanupResponseDto
  property_count: 7
  slug: duck-hub-com-cleanup-response-dto
- name: SyncResponseDto
  property_count: 8
  slug: duck-hub-com-sync-response-dto
- name: V1CreateBannerDto
  property_count: 5
  slug: duck-hub-com-v1-create-banner-dto
- name: V1CreateModifierGroupDto
  property_count: 5
  slug: duck-hub-com-v1-create-modifier-group-dto
- name: V1PatchProductDto
  property_count: 12
  slug: duck-hub-com-v1-patch-product-dto
jsonld:
- class_count: 41
  name: Duck Hub Com Context
  property_count: 74
  slug: duck-hub-com-context
layout: provider
modified: '2026-11-06'
name: Duckhub
nav: Providers
network: true
overview: 'Duckhub publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Integrations Public API and Open API. Tagged areas include Artificial Intelligence, QR, Restaurant, Software-as-a-Service, and Menus.


  The Duckhub catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Duckhub''s developer surface includes authentication, engineering blog, API reference, documentation, and 18 more developer resources.'
random_paper: 23
rate_limits:
- limit_count: 11
  name: Duck Hub Com Rate Limits
  slug: duck-hub-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Duckhub API Rules
  rule_count: 47
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 5
  slug: duck-hub-com-rules
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 35.6
    contract_quality: 55.5
    developer_ergonomics: 32.7
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Duck Hub Com Authentication
  slug: duck-hub-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Duck Hub Com Domain Security
  slug: duck-hub-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: duck-hub-com-publish-product
  slug: duck-hub-com-publish-product
slug: duck-hub-com
tags:
- Artificial Intelligence
- QR
- Restaurant
- Software-as-a-Service
- Menus
- Company
website: https://www.duck-hub.com/
---
