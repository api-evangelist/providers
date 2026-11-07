---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for managing listings, publications, media, and imprints on Kleinanzeigen. Provides operations to create, update, delete, and retrieve listings and related resources.
  name: Kleinanzeigen Professional Sellers API
  slug: kleinanzeigen-professional-sellers-api
- description: 'Kleinanzeigen API as documented publicly: 39 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Kleinanzeigen API
  slug: kleinanzeigen-api
artifact_total: 14
common:
- group: auth
  href: https://artifacts.apis.io/kleinanzeigen/well-known/kleinanzeigen-adevinta-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kleinanzeigen-adevinta-security.txt
- group: agent
  href: https://artifacts.apis.io/kleinanzeigen/well-known/kleinanzeigen-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kleinanzeigen-well-known.yml
- group: design
  href: https://artifacts.apis.io/kleinanzeigen/rules/kleinanzeigen-rules.yml
  title: ''
  type: Spectral
  url: rules/kleinanzeigen-rules.yml
- group: design
  href: https://artifacts.apis.io/kleinanzeigen/json-ld/kleinanzeigen-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kleinanzeigen-context.jsonld
- group: design
  href: https://artifacts.apis.io/kleinanzeigen/vocabulary/kleinanzeigen-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kleinanzeigen-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/kleinanzeigen/data-model/kleinanzeigen-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kleinanzeigen-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://adevinta.com/security-vulnerability/
- group: auth
  href: https://artifacts.apis.io/kleinanzeigen/authentication/kleinanzeigen-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kleinanzeigen-authentication.yml
- group: design
  href: https://artifacts.apis.io/kleinanzeigen/errors/kleinanzeigen-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kleinanzeigen-problem-types.yml
- group: design
  href: https://artifacts.apis.io/kleinanzeigen/conformance/kleinanzeigen-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kleinanzeigen-conformance.yml
- group: other
  href: https://artifacts.apis.io/kleinanzeigen/hosts/kleinanzeigen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kleinanzeigen-hosts.yml
- group: other
  href: https://artifacts.apis.io/kleinanzeigen/vendors/kleinanzeigen-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kleinanzeigen-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kleinanzeigen.de/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kleinanzeigen
- group: auth
  href: https://artifacts.apis.io/kleinanzeigen/security/kleinanzeigen-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kleinanzeigen-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/kleinanzeigen/security/kleinanzeigen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kleinanzeigen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kleinanzeigen.de/
- group: operate
  title: ''
  type: Support
  url: https://hilfe.kleinanzeigen.de/hc/de
- group: commercial
  title: ''
  type: TermsOfService
  url: https://themen.kleinanzeigen.de/impressum/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://themen.kleinanzeigen.de/datenschutzerklaerung/
coverage:
  checked: '2026-10-28'
  detail: OpenAPI spec is gated behind authentication (401 Unauthorized) at https://developer.kleinanzeigen.de/openapi.json.
  evidence:
  - status: 401
    url: https://developer.kleinanzeigen.de/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-28'
description: Kleinanzeigen is a German online classifieds platform that allows users to post free advertisements for a wide range of items and services, from furniture and electronics to jobs and real estate. Formerly known as eBay Kleinanzeigen, it connects local buyers and sellers, offering a simple, searchable marketplace without fees. The service emphasizes community-driven listings and supports categories such as vehicles, pets, and services, aiming to facilitate convenient, local transactions across Germany.
image: https://static.kleinanzeigen.de/static/img/common/logo/logo-kleinanzeigen-og-vertical.png
json_schemas:
- name: GetApiGoodsV1ListingsResponse
  property_count: 14
  slug: kleinanzeigen-get-api-goods-v1-listings-response
- name: GetApiGoodsV1Listings123E4567E89B12D3A456426614174000Respons
  property_count: 14
  slug: kleinanzeigen-get-api-goods-v1-listings123-e4567-e89-b12-d3-a456426614174000-respons
- name: GetV1ListingsResponse
  property_count: 14
  slug: kleinanzeigen-get-v1-listings-response
- name: GetV1ListingsUuidPublicationsResponse
  property_count: 27
  slug: kleinanzeigen-get-v1-listings-uuid-publications-response
- name: GetV1ListingsUuidResponse
  property_count: 14
  slug: kleinanzeigen-get-v1-listings-uuid-response
- name: PostV1ListingsRequest
  property_count: 12
  slug: kleinanzeigen-post-v1-listings-request
jsonld:
- class_count: 25
  name: Kleinanzeigen Context
  property_count: 39
  slug: kleinanzeigen-context
layout: provider
modified: '2026-10-28'
name: Kleinanzeigen
nav: Providers
network: true
overview: 'Kleinanzeigen is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Classifieds, Marketplace, Germany, free-ads, and Consumer.


  The Kleinanzeigen catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Kleinanzeigen''s developer surface includes authentication, documentation, support, and 17 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 0
  name: Kleinanzeigen Rate Limits
  slug: kleinanzeigen-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Kleinanzeigen API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: kleinanzeigen-rules
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 26.5
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 28.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/kleinanzeigen/kleinanzeigen-2026-11-03T134442.png
security:
- kind: authentication
  name: Kleinanzeigen Authentication
  slug: kleinanzeigen-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Kleinanzeigen Domain Security
  slug: kleinanzeigen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kleinanzeigen Vulnerability Disclosure
  slug: kleinanzeigen-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: kleinanzeigen
tags:
- Classifieds
- Marketplace
- Germany
- free-ads
- Consumer
website: https://kleinanzeigen.de/
---
