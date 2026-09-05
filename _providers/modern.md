---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.6
  scored_at: '2026-09-04'
api_count: 8
apis:
- baseURL: https://connect.modernis.com
  baseurl_source: declared
  description: Franchise dashboards and dashboard types
  name: Modern Dashboards API
  slug: modern-dashboards-api
- baseURL: https://connect.modernis.com
  baseurl_source: declared
  description: Work-order event types and event creation
  name: Modern Events API
  slug: modern-events-api
- baseURL: https://connect.modernis.com
  baseurl_source: declared
  description: Token exchange / authentication
  name: Modern Federation API
  slug: modern-federation-api
- baseURL: https://connect.modernis.com
  baseurl_source: declared
  description: Technician / work-order notes
  name: Modern Notes API
  slug: modern-notes-api
- baseURL: https://connect.modernis.com
  baseurl_source: declared
  description: Customer notifications
  name: Modern Notifications API
  slug: modern-notifications-api
- baseURL: https://connect.modernis.com
  baseurl_source: declared
  description: Technician records
  name: Modern Technicians API
  slug: modern-technicians-api
- baseURL: https://connect.modernis.com
  baseurl_source: declared
  description: Dashboard users
  name: Modern Users API
  slug: modern-users-api
- baseURL: https://connect.modernis.com
  baseurl_source: declared
  description: Service work order lifecycle
  name: Modern Work Orders API
  slug: modern-work-orders-api
artifact_total: 20
collections:
- collection_type: postman
  name: MODERN Partner API - Documentation
  slug: postman-modern-partner-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MODERN Partner Dashboards API
  slug: open-modern-dashboards-api
- collection_type: open
  name: MODERN Partner Dashboards Events API
  slug: open-modern-events-api
- collection_type: open
  name: MODERN Partner Dashboards Federation API
  slug: open-modern-federation-api
- collection_type: open
  name: MODERN Partner Dashboards Notes API
  slug: open-modern-notes-api
- collection_type: open
  name: MODERN Partner Dashboards Notifications API
  slug: open-modern-notifications-api
- collection_type: open
  name: MODERN Partner Dashboards Technicians API
  slug: open-modern-technicians-api
- collection_type: open
  name: MODERN Partner Dashboards Users API
  slug: open-modern-users-api
- collection_type: open
  name: MODERN Partner Dashboards Work Orders API
  slug: open-modern-work-orders-api
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/modern-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/modern-partner-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/modern-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://modernis.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.modernis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.modernis.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.modernis.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/modern-authentication.yml
- group: start
  title: ''
  type: Login
  url: https://service.modernis.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://modernis.com/privacy-policy/
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Modern (modernis.com) is a two-way customer interaction platform for heavy-equipment dealerships, unifying service communications "from intake to invoice" across construction, agriculture, mining, landscaping, and material-handling sectors. It provides two-way text and email messaging, digital repair-order approvals, inspection and warranty documentation, outbound maintenance scheduling, rental tracking, parts-order status, and DMS integration. The MODERN Partner API (docs.modernis.com, base https://connect.modernis.com) lets authorized integrators read dealership dashboards, manage service work orders, post work-order events, send customer notifications, and maintain technicians and notes on a franchise's behalf using 24-hour bearer tokens exchanged from franchise credentials.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/modern.png
layout: provider
modified: '2026-07-20'
name: Modern
nav: Providers
network: true
overview: 'Modern publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Dashboards API, Events API, Federation API, and 5 more. Tagged areas include Company, Heavy Equipment, Dealership, Field Service, and Work Orders.


  Modern''s developer surface includes documentation, API reference, authentication, and 8 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 4.5
    contract_quality: 15.8
    developer_ergonomics: 31.5
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 22.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/modern/refs/heads/main/screenshots/modern-2026-08-07T183934.png
security:
- kind: authentication
  name: Modern Authentication
  slug: modern-authentication
  summary_line: http-basic/http-bearer · 2 schemes
- kind: domain-security
  name: Modern Domain Security
  slug: modern-domain-security
  summary_line: TLSv1.3
slug: modern
tags:
- Company
- Heavy Equipment
- Dealership
- Field Service
- Work Orders
- Customer Communications
- Notification
- Partner API
website: https://modernis.com/
---
