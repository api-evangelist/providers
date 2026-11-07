---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Entitylight Agentic Access
  operation_count: 20
  slug: entitylight-agentic-access
  summary_line: 20 operations · 10 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.entitylight.com/v1
  baseurl_source: declared
  description: The Business Searches API from Entitylight — 2 operation(s) for business searches.
  name: Entitylight Business Searches API
  slug: entitylight-business-searches-api
- baseURL: https://api.entitylight.com/v1
  baseurl_source: declared
  description: The Lookups API from Entitylight — 4 operation(s) for lookups.
  name: Entitylight Lookups API
  slug: entitylight-lookups-api
- baseURL: https://api.entitylight.com/v1
  baseurl_source: declared
  description: The Ofac Screenings API from Entitylight — 2 operation(s) for ofac screenings.
  name: Entitylight Ofac Screenings API
  slug: entitylight-ofac-screenings-api
- baseURL: https://api.entitylight.com/v1
  baseurl_source: declared
  description: The Ucc Searches API from Entitylight — 2 operation(s) for ucc searches.
  name: Entitylight Ucc Searches API
  slug: entitylight-ucc-searches-api
- baseURL: https://api.entitylight.com/v1
  baseurl_source: declared
  description: The Usage API from Entitylight — 1 operation(s) for usage.
  name: Entitylight Usage API
  slug: entitylight-usage-api
- baseURL: https://api.entitylight.com/v1
  baseurl_source: declared
  description: The Watches API from Entitylight — 2 operation(s) for watches.
  name: Entitylight Watches API
  slug: entitylight-watches-api
- baseURL: https://api.entitylight.com/v1
  baseurl_source: declared
  description: The Webhook API from Entitylight — 2 operation(s) for webhook.
  name: Entitylight Webhook API
  slug: entitylight-webhook-api
artifact_total: 22
asyncapis:
- description: ''
  name: Entitylight Webhooks
  slug: entitylight-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/entitylight/agentic-access/entitylight-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/entitylight-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/entitylight/plans/entitylight-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/entitylight-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/entitylight/rules/entitylight-rules.yml
  title: ''
  type: Spectral
  url: rules/entitylight-rules.yml
- group: design
  href: https://artifacts.apis.io/entitylight/json-ld/entitylight-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/entitylight-context.jsonld
- group: design
  href: https://artifacts.apis.io/entitylight/vocabulary/entitylight-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/entitylight-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/entitylight/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/entitylight/asyncapi/entitylight-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/entitylight-webhooks.yml
- group: design
  href: https://artifacts.apis.io/entitylight/data-model/entitylight-data-model.yml
  title: ''
  type: DataModel
  url: data-model/entitylight-data-model.yml
- group: auth
  href: https://artifacts.apis.io/entitylight/authentication/entitylight-authentication.yml
  title: ''
  type: Authentication
  url: authentication/entitylight-authentication.yml
- group: design
  href: https://artifacts.apis.io/entitylight/errors/entitylight-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/entitylight-problem-types.yml
- group: design
  href: https://artifacts.apis.io/entitylight/conformance/entitylight-conformance.yml
  title: ''
  type: Conformance
  url: conformance/entitylight-conformance.yml
- group: agent
  href: https://artifacts.apis.io/entitylight/llms/entitylight-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/entitylight-llms.txt
- group: other
  href: https://artifacts.apis.io/entitylight/hosts/entitylight-hosts.yml
  title: ''
  type: Hosts
  url: hosts/entitylight-hosts.yml
- group: other
  href: https://artifacts.apis.io/entitylight/vendors/entitylight-vendors.yml
  title: ''
  type: Vendors
  url: vendors/entitylight-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://entitylight.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://entitylight.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://entitylight.com/pricing
- group: start
  title: ''
  type: Login
  url: https://entitylight.com/sign-in
- group: auth
  href: https://artifacts.apis.io/entitylight/security/entitylight-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/entitylight-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://entitylight.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://entitylight.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://entitylight.com/docs
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/entitylight
created: '2026-10-30'
description: Entitylight provides a unified API for accessing Secretary of State records, UCC filings, and court case data, enabling lenders and businesses to perform comprehensive business verification, lien searches, and lawsuit monitoring. The platform offers real-time alerts for new liens and lawsuits, detailed reporting, and a pricing model for scalable usage.
image: https://entitylight.com/opengraph-image
json_schemas:
- name: BusinessSearch
  property_count: 10
  slug: entitylight-business-search
- name: Lookup
  property_count: 19
  slug: entitylight-lookup
- name: OfacScreening
  property_count: 11
  slug: entitylight-ofac-screening
- name: UccSearch
  property_count: 11
  slug: entitylight-ucc-search
- name: Usage
  property_count: 7
  slug: entitylight-usage
- name: Watch
  property_count: 12
  slug: entitylight-watch
jsonld:
- class_count: 17
  name: Entitylight Context
  property_count: 61
  slug: entitylight-context
layout: provider
modified: '2026-10-30'
name: Entitylight
nav: Providers
network: true
overview: 'Entitylight publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Business Searches API, Lookups API, Ofac Screenings API, and 4 more. Tagged areas include Company, Business, UCC, Litigation, and Monitoring.


  The Entitylight catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Entitylight''s developer surface includes authentication, pricing, getting-started guide, and 20 more developer resources.'
plans:
- name: Entitylight Plans Pricing
  plan_count: 4
  slug: entitylight-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Entitylight Rate Limits
  slug: entitylight-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Entitylight API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: entitylight-rules
scopes:
- name: Entitylight Scopes
  scope_count: 0
  slug: entitylight-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.6
  coverage:
    artifact_dirs: 32
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 67.9
    developer_ergonomics: 31.4
    discoverability: 73.2
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 54.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/entitylight/entitylight-2026-11-03T131534.png
security:
- kind: authentication
  name: Entitylight Authentication
  slug: entitylight-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Entitylight Domain Security
  slug: entitylight-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: entitylight
tags:
- Company
- Business
- UCC
- Litigation
- Monitoring
website: https://entitylight.com
---
