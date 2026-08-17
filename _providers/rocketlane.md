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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.4
  scored_at: '2026-08-17'
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
artifact_total: 35
asyncapis:
- description: ''
  name: Rocketlane Webhooks
  slug: rocketlane-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rocketlane Comments API
  slug: open-rocketlane-comments-api
- collection_type: open
  name: Rocketlane Comments Conversations API
  slug: open-rocketlane-conversations-api
- collection_type: open
  name: Rocketlane Comments Fields API
  slug: open-rocketlane-fields-api
- collection_type: open
  name: Rocketlane Comments Invoices API
  slug: open-rocketlane-invoices-api
- collection_type: open
  name: Rocketlane Comments Phases API
  slug: open-rocketlane-phases-api
- collection_type: open
  name: Rocketlane Comments Projects API
  slug: open-rocketlane-projects-api
- collection_type: open
  name: Rocketlane Comments Resource Allocations API
  slug: open-rocketlane-resource-allocations-api
- collection_type: open
  name: Rocketlane Comments Space Documents API
  slug: open-rocketlane-space-documents-api
- collection_type: open
  name: Rocketlane Comments Spaces API
  slug: open-rocketlane-spaces-api
- collection_type: open
  name: Rocketlane Comments Tasks API
  slug: open-rocketlane-tasks-api
- collection_type: open
  name: Rocketlane Comments Time-Offs API
  slug: open-rocketlane-time-offs-api
- collection_type: open
  name: Rocketlane Comments Time Tracking API
  slug: open-rocketlane-time-tracking-api
- collection_type: open
  name: Rocketlane Comments Users API
  slug: open-rocketlane-users-api
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
  url: openapi/_original/rocketlane-openapi-original.json
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
random_paper: 21
rate_limits:
- limit_count: 2
  name: Rocketlane Rate Limits
  slug: rocketlane-rate-limits
score:
  band: strong
  composite: 59.5
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 65.6
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 60.5
  previous_composite: 59.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
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
