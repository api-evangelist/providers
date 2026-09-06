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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.3
  scored_at: '2026-09-05'
api_count: 2
apis:
- baseURL: https://api.dispatch.me
  baseurl_source: declared
  description: Scheduled times at which an assigned technician performs work for a job.
  name: Dispatch Appointments API
  slug: dispatch-appointments-api
- baseURL: https://api.dispatch.me
  baseurl_source: declared
  description: OAuth 2.0 token issuance and refresh.
  name: Dispatch Authentication API
  slug: dispatch-authentication-api
- baseURL: https://api.dispatch.me
  baseurl_source: declared
  description: Brands or divisions controlling logo and copy. Accessible only to job sources.
  name: Dispatch Brands API
  slug: dispatch-brands-api
- baseURL: https://api.dispatch.me
  baseurl_source: declared
  description: The homeowner or end customer a job belongs to.
  name: Dispatch Customers API
  slug: dispatch-customers-api
- baseURL: https://api.dispatch.me
  baseurl_source: declared
  description: Files and photos associated with a job.
  name: Dispatch Files API
  slug: dispatch-files-api
- baseURL: https://api.dispatch.me
  baseurl_source: declared
  description: A single body of work for a customer, assigned to an organization.
  name: Dispatch Jobs API
  slug: dispatch-jobs-api
- baseURL: https://api.dispatch.me
  baseurl_source: declared
  description: The branch or third-party service provider responsible for doing the work.
  name: Dispatch Organizations API
  slug: dispatch-organizations-api
- baseURL: https://api.dispatch.me
  baseurl_source: declared
  description: Where job information originated.
  name: Dispatch Sources API
  slug: dispatch-sources-api
- baseURL: https://api.dispatch.me
  baseurl_source: declared
  description: Customer surveys sent when an appointment or job completes.
  name: Dispatch Survey Responses API
  slug: dispatch-survey-responses-api
- baseURL: https://api.dispatch.me
  baseurl_source: declared
  description: Dispatchers and technicians using the Dispatch applications.
  name: Dispatch Users API
  slug: dispatch-users-api
- baseURL: https://api.dispatch.me
  baseurl_source: declared
  description: Composite object creating jobs, customers, organizations and appointments in one call.
  name: Dispatch Work Orders API
  slug: dispatch-work-orders-api
artifact_total: 26
asyncapis:
- description: ''
  name: Dispatch Webhooks
  slug: dispatch-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dispatch Files API v1 Appointments API
  slug: open-dispatch-appointments-api
- collection_type: open
  name: Dispatch Files API v1 Appointments Authentication API
  slug: open-dispatch-authentication-api
- collection_type: open
  name: Dispatch Files API v1 Appointments Brands API
  slug: open-dispatch-brands-api
- collection_type: open
  name: Dispatch Files API v1 Appointments Customers API
  slug: open-dispatch-customers-api
- collection_type: open
  name: Dispatch API v1 Appointments Files API
  slug: open-dispatch-files-api
- collection_type: open
  name: Dispatch Files API v1 Appointments Jobs API
  slug: open-dispatch-jobs-api
- collection_type: open
  name: Dispatch Files API v1 Appointments Organizations API
  slug: open-dispatch-organizations-api
- collection_type: open
  name: Dispatch Files API v1 Appointments Sources API
  slug: open-dispatch-sources-api
- collection_type: open
  name: Dispatch Files API v1 Appointments Survey Responses API
  slug: open-dispatch-survey-responses-api
- collection_type: open
  name: Dispatch Files API v1 Appointments Users API
  slug: open-dispatch-users-api
- collection_type: open
  name: Dispatch Files API v1 Appointments Work Orders API
  slug: open-dispatch-work-orders-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/dispatch-files-v1-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://dispatch.me
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/DispatchMe/v3-api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/DispatchMe/v3-api-docs/blob/master/source/index.html.md
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/DispatchMe/v3-api-docs/blob/master/source/index.html.md#getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DispatchMe
- group: company
  title: ''
  type: Blog
  url: https://dispatch.me/blog
- group: operate
  title: ''
  type: Support
  url: https://dispatch.me/contact
- group: start
  title: ''
  type: Login
  url: https://dispatch.me/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dispatch.me/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dispatch.me/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dispatch.me
- group: auth
  title: ''
  type: Authentication
  url: authentication/dispatch-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dispatch-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dispatch-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dispatch-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dispatch-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dispatch-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dispatch-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/dispatch-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dispatch-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/dispatch-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dispatch-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/dispatch-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dispatch-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dispatch-domain-security.yml
created: '2026-07-17'
description: Dispatch (Dispatch Technologies, Boston MA) is a service-orchestration platform for enterprises that fulfil work through networks of independent contractors and third-party service providers - manufacturer warranty, home and property claims, retail, franchise and proptech. Dispatch gives the brand visibility into work performed by providers who keep using their own field-service tools, and gives the homeowner a tracked, branded service experience. Its public REST API v3 exposes the core business objects - jobs, customers, organizations, appointments, users, sources, brands, survey responses and composite work orders - to job sources such as warranty companies and equipment manufacturers, and to service enterprises running first-party branch networks. The API is secured with OAuth 2.0 bearer tokens, offers a full sandbox environment, and is documented in a public GitHub repository.
image: https://dispatch.me/wp-content/uploads/2019/11/cropped-favicon-1-300x300.png
layout: provider
modified: '2026-07-20'
name: Dispatch
nav: Providers
network: true
overview: 'Dispatch publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Appointments API, Authentication API, Brands API, and 8 more. Tagged areas include Field Service, Service Orchestration, Work Orders, Scheduling, and Contractor Networks.


  The Dispatch catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Dispatch''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 20 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 23.5
    developer_ergonomics: 63.7
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 34.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dispatch/refs/heads/main/screenshots/dispatch-2026-07-25T212107.png
security:
- kind: authentication
  name: Dispatch Authentication
  slug: dispatch-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Dispatch Domain Security
  slug: dispatch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dispatch
tags:
- Field Service
- Service Orchestration
- Work Orders
- Scheduling
- Contractor Networks
- Home Services
- Warranty
- Customer Experience
- Logistics
- Company
website: https://dispatch.me
---
