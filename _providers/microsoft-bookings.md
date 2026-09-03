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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Microsoft Bookings Agentic Access
  operation_count: 23
  slug: microsoft-bookings-agentic-access
  summary_line: 23 operations · 13 acting
api_count: 7
apis:
- baseURL: https://graph.microsoft.com/
  baseurl_source: declared
  description: The Appointments API from Microsoft Bookings — 3 operation(s) for appointments.
  name: Microsoft Bookings Appointments API
  slug: microsoft-bookings-appointments-api
- baseURL: https://graph.microsoft.com/
  baseurl_source: declared
  description: The BookingBusinesses API from Microsoft Bookings — 4 operation(s) for bookingbusinesses.
  name: Microsoft Bookings BookingBusinesses API
  slug: microsoft-bookings-bookingbusinesses-api
- baseURL: https://graph.microsoft.com/
  baseurl_source: declared
  description: The Currencies API from Microsoft Bookings — 1 operation(s) for currencies.
  name: Microsoft Bookings Currencies API
  slug: microsoft-bookings-currencies-api
- baseURL: https://graph.microsoft.com/
  baseurl_source: declared
  description: The Customers API from Microsoft Bookings — 1 operation(s) for customers.
  name: Microsoft Bookings Customers API
  slug: microsoft-bookings-customers-api
- baseURL: https://graph.microsoft.com/
  baseurl_source: declared
  description: The CustomQuestions API from Microsoft Bookings — 1 operation(s) for customquestions.
  name: Microsoft Bookings CustomQuestions API
  slug: microsoft-bookings-customquestions-api
- baseURL: https://graph.microsoft.com/
  baseurl_source: declared
  description: The Services API from Microsoft Bookings — 2 operation(s) for services.
  name: Microsoft Bookings Services API
  slug: microsoft-bookings-services-api
- baseURL: https://graph.microsoft.com/
  baseurl_source: declared
  description: The StaffMembers API from Microsoft Bookings — 1 operation(s) for staffmembers.
  name: Microsoft Bookings StaffMembers API
  slug: microsoft-bookings-staffmembers-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Bookings API (Microsoft Graph) Appointments API
  slug: open-microsoft-bookings-appointments-api
- collection_type: open
  name: Microsoft Bookings API (Microsoft Graph) Appointments BookingBusinesses API
  slug: open-microsoft-bookings-bookingbusinesses-api
- collection_type: open
  name: Microsoft Bookings API (Microsoft Graph) Appointments Currencies API
  slug: open-microsoft-bookings-currencies-api
- collection_type: open
  name: Microsoft Bookings API (Microsoft Graph) Appointments Customers API
  slug: open-microsoft-bookings-customers-api
- collection_type: open
  name: Microsoft Bookings API (Microsoft Graph) Appointments CustomQuestions API
  slug: open-microsoft-bookings-customquestions-api
- collection_type: open
  name: Microsoft Bookings API (Microsoft Graph) Appointments Services API
  slug: open-microsoft-bookings-services-api
- collection_type: open
  name: Microsoft Bookings API (Microsoft Graph) Appointments StaffMembers API
  slug: open-microsoft-bookings-staffmembers-api
- collection_type: open
  name: Microsoft Bookings API (Microsoft Graph)
  slug: open-microsoft-bookings
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-bookings-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-bookings-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-bookings-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-bookings-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
created: '2026-03-13'
description: Microsoft Bookings provides scheduling and appointment management APIs through Microsoft Graph for businesses, services, staff, and customers.
finops:
- name: Microsoft Bookings Finops
  service_category: API
  slug: microsoft-bookings-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-bookings.png
layout: provider
modified: '2026-05-19'
name: Microsoft Bookings
nav: Providers
network: true
overview: 'Microsoft Bookings publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Appointments API, BookingBusinesses API, Currencies API, and 4 more. Tagged areas include Bookings, Scheduling, Appointments, and Microsoft Graph.


  Microsoft Bookings'' developer surface includes authentication, support, and 8 more developer resources.'
plans:
- name: Microsoft Bookings Plans Pricing
  plan_count: 3
  slug: microsoft-bookings-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Microsoft Bookings Rate Limits
  slug: microsoft-bookings-rate-limits
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 9
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 33.3
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 33.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-bookings/refs/heads/main/screenshots/microsoft-bookings-2026-06-20T185445.png
security:
- kind: authentication
  name: Microsoft Bookings Authentication
  slug: microsoft-bookings-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microsoft Bookings Domain Security
  slug: microsoft-bookings-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Bookings Vulnerability Disclosure
  slug: microsoft-bookings-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-bookings
tags:
- Bookings
- Scheduling
- Appointments
- Microsoft Graph
---
