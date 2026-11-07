---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Gage platform offering endpoints for builders, fabricators and installers. Documentation at the API reference page.
  name: Gage API
  slug: gage-api
- description: 'Gage API as documented publicly: 41 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Gage API
  slug: buildwithgage-com-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/buildwithgage-com/plans/buildwithgage-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/buildwithgage-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/buildwithgage-com/rules/buildwithgage-com-rules.yml
  title: ''
  type: Spectral
  url: rules/buildwithgage-com-rules.yml
- group: design
  href: https://artifacts.apis.io/buildwithgage-com/json-ld/buildwithgage-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/buildwithgage-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/buildwithgage-com/vocabulary/buildwithgage-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/buildwithgage-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/buildwithgage-com/data-model/buildwithgage-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/buildwithgage-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/buildwithgage-com/authentication/buildwithgage-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/buildwithgage-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/buildwithgage-com/conformance/buildwithgage-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buildwithgage-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/buildwithgage-com/llms/buildwithgage-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buildwithgage-com-llms.txt
- group: other
  href: https://artifacts.apis.io/buildwithgage-com/hosts/buildwithgage-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buildwithgage-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/buildwithgage-com/vendors/buildwithgage-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buildwithgage-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://buildwithgage.com/login
- group: auth
  href: https://artifacts.apis.io/buildwithgage-com/security/buildwithgage-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buildwithgage-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buildwithgage.com/
- group: docs
  title: ''
  type: Documentation
  url: https://buildwithgage.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://buildwithgage.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://buildwithgage.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://buildwithgage.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buildwithgage.com/docs/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buildwithgage.com/docs/legal/privacy
coverage:
  checked: '2026-11-03'
  detail: The provider's API reference page is HTML with no downloadable OpenAPI, AsyncAPI, GraphQL or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://buildwithgage.com/docs/api/reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Gage is a marketplace for cold‑formed steel framing. Builders submit plans, Gage reads them, prices the frame at nearby fabricators, and manages the job from approval through production to delivery. The platform connects fabricators, installers, architects, and builders, offering instant quotes and streamlined ordering for steel frames.
image: https://buildwithgage.com/og/gage-default.png
json_schemas:
- name: GetApiV1PricingRatesResponse
  property_count: 6
  slug: buildwithgage-com-get-api-v1-pricing-rates-response
- name: GetApiV1QuotesQteAb12Cd34Ef56Gh78Response
  property_count: 8
  slug: buildwithgage-com-get-api-v1-quotes-qte-ab12-cd34-ef56-gh78-response
- name: PostApiV1ProjectsRequest
  property_count: 10
  slug: buildwithgage-com-post-api-v1-projects-request
- name: PostApiV1QuotesQteAb12Cd34Ef56Gh78AcceptResponse
  property_count: 8
  slug: buildwithgage-com-post-api-v1-quotes-qte-ab12-cd34-ef56-gh78-accept-response
- name: PostApiV1QuotesRequest
  property_count: 20
  slug: buildwithgage-com-post-api-v1-quotes-request
- name: PostLeadsRequest
  property_count: 9
  slug: buildwithgage-com-post-leads-request
jsonld:
- class_count: 50
  name: Buildwithgage Com Context
  property_count: 91
  slug: buildwithgage-com-context
layout: provider
modified: '2026-11-03'
name: Gage
nav: Providers
network: true
overview: 'Gage is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Construction, Marketplace, Steel, and Developers.


  The Gage catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Gage''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, and 14 more developer resources.'
plans:
- name: Buildwithgage Com Plans Pricing
  plan_count: 3
  slug: buildwithgage-com-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Gage API Rules
  rule_count: 43
  severity_counts:
    error: 38
    hint: 0
    info: 3
    warn: 2
  slug: buildwithgage-com-rules
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 64.8
    catalog_earned_first_party: 12.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 26.2
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Buildwithgage Com Authentication
  slug: buildwithgage-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Buildwithgage Com Domain Security
  slug: buildwithgage-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: buildwithgage-com
tags:
- Construction
- Marketplace
- Steel
- Developers
website: https://buildwithgage.com/
---
