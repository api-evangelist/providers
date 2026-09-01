---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 49.9
  scored_at: '2026-09-01'
api_count: 5
apis:
- description: The Fusio Backend API provides a REST interface to configure and manage all aspects of a Fusio API management instance. It covers operations, routes, schemas, actions, connections, apps, users, and ma
  name: Fusio Backend API
  slug: fusio-backend-api
- description: The Fusio Consumer API is used by the developer portal application and enables third-party developers to request access tokens, manage their apps, and interact with protected API endpoints. It provide
  name: Fusio Consumer API
  slug: fusio-consumer-api
- description: The Fusio Worker API enables executing API action logic in multiple programming languages by forwarding requests to external worker processes. Workers are implemented in the target language (JavaScrip
  name: Fusio Worker API
  slug: fusio-worker-api
- description: The Fusio System API is the meta surface every Fusio instance exposes without configuration. It carries the discovery document at the root, the health check, the route table, and the specification gen
  name: Fusio System API
  slug: fusio-system-api
- description: The Fusio Authorization API is the OAuth2 authorization server Fusio ships in the product. It issues and refreshes access tokens across the authorization_code, client_credentials, password and refresh
  name: Fusio Authorization API
  slug: fusio-authorization-api
artifact_total: 31
asyncapis:
- description: ''
  name: Fusio Webhooks
  slug: fusio-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.fusio-project.org/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/fusio-backend.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fusio-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/fusio-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fusio-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/fusio-api-catalog.json
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/fusio-security.txt
- group: auth
  title: ''
  type: Security
  url: security/fusio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fusio-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fusio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fusio-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fusio-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/fusio-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fusio-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fusio-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fusio-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/fusio-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/fusio-cli.yml
- group: design
  title: ''
  type: Components
  url: components/fusio-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fusio-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fusio-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/fusio-backend-overlay.yaml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fusio-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fusio-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fusio-changelog.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.fusio-project.org/developers
- group: docs
  title: ''
  type: APIReference
  url: https://demo.fusio-project.org/apps/redoc
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/apioo/fusio/milestones
- group: start
  title: ''
  type: Demo
  url: https://www.fusio-project.org/demo
- group: auth
  title: ''
  type: Authentication
  url: authentication/fusio-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fusio-scopes.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apioo/fusio/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/apioo/fusio/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apioo/fusio/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apioo/fusio/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fusio-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fusio-project.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fusio-project.org/docs/bootstrap
- group: company
  title: ''
  type: Blog
  url: https://www.fusio-project.org/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/apioo/fusio/blob/master/CHANGELOG.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apioo
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apioo/fusio
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/eMrMgwsc6e
- group: other
  title: ''
  type: Marketplace
  url: https://www.fusio-project.org/marketplace
- group: build
  title: ''
  type: SDKs
  url: https://docs.fusio-project.org/docs/backend/development/sdk
created: '2026-03-16'
description: 'Fusio is Apache-2.0, self-hosted API management from apioo (Christoph Kappestein, Germany). An operator installs it and builds APIs inside it: an operation binds an HTTP method and path to an action (SQL, HTTP, MongoDB, Elasticsearch, an LLM agent, or code running in a JavaScript, Python, Java or PHP worker) and a TypeSchema-defined request and response shape. Every instance then generates its own machine-readable contract live - OpenAPI 3.0.3, OpenRPC 1.3.0 and TypeAPI - and serves an RFC 9727 api-catalog, RFC 8414 and RFC 9728 OAuth metadata, OpenID Connect discovery and an RFC 9116 security.txt out of the box. It ships its own OAuth2 authorization server, an Angular developer portal, a rate-limiting and monetization layer, a webhook and trigger system, and an MCP server that turns every published operation into an agent tool. There is no vendor-hosted tier and no pricing: the software is the product.'
features:
- description: Route and manage incoming API requests with built-in rate limiting and authentication.
  name: API Gateway
- description: Self-service developer portal for API consumers to register, browse APIs, and manage access tokens.
  name: Developer Portal
- description: Execute API action logic in JavaScript, Python, Java, PHP, and other languages through worker processes.
  name: Multi-Language Workers
- description: Browse and install pre-built API actions and adapters from the Fusio marketplace.
  name: Marketplace
- description: Define and manage API request and response schemas using TypeSchema format.
  name: Schema Management
- description: Built-in OAuth2 server for securing APIs with token-based authentication.
  name: OAuth2 Authentication
- description: Configure per-app and per-user rate limits to protect API resources.
  name: Rate Limiting
- description: Define webhook subscriptions to notify consumers of events.
  name: Webhook Support
finops:
- name: Fusio Finops
  service_category: API
  slug: fusio-finops
image: /assets/icons/fusio.png
integrations:
- description: Connect to MySQL and PostgreSQL databases as data sources for API endpoints.
  name: MySQL and PostgreSQL
- description: Use MongoDB as a NoSQL data source for API endpoints.
  name: MongoDB
- description: Integrate with Elasticsearch for search-powered API endpoints.
  name: Elasticsearch
- description: Use RabbitMQ for asynchronous message processing in API workflows.
  name: RabbitMQ
- description: Deploy Fusio and worker containers using Docker and Docker Compose.
  name: Docker
layout: provider
mcp_servers:
- description: 'Fusio ships a first-party Model Context Protocol server inside the product itself. It is not a separate package or a hosted vendor endpoint: every Fusio instance can expose its own operations as MCP t'
  name: Fusio MCP Server
  slug: fusio-mcp-server
modified: '2026-08-29'
name: Fusio
nav: Providers
network: true
overview: 'Fusio publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Backend API, Consumer API, System API, and 1 more. Tagged areas include API Management, Open-Source, REST API, API Gateway, and Developer Portal.


  The Fusio catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fusio''s developer surface includes CLI, sandbox, changelog, API reference, authentication, documentation, getting-started guide, and 39 more developer resources.'
plans:
- name: Fusio Plans Pricing
  plan_count: 0
  slug: fusio-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Fusio Rate Limits
  slug: fusio-rate-limits
scopes:
- name: Fusio Scopes
  scope_count: 58
  slug: fusio-scopes
  summary_line: 58 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 49.9
  coverage:
    artifact_dirs: 26
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 54.6
    developer_ergonomics: 85.7
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 55.3
  open_source:
    applies: true
    score: 50.0
  previous_composite: 49.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fusio/refs/heads/main/screenshots/fusio-2026-06-20T181622.png
security:
- kind: authentication
  name: Fusio Authentication
  slug: fusio-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Fusio Domain Security
  slug: fusio-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Fusio Vulnerability Disclosure
  slug: fusio-vulnerability-disclosure
  summary_line: Hackerone
slug: fusio
tags:
- API Management
- Open-Source
- REST API
- API Gateway
- Developer Portal
- OpenAPI
- Self-Hosted
- MCP
use_cases:
- description: Build and publish API products with documentation, authentication, and developer onboarding.
  name: API Product Building
- description: Use Fusio as an API gateway in front of microservices for unified access control.
  name: Microservices Gateway
- description: Connect to databases and external APIs to build data integration endpoints.
  name: Data Integration
- description: Build API backends that execute logic in multiple languages without managing servers.
  name: Serverless API Backend
website: https://www.fusio-project.org/
---
