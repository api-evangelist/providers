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
    agentic_access: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Humanapi Agentic Access
  operation_count: 15
  slug: humanapi-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 2
apis:
- baseURL: https://admin.humanapi.co
  baseurl_source: declared
  description: API endpoints to authorize a client app for the Admin API
  name: HumanAPI admin API
  slug: humanapi-admin-api
- baseURL: https://admin.humanapi.co
  baseurl_source: declared
  description: The connect API from HumanAPI — 1 operation(s) for connect.
  name: HumanAPI connect API
  slug: humanapi-connect-api
- baseURL: https://admin.humanapi.co
  baseurl_source: declared
  description: API endpoints to get orders
  name: HumanAPI orders API
  slug: humanapi-orders-api
- baseURL: https://admin.humanapi.co
  baseurl_source: declared
  description: The reports API from HumanAPI — 2 operation(s) for reports.
  name: HumanAPI reports API
  slug: humanapi-reports-api
- baseURL: https://admin.humanapi.co
  baseurl_source: declared
  description: The resources API from HumanAPI — 1 operation(s) for resources.
  name: HumanAPI resources API
  slug: humanapi-resources-api
- baseURL: https://admin.humanapi.co
  baseurl_source: declared
  description: The subscriptions API from HumanAPI — 2 operation(s) for subscriptions.
  name: HumanAPI subscriptions API
  slug: humanapi-subscriptions-api
- baseURL: https://admin.humanapi.co
  baseurl_source: declared
  description: The users API from HumanAPI — 4 operation(s) for users.
  name: HumanAPI users API
  slug: humanapi-users-api
artifact_total: 19
asyncapis:
- description: ''
  name: Humanapi Notifications Webhooks
  slug: humanapi-notifications-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: admin API
  slug: open-humanapi-admin-api
- collection_type: open
  name: admin connect API
  slug: open-humanapi-connect-api
- collection_type: open
  name: admin orders API
  slug: open-humanapi-orders-api
- collection_type: open
  name: admin reports API
  slug: open-humanapi-reports-api
- collection_type: open
  name: admin resources API
  slug: open-humanapi-resources-api
- collection_type: open
  name: admin subscriptions API
  slug: open-humanapi-subscriptions-api
- collection_type: open
  name: admin users API
  slug: open-humanapi-users-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/lexisnexis-risk-solutions/
- group: other
  title: ''
  type: Overlay
  url: overlays/humanapi-admin-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.humanapi.co
- group: docs
  title: ''
  type: Documentation
  url: https://reference.humanapi.co
- group: docs
  title: ''
  type: APIReference
  url: https://reference.humanapi.co/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://reference.humanapi.co/docs/overview
- group: operate
  title: ''
  type: Support
  url: https://support.humanapi.co
- group: start
  title: ''
  type: Login
  url: https://portal.humanapi.co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.humanapi.co/developer-terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/humanapi
- group: operate
  title: ''
  type: StatusPage
  url: https://status.humanapi.co
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/humanapi-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/humanapi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/humanapi-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/humanapi-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/humanapi-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/humanapi-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/humanapi-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/humanapi-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/humanapi-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/humanapi-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/humanapi-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/humanapi-notifications-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/humanapi-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/humanapi-agentic-access.yml
created: '2026-07-17'
description: Human API is a health-intelligence platform that provides real-time, programmatic access to structured digital health and medical data aggregated from providers, labs, pharmacies, devices and wellness apps. Its Admin API lets enterprises (notably life-insurance underwriting) create users, submit data-retrieval orders, connect a member's health-data sources, and fetch generated individual and combined reports, with webhook notifications on order completion. Authentication is a bearer JWT obtained from client-credentials token endpoints. Human API was founded in 2013, backed by a16z, and acquired by LexisNexis Risk Solutions in 2021.
image: https://github.com/humanapi.png
layout: provider
modified: '2026-07-19'
name: HumanAPI
nav: Providers
network: true
overview: 'HumanAPI publishes 7 APIs on the [APIs.io](https://apis.io/) network, including admin API, connect API, orders API, and 4 more. Tagged areas include Health, Healthcare, Health Data, Medical Records, and Insurance.


  The HumanAPI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  HumanAPI''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 21 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 57.7
    developer_ergonomics: 48.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 38.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/humanapi/refs/heads/main/screenshots/humanapi-2026-07-25T221702.png
security:
- kind: authentication
  name: Humanapi Authentication
  slug: humanapi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Humanapi Domain Security
  slug: humanapi-domain-security
  summary_line: TLSv1.2 · DMARC
slug: humanapi
tags:
- Health
- Healthcare
- Health Data
- Medical Records
- Insurance
- Underwriting
- Wellness
- Data Aggregation
- Reports
- FHIR-adjacent
website: https://portal.humanapi.co
---
