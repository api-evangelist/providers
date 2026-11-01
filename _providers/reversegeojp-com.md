---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Provides reverse and forward geocoding for Japanese addresses.
  name: ReverseGeoJP API
  slug: reversegeojp-api
- description: 'reversegeojp-com API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: reversegeojp-com API
  slug: reversegeojp-com-api
artifact_total: 11
common:
- group: operate
  href: https://artifacts.apis.io/reversegeojp-com/rate-limits/reversegeojp-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/reversegeojp-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/reversegeojp-com/plans/reversegeojp-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/reversegeojp-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/reversegeojp-com/rules/reversegeojp-com-rules.yml
  title: ''
  type: Spectral
  url: rules/reversegeojp-com-rules.yml
- group: design
  href: https://artifacts.apis.io/reversegeojp-com/json-ld/reversegeojp-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/reversegeojp-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/reversegeojp-com/vocabulary/reversegeojp-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/reversegeojp-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/reversegeojp-com/data-model/reversegeojp-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/reversegeojp-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/reversegeojp-com/authentication/reversegeojp-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/reversegeojp-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/reversegeojp-com/errors/reversegeojp-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/reversegeojp-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/reversegeojp-com/conformance/reversegeojp-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/reversegeojp-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/reversegeojp-com/hosts/reversegeojp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/reversegeojp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/reversegeojp-com/vendors/reversegeojp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/reversegeojp-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/reversegeojp-com/packages/reversegeojp-com-packages.yml
  title: ''
  type: SDKs
  url: packages/reversegeojp-com-packages.yml
- group: build
  href: https://artifacts.apis.io/reversegeojp-com/packages/reversegeojp-com-packages.yml
  title: ''
  type: Packages
  url: packages/reversegeojp-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/reversegeojp-com/security/reversegeojp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reversegeojp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://reversegeojp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.reversegeojp.com/#docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.reversegeojp.com/#docs
- group: start
  title: ''
  type: GettingStarted
  url: https://api.reversegeojp.com/#docs
- group: operate
  title: ''
  type: Support
  url: https://api.reversegeojp.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://api.reversegeojp.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://api.reversegeojp.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://api.reversegeojp.com/#plans
- group: start
  title: ''
  type: SignUp
  url: https://api.reversegeojp.com/#start
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/55tarkun/geojp-mcp
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found despite probing the API host.
  evidence:
  - status: 404
    url: https://api.reversegeojp.com/openapi.json
  - status: 404
    url: https://api.reversegeojp.com/openapi.yaml
  - status: 404
    url: https://api.reversegeojp.com/api-docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: ReverseGeoJP provides a Japanese reverse geocoding API that converts latitude/longitude coordinates into the nearest address components such as prefecture, city, town, and postal code, and also offers forward geocoding from address strings to coordinates. The service uses official Japanese address data from the Ministry of Land, Infrastructure, Transport and Tourism combined with Japan Post postal code data, offering a free tier with up to 1,000 requests per month and paid plans for higher volume. It supports both Japanese and English interfaces and provides simple HTTP GET endpoints with API key authentication.
image: https://api.reversegeojp.com/favicon.svg
json_schemas:
- name: GetGeocodeResponse
  property_count: 9
  slug: reversegeojp-com-get-geocode-response
- name: GetReverseResponse
  property_count: 6
  slug: reversegeojp-com-get-reverse-response
jsonld:
- class_count: 2
  name: Reversegeojp Com Context
  property_count: 10
  slug: reversegeojp-com-context
layout: provider
modified: '2026-10-31'
name: reversegeojp-com
nav: Providers
network: true
overview: 'reversegeojp-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Geocoding, Japan, API, and Location.


  The reversegeojp-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  reversegeojp-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 17 more developer resources.'
plans:
- name: Reversegeojp Com Plans Pricing
  plan_count: 4
  slug: reversegeojp-com-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Reversegeojp Com Rate Limits
  slug: reversegeojp-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: reversegeojp-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: reversegeojp-com-rules
scopes:
- name: Reversegeojp Com Scopes
  scope_count: 0
  slug: reversegeojp-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 91.3
    catalog_earned_first_party: 0.0
    catalog_gap: 23.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 49.5
    developer_ergonomics: 52.4
    discoverability: 57.1
    operational_transparency: 33.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Reversegeojp Com Authentication
  slug: reversegeojp-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Reversegeojp Com Domain Security
  slug: reversegeojp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: reversegeojp-com
tags:
- Company
- Geocoding
- Japan
- API
- Location
website: https://reversegeojp.com/
---
