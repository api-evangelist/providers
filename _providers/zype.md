---
access_model:
  confidence: high
  label: Paid, sales-led
  onboarding: unknown
  pricing: paid
  public: true
  source:
  - https://www.zype.com/pricing
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-09-01'
api_count: 15
apis:
- description: 'The core Zype content API: videos, playlists, categories, subtitles and subtitle playlists, transcriptions and translations, AI metadata suggestions, segments, program guides, video imports and source'
  name: Zype Platform API
  slug: platform
- description: 'Cloud playout for FAST and linear channels: channels, HLS/UDP/RTMP delivery profiles, destinations and connectors, draft and published schedule versions, revertible timeline operations, assets (blocks'
  name: Zype Playout Scheduler API
  slug: playout-scheduler
- description: Subscriptions with a reversible cancel/reactivate pair, plans and tiered plan-to-playlist binding, transactions carrying Stripe/Braintree/Recurly references, redemption codes with bulk minting and red
  name: Zype Monetization API
  slug: monetization
- description: 'The end-viewer surface: consumer records, password reset flows, parental access codes, device pin linking, and video, playlist and subscription entitlements. 24 operations.'
  name: Zype Consumers API
  slug: consumers
- description: 'Live streaming V3: encoder lifecycle including start, stop and sync, and live events with start, stop and archive. 16 operations. Supersedes the legacy /live/encoders surface still carried in the Plat'
  name: Zype Live API (V3)
  slug: live-3
- description: 'Zype''s custom-metadata model: Zobject Types define a schema (actor, director, team, season) and Zobjects are instances, attachable to videos and playlists in both directions. 16 operations.'
  name: Zype Zobjects API
  slug: zobjects
- description: 'Current analytics surface across three families: engagement (plays, viewers, hours watched, view time), revenue (new subscriptions, subscription events, subscription revenue, new transactions) and pla'
  name: Zype Analytics API (V3)
  slug: analytics-v3
- description: 'Legacy V2 analytics surface — stream hours, player requests, engagement, site counts, consumers, subscriptions, subscription events, subscription revenue and transactions. 9 operations. Superseded by '
  name: Zype Analytics API (V2)
  slug: analytics
- description: Site-scoped custom regions and global content regions, the geographic building blocks used by content rules. 7 operations.
  name: Zype Custom Regions API
  slug: content-regions
- description: Site-scoped and global content rule groups — reusable bundles of rules applied to content availability. 7 operations.
  name: Zype Content Rule Groups API
  slug: content-rule-groups
- description: Content rule profiles plus the country/state/city lookups they are built from — geo-blocking and availability windows. 7 operations.
  name: Zype Content Rule Profiles API
  slug: content-rules
- description: 'TV Everywhere / MVPD authentication implemented against the Adobe Primetime device-session flow: register a device session, create a Zype consumer, validate a session token, retrieve preauthorized res'
  name: Zype TVE API
  slug: tve
- description: 'Consumer-facing OAuth 2.0: retrieve an access token, read token status and revoke a token. 3 operations. login.zype.com serves its own RFC 8414 authorization server metadata document alongside the one'
  name: Zype Consumer Authentication API
  slug: login
- description: Retrieves the embeddable player for a video in html, js or json form — the json form returns metadata plus the Widevine, FairPlay and PlayReady DRM objects and m3u8 references — and the playlist carou
  name: Zype Player API
  slug: player
- description: Creates an upload for direct ingest of a source file into the Zype library. 1 operation.
  name: Zype Uploads API
  slug: uploads
artifact_total: 24
common:
- group: company
  title: ''
  type: Website
  url: https://www.zype.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.zype.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zype.com/reference/welcome-to-the-zype-api-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zype.com/reference/welcome-to-the-zype-api-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://www.zype.com/developers/zype-api
- group: operate
  title: ''
  type: Support
  url: https://www.zype.com/resources/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.zype.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.zype.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.zype.com/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zype
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zype-inc
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zype.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/zype-plans-pricing.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.zype.com/request-demo
- group: start
  title: ''
  type: Login
  url: https://admin.zype.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zype.com/availability-sla-and-support-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.backlight.co/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zype.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zype-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://www.zype.com/security-compliance
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zype-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.zype.com
- group: auth
  title: ''
  type: Compliance
  url: conformance/zype-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zype-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zype-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zype-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zype-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zype-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zype-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/zype-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/zype-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zype-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zype-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zype-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zype-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zype-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/zype-components.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zype-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zype-finops.yml
- group: other
  title: ''
  type: PointerVerification
  url: well-known/zype-pointer-verification.yml
created: '2025-02-12'
description: Zype is an API-first video content management and streaming platform used by enterprises and media companies to run OTT apps, FAST and linear channels, and global video distribution. The platform spans a video CMS and CRM, cloud encoding, multi-CDN delivery, AI-assisted metadata, transcription and translation, SSAI advertising and DRM, subscription and transactional monetization, consumer entitlements, TV Everywhere authentication, cloud playout scheduling with XMLTV and platform EPG export, and a no-code app builder for web, mobile and connected TV. Zype publishes fifteen OpenAPI 3.0.1 definitions covering 317 operations, an RFC 8414 OAuth authorization server advertising 148 scopes, and a first-party MCP server. Zype is a Backlight business.
finops:
- name: Zype Finops
  service_category: API
  slug: zype-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zype.png
layout: provider
mcp_servers:
- description: First-party Model Context Protocol server that exposes the Zype video platform (videos, transcriptions, playlists, categories, subtitles, analytics, monetization, zobjects and the player) to MCP-speak
  name: Zype MCP Client
  slug: zype-mcp-client
modified: '2026-08-28'
name: Zype
nav: Providers
network: true
overview: 'Zype publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Platform API, Playout Scheduler API, Monetization API, and 12 more. Tagged areas include Video, Streaming, OTT, Video CMS, and FAST.


  Zype''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 34 more developer resources.'
plans:
- name: Zype Plans Pricing
  plan_count: 7
  slug: zype-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Zype Rate Limits
  slug: zype-rate-limits
scopes:
- name: Zype Scopes
  scope_count: 0
  slug: zype-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.4
  coverage:
    artifact_dirs: 23
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 45.9
    developer_ergonomics: 63.1
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 28.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 53.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zype/refs/heads/main/screenshots/zype-2026-06-20T202013.png
security:
- kind: authentication
  name: Zype Authentication
  slug: zype-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Zype Domain Security
  slug: zype-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zype Vulnerability Disclosure
  slug: zype-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Zype Trust Center
  slug: zype-trust-center
  summary_line: trust center published
slug: zype
tags:
- Video
- Streaming
- OTT
- Video CMS
- FAST
- Linear TV
- Playout
- Monetization
- Live Streaming
- Analytics
- Media and Entertainment
- DRM
- Advertising
- Encoding
- EPG
website: https://www.zype.com/
---
