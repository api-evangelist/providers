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
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 118
  human_in_the_loop: 16
  name: Nash Agentic Access
  operation_count: 173
  slug: nash-agentic-access
  summary_line: 173 operations · 118 acting · 16 human-in-the-loop
api_count: 30
apis:
- description: LLM-backed domain tools
  name: Nash AI Functions API
  slug: nash-ai-functions-api
- description: Annotate
  name: Nash Annotate API
  slug: nash-annotate-api
- description: Batch Job
  name: Nash Batch Job API
  slug: nash-batch-job-api
- description: Provider contract pricing and version listings
  name: Nash Contracts API
  slug: nash-contracts-api
- description: Couriers
  name: Nash Couriers API
  slug: nash-couriers-api
- description: Delivery Windows
  name: Nash Delivery Windows API
  slug: nash-delivery-windows-api
- description: Dispatch Strategies
  name: Nash Dispatch Strategies API
  slug: nash-dispatch-strategies-api
- description: Feedback
  name: Nash Feedback API
  slug: nash-feedback-api
- description: Inbound endpoints fleets call to update in-flight deliveries.
  name: Nash Fleet API
  slug: nash-fleet-api
- description: Job
  name: Nash Job API
  slug: nash-job-api
- description: Messaging
  name: Nash Messaging API
  slug: nash-messaging-api
- description: Miscellaneous
  name: Nash Miscellaneous API
  slug: nash-miscellaneous-api
- description: Notifications
  name: Nash Notifications API
  slug: nash-notifications-api
- description: Create, read, update, and delete route optimization strategies.
  name: Nash Optimization Strategies API
  slug: nash-optimization-strategies-api
- description: Order
  name: Nash Order API
  slug: nash-order-api
- description: Organizations
  name: Nash Organizations API
  slug: nash-organizations-api
- description: Provider
  name: Nash Provider API
  slug: nash-provider-api
- description: Route
  name: Nash Route API
  slug: nash-route-api
- description: Org-scoped geographic areas the route optimizer must avoid traversing.
  name: Nash Route Restrictions API
  slug: nash-route-restrictions-api
- description: Shifts
  name: Nash Shifts API
  slug: nash-shifts-api
- description: Shipping operations
  name: Nash Shipping API
  slug: nash-shipping-api
- description: Store Catalog
  name: Nash Store Catalog API
  slug: nash-store-catalog-api
- description: Store Locations
  name: Nash Store Locations API
  slug: nash-store-locations-api
- description: Templates
  name: Nash Templates API
  slug: nash-templates-api
- description: User, role, and organization-membership management.
  name: Nash Users API
  slug: nash-users-api
- description: Vehicles
  name: Nash Vehicles API
  slug: nash-vehicles-api
- description: Webhook delivery inspection
  name: Nash Webhooks API
  slug: nash-webhooks-api
- description: Workflow automation management
  name: Nash Workflow API
  slug: nash-workflow-api
- description: Workflow execution history and monitoring
  name: Nash Workflow Execution API
  slug: nash-workflow-execution-api
- description: Zones
  name: Nash Zones API
  slug: nash-zones-api
artifact_total: 39
asyncapis:
- description: Real-time delivery events Nash pushes to subscriber endpoints over HTTP, delivered and signed via Svix. Each message carries `type`, `event`, and `data`. Endpoints are registered per event type in the
  name: Nash Webhooks
  slug: nash-webhooks-asyncapi
- description: ''
  name: Nash Webhooks
  slug: nash-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.nash.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.usenash.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usenash.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.usenash.com/api-reference/api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.usenash.com/reference/plan-your-integration
- group: start
  title: ''
  type: Quickstart
  url: https://docs.usenash.com/reference/generating-api-key-and-org-id
- group: operate
  title: ''
  type: Support
  url: https://help.usenash.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.usenash.com
- group: company
  title: ''
  type: Blog
  url: https://www.nash.ai/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.usenash.com/release-notes/change
- group: operate
  title: ''
  type: StatusPage
  url: https://status.usenash.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usenash
- group: start
  title: ''
  type: SignUp
  url: https://portal.usenash.com
- group: start
  title: ''
  type: Login
  url: https://portal.usenash.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nash.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nash.ai/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nash.ai/legal/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nash-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nash-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nash-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nash-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nash-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nash-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.nash.ai/legal/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/nash-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/nash-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nash-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nash-domain-security.yml
- group: design
  title: ''
  type: Components
  url: components/nash-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Nash is an AI-powered last-mile delivery orchestration platform that lets retailers, restaurants, grocers, pharmacies, and logistics teams quote, dispatch, and track deliveries across a network of third-party couriers and their own internal fleets from a single API. The Nash Platform API covers orders, jobs (deliveries), quoting, dispatch strategies, route optimization, delivery windows, zones, store locations, shifts, store catalog, notifications, and signed webhooks, alongside a Fleet API for owned-fleet delivery reporting and a Nash Agent copilot exposed over a Model Context Protocol (MCP) server for agent-driven delivery operations. Backed by a16z.
image: https://www.nash.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: nash-mcp.yml
  slug: nash-mcpyml
modified: '2026-07-20'
name: Nash
nav: Providers
network: true
overview: 'Nash publishes 30 APIs on the [APIs.io](https://apis.io/) network, including AI Functions API, Annotate API, Batch Job API, and 27 more. Tagged areas include Company, Delivery, Last-Mile Delivery, Logistics, and Dispatch.


  The Nash catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Nash''s developer surface includes documentation, API reference, getting-started guide, quickstart, support, engineering blog, changelog, and 23 more developer resources.'
random_paper: 26
rate_limits:
- limit_count: 0
  name: Nash Rate Limits
  slug: nash-rate-limits
score:
  band: developing
  composite: 55.3
  delta: -0.4
  facets:
    commercial_clarity: 60.5
    contract_quality: 64.4
    developer_ergonomics: 51.6
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 55.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 30
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Nash Authentication
  slug: nash-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nash Domain Security
  slug: nash-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nash Vulnerability Disclosure
  slug: nash-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Nash Trust Center
  slug: nash-trust-center
  summary_line: SOC 2
slug: nash
tags:
- Company
- Delivery
- Last-Mile Delivery
- Logistics
- Dispatch
- Route Optimization
- Fleet Management
- Courier
- Shipping
- Orders
- Webhooks
- AI Agents
website: https://www.nash.ai
---
