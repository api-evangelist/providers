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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: SpaceIQ's (SiQ) GraphQL API. A single endpoint at https://api.spaceiq.com/queries accepts POST requests with a JSON query body and an access-token bearer header. Read operations cover companies, build
  name: SiQ GraphQL API
  slug: siq-graphql-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/spaceiq-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://eptura.com/spaceiq/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.spaceiq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.spaceiq.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.spaceiq.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.spaceiq.com/
- group: company
  title: ''
  type: Blog
  url: https://eptura.com/discover-more/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://eptura.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://eptura.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://eptura.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://eptura.com/terms/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.eptura.com/
- group: auth
  title: ''
  type: Compliance
  url: https://security.eptura.com/
- group: auth
  title: ''
  type: Security
  url: https://security.eptura.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/spaceiq-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spaceiq-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spaceiq-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spaceiq-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spaceiq-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spaceiq-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/spaceiq-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spaceiq-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/spaceiq-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spaceiq-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spaceiq-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'SpaceIQ (branded SiQ, now part of Eptura) is a workplace and space-management platform for optimizing physical office environments: space planning, desk and meeting-room booking, hoteling, moves management, wayfinding, floorplan management, occupancy analytics, building-attendance reporting, and real-estate forecasting. SpaceIQ exposes a GraphQL API (schema version 1.7) at api.spaceiq.com/queries for reading workplace data (companies, buildings, floors, spaces, departments, employees, meeting-room calendars, map images, and reports/exports) and for creating and deleting meeting-room calendar events. All access is over HTTPS with an admin/IT-generated access token; the schema is fully introspectable.'
image: https://eptura.com/spaceiq/
layout: provider
modified: '2026-07-21'
name: SpaceIQ
nav: Providers
network: true
overview: 'SpaceIQ publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Workplace Management, Space Management, Facilities Management, and Desk Booking.


  SpaceIQ''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, support, authentication, and 19 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 32.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spaceiq/refs/heads/main/screenshots/spaceiq-2026-09-02T160308.png
security:
- kind: authentication
  name: Spaceiq Authentication
  slug: spaceiq-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Spaceiq Domain Security
  slug: spaceiq-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Spaceiq Vulnerability Disclosure
  slug: spaceiq-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Spaceiq Trust Center
  slug: spaceiq-trust-center
  summary_line: ISO 27001, FedRAMP, GDPR
slug: spaceiq
tags:
- Company
- Workplace Management
- Space Management
- Facilities Management
- Desk Booking
- Hoteling
- Meeting Rooms
- Occupancy Analytics
- Real-Estate
- Floor Plans
- GraphQL
- IWMS
- Eptura
website: https://eptura.com/spaceiq/
---
