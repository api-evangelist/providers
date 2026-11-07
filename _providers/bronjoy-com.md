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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 19.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Bronjoy platform
  name: Bronjoy API
  slug: bronjoy-api
- baseURL: https://api.bronjoy.com/api
  baseurl_source: declared
  description: 'Bronjoy Api-spec API: 313 operations.'
  name: Bronjoy Api-spec API
  slug: bronjoy-api-spec-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/bronjoy-com/rules/bronjoy-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bronjoy-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bronjoy-com/json-ld/bronjoy-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bronjoy-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/bronjoy-com/vocabulary/bronjoy-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bronjoy-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bronjoy-com/conformance/bronjoy-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bronjoy-com-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/bronjoy-com/plans/bronjoy-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bronjoy-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bronjoy-com/data-model/bronjoy-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bronjoy-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/bronjoy-com/authentication/bronjoy-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bronjoy-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/bronjoy-com/errors/bronjoy-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bronjoy-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/bronjoy-com/llms/bronjoy-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bronjoy-com-llms.txt
- group: other
  href: https://artifacts.apis.io/bronjoy-com/hosts/bronjoy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bronjoy-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bronjoy-com/vendors/bronjoy-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bronjoy-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bronjoy.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bronjoy.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://bronjoy.com/business/pricing
- group: start
  title: ''
  type: Login
  url: https://bronjoy.com/login
- group: other
  title: ''
  type: Leadership
  url: https://bronjoy.com/bukhara/education/team
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bronjoy.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bronjoy.com/api-reference
- group: auth
  href: https://artifacts.apis.io/bronjoy-com/security/bronjoy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bronjoy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bronjoy.com/
created: '2026-11-03'
description: Bronjoy is a platform that enables users in Uzbekistan to find and book appointments at over 24,000 salons, clinics, and service venues. The service provides detailed information such as addresses, opening hours, phone numbers, and online booking options where available, helping customers quickly schedule services across the country.
image: https://bronjoy.com/logo.png
json_schemas:
- name: AppointmentResource
  property_count: 34
  slug: bronjoy-com-appointment-resource
- name: CreateOrganizationRequest
  property_count: 19
  slug: bronjoy-com-create-organization-request
- name: OrganizationProfileResource
  property_count: 46
  slug: bronjoy-com-organization-profile-resource
- name: OrganizationResource
  property_count: 34
  slug: bronjoy-com-organization-resource
- name: SubscriptionResource
  property_count: 20
  slug: bronjoy-com-subscription-resource
- name: UpdateOrganizationProfileRequest
  property_count: 24
  slug: bronjoy-com-update-organization-profile-request
jsonld:
- class_count: 120
  name: Bronjoy Com Context
  property_count: 371
  slug: bronjoy-com-context
layout: provider
modified: '2026-11-03'
name: Bronjoy
nav: Providers
network: true
overview: 'Bronjoy publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Api-spec API, and 1 more. Tagged areas include Company, Booking, Uzbekistan, Salon, and Healthcare.


  The Bronjoy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bronjoy''s developer surface includes authentication, pricing, documentation, API reference, and 16 more developer resources.'
plans:
- name: Bronjoy Com Plans Pricing
  plan_count: 2
  slug: bronjoy-com-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Bronjoy API Rules
  rule_count: 39
  severity_counts:
    error: 26
    hint: 0
    info: 4
    warn: 9
  slug: bronjoy-com-rules
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 50.7
    developer_ergonomics: 20.2
    discoverability: 67.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bronjoy Com Authentication
  slug: bronjoy-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bronjoy Com Domain Security
  slug: bronjoy-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bronjoy-com
tags:
- Company
- Booking
- Uzbekistan
- Salon
- Healthcare
website: https://bronjoy.com/
---
