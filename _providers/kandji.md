---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: true
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 53
  human_in_the_loop: 10
  name: Kandji Agentic Access
  operation_count: 122
  slug: kandji-agentic-access
  summary_line: 122 operations · 53 acting · 10 human-in-the-loop
api_count: 2
apis:
- description: 'Hosted, tenant-scoped Model Context Protocol server that exposes the Iru Enterprise API surface as MCP tools for Claude Desktop, Cursor, OpenAI Codex and other MCP clients. Enabled per API token with '
  name: Iru MCP Server
  slug: iru-mcp-server
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Audit API from Iru — 1 operation(s) for audit.
  name: Iru Audit API
  slug: kandji-audit-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Behavioral Detections API from Iru — 1 operation(s) for behavioral detections.
  name: Iru Behavioral Detections API
  slug: kandji-behavioral-detections-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Blueprints API from Iru — 6 operation(s) for blueprints.
  name: Iru Blueprints API
  slug: kandji-blueprints-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Devices API from Iru — 34 operation(s) for devices.
  name: Iru Devices API
  slug: kandji-devices-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Integrations API from Iru — 8 operation(s) for integrations.
  name: Iru Integrations API
  slug: kandji-integrations-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Library API from Iru — 13 operation(s) for library.
  name: Iru Library API
  slug: kandji-library-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Prism API from Iru — 19 operation(s) for prism.
  name: Iru Prism API
  slug: kandji-prism-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Self Service API from Iru — 1 operation(s) for self service.
  name: Iru Self Service API
  slug: kandji-self-service-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Settings API from Iru — 1 operation(s) for settings.
  name: Iru Settings API
  slug: kandji-settings-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Tags API from Iru — 2 operation(s) for tags.
  name: Iru Tags API
  slug: kandji-tags-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Threat Details API from Iru — 1 operation(s) for threat details.
  name: Iru Threat Details API
  slug: kandji-threat-details-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Upload To S3 API from Iru — 1 operation(s) for upload to s3.
  name: Iru Upload To S3 API
  slug: kandji-upload-to-s3-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Users API from Iru — 2 operation(s) for users.
  name: Iru Users API
  slug: kandji-users-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Vulnerability Management API from Iru — 5 operation(s) for vulnerability management.
  name: Iru Vulnerability Management API
  slug: kandji-vulnerability-management-api
artifact_total: 24
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
  name: Iru MCP Server
  slug: iru-mcp-server
modified: '2026-08-01'
name: Iru
nav: Providers
network: true
overview: 'Iru publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Audit API, Behavioral Detections API, Blueprints API, and 11 more. Tagged areas include Company, Device Management, Mobile Device Management, apple-management, and Endpoint Security.


  Iru''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 35 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 1
  name: Kandji Rate Limits
  slug: kandji-rate-limits
score:
  band: strong
  composite: 58.2
  coverage:
    artifact_dirs: 21
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 54.5
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 58.2
  provenance:
    agentic_access: first-party
    conformance: first-party
    contracts:
      callable: 92.9
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
- Device Management
- Mobile Device Management
- apple-management
- Endpoint Security
- endpoint-detection-response
- Vulnerability Management
- Compliance Automation
- Workforce Identity
- IT Operations
- MCP
- agent-native
website: https://www.iru.com/
---
