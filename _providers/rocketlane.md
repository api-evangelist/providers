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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 81.7
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 47
  human_in_the_loop: 0
  name: Rocketlane Agentic Access
  operation_count: 76
  slug: rocketlane-agentic-access
  summary_line: 76 operations · 47 acting
api_count: 13
apis:
- description: Endpoints for comments resource
  name: Rocketlane Comments API
  slug: rocketlane-comments-api
- description: Endpoints for conversations resource
  name: Rocketlane Conversations API
  slug: rocketlane-conversations-api
- description: Endpoints for fields resource
  name: Rocketlane Fields API
  slug: rocketlane-fields-api
- description: Endpoints for invoices resource
  name: Rocketlane Invoices API
  slug: rocketlane-invoices-api
- description: Endpoints for phases resource
  name: Rocketlane Phases API
  slug: rocketlane-phases-api
- description: Endpoints for projects resource
  name: Rocketlane Projects API
  slug: rocketlane-projects-api
- description: Endpoints for resource allocation resource
  name: Rocketlane Resource Allocations API
  slug: rocketlane-resource-allocations-api
- description: Endpoints for space tabs resource
  name: Rocketlane Space Documents API
  slug: rocketlane-space-documents-api
- description: Endpoints for space resource
  name: Rocketlane Spaces API
  slug: rocketlane-spaces-api
- description: Endpoints for tasks resource
  name: Rocketlane Tasks API
  slug: rocketlane-tasks-api
- description: Endpoints for time-offs resource
  name: Rocketlane Time-Offs API
  slug: rocketlane-time-offs-api
- description: Endpoints for time entries and timesheets
  name: Rocketlane Time Tracking API
  slug: rocketlane-time-tracking-api
- description: Endpoints for users resource
  name: Rocketlane Users API
  slug: rocketlane-users-api
artifact_total: 21
asyncapis:
- description: ''
  name: Rocketlane Webhooks
  slug: rocketlane-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rocketlane-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.rocketlane.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.rocketlane.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developer.rocketlane.com/reference/tasks
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.rocketlane.com/docs/overview
- group: operate
  title: ''
  type: Support
  url: https://help.rocketlane.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://www.rocketlane.com/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rocketlane.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.rocketlane.com/signup
- group: start
  title: ''
  type: Login
  url: https://www.rocketlane.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rocketlane.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rocketlane.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Rocketlane
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rocketlane.com
- group: auth
  title: ''
  type: Compliance
  url: https://www.rocketlane.com/trust
- group: auth
  title: ''
  type: Security
  url: https://www.rocketlane.com/responsible-disclosure
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rocketlane-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rocketlane-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/rocketlane-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/rocketlane-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rocketlane-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rocketlane-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rocketlane-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/rocketlane-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rocketlane-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rocketlane-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rocketlane-data-model.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/rocketlane-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/rocketlane-overlay.yaml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rocketlane-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rocketlane-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/rocketlane-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rocketlane-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rocketlane-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rocketlane.com
created: '2026-07-17'
description: Rocketlane is an AI-powered Professional Services Automation (PSA) platform that unifies customer onboarding, project delivery, resource management, time tracking, and professional-services financials in one system. Its public REST API (base https://api.rocketlane.com/api/1.0/) exposes projects, tasks, phases, spaces, space documents, custom fields, time entries, time-offs, resource allocations, users, and invoices, authenticated with a workspace api-key header and paginated with cursors. Outbound webhooks broadcast task, project, and phase lifecycle events, and a first-party CLI (@rocketlane/rli) supports building apps for the Rocketlane Marketplace. Originally added to the API Evangelist network as a portfolio-company lead (8vc, Insight Partners); enriched from its live developer surface.
image: https://cdn.prod.website-files.com/6360d3edc696260ba2aecbc7/64e613d0f901abbf2430f1f8_banner.webp
layout: provider
mcp_servers:
- description: ''
  name: rocketlane-mcp.yml
  slug: rocketlane-mcpyml
modified: '2026-07-21'
name: Rocketlane
nav: Providers
network: true
overview: 'Rocketlane publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Conversations API, Fields API, and 10 more. Tagged areas include Company, Professional Services Automation, Project Management, Customer Onboarding, and Resource Management.


  The Rocketlane catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Rocketlane''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 29 more developer resources.'
random_paper: 44
rate_limits:
- limit_count: 0
  name: Rocketlane Rate Limits
  slug: rocketlane-rate-limits
score:
  band: developing
  composite: 57.5
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 61.9
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 57.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Rocketlane Authentication
  slug: rocketlane-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rocketlane Domain Security
  slug: rocketlane-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rocketlane Vulnerability Disclosure
  slug: rocketlane-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Rocketlane Trust Center
  slug: rocketlane-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR, CSA STAR
slug: rocketlane
tags:
- Company
- Professional Services Automation
- Project Management
- Customer Onboarding
- Resource Management
- Time Tracking
- PSA
- SaaS
website: https://rocketlane.com
---
