---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Loggi Agentic Access
  operation_count: 11
  slug: loggi-agentic-access
  summary_line: 11 operations · 8 acting
api_count: 18
apis:
- description: Loggi's REST integration platform for freight quotation, shipment creation (sync/async), label generation, package update/cancel, package details, real-time tracking, webhooks, integrator management a
  name: Loggi Platform API
  slug: loggi-platform-api
- baseURL: https://api.loggi.com
  baseurl_source: declared
  description: The AuthAPI API from Loggi — 2 operation(s) for authapi.
  name: Loggi Auth API
  slug: loggi-authapi-api
- baseURL: https://api.loggi.com
  baseurl_source: declared
  description: The DetailsAPI API from Loggi — 1 operation(s) for detailsapi.
  name: Loggi Details API
  slug: loggi-detailsapi-api
- baseURL: https://api.loggi.com
  baseurl_source: declared
  description: The DropoffLocationsAPI API from Loggi — 1 operation(s) for dropofflocationsapi.
  name: Loggi Dropoff Locations API
  slug: loggi-dropofflocationsapi-api
- baseURL: https://api.loggi.com
  baseurl_source: declared
  description: The IntegratorCompanyAPI API from Loggi — 1 operation(s) for integratorcompanyapi.
  name: Loggi Integrator Company API
  slug: loggi-integratorcompanyapi-api
- baseURL: https://api.loggi.com
  baseurl_source: declared
  description: The LabelAPI API from Loggi — 1 operation(s) for labelapi.
  name: Loggi Label API
  slug: loggi-labelapi-api
- baseURL: https://api.loggi.com
  baseurl_source: declared
  description: The PackageCancelAPI API from Loggi — 1 operation(s) for packagecancelapi.
  name: Loggi Package Cancel API
  slug: loggi-packagecancelapi-api
- baseURL: https://api.loggi.com
  baseurl_source: declared
  description: The PackageUpdateAPI API from Loggi — 1 operation(s) for packageupdateapi.
  name: Loggi Package Update API
  slug: loggi-packageupdateapi-api
- baseURL: https://api.loggi.com
  baseurl_source: declared
  description: The QuotationAPI API from Loggi — 1 operation(s) for quotationapi.
  name: Loggi Quotation API
  slug: loggi-quotationapi-api
- baseURL: https://api.loggi.com
  baseurl_source: declared
  description: The ShipmentAPI API from Loggi — 1 operation(s) for shipmentapi.
  name: Loggi Shipment API
  slug: loggi-shipmentapi-api
- baseURL: https://api.loggi.com
  baseurl_source: declared
  description: The TrackingAPI API from Loggi — 1 operation(s) for trackingapi.
  name: Loggi Tracking API
  slug: loggi-trackingapi-api
artifact_total: 34
asyncapis:
- description: ''
  name: Loggi Webhooks
  slug: loggi-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/loggi/refs/heads/main/agentic-access/loggi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/loggi-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/loggi/refs/heads/main/rules/loggi-rules.yml
  title: ''
  type: Spectral
  url: rules/loggi-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/loggi/refs/heads/main/json-ld/loggi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/loggi-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/loggi/refs/heads/main/vocabulary/loggi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/loggi-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/loggi/refs/heads/main/errors/loggi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/loggi-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/loggi/refs/heads/main/hosts/loggi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/loggi-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/loggi/refs/heads/main/integrations/loggi-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/loggi-integration-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/loggi/refs/heads/main/vendors/loggi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/loggi-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/loggi/refs/heads/main/scopes/loggi-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/loggi-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.loggi.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.api.loggi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.loggi.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.api.loggi.com/reference/nossa-documenta%C3%A7%C3%A3o
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.api.loggi.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://ajuda.loggi.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.loggi.com/contas/criar/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.loggi.com/aviso-privacidade-clientes/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/loggi/refs/heads/main/llms/loggi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/loggi-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/loggi/refs/heads/main/well-known/loggi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/loggi-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/loggi/refs/heads/main/authentication/loggi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/loggi-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/loggi/refs/heads/main/conventions/loggi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/loggi-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/loggi/refs/heads/main/lifecycle/loggi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/loggi-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/loggi/refs/heads/main/lifecycle/loggi-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/loggi-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/loggi/refs/heads/main/asyncapi/loggi-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/loggi-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/loggi/refs/heads/main/mcp/loggi-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/loggi-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/loggi/refs/heads/main/errors/loggi-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/loggi-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/loggi/refs/heads/main/conformance/loggi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/loggi-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/loggi/refs/heads/main/data-model/loggi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/loggi-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/loggi/refs/heads/main/security/loggi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/loggi-domain-security.yml
created: '2026-07-17'
description: 'Loggi is the largest private shipping and last-mile logistics company in Brazil, operating its own delivery network across more than 4,000 municipalities. Loggi publishes a REST developer platform (docs.api.loggi.com) that lets partner platforms and integrators estimate freight prices and delivery times, create single or multiple shipments (synchronously or asynchronously), generate Loggi shipping labels, update or cancel packages, retrieve package details, track packages in real time, and receive delivery status updates via webhooks. Authentication is OAuth2 client-credentials style (client_id/client_secret exchanged for a JWT). Backed by Fifth Wall, GGV Capital and SoftBank Vision Fund. Sector: logistics.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/loggi.png
json_schemas:
- name: ListDropoffLocationsRequest
  property_count: 11
  slug: loggi-list-dropoff-locations-request
- name: ListDropoffLocationsResponse
  property_count: 2
  slug: loggi-list-dropoff-locations-response
- name: QuoteRequest
  property_count: 3
  slug: loggi-quote-request
- name: QuoteResponse
  property_count: 1
  slug: loggi-quote-response
- name: ServiceAccountTokenRequest
  property_count: 2
  slug: loggi-service-account-token-request
- name: ServiceAccountTokenResponse
  property_count: 2
  slug: loggi-service-account-token-response
- name: v1CreateAsyncShipmentRequest
  property_count: 6
  slug: loggi-v1-create-async-shipment-request
- name: v1CreateAsyncShipmentResponse
  property_count: 1
  slug: loggi-v1-create-async-shipment-response
- name: v1CreateLabelRequest
  property_count: 5
  slug: loggi-v1-create-label-request
- name: v1CreateLabelResponse
  property_count: 2
  slug: loggi-v1-create-label-response
- name: v1IntegratorCompanyResponse
  property_count: 1
  slug: loggi-v1-integrator-company-response
- name: v1PackageCancelResponse
  property_count: 2
  slug: loggi-v1-package-cancel-response
- name: v1PackageDetailsResponse
  property_count: 1
  slug: loggi-v1-package-details-response
- name: v1PackageUpdateRequest
  property_count: 1
  slug: loggi-v1-package-update-request
- name: v1PackageUpdateResponse
  property_count: 2
  slug: loggi-v1-package-update-response
- name: v1TrackPackageTrackingCodeResponse
  property_count: 1
  slug: loggi-v1-track-package-tracking-code-response
jsonld:
- class_count: 30
  name: Loggi Context
  property_count: 89
  slug: loggi-context
layout: provider
modified: '2026-07-20'
name: Loggi
nav: Providers
network: true
overview: 'Loggi publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Details API, Dropoff Locations API, and 8 more. Tagged areas include Company, Logistics, Shipping, Last Mile Delivery, and Freight.


  The Loggi catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Loggi''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, and 23 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Loggi API Rules
  rule_count: 16
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 3
  slug: loggi-rules
scopes:
- name: Loggi Scopes
  scope_count: 0
  slug: loggi-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 23.7
    contract_governance: 22.0
    contract_quality: 67.6
    developer_ergonomics: 35.7
    discoverability: 78.6
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 10
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/loggi/refs/heads/main/screenshots/loggi-2026-07-25T225453.png
security:
- kind: authentication
  name: Loggi Authentication
  slug: loggi-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Loggi Domain Security
  slug: loggi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: loggi
tags:
- Company
- Logistics
- Shipping
- Last Mile Delivery
- Freight
- Tracking
- Brazil
website: https://www.loggi.com/
---
