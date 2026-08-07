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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Flat REST API for Hull's Customer Data Platform, addressing objects by ID under the /api/v1 prefix on a per-organization hullapp.io subdomain. Covers Users, Accounts, Events, Segments, organization/co
  name: Hull HTTP API
  slug: hull-http-api
artifact_total: 5
asyncapis:
- description: ''
  name: Hull Webhooks
  slug: hull-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.hull.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.hull.io/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.hull.io/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.hull.io/docs/reference/http_api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.hull.io/docs/guides/
- group: company
  title: ''
  type: Blog
  url: https://www.hull.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hull.io/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hull.io/pp/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hull
- group: auth
  title: ''
  type: Authentication
  url: authentication/hull-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hull-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hull-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hull-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hull.io/
- group: build
  title: ''
  type: Packages
  url: packages/hull-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hull-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hull-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hull-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hull-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hull-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hull-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hull-domain-security.yml
created: '2026-07-17'
description: Hull is a real-time Customer Data Platform (CDP) that unifies customer data from every source — web, product, CRM, marketing and support tools, databases and files — into a single User and Account profile using claim-based identity resolution. It ingests, computes and enriches data through a data-lifecycle pipeline (Ingest / Compute / Notify), organizes people and companies into Segments, and syncs the resulting profiles out to more than fifty tools via Connectors ("ships"). Developers integrate through a flat HTTP API at https://{organization}.hullapp.io/api/v1 covering Users, Accounts, Events, Segments, Status and Bulk operations, plus first-party Node, browser, PHP and Ruby client libraries and an outgoing/incoming webhook surface. Hull is now part of MessageBird (Bird) and is no longer accepting new customers.
image: https://www.hull.io/assets/images/logo/logo_dark@2x.png
layout: provider
mcp_servers:
- description: ''
  name: hull-mcp.yml
  slug: hull-mcpyml
modified: '2026-07-19'
name: Hull
nav: Providers
network: true
overview: 'Hull publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customer Data Platform, CDP, Identity Resolution, and Data Integration.


  The Hull catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hull''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, authentication, and 16 more developer resources.'
random_paper: 98
score:
  band: thin
  composite: 41.2
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 51.6
    developer_ergonomics: 56.5
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 28.9
  previous_composite: 41.2
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hull/refs/heads/main/screenshots/hull-2026-07-25T221636.png
security:
- kind: authentication
  name: Hull Authentication
  slug: hull-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Hull Domain Security
  slug: hull-domain-security
  summary_line: DMARC
slug: hull
tags:
- Company
- Customer Data Platform
- CDP
- Identity Resolution
- Data Integration
- Customer Data
- Marketing
- Real-time
- iPaaS
- Analytics
website: https://www.hull.io
---
