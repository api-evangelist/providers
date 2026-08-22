---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 53
  human_in_the_loop: 10
  name: Kandji Agentic Access
  operation_count: 122
  slug: kandji-agentic-access
  summary_line: 122 operations · 53 acting · 10 human-in-the-loop
api_count: 3
apis:
- description: Tenant-scoped REST API for the Iru (formerly Kandji) endpoint platform. 121 operations across 94 paths covering device inventory and details, 18 device actions (lock, erase, restart, shutdown, lost mo
  name: Iru Endpoint Management API
  slug: iru-endpoint-management-api
- description: Single-operation S3 pre-signed upload contract returned by the Custom App and IPA App creation endpoints of the Iru Endpoint Management API. The upload URL is variable per request; the provider publis
  name: Iru Library Item Upload API
  slug: iru-library-item-upload-api
- description: 'Hosted, tenant-scoped Model Context Protocol server that exposes the Iru Enterprise API surface as MCP tools for Claude Desktop, Cursor, OpenAI Codex and other MCP clients. Enabled per API token with '
  name: Iru MCP Server
  slug: iru-mcp-server
artifact_total: 12
collections:
- collection_type: open
  name: Iru Endpoint Management API
  slug: open-kandji-endpoint-management
- collection_type: open
  name: Upload to S3
  slug: open-kandji-upload-to-s3
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kandji-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/kandji-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kandji-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.iru.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.iru.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.iru.com/en/endpoint/api/iru-api-overview
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.kandji.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.iru.com/en/endpoint/getting-started/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.kandji.io/
- group: company
  title: ''
  type: Blog
  url: https://www.iru.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kandji-inc
- group: commercial
  title: ''
  type: Pricing
  url: https://www.iru.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.iru.com/request-demo
- group: start
  title: ''
  type: Login
  url: https://www.iru.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.iru.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iru.com/legal/privacy
- group: build
  title: ''
  type: Postman
  url: https://api-docs.kandji.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kandji.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.iru.com/updates/
- group: operate
  title: ''
  type: ChangeLogRSS
  url: https://updates.iru.com/feed-en
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kandji-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://www.iru.com/security/responsible-disclosure-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.iru.com/security
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/kandji_stock/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/kandji-endpoint-management-openapi.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kandji-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/kandji-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/kandji-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/kandji-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kandji-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kandji-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kandji-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kandji-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kandji-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kandji-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kandji-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kandji-lifecycle.yml
- group: operate
  title: ''
  type: ReleaseStages
  url: https://docs.iru.com/en/iru/platform-overview/iru-release-stages
- group: design
  title: ''
  type: Conformance
  url: conformance/kandji-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kandji-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/kandji-endpoint-management-overlay.yaml
created: '2026-08-01'
description: Iru (formerly Kandji) is a San Francisco based endpoint management and security company whose AI-powered platform unifies workforce identity and access, cross-platform endpoint management for macOS, iOS, iPadOS, tvOS, visionOS, Windows and Android, endpoint detection and response, vulnerability management, compliance automation and a customer-facing trust center behind a single agent. The company rebranded from Kandji to Iru on 22 October 2025; the product surface, the developer documentation and the API hostnames still carry the kandji.io domain. The Iru Endpoint Management API is a tenant-scoped REST API published as OpenAPI 3.0.0 and as a public Postman collection, covering devices and device actions, Blueprints, Library Items, Prism inventory reporting, Automated Device Enrollment, tags, users, threats and vulnerabilities, and it also backs a hosted, tenant-scoped Model Context Protocol server for AI assistants.
image: https://www.iru.com/hubfs/assets/favicons/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: kandji-mcp.yml
  slug: kandji-mcpyml
modified: '2026-08-01'
name: Iru
nav: Providers
network: true
overview: 'Iru publishes 2 APIs on the [APIs.io](https://apis.io/) network: Endpoint Management API and Library Item Upload API. Tagged areas include Company, device-management, mobile-device-management, apple-management, and endpoint-security.


  Iru''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 35 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 1
  name: Kandji Rate Limits
  slug: kandji-rate-limits
score:
  band: strong
  composite: 58.9
  delta: 0.4
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 30.3
    contract_quality: 49.3
    developer_ergonomics: 70.8
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 65.8
  previous_composite: 58.5
  provenance:
    agentic_access: first-party
    conformance: first-party
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kandji/refs/heads/main/screenshots/kandji-2026-08-07T171059.png
security:
- kind: authentication
  name: Kandji Authentication
  slug: kandji-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Kandji Domain Security
  slug: kandji-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kandji Vulnerability Disclosure
  slug: kandji-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Kandji Trust Center
  slug: kandji-trust-center
  summary_line: SOC 2 Type II, ISO 27001
slug: kandji
tags:
- Company
- device-management
- mobile-device-management
- apple-management
- endpoint-security
- endpoint-detection-response
- vulnerability-management
- compliance-automation
- workforce-identity
- it-operations
- mcp
- agent-native
website: https://www.iru.com/
---
