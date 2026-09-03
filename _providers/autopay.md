---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 15
  human_in_the_loop: 3
  name: Autopay Agentic Access
  operation_count: 30
  slug: autopay-agentic-access
  summary_line: 30 operations · 15 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: The Autopay Accounting API provides Autopay invoicing data to external accounting and ERP systems, enabling automated reconciliation of parking revenue and invoice export.
  name: Autopay Accounting API
  slug: accounting-api
- description: The Autopay Booking API enables assignment of anonymous parking permits to vehicles, supporting short-term and pre-booked parking allocations in managed parking facilities.
  name: Autopay Booking API
  slug: booking-api
- description: The Autopay Parking API handles zone entry notifications and parking session modifications, enabling integration with parking gate systems, sensors, and barrier control equipment to track vehicle arri
  name: Autopay Parking API
  slug: parking-api
- description: The Autopay Payment API enables third-party systems to take payment responsibility for parking sessions, supporting employer-paid parking, fleet-billed parking, and visitor parking validation workflow
  name: Autopay Payment API
  slug: payment-api
- description: The Autopay Permit Tenant API enables tenants in managed properties to manage their parking permits, including adding vehicles, modifying permit allocations, and tracking permit usage within their ass
  name: Autopay Permit Tenant API
  slug: permit-tenant-api
- description: The Autopay Fleet API provides fleet information for company vehicle fleets, enabling fleet managers to track vehicle parking activity, costs, and permit usage across all fleet vehicles.
  name: Autopay Fleet API
  slug: fleet-api
- description: The Autopay Statistics API exports parking statistics for operators and landlords, providing data on occupancy rates, revenue, session volumes, and permit utilization for parking facility management a
  name: Autopay Statistics API
  slug: statistics-api
- description: The Autopay Vehicle API fetches data about a vehicle in a specific parking zone, providing real-time information on vehicle presence, active session status, and permit validity for enforcement and acc
  name: Autopay Vehicle API
  slug: vehicle-api
- description: The Autopay Tap and Park API enables third-party applications to validate parking sessions in Autopay-managed zones, supporting contactless parking validation via NFC, mobile apps, or access control s
  name: Autopay Tap and Park API
  slug: tap-park-api
- baseURL: https://api.autopay.io
  baseurl_source: spec
  description: Invoice export for accounting and ERP reconciliation
  name: Autopay Accounting API
  slug: autopay-accounting-api
- baseURL: https://api.autopay.io
  baseurl_source: spec
  description: Permit booking creation, modification, status, and availability
  name: Autopay Booking API
  slug: autopay-booking-api
- baseURL: https://api.autopay.io
  baseurl_source: spec
  description: Customer club membership management
  name: Autopay Customer Club API
  slug: autopay-customer-club-api
- baseURL: https://api.autopay.io
  baseurl_source: spec
  description: Fleet vehicle management and parking/toll service retrieval
  name: Autopay Fleet API
  slug: autopay-fleet-api
- baseURL: https://api.autopay.io
  baseurl_source: spec
  description: Parking session product changes
  name: Autopay Parking API
  slug: autopay-parking-api
- baseURL: https://api.autopay.io
  baseurl_source: spec
  description: External payment registration and parking connection
  name: Autopay Payment API
  slug: autopay-payment-api
- baseURL: https://api.autopay.io
  baseurl_source: spec
  description: Tenant permit allocations and end-user permit lifecycle
  name: Autopay Permit API
  slug: autopay-permit-api
- baseURL: https://api.autopay.io
  baseurl_source: spec
  description: Parking statistics export
  name: Autopay Statistics API
  slug: autopay-statistics-api
- baseURL: https://api.autopay.io
  baseurl_source: spec
  description: Zone availability and detailed parking session status
  name: Autopay Status API
  slug: autopay-status-api
- baseURL: https://api.autopay.io
  baseurl_source: spec
  description: Vehicle permit and session lookups
  name: Autopay Vehicle API
  slug: autopay-vehicle-api
artifact_total: 51
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Autopay Accounting API
  slug: open-autopay-accounting-api
- collection_type: open
  name: Autopay Accounting Booking API
  slug: open-autopay-booking-api
- collection_type: open
  name: Autopay Accounting Customer Club API
  slug: open-autopay-customer-club-api
- collection_type: open
  name: Autopay Accounting Fleet API
  slug: open-autopay-fleet-api
- collection_type: open
  name: Autopay Accounting Parking API
  slug: open-autopay-parking-api
- collection_type: open
  name: Autopay Accounting Payment API
  slug: open-autopay-payment-api
- collection_type: open
  name: Autopay Accounting Permit API
  slug: open-autopay-permit-api
- collection_type: open
  name: Autopay Accounting Statistics API
  slug: open-autopay-statistics-api
- collection_type: open
  name: Autopay Accounting Status API
  slug: open-autopay-status-api
- collection_type: open
  name: Autopay Accounting Vehicle API
  slug: open-autopay-vehicle-api
- collection_type: open
  name: Autopay API
  slug: open-autopay
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/autopay-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/autopay-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/autopay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/autopay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/autopay-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/autopay-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/autopay
- group: start
  title: ''
  type: Portal
  url: https://developer.autopay.io
- group: company
  title: ''
  type: Website
  url: https://autopay.no
- group: docs
  title: ''
  type: Documentation
  url: https://developer.autopay.io
- group: auth
  title: ''
  type: Authentication
  url: https://developer.autopay.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.autopay.io
- group: agent
  title: ''
  type: LlmsText
  url: https://autopay.io/llms.txt
created: '2025-02-08'
description: Autopay is a Norwegian parking payment and management platform that provides APIs for parking operators, landlords, fleet managers, and third-party integrators. The platform enables automated parking permit management, payment processing, fleet tracking, and parking statistics with 13+ distinct API endpoints. All integrators must accept the Autopay API Usage Agreement before accessing the APIs.
features:
- description: All Autopay APIs use OAuth for secure authentication and authorization. Integrators must obtain API credentials and accept the Usage Agreement before accessing production endpoints.
  name: OAuth Authentication
- description: Comprehensive parking permit lifecycle management for landlords, operators, and tenants including allocation, assignment, modification, and expiration.
  name: Permit Management
- description: Real-time counts of active parking sessions in parking zones via the Status API, enabling dynamic pricing and occupancy monitoring.
  name: Real-Time Zone Status
- description: Corporate fleet parking management with automatic billing to fleet accounts and vehicle-level tracking across parking facilities.
  name: Fleet Parking Integration
- description: Tap and Park API for third-party validation of parking sessions in Autopay zones, supporting retail validation, employer programs, and visitor parking workflows.
  name: Parking Validation
finops:
- name: Autopay Finops
  service_category: API
  slug: autopay-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/autopay.png
integrations:
- description: Export Autopay invoicing data to external ERP and accounting systems via the Accounting API for automated reconciliation.
  name: Accounting Systems
- description: Integration with building access control and gate systems via the Parking API for automated entry/exit tracking.
  name: Building Access Control
- description: Connect corporate fleet management software with Autopay for parking cost tracking and vehicle permit assignment.
  name: Fleet Management Platforms
layout: provider
modified: '2026-04-19'
name: Autopay
nav: Providers
network: true
overview: 'Autopay publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounting API, Booking API, Customer Club API, and 7 more. Tagged areas include Parking, Parking Payments, Fleet Management, Permits, and Parking Operators.


  Autopay''s developer surface includes authentication, developer portal, documentation, and 10 more developer resources.'
plans:
- name: Autopay Plans Pricing
  plan_count: 3
  slug: autopay-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Autopay Rate Limits
  slug: autopay-rate-limits
scopes:
- name: Autopay Scopes
  scope_count: 3
  slug: autopay-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 13
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 48.4
    developer_ergonomics: 31.0
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 33.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 50.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/autopay/refs/heads/main/screenshots/autopay-2026-06-20T172701.png
security:
- kind: authentication
  name: Autopay Authentication
  slug: autopay-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Autopay Domain Security
  slug: autopay-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Autopay Vulnerability Disclosure
  slug: autopay-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: autopay
tags:
- Parking
- Parking Payments
- Fleet Management
- Permits
- Parking Operators
- Norway
use_cases:
- description: Landlords manage tenant parking permits and allocations through the Permit Landlord and Tenant APIs for residential and commercial properties.
  name: Property Parking Management
- description: Companies manage fleet vehicle parking costs and permits using the Fleet API with automatic billing to corporate accounts.
  name: Corporate Fleet Parking
- description: Parking operators export revenue and occupancy statistics from the Statistics API into accounting and BI systems for reporting.
  name: Parking Revenue Reporting
- description: Retail, hospitality, and office tenants validate visitor parking through the Tap and Park API integrated with access control or POS systems.
  name: Visitor Parking Validation
website: https://autopay.no
---
