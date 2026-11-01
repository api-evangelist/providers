---
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Parcelone Agentic Access
  operation_count: 21
  slug: parcelone-agentic-access
  summary_line: 21 operations · 4 acting
api_count: 2
apis:
- baseURL: https://sandbox.parcelone.io/shippingapi/v1
  baseurl_source: declared
  description: The closing API from ParcelOne — 4 operation(s) for closing.
  name: ParcelOne Closing API
  slug: parcelone-closing-api
- baseURL: https://sandbox.parcelone.io/shippingapi/v1
  baseurl_source: declared
  description: The customer API from ParcelOne — 1 operation(s) for customer.
  name: ParcelOne Customer API
  slug: parcelone-customer-api
- baseURL: https://sandbox.parcelone.io/shippingapi/v1
  baseurl_source: declared
  description: The customs API from ParcelOne — 3 operation(s) for customs.
  name: ParcelOne Customs API
  slug: parcelone-customs-api
- baseURL: https://sandbox.parcelone.io/shippingapi/v1
  baseurl_source: declared
  description: The datetime API from ParcelOne — 1 operation(s) for datetime.
  name: ParcelOne Datetime API
  slug: parcelone-datetime-api
- baseURL: https://sandbox.parcelone.io/shippingapi/v1
  baseurl_source: declared
  description: The mandator API from ParcelOne — 1 operation(s) for mandator.
  name: ParcelOne Mandator API
  slug: parcelone-mandator-api
- baseURL: https://sandbox.parcelone.io/shippingapi/v1
  baseurl_source: declared
  description: The mobilereturn API from ParcelOne — 1 operation(s) for mobilereturn.
  name: ParcelOne Mobilereturn API
  slug: parcelone-mobilereturn-api
- baseURL: https://sandbox.parcelone.io/shippingapi/v1
  baseurl_source: declared
  description: The profile API from ParcelOne — 4 operation(s) for profile.
  name: ParcelOne Profile API
  slug: parcelone-profile-api
- baseURL: https://sandbox.parcelone.io/shippingapi/v1
  baseurl_source: declared
  description: The shipment API from ParcelOne — 5 operation(s) for shipment.
  name: ParcelOne Shipment API
  slug: parcelone-shipment-api
artifact_total: 25
common:
- group: other
  href: https://artifacts.apis.io/parcelone/capabilities/parcelone-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/parcelone-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/parcelone/agentic-access/parcelone-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/parcelone-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/parcelone/rules/parcelone-rules.yml
  title: ''
  type: Spectral
  url: rules/parcelone-rules.yml
- group: design
  href: https://artifacts.apis.io/parcelone/json-ld/parcelone-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/parcelone-context.jsonld
- group: design
  href: https://artifacts.apis.io/parcelone/vocabulary/parcelone-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/parcelone-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/parcelone/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/parcelone/data-model/parcelone-data-model.yml
  title: ''
  type: DataModel
  url: data-model/parcelone-data-model.yml
- group: design
  href: https://artifacts.apis.io/parcelone/conventions/parcelone-conventions.yml
  title: ''
  type: Conventions
  url: conventions/parcelone-conventions.yml
- group: design
  href: https://artifacts.apis.io/parcelone/errors/parcelone-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/parcelone-problem-types.yml
- group: design
  href: https://artifacts.apis.io/parcelone/conformance/parcelone-conformance.yml
  title: ''
  type: Conformance
  url: conformance/parcelone-conformance.yml
- group: agent
  href: https://artifacts.apis.io/parcelone/llms/parcelone-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/parcelone-llms.txt
- group: other
  href: https://artifacts.apis.io/parcelone/hosts/parcelone-hosts.yml
  title: ''
  type: Hosts
  url: hosts/parcelone-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://parcel.one/en/legal-notice/
- group: auth
  href: https://artifacts.apis.io/parcelone/authentication/parcelone-authentication.yml
  title: ''
  type: Authentication
  url: authentication/parcelone-authentication.yml
- group: auth
  href: https://artifacts.apis.io/parcelone/security/parcelone-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/parcelone-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://parcel.one/
- group: docs
  title: ''
  type: Documentation
  url: https://sandbox.parcelone.io/apidoc/
- group: docs
  title: ''
  type: APIReference
  url: https://sandbox.parcelone.io/apidoc/
- group: operate
  title: ''
  type: Support
  url: https://parcel.one/en/contact/
- group: company
  title: ''
  type: Blog
  url: https://parcel.one/de/blog/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sandbox.parcelone.io/apidoc/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://parcel.one/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: ParcelOne provides international shipping, fulfillment, tracking, customs, and local delivery solutions for e‑commerce businesses, operating a centrally located logistics hub in Germany with AI‑driven high‑speed sorting to enable cross‑border commerce and optimized local deliveries worldwide.
image: https://parcel.one/wp-content/uploads/2026/07/Captura-de-pantalla-2026-07-30-185545.png
json_schemas:
- name: Customer
  property_count: 7
  slug: parcelone-customer
- name: Format
  property_count: 6
  slug: parcelone-format
- name: MobileReturnsResult
  property_count: 2
  slug: parcelone-mobile-returns-result
- name: Profile
  property_count: 5
  slug: parcelone-profile
- name: ShipmentDocumentsResult
  property_count: 11
  slug: parcelone-shipment-documents-result
- name: ShipmentResult
  property_count: 12
  slug: parcelone-shipment-result
jsonld:
- class_count: 38
  name: Parcelone Context
  property_count: 183
  slug: parcelone-context
layout: provider
modified: '2026-10-28'
name: ParcelOne
nav: Providers
network: true
overview: 'ParcelOne publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Closing API, Customer API, Customs API, and 5 more. Tagged areas include Logistics, Shipping, E-commerce, Fulfillment, and International.


  The ParcelOne catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ParcelOne''s developer surface includes authentication, documentation, API reference, support, engineering blog, and 16 more developer resources.'
plans:
- name: Parcelone Plans Pricing
  plan_count: 0
  slug: parcelone-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Parcelone Rate Limits
  slug: parcelone-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: ParcelOne API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: parcelone-rules
scopes:
- name: Parcelone Scopes
  scope_count: 0
  slug: parcelone-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 30
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 67.4
    developer_ergonomics: 47.0
    discoverability: 66.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - global
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Parcelone Authentication
  slug: parcelone-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Parcelone Domain Security
  slug: parcelone-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 3
skills:
- name: create-shipment
  slug: parcelone-create-shipment
- name: parcelone-shipping
  slug: parcelone-shipping
- name: parcelone-tracklmc
  slug: parcelone-tracklmc
slug: parcelone
tags:
- Logistics
- Shipping
- E-commerce
- Fulfillment
- International
website: https://parcel.one/
---
