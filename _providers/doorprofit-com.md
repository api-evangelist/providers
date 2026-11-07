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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for DoorProfit providing crime and offender data.
  name: DoorProfit API
  slug: doorprofit-api
- description: 'doorprofit-com API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: doorprofit-com API
  slug: doorprofit-com-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/doorprofit-com/plans/doorprofit-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/doorprofit-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/doorprofit-com/rules/doorprofit-com-rules.yml
  title: ''
  type: Spectral
  url: rules/doorprofit-com-rules.yml
- group: design
  href: https://artifacts.apis.io/doorprofit-com/json-ld/doorprofit-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/doorprofit-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/doorprofit-com/vocabulary/doorprofit-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/doorprofit-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/doorprofit-com/data-model/doorprofit-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/doorprofit-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/doorprofit-com/conventions/doorprofit-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/doorprofit-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/doorprofit-com/authentication/doorprofit-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/doorprofit-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/doorprofit-com/conformance/doorprofit-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/doorprofit-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/doorprofit-com/llms/doorprofit-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/doorprofit-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/doorprofit-com/well-known/doorprofit-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/doorprofit-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/doorprofit-com/hosts/doorprofit-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/doorprofit-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/doorprofit-com/vendors/doorprofit-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/doorprofit-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.doorprofit.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://www.doorprofit.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://api.doorprofit.com/privacy/
- group: docs
  title: ''
  type: Documentation
  url: https://api.doorprofit.com/docs/
- group: start
  title: ''
  type: SignUp
  url: https://api.doorprofit.com/signup
- group: start
  title: ''
  type: GettingStarted
  url: https://api.doorprofit.com/docs
- group: auth
  href: https://artifacts.apis.io/doorprofit-com/security/doorprofit-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doorprofit-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doorprofit.com/
coverage:
  checked: '2026-11-05'
  detail: API requires an API key obtained via signup, blocking public access to contract.
  evidence:
  - status: 200
    url: https://api.doorprofit.com/signup/
  reason: auth-required
  state: gated
created: '2026-11-05'
description: DoorProfit offers interactive crime maps and neighborhood safety scores that grade U.S. locations from A+ to F using FBI Uniform Crime Reporting and NIBRS data. The platform includes a registered‑offender search and a real‑estate deal analyzer that integrates crime scores for investors, families, renters, and property managers. It is available via web, iOS, and Android applications.
image: https://www.doorprofit.com/assets/images/doorprofit-og.png
json_schemas:
- name: GetCrimeResponse
  property_count: 8
  slug: doorprofit-com-get-crime-response
- name: GetV1CrimeResponse
  property_count: 2
  slug: doorprofit-com-get-v1-crime-response
- name: GetV1NeighborhoodResponse
  property_count: 2
  slug: doorprofit-com-get-v1-neighborhood-response
- name: GetV1OffendersResponse
  property_count: 2
  slug: doorprofit-com-get-v1-offenders-response
- name: GetV1UsageResponse
  property_count: 3
  slug: doorprofit-com-get-v1-usage-response
jsonld:
- class_count: 5
  name: Doorprofit Com Context
  property_count: 12
  slug: doorprofit-com-context
layout: provider
modified: '2026-11-05'
name: doorprofit-com
nav: Providers
network: true
overview: 'doorprofit-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Crime, Neighborhood Safety, Registered Offender Search, Mobile App, and Real Estate Investment.


  The doorprofit-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  doorprofit-com''s developer surface includes authentication, support, documentation, signup flow, getting-started guide, and 15 more developer resources.'
plans:
- name: Doorprofit Com Plans Pricing
  plan_count: 4
  slug: doorprofit-com-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: doorprofit-com API Rules
  rule_count: 39
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 1
  slug: doorprofit-com-rules
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 25.0
    developer_ergonomics: 38.1
    discoverability: 57.1
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
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Doorprofit Com Authentication
  slug: doorprofit-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Doorprofit Com Domain Security
  slug: doorprofit-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: doorprofit-com
tags:
- Crime
- Neighborhood Safety
- Registered Offender Search
- Mobile App
- Real Estate Investment
website: https://doorprofit.com/
---
