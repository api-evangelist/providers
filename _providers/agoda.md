---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.9
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: 'Agoda API as documented publicly: 13 operations. Contract generated from the documentation by API Evangelist (2026-09-22); not the provider''s own document.'
  name: Agoda API
  slug: agoda-api
artifact_total: 13
asyncapis:
- description: ''
  name: Agoda Webhooks
  slug: agoda-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agoda/refs/heads/main/rules/agoda-rules.yml
  title: ''
  type: Spectral
  url: rules/agoda-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agoda/refs/heads/main/json-ld/agoda-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agoda-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agoda/refs/heads/main/vocabulary/agoda-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agoda-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agoda/refs/heads/main/asyncapi/agoda-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/agoda-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agoda/refs/heads/main/data-model/agoda-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agoda-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agoda/refs/heads/main/authentication/agoda-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agoda-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agoda/refs/heads/main/conformance/agoda-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agoda-conformance.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/agoda-public
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agoda/refs/heads/main/well-known/agoda-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agoda-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agoda/refs/heads/main/well-known/agoda-agoda-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agoda-agoda-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agoda/refs/heads/main/well-known/agoda-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agoda-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agoda/refs/heads/main/vendors/agoda-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agoda-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.agoda.com/supply/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.agoda.com/supply/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.agoda.com/supply/docs/how-to-become-a-partner
- group: operate
  title: ''
  type: Support
  url: https://www.agoda.com/info/contact.html
- group: company
  title: ''
  type: Blog
  url: https://www.agoda.com/blog
- group: company
  title: ''
  type: Website
  url: https://agoda.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agoda/refs/heads/main/security/agoda-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agoda-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agoda/refs/heads/main/security/agoda-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agoda-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agoda.com/
coverage:
  checked: 2026-09-22
  detail: Developer docs return HTTP 429 Too Many Requests, indicating rate limiting without authentication.
  evidence:
  - status: 301
    url: https://developer.agoda.com/supply/docs
  reason: partner-login
  state: gated
created: '2026-09-22'
description: Agoda is a global online travel agency offering hotel, flight, and vacation rental bookings. The platform provides a wide range of accommodations across more than 2 million properties worldwide, featuring free cancellation, price comparison, and localized support. Agoda serves travelers with a multilingual interface, various payment options, and a focus on delivering convenient, affordable travel experiences.
image: https://www.agoda.com/favicon.ico
json_schemas:
- name: PostCmHotelcontractsResponse
  property_count: 3
  slug: agoda-post-cm-hotelcontracts-response
- name: PostCmHotelcontractssignResponse
  property_count: 3
  slug: agoda-post-cm-hotelcontractssign-response
- name: PostCmHotelproductsRequest
  property_count: 1
  slug: agoda-post-cm-hotelproducts-request
- name: PostCmHotelproductsResponse
  property_count: 3
  slug: agoda-post-cm-hotelproducts-response
- name: PostCmRateplansResponse
  property_count: 3
  slug: agoda-post-cm-rateplans-response
- name: PostCmRoomsResponse
  property_count: 3
  slug: agoda-post-cm-rooms-response
jsonld:
- class_count: 17
  name: Agoda Context
  property_count: 2
  slug: agoda-context
layout: provider
modified: '2026-09-22'
name: Agoda
nav: Providers
network: true
overview: 'Agoda publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Booking, Hotels, and Online.


  The Agoda catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Agoda''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, and 15 more developer resources.'
random_paper: 2
rules:
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: Agoda API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 2
  slug: agoda-rules
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 31.4
    developer_ergonomics: 47.6
    discoverability: 57.1
    operational_transparency: 18.4
  previous_composite: 28.5
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
    score: 22.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agoda Authentication
  slug: agoda-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Agoda Domain Security
  slug: agoda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agoda Vulnerability Disclosure
  slug: agoda-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: agoda
tags:
- Company
- Travel
- Booking
- Hotels
- Online
website: https://agoda.com/
---
