---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''https://silvercar.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.dealerware.com/ — a different registrable domain (silvercar.com -> dealerware.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 81
  human_in_the_loop: 3
  name: Silvercar Agentic Access
  operation_count: 174
  slug: silvercar-agentic-access
  summary_line: 174 operations · 81 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: Administrative actions and resources
  name: silvercar Admin API
  slug: silvercar-admin-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: Agreement actions and resources
  name: silvercar Agreements API
  slug: silvercar-agreements-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: Version 2 of Availability which supports vehicle grouping and schedulers
  name: silvercar Availability 2.0 API
  slug: silvercar-availability-2-0-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: The Availability API from silvercar — 9 operation(s) for availability.
  name: silvercar Availability API
  slug: silvercar-availability-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: Contactless Contract actions and resources
  name: silvercar Contactless API
  slug: silvercar-contactless-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: Contract actions and resources
  name: silvercar Contracts API
  slug: silvercar-contracts-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: The CreateBlacklist API from silvercar — 1 operation(s) for createblacklist.
  name: silvercar Create Blacklist API
  slug: silvercar-createblacklist-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: Customer actions and resources
  name: silvercar Customers API
  slug: silvercar-customers-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: Dealership actions and resources
  name: silvercar Dealerships API
  slug: silvercar-dealerships-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: The DeleteCustomerFromBlacklist API from silvercar — 1 operation(s) for deletecustomerfromblacklist.
  name: silvercar Delete Customer From Blacklist API
  slug: silvercar-deletecustomerfromblacklist-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: The Documents API from silvercar — 1 operation(s) for documents.
  name: silvercar Documents API
  slug: silvercar-documents-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: Driver actions and resources
  name: silvercar Drivers API
  slug: silvercar-drivers-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: Employee actions and resources
  name: silvercar Employees API
  slug: silvercar-employees-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: Employer Information actions on a Customer resource
  name: silvercar Employer Info API
  slug: silvercar-employer-info-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: The Fleet Settings API from silvercar — 3 operation(s) for fleet settings.
  name: silvercar Fleet Settings API
  slug: silvercar-fleet-settings-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: Fleet actions and resources
  name: silvercar Fleets API
  slug: silvercar-fleets-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: Geolocation services for lite valet
  name: silvercar Geolocation API
  slug: silvercar-geolocation-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: The Insurance API from silvercar — 1 operation(s) for insurance.
  name: silvercar Insurance API
  slug: silvercar-insurance-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: Contract invoicing and pricing actions
  name: silvercar Invoicing API
  slug: silvercar-invoicing-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: Vehicle/reservation issue actions
  name: silvercar Issues API
  slug: silvercar-issues-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: The Makes API from silvercar — 1 operation(s) for makes.
  name: silvercar Makes API
  slug: silvercar-makes-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: The Models API from silvercar — 1 operation(s) for models.
  name: silvercar Models API
  slug: silvercar-models-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: The Note API from silvercar — 1 operation(s) for note.
  name: silvercar Note API
  slug: silvercar-note-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: The Notes API from silvercar — 3 operation(s) for notes.
  name: silvercar Notes API
  slug: silvercar-notes-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: The Private API from silvercar — 4 operation(s) for private.
  name: silvercar Private API
  slug: silvercar-private-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: The QueryDNR API from silvercar — 1 operation(s) for querydnr.
  name: silvercar Query DNR API
  slug: silvercar-querydnr-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: The Radial Distance API from silvercar — 1 operation(s) for radial distance.
  name: silvercar Radial Distance API
  slug: silvercar-radial-distance-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: Customer Remote Profile actions and resources
  name: silvercar Remote Profile API
  slug: silvercar-remote-profile-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: The Rental Agreement API from silvercar — 1 operation(s) for rental agreement.
  name: silvercar Rental Agreement API
  slug: silvercar-rental-agreement-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: Generic reporting discovery and data retrieval endpoints
  name: silvercar Reporting API
  slug: silvercar-reporting-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: The Reservations API from silvercar — 1 operation(s) for reservations.
  name: silvercar Reservations API
  slug: silvercar-reservations-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: The Roles API from silvercar — 2 operation(s) for roles.
  name: silvercar Roles API
  slug: silvercar-roles-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: The SCBA Booking Flow API from silvercar — 2 operation(s) for scba booking flow.
  name: silvercar SCBA Booking Flow API
  slug: silvercar-scba-booking-flow-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: The Service Advisors API from silvercar — 1 operation(s) for service advisors.
  name: silvercar Service Advisors API
  slug: silvercar-service-advisors-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: Telematics actions and resources
  name: silvercar Telematics API
  slug: silvercar-telematics-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: Single-user actions and resources
  name: silvercar User API
  slug: silvercar-user-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: Multiple-user actions and resources
  name: silvercar Users API
  slug: silvercar-users-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: Vehicle actions and resources
  name: silvercar Vehicles API
  slug: silvercar-vehicles-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: The Warranties API from silvercar — 1 operation(s) for warranties.
  name: silvercar Warranties API
  slug: silvercar-warranties-api
- baseURL: https://api.dealerware.com
  baseurl_source: declared
  description: Dealership webhook actions and resources
  name: silvercar Webhooks API
  slug: silvercar-webhooks-api
artifact_total: 53
asyncapis:
- description: ''
  name: Silvercar Webhooks
  slug: silvercar-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/silvercar/refs/heads/main/agentic-access/silvercar-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/silvercar-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/silvercar/refs/heads/main/rules/silvercar-rules.yml
  title: ''
  type: Spectral
  url: rules/silvercar-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/silvercar/refs/heads/main/json-ld/silvercar-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/silvercar-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/silvercar/refs/heads/main/vocabulary/silvercar-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/silvercar-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/silvercar/refs/heads/main/data-model/silvercar-data-model.yml
  title: ''
  type: DataModel
  url: data-model/silvercar-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/silvercar/refs/heads/main/errors/silvercar-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/silvercar-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/silvercar/refs/heads/main/conformance/silvercar-conformance.yml
  title: ''
  type: Conformance
  url: conformance/silvercar-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/silvercar/refs/heads/main/hosts/silvercar-hosts.yml
  title: ''
  type: Hosts
  url: hosts/silvercar-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/silvercar/refs/heads/main/vendors/silvercar-vendors.yml
  title: ''
  type: Vendors
  url: vendors/silvercar-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.dealerware.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/silvercar/refs/heads/main/scopes/silvercar-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/silvercar-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/silvercar/refs/heads/main/security/silvercar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/silvercar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://silvercar.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.dealerware.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.dealerware.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.dealerware.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.dealerware.com/docs/quickstart-guide
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/silvercar/refs/heads/main/authentication/silvercar-authentication.yml
  title: ''
  type: Authentication
  url: authentication/silvercar-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.dealerware.com/docs/deprecation-1
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/silvercar/refs/heads/main/asyncapi/silvercar-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/silvercar-webhooks.yml
- group: operate
  title: ''
  type: Support
  url: https://developer.dealerware.com/docs/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dealerware.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dealerware.com/privacy-policy/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/silvercar/refs/heads/main/well-known/silvercar-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/silvercar-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/silvercar/refs/heads/main/conventions/silvercar-conventions.yml
  title: ''
  type: Conventions
  url: conventions/silvercar-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/silvercar/refs/heads/main/lifecycle/silvercar-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/silvercar-lifecycle.yml
created: '2026-07-17'
description: Silvercar began as an Austin, Texas premium car-rental startup (all-silver Audi fleet) and was a Slow Ventures portfolio company. After Audi acquired it, the team pivoted the technology into Dealerware, a dealership fleet-management and courtesy/loaner-mobility SaaS platform. silvercar.com now 301-redirects to dealerware.com, and the company's public developer surface is the Dealerware Partner Integration API — a versioned (v4) REST API on a ReadMe developer hub at developer.dealerware.com covering contracts, reservations, customers, dealerships, fleets, vehicles, drivers, employees, payments, reporting, and webhooks. Authentication is OAuth 2.0 machine-to-machine (client_credentials) via Auth0, returning RS256-signed JWT bearer tokens.
image: https://files.readme.io/ce942b596bb59005caaba879dd9e42d25b4fd618aa4444310d4148fdb273781c-small-dw_darkmode.png
json_schemas:
- name: AdminDealershipContractManifestResponse
  property_count: 29
  slug: silvercar-admin-dealership-contract-manifest-response
- name: AdminDealershipContractResponse
  property_count: 37
  slug: silvercar-admin-dealership-contract-response
- name: AdminDealershipSettingsResponse
  property_count: 28
  slug: silvercar-admin-dealership-settings-response
- name: AdminFleetResponse
  property_count: 22
  slug: silvercar-admin-fleet-response
- name: AdminVehicleResponse-2
  property_count: 40
  slug: silvercar-admin-vehicle-response-2
- name: AdminVehicleResponse
  property_count: 39
  slug: silvercar-admin-vehicle-response
jsonld:
- class_count: 120
  name: Silvercar Context
  property_count: 393
  slug: silvercar-context
layout: provider
modified: '2026-07-21'
name: silvercar
nav: Providers
network: true
overview: 'silvercar publishes 40 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Agreements API, Availability 2.0 API, and 37 more. Tagged areas include Company, Automotive, Car Rental, Fleet Management, and Mobility.


  The silvercar catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  silvercar''s developer surface includes documentation, API reference, getting-started guide, authentication, support, and 21 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: silvercar API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 3
  slug: silvercar-rules
scopes:
- name: Silvercar Scopes
  scope_count: 0
  slug: silvercar-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 10.0
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 64.4
    developer_ergonomics: 33.3
    discoverability: 67.9
    operational_transparency: 11.8
  previous_composite: 30.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 40
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/silvercar/refs/heads/main/screenshots/silvercar-2026-09-02T155508.png
security:
- kind: authentication
  name: Silvercar Authentication
  slug: silvercar-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Silvercar Domain Security
  slug: silvercar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: silvercar
tags:
- Company
- Automotive
- Car Rental
- Fleet Management
- Mobility
- Dealership
- Rentals
- Software-as-a-Service
website: https://silvercar.com
---
