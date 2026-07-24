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
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 39.4
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: REST API for delivery visits, route plans, route optimization, vehicles, drivers, clients, invoices and lifecycle webhooks. Token-header authenticated, JSON over HTTPS, versioned at /v1.
  name: SimpliRoute API
  slug: simpliroute-api
artifact_total: 5
asyncapis:
- description: ''
  name: Simpliroute Webhooks
  slug: simpliroute-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://simpliroute.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://simpliroute.com/en/development
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.simpliroute.com/
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.simpliroute.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.simpliroute.com/#introduction
- group: operate
  title: ''
  type: Support
  url: https://help.simpliroute.com/en
- group: company
  title: ''
  type: Blog
  url: https://simpliroute.com/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/simpliroute
- group: start
  title: ''
  type: SignUp
  url: https://app2.simpliroute.com/#/signup
- group: start
  title: ''
  type: Login
  url: https://app2.simpliroute.com/#/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://simpliroute.com/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://simpliroute.com/en/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/simpliroute-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/simpliroute-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/simpliroute-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/simpliroute-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/simpliroute-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/simpliroute-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/simpliroute-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/simpliroute-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/simpliroute-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/simpliroute-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simpliroute-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/simpliroute-llms.txt
created: '2026-07-17'
description: SimpliRoute is an AI-powered last-mile route optimization and delivery management platform, founded in Chile and operating across Latin America and beyond. Its REST API (base URL https://api.simpliroute.com/v1, authenticated with an Authorization Token header) lets developers create delivery and pickup visits, build daily plans, run the route-optimization engine over vehicles and deliveries, manage vehicles, drivers, couriers, clients, skills, zones and fleets, handle invoices, and subscribe to lifecycle webhooks (route started, on its way, checkout, route finished). First-party Node/TypeScript and Python SDKs are published under the github.com/simpliroute organization.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/simpliroute.png
layout: provider
mcp_servers:
- description: ''
  name: simpliroute-mcp.yml
  slug: simpliroute-mcpyml
modified: '2026-07-21'
name: Simpliroute
nav: Providers
network: true
overview: 'Simpliroute publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Route Optimization, Last Mile Delivery, and Delivery Management.


  The Simpliroute catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Simpliroute''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 18 more developer resources.'
random_paper: 40
score:
  band: thin
  composite: 38.2
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 22.6
    developer_ergonomics: 73.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 38.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Simpliroute Authentication
  slug: simpliroute-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Simpliroute Domain Security
  slug: simpliroute-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: simpliroute
tags:
- Company
- Logistics
- Route Optimization
- Last Mile Delivery
- Delivery Management
- Fleet Management
- Transportation
- Webhooks
website: https://simpliroute.com
---
