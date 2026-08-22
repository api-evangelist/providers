---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.6
  scored_at: '2026-08-19'
api_count: 5
apis:
- description: 'OAuth 2.0 REST API for managing Snapchat advertising: organizations, ad accounts, campaigns, ad squads, ads, creatives, media, audience segments, measurement/reporting, the Conversions API (server-to-'
  name: Snapchat Marketing API
  slug: snapchat-marketing-api
- description: Server-to-server conversion event ingestion for web, app, and offline events, keyed by asset (Pixel ID for web/offline, Snap App ID for mobile app). Served from tr.snapchat.com; v3 (/v3/{asset_id}/eve
  name: Snap Conversions API
  slug: snap-conversions-api
- description: Snap's first-party hosted Model Context Protocol server, letting supported agents read the caller's authorized Snapchat Ads data over streamable HTTP. Read-only in this release; write access is docume
  name: Snapchat Ads MCP
  slug: snapchat-ads-mcp
- description: OAuth 2.0 and OpenID Connect identity platform for "Login with Snapchat", plus Creative Kit and Bitmoji Kit. Lets third-party apps authenticate Snapchatters, fetch approved profile fields, and share c
  name: Snap Kit / Login Kit
  slug: snap-kit-login-kit
- description: SDK and API for embedding Snap's augmented-reality Lenses (Lens Studio content) into third-party mobile and web apps, including a push-to-device API for managing Lens groups and experiences.
  name: Camera Kit
  slug: camera-kit
artifact_total: 14
asyncapis:
- description: ''
  name: Snap Lead Gen Webhooks
  slug: snap-lead-gen-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.snap.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.snap.com/api/marketing-api/Ads-API/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developers.snap.com/api/marketing-api/Ads-API/api-patterns
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.snap.com/api/marketing-api/Ads-API/quick-start
- group: auth
  title: ''
  type: Authentication
  url: authentication/snap-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/snap-scopes.yml
- group: build
  title: ''
  type: SDKs
  url: packages/snap-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/snap-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/snap-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/snap-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/snap-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/snap-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/snap-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/snap-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/snap-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/snap-tool-crosswalk.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/snap-conversions-api-v3-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/snap-conversions-api-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/snap-conversions-api-v3-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/snap-conversions-api-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/snap-lead-gen-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/snap-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/snap-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/snap-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/snap-components.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/snap-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/snap-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/snap-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snap-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/snap-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/snap-vulnerability-disclosure.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/snap-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Snapchat
- group: company
  title: ''
  type: Blog
  url: https://eng.snap.com/
- group: operate
  title: ''
  type: Support
  url: https://businesshelp.snapchat.com
- group: start
  title: ''
  type: SignUp
  url: https://ads.snapchat.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://snap.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://snap.com/privacy/privacy-policy
created: '2026-07-17'
description: 'Snap Inc. is the technology company behind Snapchat, Bitmoji, Spectacles, and Lens Studio. Its Snap for Developers program exposes several public APIs and SDKs: the Snapchat Marketing API (Ads API, Ads Gallery API, Conversions API, and Public Profile API) for programmatically managing organizations, ad accounts, campaigns, ad squads, ads, creatives, audiences, measurement, and server-to-server conversion events; Snap Kit / Login Kit for OAuth 2.0 and OpenID Connect powered "Login with Snapchat", Creative Kit, and Bitmoji Kit; and Camera Kit for embedding Snap''s augmented-reality Lenses into third-party apps and web experiences. The Marketing API is an OAuth 2.0 REST API served from adsapi.snapchat.com/v1 with cursor pagination and a structured request envelope. Snap publishes first-party OpenAPI 3.0 for the Conversions API in its own Business SDK repositories, ships a hosted read-only MCP server for Snapchat Ads at mcp.snapchat.com/ads with pre-registered OAuth clients for
  five agents, and delivers lead-generation leads by HMAC-signed webhook. First-party SDKs are published for Java, Python, PHP, Ruby, Go, JavaScript (Camera Kit on npm), Android, and iOS. Snap was surfaced as a portfolio company of General Catalyst and enriched into the API Evangelist network.'
image: https://developers.snap.com/img/snap-developer-logo.png
layout: provider
mcp_servers:
- description: ''
  name: snap-mcp.yml
  slug: snap-mcpyml
modified: '2026-08-13'
name: Snap
nav: Providers
network: true
overview: 'Snap publishes 1 API on the [APIs.io](https://apis.io/) network: Conversions API. Tagged areas include Company, Advertising, Marketing, Social Media, and Augmented Reality.


  The Snap catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Snap''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, engineering blog, and 32 more developer resources.'
plans:
- name: Snap Plans Pricing
  plan_count: 0
  slug: snap-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Snap Rate Limits
  slug: snap-rate-limits
scopes:
- name: Snap Scopes
  scope_count: 0
  slug: snap-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 54.8
  delta: 0.9
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 30.3
    contract_quality: 46.2
    developer_ergonomics: 73.2
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 76.3
  previous_composite: 53.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/snap/refs/heads/main/screenshots/snap-2026-08-17T081939.png
security:
- kind: authentication
  name: Snap Authentication
  slug: snap-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Snap Domain Security
  slug: snap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Snap Vulnerability Disclosure
  slug: snap-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Snap Trust Center
  slug: snap-trust-center
  summary_line: trust center published
slug: snap
tags:
- Company
- Advertising
- Marketing
- Social Media
- Augmented Reality
- Camera
- Authentication
- Identity
- Conversions
- Attribution
- SDKs
website: https://developers.snap.com
---
