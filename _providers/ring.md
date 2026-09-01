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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'The Ring Partner API (Amazon Vision API / AVA) lets certified Ring Appstore partners access Ring device data and media on behalf of consenting users: list and inspect devices, read status/capabilities'
  name: Ring Partner API
  slug: ring-partner-api
artifact_total: 6
asyncapis:
- description: ''
  name: Ring Webhooks
  slug: ring-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://ring.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ring.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.amazon.com/docs/ring/api-documentation.html
- group: docs
  title: ''
  type: APIReference
  url: https://developer.amazon.com/docs/ring/api-documentation.html#endpoint-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.amazon.com/docs/ring/get-started.html
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ring-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ring-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ring-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ring-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ring-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/ring-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ring-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ring.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/ring-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ring-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/ring-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ring-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ring-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ring-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ring-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ring-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://ring.com/.well-known/security.txt
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.amazon.com/docs/ring/release-notes.html
- group: operate
  title: ''
  type: Support
  url: https://support.ring.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.ring.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://ring.com/protect-plans
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ring.com/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ring.com/terms
- group: other
  title: ''
  type: Store
  url: https://ring.com/appstore
created: '2026-07-17'
description: Ring is an Amazon home-security company (doorbells, cameras, alarm systems, and the Ring Protect subscription) that in 2026 launched the Ring Developer platform and Ring Appstore. Third-party developers can build video-powered apps against the Ring Partner API — a REST API served from api.amazonvision.com (Amazon Vision API / AVA) that follows the JSON:API format and is secured with OAuth 2.0 one-way account linking. The API exposes device discovery, device status/capabilities/location/configurations, event history, WebRTC/WHEP live video, media clip and image downloads, subscription queries, and a webhook event surface (motion, button press, device online/offline, subscription changes). Ring also publishes a remote Model Context Protocol (MCP) server backed by an Amazon Bedrock Knowledge Base so AI coding assistants can query the documentation while building integrations, and publishes a HackerOne bug-bounty via a /.well-known/security.txt.
image: https://developer.ring.com/og-image.png
layout: provider
mcp_servers:
- description: The Ring Appstore Knowledge MCP Server is a remote Model Context Protocol server backed by an Amazon Bedrock Knowledge Base. It connects an AI coding assistant (Kiro, Cursor, Cline, Claude Desktop) to
  name: Ring MCP Server
  slug: ring-mcp-server
modified: '2026-07-21'
name: Ring
nav: Providers
network: true
overview: 'Ring publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Home Security, Smart Home, IoT, and Video.


  The Ring catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ring''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 22 more developer resources.'
random_paper: 12
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 42.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ring/refs/heads/main/screenshots/ring-2026-08-17T081710.png
security:
- kind: authentication
  name: Ring Authentication
  slug: ring-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Ring Domain Security
  slug: ring-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ring Vulnerability Disclosure
  slug: ring-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: ring
tags:
- Company
- Home Security
- Smart Home
- IoT
- Video
- Camera
- Doorbells
- Webhook
- WebRTC
- Amazon
- Developer Platform
- MCP
website: https://ring.com
---
