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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Wistia Agentic Access
  operation_count: 48
  slug: wistia-agentic-access
  summary_line: 48 operations · 32 acting
api_count: 4
apis:
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
- description: The Allowed Domains API from Wistia — 2 operation(s) for allowed domains.
  name: Wistia Allowed Domains API
  slug: wistia-allowed-domains-api
- description: The Analytics:Account API from Wistia — 4 operation(s) for analytics:account.
  name: Wistia Analytics:Account API
  slug: wistia-analytics-account-api
- description: The Analytics:Media API from Wistia — 7 operation(s) for analytics:media.
  name: Wistia Analytics:Media API
  slug: wistia-analytics-media-api
- description: The Analytics:Webinar API from Wistia — 5 operation(s) for analytics:webinar.
  name: Wistia Analytics:Webinar API
  slug: wistia-analytics-webinar-api
- description: The Background Job Status API from Wistia — 1 operation(s) for background job status.
  name: Wistia Background Job Status API
  slug: wistia-background-job-status-api
- description: The Brands API from Wistia — 1 operation(s) for brands.
  name: Wistia Brands API
  slug: wistia-brands-api
- description: The Bulk Actions API from Wistia — 1 operation(s) for bulk actions.
  name: Wistia Bulk Actions API
  slug: wistia-bulk-actions-api
- description: The Channel Collaborators API from Wistia — 2 operation(s) for channel collaborators.
  name: Wistia Channel Collaborators API
  slug: wistia-channel-collaborators-api
- description: The Channel Episodes API from Wistia — 6 operation(s) for channel episodes.
  name: Wistia Channel Episodes API
  slug: wistia-channel-episodes-api
- description: The Custom Metadata Field Definitions API from Wistia — 3 operation(s) for custom metadata field definitions.
  name: Wistia Custom Metadata Field Definitions API
  slug: wistia-custom-metadata-field-definitions-api
- description: The Custom Metadata Field Values API from Wistia — 2 operation(s) for custom metadata field values.
  name: Wistia Custom Metadata Field Values API
  slug: wistia-custom-metadata-field-values-api
- description: The Deleted Media API from Wistia — 2 operation(s) for deleted media.
  name: Wistia Deleted Media API
  slug: wistia-deleted-media-api
- description: The Expiring Access Tokens API from Wistia — 1 operation(s) for expiring access tokens.
  name: Wistia Expiring Access Tokens API
  slug: wistia-expiring-access-tokens-api
- description: The Extended Audio Descriptions API from Wistia — 4 operation(s) for extended audio descriptions.
  name: Wistia Extended Audio Descriptions API
  slug: wistia-extended-audio-descriptions-api
- description: The Folder Sharings API from Wistia — 2 operation(s) for folder sharings.
  name: Wistia Folder Sharings API
  slug: wistia-folder-sharings-api
- description: The Live Stream Event Registrations API from Wistia — 1 operation(s) for live stream event registrations.
  name: Wistia Live Stream Event Registrations API
  slug: wistia-live-stream-event-registrations-api
- description: The Live Stream Events API from Wistia — 2 operation(s) for live stream events.
  name: Wistia Live Stream Events API
  slug: wistia-live-stream-events-api
- description: The Localizations API from Wistia — 2 operation(s) for localizations.
  name: Wistia Localizations API
  slug: wistia-localizations-api
- description: The Media API from Wistia — 11 operation(s) for media.
  name: Wistia Media API
  slug: wistia-media-api
- description: The Project Sharings API from Wistia — 2 operation(s) for project sharings.
  name: Wistia Project Sharings API
  slug: wistia-project-sharings-api
- description: The Projects API from Wistia — 3 operation(s) for projects.
  name: Wistia Projects API
  slug: wistia-projects-api
- description: The Push Devices API from Wistia — 2 operation(s) for push devices.
  name: Wistia Push Devices API
  slug: wistia-push-devices-api
- description: The Remix API from Wistia — 5 operation(s) for remix.
  name: Wistia Remix API
  slug: wistia-remix-api
- description: The Resource URLs API from Wistia — 1 operation(s) for resource urls.
  name: Wistia Resource URLs API
  slug: wistia-resource-urls-api
- description: The Review Bundles API from Wistia — 2 operation(s) for review bundles.
  name: Wistia Review Bundles API
  slug: wistia-review-bundles-api
- description: The Search API from Wistia — 1 operation(s) for search.
  name: Wistia Search API
  slug: wistia-search-api
- description: The Share Links API from Wistia — 2 operation(s) for share links.
  name: Wistia Share Links API
  slug: wistia-share-links-api
- description: The Stats:Account API from Wistia — 2 operation(s) for stats:account.
  name: Wistia Stats:Account API
  slug: wistia-stats-account-api
- description: The Stats:Events API from Wistia — 2 operation(s) for stats:events.
  name: Wistia Stats:Events API
  slug: wistia-stats-events-api
- description: The Stats:Media API from Wistia — 3 operation(s) for stats:media.
  name: Wistia Stats:Media API
  slug: wistia-stats-media-api
- description: The Stats:Projects API from Wistia — 1 operation(s) for stats:projects.
  name: Wistia Stats:Projects API
  slug: wistia-stats-projects-api
- description: The Stats:Visitors API from Wistia — 2 operation(s) for stats:visitors.
  name: Wistia Stats:Visitors API
  slug: wistia-stats-visitors-api
- description: The Subfolders API from Wistia — 5 operation(s) for subfolders.
  name: Wistia Subfolders API
  slug: wistia-subfolders-api
- description: The Taggings API from Wistia — 1 operation(s) for taggings.
  name: Wistia Taggings API
  slug: wistia-taggings-api
- description: The Trims API from Wistia — 1 operation(s) for trims.
  name: Wistia Trims API
  slug: wistia-trims-api
- description: The Webinar Collaborators API from Wistia — 2 operation(s) for webinar collaborators.
  name: Wistia Webinar Collaborators API
  slug: wistia-webinar-collaborators-api
- description: The Webinar Registrations API from Wistia — 1 operation(s) for webinar registrations.
  name: Wistia Webinar Registrations API
  slug: wistia-webinar-registrations-api
artifact_total: 73
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/wistia-capability-edges.yml
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
overview: 'Wistia publishes 48 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Account API, AllowedDomains API, and 45 more. Tagged areas include Video Hosting, Video Marketing, Video Analytics, Lead Generation, and Webinars.


  The Wistia catalog on APIs.io includes 2 event-driven AsyncAPI specifications and 1 Spectral governance ruleset.


  Wistia''s developer surface includes authentication, CLI, changelog, documentation, API reference, getting-started guide, pricing, and 34 more developer resources.'
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
  composite: 62.8
  coverage:
    artifact_dirs: 27
    catalog_gap: 60.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -1.9
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 29.5
    contract_quality: 65.0
    developer_ergonomics: 54.2
    discoverability: 57.4
    governance: 29.5
    operational_transparency: 61.8
  previous_composite: 64.7
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
