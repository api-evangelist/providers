---
agent_readiness:
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'REST APIs from BlueScope''s Developer Centre that enable EDI trading with BlueScope business units (Orrcon, BlueScope Steel Distribution/BSFP, BlueScope Buildings/BBC, CIPA): sending purchase orders in'
  name: BlueScope EDI Trading APIs
  slug: bluescope-edi-apis
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/bluescope/conventions/bluescope-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bluescope-conventions.yml
- group: auth
  href: https://artifacts.apis.io/bluescope/authentication/bluescope-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bluescope-authentication.yml
- group: design
  href: https://artifacts.apis.io/bluescope/conformance/bluescope-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bluescope-conformance.yml
- group: other
  href: https://artifacts.apis.io/bluescope/hosts/bluescope-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bluescope-hosts.yml
- group: other
  href: https://artifacts.apis.io/bluescope/vendors/bluescope-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bluescope-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.bluescope.com/
- group: auth
  href: https://artifacts.apis.io/bluescope/security/bluescope-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bluescope-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bluescope.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.bluescope.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.bluescope.com/contact
- group: company
  title: ''
  type: Investors
  url: https://www.bluescope.com/investors
- group: company
  title: ''
  type: Careers
  url: https://www.bluescope.com/careers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bluescope.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bluescope.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bluescope-steel
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/tvbluescope
coverage:
  checked: '2026-10-21'
  detail: BlueScope's Developer Centre (Azure API Management) returns an empty API and product list to anonymous visitors (/developer/apis -> {"value":[]}); API definitions appear only after sign-up and an admin-approved product subscription, so no OpenAPI could be fetched, though GS1 JSON Schemas and examples are public in the welcome-pack zips.
  evidence:
  - status: 200
    url: https://developer.apiaut.bluescope.com/
  - status: 200
    url: https://developer.apiaut.bluescope.com/developer/apis?api-version=2022-04-01-preview
  - status: 200
    url: https://developer.apiaut.bluescope.com/developer/products?api-version=2022-04-01-preview
  - status: 200
    url: https://developer.apiaut.bluescope.com/apis
  - status: 200
    url: https://developer.apiaut.bluescope.com/content/GS1POA.zip
  - status: 404
    url: https://www.bluescope.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-21'
description: 'BlueScope (BlueScope Steel Limited, ASX-listed, headquartered in Australia) is a steel supplier and manufacturer for the building and construction industries, producing flat and painted steel products sold under brands including COLORBOND, ZINCALUME, LYSAGHT, TRUECORE and Butler, with operations across Australia, New Zealand, North America, ASEAN and China. BlueScope runs a Developer Centre (developer.apiaut.bluescope.com, an Azure API Management portal) for B2B EDI trading with its business units: REST APIs accepting XML or JSON for purchase orders, order responses, shipment notifications, invoices, test certificates and GS1 transport messages, with the API list visible only after sign-up and approved product subscription. dev.bluescope.com is a staging copy of the corporate site, not the developer portal.'
examples:
- key_count: 5
  name: Bluescope Asi Test Certificate Example
  slug: bluescope-asi-test-certificate-example
- key_count: 5
  name: Bluescope Gs1 Cipa Purchase Order Example
  slug: bluescope-gs1-cipa-purchase-order-example
- key_count: 1
  name: Bluescope Gs1 Distribution Purchase Order Example
  slug: bluescope-gs1-distribution-purchase-order-example
- key_count: 5
  name: Bluescope Gs1 Order Response Example
  slug: bluescope-gs1-order-response-example
image: https://www.bluescope.com/content/dam/bluescope/corporate/bluescope-com/global/assets/Header_Logo.svg
json_schemas:
- name: The Root Schema
  property_count: 5
  slug: bluescope-gs1-despatch-advice
- name: Bluescope Gs1 Invoice
  property_count: 5
  slug: bluescope-gs1-invoice
- name: The Root Schema
  property_count: 5
  slug: bluescope-gs1-order-response
layout: provider
modified: '2026-10-21'
name: BlueScope
nav: Providers
network: true
overview: 'BlueScope is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Steel, Manufacturing, Building Materials, and Construction.


  BlueScope''s developer surface includes authentication, documentation, support, YouTube channel, and 12 more developer resources.'
plans:
- name: Bluescope Plans Pricing
  plan_count: 0
  slug: bluescope-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Bluescope Rate Limits
  slug: bluescope-rate-limits
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 12.0
    developer_ergonomics: 26.2
    discoverability: 58.9
    operational_transparency: 0.0
  previous_composite: 21.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bluescope Authentication
  slug: bluescope-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Bluescope Domain Security
  slug: bluescope-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bluescope
tags:
- Company
- Steel
- Manufacturing
- Building Materials
- Construction
- Australia
- ASX
website: https://www.bluescope.com/
---
