---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 67.3
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 130
  human_in_the_loop: 9
  name: Plex Agentic Access
  operation_count: 258
  slug: plex-agentic-access
  summary_line: 258 operations · 130 acting · 9 human-in-the-loop
api_count: 3
apis:
- description: The official HTTP API exposed by every Plex Media Server. Version 1.2.2 of the published contract describes 258 operations across 205 paths — library sections and items, metadata and artwork, playlist
  name: Plex Media Server API
  slug: plex-media-server-api
- description: 'The plex.tv cloud API that issues and refreshes the credentials every Plex Media Server call depends on: PIN-based device linking, JWK public-key registration, nonce issuance, device-JWT exchange for '
  name: Plex Account and Authentication API
  slug: plex-account-api
- description: A first-party remote Model Context Protocol server operated by Plex at https://plex.tv/internal/mcp. It advertises RFC 9728 protected-resource metadata, RFC 8414 authorization-server metadata and Open
  name: Plex MCP Server
  slug: plex-mcp-server
artifact_total: 10
asyncapis:
- description: ''
  name: Plex Webhooks
  slug: plex-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.plex.tv/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.plex.tv/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.plex.tv/pms/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.plex.tv/pms/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.plex.tv/pms/#section/API-Info/Authenticating-with-Plex
- group: operate
  title: ''
  type: Support
  url: https://support.plex.tv/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.plex.tv/
- group: operate
  title: ''
  type: Community
  url: https://forums.plex.tv/
- group: company
  title: ''
  type: Blog
  url: https://www.plex.tv/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/plexinc
- group: commercial
  title: ''
  type: Pricing
  url: https://www.plex.tv/plans/
- group: start
  title: ''
  type: SignUp
  url: https://www.plex.tv/sign-up/
- group: start
  title: ''
  type: Login
  url: https://app.plex.tv/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.plex.tv/about/privacy-legal/plex-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.plex.tv/about/privacy-legal/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.plex.tv/
- group: other
  title: ''
  type: Downloads
  url: https://www.plex.tv/media-server-downloads/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/plex_stock/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/plex-media-server-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/plex-media-server-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/plex-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/plex-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/plex-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/plex-security.txt
- group: auth
  title: ''
  type: Security
  url: https://support.plex.tv/articles/reporting-security-issues/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/plex-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plex-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/plex-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/plex-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/plex-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/plex-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/plex-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/plex-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/plex-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/plex-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/plex-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/plex-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/plex-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/plex-packages.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/plex-agentic-access.yml
created: '2026-08-05'
description: Plex, Inc. is a personal-media and streaming company whose Plex Media Server organizes, transcodes and streams a user's own movies, TV, music and photos to Plex client apps on virtually every platform, alongside a free ad-supported live TV and on-demand catalog, Discover, Rentals, the Plexamp music player and the paid Plex Pass tier. In September 2025 Plex published official documentation for the Plex Media Server HTTP API for the first time — an OpenAPI 3.1 contract covering libraries, metadata, playlists, play queues, sessions, DVR/Live TV, transcoding and server administration — together with a new public-key JWT authentication flow on plex.tv, Plex Pass webhooks, and an OAuth-protected remote MCP server for agents.
image: https://www.plex.tv/wp-content/themes/plex/assets/img/plex-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: plex-mcp.yml
  slug: plex-mcpyml
modified: '2026-08-05'
name: Plex
nav: Providers
network: true
overview: 'Plex publishes 1 API on the [APIs.io](https://apis.io/) network: Media Server API. Tagged areas include Company, Media, Streaming, Video, and Music.


  The Plex catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Plex''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 34 more developer resources.'
random_paper: 102
scopes:
- name: Plex Scopes
  scope_count: 7
  slug: plex-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: strong
  composite: 57.8
  delta: -2.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 70.0
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 63.2
  previous_composite: 59.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Plex Authentication
  slug: plex-authentication
  summary_line: apiKey/jwt/oauth2 · 4 schemes
- kind: domain-security
  name: Plex Domain Security
  slug: plex-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Plex Vulnerability Disclosure
  slug: plex-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: plex
tags:
- Company
- Media
- Streaming
- Video
- Music
- Media Server
- Entertainment
- Self-Hosted
- Personal Media
- Home Automation
website: https://www.plex.tv/
---
