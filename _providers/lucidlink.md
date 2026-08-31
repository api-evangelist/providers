---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.0
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The self-hosted administrative REST API for the new LucidLink platform, delivered as the lucidlink/lucidlink-api Docker image and run on customer infrastructure so that LucidLink's zero-knowledge mode
  name: LucidLink Management API
  slug: lucidlink-management-api
- description: The LucidLink-hosted workspace web service used by the LucidLink apps and by the admin tool surface of the official LucidLink MCP server. Exposes service accounts, workspaces, members, groups, filespa
  name: LucidLink Web Service API v2
  slug: lucidlink-web-service-api-v2
- description: Billing operations.
  name: LucidLink Billing API
  slug: lucidlink-billing-api
- description: Domain operations.
  name: LucidLink Domain API
  slug: lucidlink-domain-api
- description: Filespace operations.
  name: LucidLink Filespace API
  slug: lucidlink-filespace-api
artifact_total: 12
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/lucidlink-service-api-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lucidlink-trust-center.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lucidlink-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.lucidlink.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.lucidlink.com/developer-platform
- group: docs
  title: ''
  type: Documentation
  url: https://support.lucidlink.com/hc/en-us/sections/45107391668493-LucidLink-Developer-Platform
- group: docs
  title: ''
  type: APIReference
  url: https://api.lucidlink.com/docs/api/v1/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.lucidlink.com/hc/en-us/articles/40221700126605-Deployment-Usage-LucidLink-API-Container
- group: operate
  title: ''
  type: Support
  url: https://support.lucidlink.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.lucidlink.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LucidLink
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lucidlink.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.lucidlink.com/register
- group: start
  title: ''
  type: Login
  url: https://app.lucidlink.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lucidlink.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lucidlink.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lucidlink.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.lucidlink.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.lucidlink.com/hc/en-us/sections/31125638256269-Release-notes
- group: commercial
  title: ''
  type: Plans
  url: plans/lucidlink-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lucidlink-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lucidlink-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lucidlink-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lucidlink-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lucidlink-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/lucidlink-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/lucidlink-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lucidlink-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lucidlink-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/lucidlink-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lucidlink-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/lucidlink-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lucidlink-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lucidlink-sandbox.yml
created: '2026-08-25'
description: 'LucidLink Corp. is a cloud file-streaming company whose product is a "filespace" — a shared, cloud-native filesystem that mounts on macOS, Windows, Linux, iOS and Android and streams only the bytes an application actually asks for, so distributed teams can open multi-gigabyte media, design and AEC files directly from S3 object storage without syncing or downloading them first. LucidLink is built around a zero-knowledge encryption model in which the customer holds the keys, which shapes its developer surface: the LucidLink Developer Platform ships a public cloud Service API for domain, filespace and billing management (OAuth2 client-credentials, Swagger 2.0 reference published at api.lucidlink.com), a self-hosted Management API delivered as a Docker container so administrative calls never traverse LucidLink infrastructure, a beta Python SDK on PyPI, LucidLink Connect for linking external S3 objects into a filespace, and a beta MCP server that exposes filespace read, write, search,
  locking and audit operations as tools for MCP-compatible agents.'
image: https://dhgs2q3hgrx0j.cloudfront.net/lucidlink_logo_846354e8f3.png
layout: provider
mcp_servers:
- description: 'Official LucidLink MCP server (beta). Gives MCP-compatible agents a shared, persistent

    LucidLink filespace they can read, write, search, lock and audit — the "shared data

    layer for agentic AI" LucidLi'
  name: LucidLink MCP Server
  slug: lucidlink-mcp-server
modified: '2026-08-25'
name: LucidLink
nav: Providers
network: true
overview: 'LucidLink publishes 3 APIs on the [APIs.io](https://apis.io/) network: Billing API, Domain API, and Filespace API. Tagged areas include Company, Cloud Storage, File Streaming, File Collaboration, and Media and Entertainment.


  LucidLink''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Lucidlink Plans Pricing
  plan_count: 3
  slug: lucidlink-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Lucidlink Rate Limits
  slug: lucidlink-rate-limits
scopes:
- name: Lucidlink Scopes
  scope_count: 0
  slug: lucidlink-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.1
  coverage:
    artifact_dirs: 21
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 41.3
    developer_ergonomics: 80.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 56.7
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Lucidlink Authentication
  slug: lucidlink-authentication
  summary_line: oauth2/http-bearer · 3 schemes
- kind: domain-security
  name: Lucidlink Domain Security
  slug: lucidlink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Lucidlink Trust Center
  slug: lucidlink-trust-center
  summary_line: SOC 2 Type I, SOC 2 Type II, ISO 27001, TPN (Trusted Partner Network), TPN Gold Shield, GDPR, CCPA
slug: lucidlink
tags:
- Company
- Cloud Storage
- File Streaming
- File Collaboration
- Media and Entertainment
- Object Storage
- Developer Platform
- MCP
- Agentic AI
- Zero-Knowledge Encryption
- Identity and Access Management
website: https://www.lucidlink.com/
---
