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
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://www.workmarket.com/api/v1
  baseurl_source: declared
  description: The Addressbook API from Work Market — 5 operation(s) for addressbook.
  name: Work Market Addressbook API
  slug: work-market-addressbook-api
- baseURL: https://www.workmarket.com/api/v1
  baseurl_source: declared
  description: The Assignments API from Work Market — 39 operation(s) for assignments.
  name: Work Market Assignments API
  slug: work-market-assignments-api
- baseURL: https://www.workmarket.com/api/v1
  baseurl_source: declared
  description: The Authorization API from Work Market — 1 operation(s) for authorization.
  name: Work Market Authorization API
  slug: work-market-authorization-api
- baseURL: https://www.workmarket.com/api/v1
  baseurl_source: declared
  description: The Constants API from Work Market — 6 operation(s) for constants.
  name: Work Market Constants API
  slug: work-market-constants-api
- baseURL: https://www.workmarket.com/api/v1
  baseurl_source: declared
  description: The Custom Fields API from Work Market — 1 operation(s) for custom fields.
  name: Work Market Custom Fields API
  slug: work-market-custom-fields-api
- baseURL: https://www.workmarket.com/api/v1
  baseurl_source: declared
  description: The Labels API from Work Market — 3 operation(s) for labels.
  name: Work Market Labels API
  slug: work-market-labels-api
- baseURL: https://www.workmarket.com/api/v1
  baseurl_source: declared
  description: The Locations API from Work Market — 1 operation(s) for locations.
  name: Work Market Locations API
  slug: work-market-locations-api
- baseURL: https://www.workmarket.com/api/v1
  baseurl_source: declared
  description: The Projects API from Work Market — 2 operation(s) for projects.
  name: Work Market Projects API
  slug: work-market-projects-api
- baseURL: https://www.workmarket.com/api/v1
  baseurl_source: declared
  description: The Talent Pools API from Work Market — 6 operation(s) for talent pools.
  name: Work Market Talent Pools API
  slug: work-market-talent-pools-api
- baseURL: https://www.workmarket.com/api/v1
  baseurl_source: declared
  description: The UpdateCheckIn API from Work Market — 2 operation(s) for updatecheckin.
  name: Work Market UpdateCheckIn API
  slug: work-market-updatecheckin-api
artifact_total: 35
asyncapis:
- description: ''
  name: Work Market Webhooks
  slug: work-market-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Swagger spec for Work Market API v1 Addressbook API
  slug: open-work-market-addressbook-api
- collection_type: open
  name: Swagger spec for Work Market API v1 Addressbook Assignments API
  slug: open-work-market-assignments-api
- collection_type: open
  name: Swagger spec for Work Market API v1 Addressbook Authorization API
  slug: open-work-market-authorization-api
- collection_type: open
  name: Swagger spec for Work Market API v1 Addressbook Constants API
  slug: open-work-market-constants-api
- collection_type: open
  name: Swagger spec for Work Market API v1 Addressbook Custom Fields API
  slug: open-work-market-custom-fields-api
- collection_type: open
  name: Swagger spec for Work Market API v1 Addressbook Labels API
  slug: open-work-market-labels-api
- collection_type: open
  name: Swagger spec for Work Market API v1 Addressbook Locations API
  slug: open-work-market-locations-api
- collection_type: open
  name: Swagger spec for Work Market API v1 Addressbook Projects API
  slug: open-work-market-projects-api
- collection_type: open
  name: Swagger spec for Work Market API v1 Addressbook Talent Pools API
  slug: open-work-market-talent-pools-api
- collection_type: open
  name: Swagger spec for Work Market API v1 Addressbook UpdateCheckIn API
  slug: open-work-market-updatecheckin-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/work-market-employer-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/work-market-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://workmarket.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.workmarket.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.workmarket.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://employer-api.workmarket.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.workmarket.com/page/best-practices
- group: operate
  title: ''
  type: Support
  url: https://workmarket.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.workmarket.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/workmarket-oss
- group: operate
  title: ''
  type: StatusPage
  url: https://status.workmarket.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workmarket.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workmarket.com/privacy
- group: start
  title: ''
  type: Login
  url: https://www.workmarket.com/login
- group: start
  title: ''
  type: SignUp
  url: https://www.workmarket.com/contractors/join-workmarket
- group: build
  title: ''
  type: Postman
  url: https://www.getpostman.com/collections/e4829238bea777d8995a
- group: design
  title: ''
  type: Webhooks
  url: https://developer.workmarket.com/page/webhooks
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/work-market-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/work-market-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/work-market-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/work-market-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/work-market-mcp.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/work-market-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/work-market-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/work-market-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/work-market-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/work-market-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/work-market-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/work-market-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: WorkMarket, an ADP company, is an independent contractor management platform that helps businesses organize, manage, and pay their extended workforce of 1099 contractors and freelancers. The platform covers contractor onboarding and verification, Labor Clouds for organizing talent by skill and location, assignment creation and tracking, compliance support, and fast payment processing. The WorkMarket Employer API exposes assignments, talent pools, address book, custom fields, labels, projects, and payment approval as a REST API, with webhooks, a Relay automation tool, and a certified MuleSoft connector for enterprise integration.
image: https://files.readme.io/df14adf-wm.dev.portal.logo.png
json_schemas:
- name: AssignmentDetails
  property_count: 49
  slug: work-market-assignment-details
- name: AssignmentListItem
  property_count: 32
  slug: work-market-assignment-list-item
- name: Client
  property_count: 3
  slug: work-market-client
- name: CustomField
  property_count: 6
  slug: work-market-custom-field
- name: Location
  property_count: 12
  slug: work-market-location
- name: Payment
  property_count: 7
  slug: work-market-payment
- name: Pricing
  property_count: 15
  slug: work-market-pricing
- name: Project
  property_count: 2
  slug: work-market-project
- name: TalentPool
  property_count: 6
  slug: work-market-talent-pool
- name: Template
  property_count: 43
  slug: work-market-template
layout: provider
mcp_servers:
- description: No official WorkMarket MCP server was found (npm, the official MCP registry surface, and the developer portal were searched 2026-07-21). This is a candidate tool list derived one-to-one from the 66 op
  name: Work Market MCP Server
  slug: work-market-mcp-server
modified: '2026-07-21'
name: Work Market
nav: Providers
network: true
overview: 'Work Market publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Addressbook API, Assignments API, Authorization API, and 7 more. Tagged areas include Workforce Management, Contractors, Freelance, Gig Economy, and Human Resources.


  The Work Market catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Work Market''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, sandbox, and 23 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 20
    catalog_gap: 68.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 54.5
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 22.4
  previous_composite: 41.9
  provenance:
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
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/work-market/refs/heads/main/screenshots/work-market-2026-08-17T082936.png
security:
- kind: authentication
  name: Work Market Authentication
  slug: work-market-authentication
  summary_line: accessToken · 1 scheme
- kind: domain-security
  name: Work Market Domain Security
  slug: work-market-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: work-market
tags:
- Workforce Management
- Contractors
- Freelance
- Gig Economy
- Human Resources
- Payments
- Field Services
- Staffing
website: https://workmarket.com
---
