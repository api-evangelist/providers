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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Provides fast and accurate geocoding services with forward and reverse geocoding, requiring an API key.
  name: GeocodeFarm API
  slug: geocodefarm-api
- baseURL: https://api.geocodefarm.com
  baseurl_source: declared
  description: 'Geocode.Farm API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Geocode.Farm API
  slug: geocode-farm-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/geocode-farm/plans/geocode-farm-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/geocode-farm-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/geocode-farm/rules/geocode-farm-rules.yml
  title: ''
  type: Spectral
  url: rules/geocode-farm-rules.yml
- group: design
  href: https://artifacts.apis.io/geocode-farm/json-ld/geocode-farm-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/geocode-farm-context.jsonld
- group: design
  href: https://artifacts.apis.io/geocode-farm/vocabulary/geocode-farm-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/geocode-farm-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/geocode-farm/data-model/geocode-farm-data-model.yml
  title: ''
  type: DataModel
  url: data-model/geocode-farm-data-model.yml
- group: design
  href: https://artifacts.apis.io/geocode-farm/conventions/geocode-farm-conventions.yml
  title: ''
  type: Conventions
  url: conventions/geocode-farm-conventions.yml
- group: auth
  href: https://artifacts.apis.io/geocode-farm/authentication/geocode-farm-authentication.yml
  title: ''
  type: Authentication
  url: authentication/geocode-farm-authentication.yml
- group: design
  href: https://artifacts.apis.io/geocode-farm/errors/geocode-farm-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/geocode-farm-problem-types.yml
- group: design
  href: https://artifacts.apis.io/geocode-farm/conformance/geocode-farm-conformance.yml
  title: ''
  type: Conformance
  url: conformance/geocode-farm-conformance.yml
- group: agent
  href: https://artifacts.apis.io/geocode-farm/llms/geocode-farm-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/geocode-farm-llms.txt
- group: other
  href: https://artifacts.apis.io/geocode-farm/hosts/geocode-farm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/geocode-farm-hosts.yml
- group: build
  href: https://artifacts.apis.io/geocode-farm/packages/geocode-farm-packages.yml
  title: ''
  type: SDKs
  url: packages/geocode-farm-packages.yml
- group: build
  href: https://artifacts.apis.io/geocode-farm/packages/geocode-farm-packages.yml
  title: ''
  type: Packages
  url: packages/geocode-farm-packages.yml
- group: auth
  href: https://artifacts.apis.io/geocode-farm/security/geocode-farm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/geocode-farm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://geocodefarm.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.geocodefarm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://geocodefarm.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://geocodefarm.com/documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://geocodefarm.com/documentation/
- group: operate
  title: ''
  type: Support
  url: https://geocodefarm.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://geocodefarm.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/geocodefarm
- group: commercial
  title: ''
  type: Pricing
  url: https://geocodefarm.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://geocode.farm/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://geocodefarm.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://geocodefarm.com/privacy-policy/
coverage:
  checked: '2026-10-28'
  detail: Documentation provides API details but no OpenAPI or other machine‑readable contract is published.
  evidence:
  - status: 200
    url: https://geocodefarm.com/documentation/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Geocode.Farm provides a fast, accurate, and affordable global geocoding API that converts addresses to geographic coordinates and vice versa. It supports bulk geocoding, offers a free tier, detailed documentation, and flexible pricing plans for developers and enterprises worldwide. The service emphasizes reliability, scalability, and ease of integration across various platforms and programming languages.
image: https://geocodefarm.com/wp-content/uploads/geocodefarm_icon_pin_01.png
json_schemas:
- name: GetForwardResponse
  property_count: 4
  slug: geocode-farm-get-forward-response
- name: GetReverseResponse
  property_count: 4
  slug: geocode-farm-get-reverse-response
- name: GetV3ForwardResponse
  property_count: 3
  slug: geocode-farm-get-v3-forward-response
jsonld:
- class_count: 3
  name: Geocode Farm Context
  property_count: 7
  slug: geocode-farm-context
layout: provider
modified: '2026-10-28'
name: Geocode.Farm
nav: Providers
network: true
overview: 'Geocode.Farm is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Geocoding, Location, Data, and Services.


  The Geocode.Farm catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Geocode.Farm''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Geocode Farm Plans Pricing
  plan_count: 6
  slug: geocode-farm-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Geocode Farm Rate Limits
  slug: geocode-farm-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Geocode.Farm API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: geocode-farm-rules
scopes:
- name: Geocode Farm Scopes
  scope_count: 0
  slug: geocode-farm-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 30
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.9
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 21.7
    developer_ergonomics: 41.7
    discoverability: 64.3
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 47.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
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
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/geocode-farm/geocode-farm-2026-11-03T132602.png
security:
- kind: authentication
  name: Geocode Farm Authentication
  slug: geocode-farm-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Geocode Farm Domain Security
  slug: geocode-farm-domain-security
  summary_line: TLSv1.3 · DMARC
slug: geocode-farm
tags:
- Geocoding
- Location
- Data
- Services
website: https://geocodefarm.com/
---
