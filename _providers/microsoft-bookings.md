---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - finops
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Microsoft Bookings Agentic Access
  operation_count: 23
  slug: microsoft-bookings-agentic-access
  summary_line: 23 operations · 13 acting
api_count: 1
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
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The solutions.bookingBusiness API from Microsoft Bookings — 26 operation(s) for solutions.bookingbusiness.
  name: Microsoft Bookings Solutions.booking Business API
  slug: microsoft-bookings-solutions-bookingbusiness-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The solutions.bookingCurrency API from Microsoft Bookings — 3 operation(s) for solutions.bookingcurrency.
  name: Microsoft Bookings Solutions.booking Currency API
  slug: microsoft-bookings-solutions-bookingcurrency-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The Staff Members API from Microsoft Bookings — 1 operation(s) for staff members.
  name: Microsoft Bookings Staff Members API
  slug: microsoft-bookings-staff-members-api
artifact_total: 36
collections:
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
  href: https://artifacts.apis.io/microsoft-bookings/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.microsoft/
- group: design
  href: https://artifacts.apis.io/microsoft-bookings/rules/microsoft-bookings-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-bookings-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-bookings/json-ld/microsoft-bookings-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-bookings-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-bookings/vocabulary/microsoft-bookings-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-bookings-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/microsoft-bookings/data-model/microsoft-bookings-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-bookings-data-model.yml
- group: design
  href: https://artifacts.apis.io/microsoft-bookings/conventions/microsoft-bookings-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-bookings-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/graph/versioning-and-support
- group: design
  href: https://artifacts.apis.io/microsoft-bookings/lifecycle/microsoft-bookings-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-bookings-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-bookings/errors/microsoft-bookings-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-bookings-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-bookings/conformance/microsoft-bookings-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-bookings-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-bookings/llms/microsoft-bookings-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-bookings-llms.txt
- group: auth
  href: https://artifacts.apis.io/microsoft-bookings/well-known/microsoft-bookings-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-bookings-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-bookings/well-known/microsoft-bookings-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-bookings-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-bookings/hosts/microsoft-bookings-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-bookings-hosts.yml
- group: build
  href: https://artifacts.apis.io/microsoft-bookings/integrations/microsoft-bookings-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/microsoft-bookings-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/microsoft-bookings/vendors/microsoft-bookings-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-bookings-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-bookings/packages/microsoft-bookings-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-bookings-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/changelog
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/category/azure/blog/analyticsonazure
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/android/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.microsoft.com/
- group: auth
  href: https://artifacts.apis.io/microsoft-bookings/security/microsoft-bookings-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-bookings-trust-center.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-bookings/finops/microsoft-bookings-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-bookings-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: agent
  href: https://artifacts.apis.io/microsoft-bookings/agentic-access/microsoft-bookings-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-bookings-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-bookings/security/microsoft-bookings-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-bookings-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-bookings/security/microsoft-bookings-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-bookings-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-bookings/authentication/microsoft-bookings-authentication.yml
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
- has_sources: false
  method: generated
  name: Microsoft Bookings Finops
  primary_unit: request
  service_category: API
  slug: microsoft-bookings-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-bookings.png
json_schemas:
- name: GenericList
  property_count: 1
  slug: microsoft-bookings-generic-list
- name: GenericObject
  property_count: 0
  slug: microsoft-bookings-generic-object
- name: microsoft.graph.bookingAppointment
  property_count: 34
  slug: microsoft-bookings-microsoft-graph-booking-appointment
- name: microsoft.graph.bookingBusiness
  property_count: 23
  slug: microsoft-bookings-microsoft-graph-booking-business
- name: microsoft.graph.bookingCustomQuestion
  property_count: 7
  slug: microsoft-bookings-microsoft-graph-booking-custom-question
- name: microsoft.graph.bookingService
  property_count: 26
  slug: microsoft-bookings-microsoft-graph-booking-service
- name: dateTimeTimeZone
  property_count: 3
  slug: microsoft-bookings-microsoft-graph-date-time-time-zone
- name: staffAvailabilityItem
  property_count: 3
  slug: microsoft-bookings-microsoft-graph-staff-availability-item
jsonld:
- class_count: 120
  name: Microsoft Bookings Context
  property_count: 248
  slug: microsoft-bookings-context
layout: provider
modified: '2026-05-19'
name: Microsoft Bookings
nav: Providers
network: true
overview: 'Microsoft Bookings publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Appointments API, BookingBusinesses API, Currencies API, and 6 more. Tagged areas include Booking, Scheduling, Appointments, and Microsoft Graph.


  The Microsoft Bookings catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft Bookings'' developer surface includes changelog, engineering blog, getting-started guide, documentation, authentication, support, and 33 more developer resources.'
plans:
- name: Microsoft Bookings Plans Pricing
  plan_count: 0
  slug: microsoft-bookings-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Microsoft Bookings Rate Limits
  slug: microsoft-bookings-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Microsoft Bookings API Rules
  rule_count: 50
  severity_counts:
    error: 42
    hint: 0
    info: 4
    warn: 4
  slug: microsoft-bookings-rules
score:
  band: developing
  composite: 50.6
  coverage:
    artifact_dirs: 29
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 16.0
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 58.6
    developer_ergonomics: 58.9
    discoverability: 50.0
    operational_transparency: 52.6
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/microsoft-bookings/microsoft-bookings-2026-06-20T185445.png
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
- kind: trust-center
  name: Microsoft Bookings Trust Center
  slug: microsoft-bookings-trust-center
  summary_line: GDPR
skill_count: 1
skills:
- name: microsoft-bookings-book-appointment
  slug: microsoft-bookings-book-appointment
slug: microsoft-bookings
tags:
- Booking
- Scheduling
- Appointments
- Microsoft Graph
website: https://www.microsoft.com/
---
