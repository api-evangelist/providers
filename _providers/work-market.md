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
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-07-28'
api_count: 10
apis:
- description: The Addressbook API from Work Market — 5 operation(s) for addressbook.
  name: Work Market Addressbook API
  slug: work-market-addressbook-api
- description: The Assignments API from Work Market — 39 operation(s) for assignments.
  name: Work Market Assignments API
  slug: work-market-assignments-api
- description: The Authorization API from Work Market — 1 operation(s) for authorization.
  name: Work Market Authorization API
  slug: work-market-authorization-api
- description: The Constants API from Work Market — 6 operation(s) for constants.
  name: Work Market Constants API
  slug: work-market-constants-api
- description: The Custom Fields API from Work Market — 1 operation(s) for custom fields.
  name: Work Market Custom Fields API
  slug: work-market-custom-fields-api
- description: The Labels API from Work Market — 3 operation(s) for labels.
  name: Work Market Labels API
  slug: work-market-labels-api
- description: The Locations API from Work Market — 1 operation(s) for locations.
  name: Work Market Locations API
  slug: work-market-locations-api
- description: The Projects API from Work Market — 2 operation(s) for projects.
  name: Work Market Projects API
  slug: work-market-projects-api
- description: The Talent Pools API from Work Market — 6 operation(s) for talent pools.
  name: Work Market Talent Pools API
  slug: work-market-talent-pools-api
- description: The UpdateCheckIn API from Work Market — 2 operation(s) for updatecheckin.
  name: Work Market UpdateCheckIn API
  slug: work-market-updatecheckin-api
artifact_total: 24
asyncapis:
- description: ''
  name: Work Market Webhooks
  slug: work-market-webhooks
common:
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
- description: ''
  name: work-market-mcp.yml
  slug: work-market-mcpyml
modified: '2026-07-21'
name: Work Market
nav: Providers
network: true
overview: 'Work Market publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Addressbook API, Assignments API, Authorization API, and 7 more. Tagged areas include Workforce Management, Contractors, Freelance, Gig Economy, and Human Resources.


  The Work Market catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Work Market''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, sandbox, and 22 more developer resources.'
random_paper: 34
score:
  band: developing
  composite: 49.7
  delta: -6.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 67.7
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 55.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
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
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
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
