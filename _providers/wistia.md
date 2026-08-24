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
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.8
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Wistia Agentic Access
  operation_count: 48
  slug: wistia-agentic-access
  summary_line: 48 operations · 32 acting
api_count: 16
apis:
- description: REST API providing programmatic access to medias, projects, accounts, customizations, captions, and statistics in a Wistia account. Data is returned in JSON over HTTPS. Authentication uses Bearer Toke
  name: Wistia Data API
  slug: data-api
- description: The current STABLE release of Wistia's modern Data API — 55 paths and 85 operations covering media, folders, subfolders, folder sharings, captions, localizations, trims, customizations, tags, taggings
  name: Wistia Data API 2026-01
  slug: data-api-2026-01
- description: 'The edge description of Wistia''s modern API — 115 paths and 167 operations, the preview of what lands in the next dated stable release. It carries surfaces absent from 2026-01: Remix (AI video editing'
  name: Wistia Data API (modern, edge)
  slug: data-api-modern-edge
- description: Wistia's first-party hosted Model Context Protocol server, exposing 125 tools across the media, folders, channels, captions, customizations, tags, webinars, sharing, account, analytics, stats and remi
  name: Wistia MCP Server
  slug: mcp
- description: Endpoint for uploading video files directly to a Wistia account, typically used in conjunction with the Data API to manage uploaded media. Authentication uses the same API access token.
  name: Wistia Upload API
  slug: upload-api
- description: Real-time webhook deliveries from Wistia for documented media lifecycle events. Deliveries are HTTP POST with a JSON body and are signed via HMAC-SHA256 using the consumer's configured webhook secret,
  name: Wistia Webhooks
  slug: webhooks
- description: The Account API from Wistia — 1 operation(s) for account.
  name: Wistia Account API
  slug: wistia-account-api
- description: The AllowedDomains API from Wistia — 2 operation(s) for alloweddomains.
  name: Wistia AllowedDomains API
  slug: wistia-alloweddomains-api
- description: The Captions API from Wistia — 3 operation(s) for captions.
  name: Wistia Captions API
  slug: wistia-captions-api
- description: The Channels API from Wistia — 2 operation(s) for channels.
  name: Wistia Channels API
  slug: wistia-channels-api
- description: The Customizations API from Wistia — 1 operation(s) for customizations.
  name: Wistia Customizations API
  slug: wistia-customizations-api
- description: The Folders API from Wistia — 3 operation(s) for folders.
  name: Wistia Folders API
  slug: wistia-folders-api
- description: The Medias API from Wistia — 8 operation(s) for medias.
  name: Wistia Medias API
  slug: wistia-medias-api
- description: The Tags API from Wistia — 3 operation(s) for tags.
  name: Wistia Tags API
  slug: wistia-tags-api
- description: The Tokens API from Wistia — 1 operation(s) for tokens.
  name: Wistia Tokens API
  slug: wistia-tokens-api
- description: The Webinars API from Wistia — 3 operation(s) for webinars.
  name: Wistia Webinars API
  slug: wistia-webinars-api
artifact_total: 39
asyncapis:
- description: AsyncAPI 2.6 description of Wistia's webhook surface. Wistia delivers real-time notifications about media lifecycle events to a consumer endpoint configured in your Wistia account. All webhooks are de
  name: Wistia Webhooks API
  slug: wistia-asyncapi
- description: ''
  name: Wistia Webhooks
  slug: wistia-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wistia Data Account API
  slug: open-wistia-account-api
- collection_type: open
  name: Wistia Data Account AllowedDomains API
  slug: open-wistia-alloweddomains-api
- collection_type: open
  name: Wistia Data Account Captions API
  slug: open-wistia-captions-api
- collection_type: open
  name: Wistia Data Account Channels API
  slug: open-wistia-channels-api
- collection_type: open
  name: Wistia Data Account Customizations API
  slug: open-wistia-customizations-api
- collection_type: open
  name: Wistia Data Account Folders API
  slug: open-wistia-folders-api
- collection_type: open
  name: Wistia Data Account Medias API
  slug: open-wistia-medias-api
- collection_type: open
  name: Wistia Data Account Tags API
  slug: open-wistia-tags-api
- collection_type: open
  name: Wistia Data Account Tokens API
  slug: open-wistia-tokens-api
- collection_type: open
  name: Wistia Data Account Webinars API
  slug: open-wistia-webinars-api
- collection_type: open
  name: Wistia Data API
  slug: open-wistia
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wistia-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/wistia-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wistia-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wistia-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wistia-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wistia-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/wistia-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/wistia-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/wistia-cli.yml
- group: design
  title: ''
  type: Components
  url: components/wistia-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wistia-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wistia-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wistia-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wistia-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/wistia-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wistia-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wistia.com
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.wistia.com/docs/wistia-deprecation-schedule
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/wistia-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wistia-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.wistia.com/
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wistia-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/wistia-tool-crosswalk.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/wistia-data-api-2026-01-overlay.yaml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wistia
- group: company
  title: ''
  type: Website
  url: https://wistia.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wistia.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.wistia.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.wistia.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.wistia.com/docs/making-api-requests
- group: commercial
  title: ''
  type: Pricing
  url: https://wistia.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://wistia.com/signup
- group: operate
  title: ''
  type: Support
  url: https://wistia.com/support
- group: other
  title: ''
  type: Developers
  url: https://docs.wistia.com
- group: company
  title: ''
  type: Blog
  url: https://wistia.com/learn
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wistia.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wistia.com/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wistia
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wistia-llms.txt
created: '2026-05-11'
description: 'Wistia is an all-in-one video marketing platform for businesses that combines branded video hosting, webinars, video editing, webcam and screen recording, and deep viewer analytics for B2B marketing teams focused on lead generation, brand control, and content performance. Founded in 2006, Wistia is used by more than 425,000 businesses and integrates with major marketing automation and CRM platforms. Wistia ships an unusually complete developer surface for its category: a frozen evergreen Data API at https://api.wistia.com/v1 alongside a header-versioned modern API at https://api.wistia.com/modern with dated stable releases (2026-01), OpenAPI 3.1 descriptions made discoverable through an RFC 9727 api-catalog linkset, OAuth 2.0 with RFC 8414/9728 discovery and dynamic client registration, a hosted MCP server at https://api.wistia.com/mcp/api, a Go CLI, a Speakeasy-generated TypeScript SDK, and the Aurora `<wistia-player>` web component.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wistia.png
layout: provider
mcp_servers:
- description: 'Wistia operates a first-party, hosted MCP server that exposes the Wistia Data API to agents: media, folders, channels, captions, analytics and AI remix. It is a REMOTE streamable-HTTP endpoint — an ag'
  name: Wistia API MCP Server
  slug: wistia-api-mcp-server
modified: '2026-08-14'
name: Wistia
nav: Providers
network: true
overview: 'Wistia publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Data API, Data API 2026-01, Data API (modern, edge), and 11 more. Tagged areas include Video Hosting, Video Marketing, Video Analytics, Lead Generation, and Webinars.


  The Wistia catalog on APIs.io includes 2 event-driven AsyncAPI specifications and 1 Spectral governance ruleset.


  Wistia''s developer surface includes authentication, CLI, changelog, documentation, API reference, getting-started guide, pricing, and 33 more developer resources.'
plans:
- name: Wistia Plans Pricing
  plan_count: 4
  slug: wistia-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 4
  name: Wistia Rate Limits
  slug: wistia-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Wistia API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: wistia-asyncapi-spectral-rules
scopes:
- name: Wistia Scopes
  scope_count: 0
  slug: wistia-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 65.5
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 41.7
    contract_quality: 64.5
    developer_ergonomics: 54.2
    discoverability: 81.5
    governance: 41.7
    operational_transparency: 53.9
  previous_composite: 65.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wistia/refs/heads/main/screenshots/wistia-2026-06-20T201532.png
security:
- kind: authentication
  name: Wistia Authentication
  slug: wistia-authentication
  summary_line: http/oauth2 · 4 schemes
- kind: domain-security
  name: Wistia Domain Security
  slug: wistia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Wistia Trust Center
  slug: wistia-trust-center
  summary_line: SOC 2, PCI DSS, FedRAMP, GDPR
slug: wistia
tags:
- Video Hosting
- Video Marketing
- Video Analytics
- Lead Generation
- Webinars
- B2B Marketing
- Video Captions
- Localization
- MCP
- Media Management
website: https://wistia.com
---
