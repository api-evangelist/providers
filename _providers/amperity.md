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
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 4
  human_in_the_loop: 2
  name: Amperity Agentic Access
  operation_count: 19
  slug: amperity-agentic-access
  summary_line: 19 operations · 4 acting · 2 human-in-the-loop
api_count: 5
apis:
- description: RESTful API for programmatic access to an Amperity tenant — list and manage campaigns, campaign drafts, segments, ingest jobs, audit events, and workflow runs. Authenticated with an OAuth2 client-cred
  name: Amperity API
  slug: amperity-api
- description: Amperity's preview track for the Amperity API, published as a separate OpenAPI document alongside the stable 2024-04-01 spec. Currently adds GET /campaign-drafts on top of the stable operation set. Sa
  name: Amperity API (Unstable)
  slug: amperity-api-unstable
- description: Amperity's official hosted remote Model Context Protocol server. A single public endpoint at https://mcp.amperity.com routes each request to the Amperity stack holding the calling user's tenant, and e
  name: Amperity MCP Server
  slug: amperity-mcp-server
- description: RESTful API for real-time access to unified customer profiles. List indexes, fetch an index, and read paginated customer profiles (or a single profile) for personalization and downstream activation. J
  name: Amperity Profile API
  slug: amperity-profile-api
- description: Low-latency, high-throughput REST API for real-time ingestion of event data from external systems into Amperity. POST JSON or XML payloads (up to 1 MB) to a tenant-specific stream. JWT bearer auth wit
  name: Amperity Streaming API
  slug: amperity-streaming-api
artifact_total: 15
asyncapis:
- description: ''
  name: Amperity Webhooks
  slug: amperity-webhooks
collections:
- collection_type: open
  name: Amperity API
  slug: open-amperity-control-plane-2024-04-01
- collection_type: open
  name: Amperity API (Unstable)
  slug: open-amperity-control-plane-unstable
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amperity-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.amperity.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.amperity.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.amperity.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.amperity.com/reference/api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.amperity.com/api/overview.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amperity
- group: operate
  title: ''
  type: StatusPage
  url: https://status.amperity.com
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.amperity.com/api/versioning.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amperity-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/amperity-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/amperity-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amperity-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amperity-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/amperity-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/amperity-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/amperity-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amperity-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amperity-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amperity-domain-security.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/amperity-control-plane-2024-04-01-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/amperity-control-plane-overlay.yaml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/amperity-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/amperity-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/amperity-cli.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/amperity-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/amperity-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/amperity-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/amperity-webhooks.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amperity-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.amperity.com/
created: '2026-07-17'
description: 'Amperity is a Seattle-based customer data platform (CDP) that helps consumer brands build accurate, unified customer profiles by stitching together fragmented first-party data from across their systems. Using AI-powered identity resolution (its patented Stitch technology), Amperity assembles a durable Customer 360 that powers segmentation, marketing campaigns, personalization, analytics, and activation to downstream destinations. For developers, Amperity exposes three public REST APIs: the Amperity API for programmatic access to tenant resources (campaigns, segments, ingest jobs, audit events, and workflow runs), the Profile API for real-time access to unified customer profiles by index, and the Streaming API for low-latency, high-throughput ingestion of events from external systems. Amperity publishes a downloadable OpenAPI 3.0.3 document for the Amperity API plus a separate unstable preview spec, and it hosts an official remote Model Context Protocol server at mcp.amperity.com
  exposing more than 200 tools across databases, queries, Stitch identity resolution, couriers, destinations, campaigns, journeys and predictive models, gated by OAuth2 authorization-code with PKCE and per-session safety modes. The REST APIs use OAuth2 client-credentials tokens (JWT bearer), cursor pagination, date-based versioning via an api-version header, and an RFC 8594 deprecation/sunset policy. Amperity serves retail, travel, hospitality, financial services, and other consumer-facing verticals.'
image: https://docs.amperity.com/_static/icon-light.svg
layout: provider
mcp_servers:
- description: ''
  name: amperity-mcp.yml
  slug: amperity-mcpyml
modified: '2026-08-13'
name: Amperity
nav: Providers
network: true
overview: 'Amperity publishes 2 APIs on the [APIs.io](https://apis.io/) network, including API (Unstable), and 1 more. Tagged areas include Company, Enterprise, Customer Data Platform, CDP, and Identity Resolution.


  The Amperity catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Amperity''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, CLI, sandbox, and 25 more developer resources.'
plans:
- name: Amperity Plans Pricing
  plan_count: 0
  slug: amperity-plans-pricing
random_paper: 130
rate_limits:
- limit_count: 4
  name: Amperity Rate Limits
  slug: amperity-rate-limits
score:
  band: developing
  composite: 55.9
  delta: 30.9
  facets:
    commercial_clarity: 15.8
    contract_quality: 66.4
    developer_ergonomics: 67.4
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 84.2
  previous_composite: 25.0
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/amperity/refs/heads/main/screenshots/amperity-2026-07-25T200122.png
security:
- kind: authentication
  name: Amperity Authentication
  slug: amperity-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Amperity Domain Security
  slug: amperity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Amperity Trust Center
  slug: amperity-trust-center
  summary_line: trust center published
slug: amperity
tags:
- Company
- Enterprise
- Customer Data Platform
- CDP
- Identity Resolution
- Customer 360
- Marketing
- Data
- Profiles
- Analytics
- MCP
- Agents
- Retail
- Identity
website: https://www.amperity.com
---
