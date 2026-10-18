---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.5
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: FareHarbor Integration Center API
  name: FareHarbor Integration Center
  slug: fareharbor-integration-center
- baseURL: https://fareharbor.com/api/external/v1
  baseurl_source: declared
  description: The `/availabilities` endpoint is used to retrieve all bookable availabilities for a single item within a specified date or date range. The request pulls availability data from the Item calendar of th
  name: FareHarbor Availabilities Endpoints API
  slug: fareharbor-availabilities-endpoints-api
- baseURL: https://fareharbor.com/api/external/v1
  baseurl_source: declared
  description: The bookings endpoints in the FareHarbor API provide comprehensive functionalities for managing reservations efficiently. These endpoints enable developers and business owners to integrate and automat
  name: FareHarbor Bookings Endpoints API
  slug: fareharbor-bookings-endpoints-api
- baseURL: https://fareharbor.com/api/external/v1
  baseurl_source: declared
  description: The check-in endpoints in the FareHarbor API provide essential capabilities for managing the check-in processes efficiently and seamlessly. These endpoints are crucial for businesses in the tour and a
  name: FareHarbor Checkin Endpoints API
  slug: fareharbor-checkin-endpoints-api
- baseURL: https://fareharbor.com/api/external/v1
  baseurl_source: declared
  description: 'The Company endpoints in the FareHarbor API provide robust functionalities for accessing and managing information related to companies that offer tours and activities. These endpoints are crucial for '
  name: FareHarbor Company Endpoints API
  slug: fareharbor-company-endpoints-api
- baseURL: https://fareharbor.com/api/external/v1
  baseurl_source: declared
  description: The Crew Members endpoints in the FareHarbor API provide comprehensive functionality for managing crew assignments on availabilities. These endpoints allow you to assign, update, and remove crew membe
  name: FareHarbor Crew Members Endpoints API
  slug: fareharbor-crew-members-endpoints-api
- baseURL: https://fareharbor.com/api/external/v1
  baseurl_source: declared
  description: The Items endpoints in the FareHarbor API provide comprehensive access to detailed information about the various activities and services offered by a company. These endpoints are essential for any app
  name: FareHarbor Items Endpoints API
  slug: fareharbor-items-endpoints-api
- baseURL: https://fareharbor.com/api/external/v1
  baseurl_source: declared
  description: With our `/lodgings` endpoints our API Partners are able to retrieve our charters’ lodging options, both on a dashboard level as well as on the availability level, and offer these for customers to cho
  name: FareHarbor Lodging Endpoints API
  slug: fareharbor-lodging-endpoints-api
- baseURL: https://fareharbor.com/api/external/v1
  baseurl_source: declared
  description: The Ping API from FareHarbor — 1 operation(s) for ping.
  name: FareHarbor Ping API
  slug: fareharbor-ping-api
- baseURL: https://fareharbor.com/api/external/v1
  baseurl_source: declared
  description: The Roles endpoints provide access to role definitions within companies, enabling structured crew member assignments with specific responsibilities and permissions.
  name: FareHarbor Roles Endpoints API
  slug: fareharbor-roles-endpoints-api
- baseURL: https://fareharbor.com/api/external/v1
  baseurl_source: declared
  description: The Users endpoints provide access to user information within the context of company operations, specifically for crew management purposes.
  name: FareHarbor Users Endpoints API
  slug: fareharbor-users-endpoints-api
artifact_total: 22
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fareharbor/refs/heads/main/rules/fareharbor-rules.yml
  title: ''
  type: Spectral
  url: rules/fareharbor-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fareharbor/refs/heads/main/json-ld/fareharbor-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fareharbor-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fareharbor/refs/heads/main/vocabulary/fareharbor-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fareharbor-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fareharbor/refs/heads/main/conformance/fareharbor-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fareharbor-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fareharbor/refs/heads/main/vendors/fareharbor-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fareharbor-vendors.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fareharbor/refs/heads/main/data-model/fareharbor-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fareharbor-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.fareharbor.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fareharbor/refs/heads/main/security/fareharbor-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/fareharbor-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fareharbor/refs/heads/main/errors/fareharbor-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fareharbor-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fareharbor/refs/heads/main/llms/fareharbor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fareharbor-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fareharbor/refs/heads/main/well-known/fareharbor-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fareharbor-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fareharbor/refs/heads/main/well-known/fareharbor-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fareharbor-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fareharbor/refs/heads/main/well-known/fareharbor-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fareharbor-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fareharbor/refs/heads/main/hosts/fareharbor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fareharbor-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://help.fareharbor.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fareharbor.com/
- group: start
  title: ''
  type: SignUp
  url: https://marketing.fareharbor.com/become-an-affiliate/signup/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.fareharbor.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.fareharbor.com/api/external/v1/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FareHarbor
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fareharbor/refs/heads/main/security/fareharbor-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/fareharbor-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fareharbor/refs/heads/main/security/fareharbor-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/fareharbor-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fareharbor/refs/heads/main/security/fareharbor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fareharbor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fareharbor.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://api.fareharbor.com/mcp
  - status: 403
    url: https://fareharbor.com/mcp
  - status: 401
    url: https://help.fareharbor.com/mcp
  - status: 200
    url: https://fareharbor.com/
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: FareHarbor provides online booking software for tours, activities, rentals, and attractions, enabling businesses to manage reservations, payments, and customer experiences through a scalable, cloud‑based platform. The solution supports multi‑channel sales, staff management, reporting, and integrations with partners, aiming to simplify operations for tour operators and activity providers worldwide.
image: https://marketing.fareharbor.com/wp-content/uploads/2023/03/Home-First-fold-2.png
json_schemas:
- name: AVAILABILITY_RESPONSE_JSON_SCHEMA
  property_count: 1
  slug: fareharbor-availability-response-json-schema
- name: BOOKING_RESPONSE_JSON_SCHEMA
  property_count: 1
  slug: fareharbor-booking-response-json-schema
- name: BOOKING_WITH_PAYMENTS_RESPONSE_JSON_SCHEMA
  property_count: 1
  slug: fareharbor-booking-with-payments-response-json-schema
- name: BOOKING_WITH_RESOURCE_USES_RESPONSE_JSON_SCHEMA
  property_count: 1
  slug: fareharbor-booking-with-resource-uses-response-json-schema
- name: ITEM_RESPONSE_JSON_SCHEMA
  property_count: 1
  slug: fareharbor-item-response-json-schema
- name: ITEMS_RESPONSE_JSON_SCHEMA
  property_count: 1
  slug: fareharbor-items-response-json-schema
jsonld:
- class_count: 40
  name: Fareharbor Context
  property_count: 57
  slug: fareharbor-context
layout: provider
modified: '2026-10-12'
name: FareHarbor
nav: Providers
network: true
overview: 'FareHarbor publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Availabilities Endpoints API, Bookings Endpoints API, Checkin Endpoints API, and 8 more. Tagged areas include Travel, Booking, Software-as-a-Service, Tourism, and Software.


  The FareHarbor catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FareHarbor''s developer surface includes support, signup flow, documentation, API reference, and 20 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: FareHarbor API Rules
  rule_count: 13
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 0
  slug: fareharbor-rules
score:
  band: developing
  composite: 42.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 19.7
    contract_quality: 60.9
    developer_ergonomics: 21.4
    discoverability: 73.2
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 27.8
security:
- kind: domain-security
  name: Fareharbor Domain Security
  slug: fareharbor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fareharbor Vulnerability Disclosure
  slug: fareharbor-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Fareharbor Trust Center
  slug: fareharbor-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: fareharbor
tags:
- Travel
- Booking
- Software-as-a-Service
- Tourism
- Software
website: https://fareharbor.com/
---
