---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 41
  human_in_the_loop: 1
  name: Qminder Agentic Access
  operation_count: 53
  slug: qminder-agentic-access
  summary_line: 53 operations · 41 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.qminder.com
  baseurl_source: declared
  description: Manage scheduled appointments
  name: Qminder Appointments API
  slug: qminder-appointments-api
- baseURL: https://api.qminder.com
  baseurl_source: declared
  description: Manage custom data fields for locations
  name: Qminder Input Fields API
  slug: qminder-input-fields-api
- baseURL: https://api.qminder.com
  baseurl_source: declared
  description: Manage virtual queues within locations
  name: Qminder Lines API
  slug: qminder-lines-api
- baseURL: https://api.qminder.com
  baseurl_source: declared
  description: Manage physical service locations
  name: Qminder Locations API
  slug: qminder-locations-api
- baseURL: https://api.qminder.com
  baseurl_source: declared
  description: Manage visitor queue entries
  name: Qminder Tickets API
  slug: qminder-tickets-api
- baseURL: https://api.qminder.com
  baseurl_source: declared
  description: Manage user accounts and permissions
  name: Qminder Users API
  slug: qminder-users-api
- baseURL: https://api.qminder.com
  baseurl_source: declared
  description: Manage webhook subscriptions
  name: Qminder Webhooks API
  slug: qminder-webhooks-api
artifact_total: 25
asyncapis:
- description: ''
  name: Qminder Events Webhooks
  slug: qminder-events-webhooks
collections:
- collection_type: open
  name: Qminder Appointments API
  slug: open-qminder-appointments-api
- collection_type: open
  name: Qminder Appointments Input Fields API
  slug: open-qminder-input-fields-api
- collection_type: open
  name: Qminder Appointments Lines API
  slug: open-qminder-lines-api
- collection_type: open
  name: Qminder Appointments Locations API
  slug: open-qminder-locations-api
- collection_type: open
  name: Qminder Appointments Tickets API
  slug: open-qminder-tickets-api
- collection_type: open
  name: Qminder Appointments Users API
  slug: open-qminder-users-api
- collection_type: open
  name: Qminder Appointments Webhooks API
  slug: open-qminder-webhooks-api
common:
- group: commercial
  href: https://artifacts.apis.io/qminder/plans/qminder-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/qminder-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/qminder/capabilities/qminder-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/qminder-capability-edges.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.qminder.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.qminder.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.qminder.com/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.qminder.com/reference/overview
- group: docs
  href: https://artifacts.apis.io/qminder/openapi/_original/qminder-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/qminder-openapi-original.json
- group: agent
  href: https://artifacts.apis.io/qminder/llms/qminder-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/qminder-llms.txt
- group: auth
  href: https://artifacts.apis.io/qminder/authentication/qminder-authentication.yml
  title: ''
  type: Authentication
  url: authentication/qminder-authentication.yml
- group: build
  href: https://artifacts.apis.io/qminder/packages/qminder-packages.yml
  title: ''
  type: SDKs
  url: packages/qminder-packages.yml
- group: build
  href: https://artifacts.apis.io/qminder/packages/qminder-packages.yml
  title: ''
  type: Packages
  url: packages/qminder-packages.yml
- group: agent
  href: https://artifacts.apis.io/qminder/mcp/qminder-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/qminder-mcp.yml
- group: agent
  href: https://artifacts.apis.io/qminder/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/qminder/agentic-access/qminder-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/qminder-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/qminder/asyncapi/qminder-events-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/qminder-events-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/qminder/rate-limits/qminder-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/qminder-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/qminder/errors/qminder-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/qminder-problem-types.yml
- group: design
  href: https://artifacts.apis.io/qminder/conventions/qminder-conventions.yml
  title: ''
  type: Conventions
  url: conventions/qminder-conventions.yml
- group: design
  href: https://artifacts.apis.io/qminder/data-model/qminder-data-model.yml
  title: ''
  type: DataModel
  url: data-model/qminder-data-model.yml
- group: design
  href: https://artifacts.apis.io/qminder/conformance/qminder-conformance.yml
  title: ''
  type: Conformance
  url: conformance/qminder-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.qminder.com/security/
- group: auth
  href: https://artifacts.apis.io/qminder/security/qminder-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/qminder-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/qminder/security/qminder-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qminder-domain-security.yml
- group: other
  href: https://artifacts.apis.io/qminder/overlays/qminder-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qminder-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/qminder/lifecycle/qminder-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/qminder-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qminder.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Qminder
- group: company
  title: ''
  type: Blog
  url: https://www.qminder.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.qminder.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.qminder.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.qminder.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.qminder.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qminder.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qminder.com/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://www.qminder.com
created: '2026-07-17'
description: Qminder is a cloud-based queue management and appointment scheduling platform that helps retail, healthcare, government, and education organizations manage visitor flow, virtual queues, and service points across physical locations. Its developer platform exposes a REST API and a GraphQL API (with real-time subscriptions) at api.qminder.com for creating tickets, calling and serving visitors, scheduling appointments, managing locations, lines, desks, users, and custom input fields, plus webhooks for ticket, line, and location events. An official JavaScript/TypeScript SDK (qminder-api) is published to npm.
finops:
- has_sources: true
  method: derived
  name: Qminder Finops
  primary_unit: subscription
  service_category: ''
  slug: qminder-finops
  template: false
image: https://www.qminder.com/favicon.ico
layout: provider
modified: '2026-07-20'
name: Qminder
nav: Providers
network: true
overview: 'Qminder publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Appointments API, Input Fields API, Lines API, and 4 more. Tagged areas include Company, Queue Management, Appointment Scheduling, Visitor Management, and Customer Experience.


  The Qminder catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Qminder''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, pricing, and 28 more developer resources.'
plans:
- name: Qminder Plans Pricing
  plan_count: 7
  slug: qminder-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Qminder Rate Limits
  slug: qminder-rate-limits
score:
  band: strong
  composite: 64.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 54.5
    developer_ergonomics: 66.1
    discoverability: 66.1
    operational_transparency: 50.0
  previous_composite: 56.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/qminder/qminder-2026-08-17T081418.png
security:
- kind: authentication
  name: Qminder Authentication
  slug: qminder-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Qminder Domain Security
  slug: qminder-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Qminder Trust Center
  slug: qminder-trust-center
  summary_line: SOC 2, HIPAA, GDPR
skill_count: 3
skills:
- name: Check a visitor into a queue and serve them
  slug: qminder-check-in-and-serve
- name: Register and manage webhook listeners
  slug: qminder-manage-webhooks
- name: Schedule and check in an appointment
  slug: qminder-schedule-appointment
slug: qminder
tags:
- Company
- Queue Management
- Appointment Scheduling
- Visitor Management
- Customer Experience
- REST
- GraphQL
- Webhook
- Software-as-a-Service
- Scheduling
website: https://www.qminder.com
---
