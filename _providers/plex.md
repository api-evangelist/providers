---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 60.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 130
  human_in_the_loop: 9
  name: Plex Agentic Access
  operation_count: 258
  slug: plex-agentic-access
  summary_line: 258 operations · 130 acting · 9 human-in-the-loop
api_count: 31
apis:
- description: 'The plex.tv cloud API that issues and refreshes the credentials every Plex Media Server call depends on: PIN-based device linking, JWK public-key registration, nonce issuance, device-JWT exchange for '
  name: Plex Account and Authentication API
  slug: plex-account-api
- description: A first-party remote Model Context Protocol server operated by Plex at https://plex.tv/internal/mcp. It advertises RFC 9728 protected-resource metadata, RFC 8414 authorization-server metadata and Open
  name: Plex MCP Server
  slug: plex-mcp-server
- description: Activities provide a way to monitor and control asynchronous operations on the server. In order to receive real-time updates for activities, a client would normally subscribe via either EventSource or
  name: Plex Activities API
  slug: plex-activities-api
- description: 'The butler is responsible for running periodic tasks. Some tasks run daily, others every few days, and some weekly. These includes database maintenance, metadata updating, thumbnail generation, media '
  name: Plex Butler API
  slug: plex-butler-api
- description: The Collections API from Plex — 1 operation(s) for collections.
  name: Plex Collections API
  slug: plex-collections-api
- description: The actual content of the media provider
  name: Plex Content API
  slug: plex-content-api
- description: Media grabbers provide ways for media to be obtained for a given protocol. The simplest ones are `stream` and `download`. More complex grabbers can have associated devices Network tuners can present t
  name: Plex Devices API
  slug: plex-devices-api
- description: The Download Queue API from Plex — 8 operation(s) for download queue.
  name: Plex Download Queue API
  slug: plex-download-queue-api
- description: The DVR provides means to watch and record live TV. This section of endpoints describes how to setup the DVR itself
  name: Plex DV Rs API
  slug: plex-dvrs-api
- description: The EPG (Electronic Program Guide) is responsible for obtaining metadata for what is airing on each channel and when
  name: Plex EPG API
  slug: plex-epg-api
- description: The server can notify clients in real-time of a wide range of events, from library scanning, to preferences being modified, to changes to media, and many other things. This is also the mechanism by wh
  name: Plex Events API
  slug: plex-events-api
- description: General endpoints for basic PMS operation not specific to any media provider
  name: Plex General API
  slug: plex-general-api
- description: The hubs within a media provider
  name: Plex Hubs API
  slug: plex-hubs-api
- description: Library endpoints which are outside of the Media Provider API. Typically this is manipulation of the library (adding/removing sections, modifying preferences, etc).
  name: Plex Library API
  slug: plex-library-api
- description: Endpoints for manipulating collections. In addition to these endpoints, `/library/collections/:collectionId/X` will be rerouted to `/library/metadata/:collectionId/X` and respond to those endpoints as
  name: Plex Library Collections API
  slug: plex-library-collections-api
- description: Endpoints for manipulating playlists.
  name: Plex Library Playlists API
  slug: plex-library-playlists-api
- description: LiveTV contains the playback sessions of a channel from a DVR device
  name: Plex Live TV API
  slug: plex-live-tv-api
- description: Logging mechanism to allow clients to log to the server
  name: Plex Log API
  slug: plex-log-api
- description: The Metadata Agents API from Plex — 5 operation(s) for metadata agents.
  name: Plex Metadata Agents API
  slug: plex-metadata-agents-api
- description: The playqueue feature within a media provider A play queue represents the current list of media for playback. Although queues are persisted by the server, they should be regarded by the user as a fair
  name: Plex Play Queue API
  slug: plex-play-queue-api
- description: The playlist feature within a media provider Playlists are ordered collections of media. They can be dumb (just a list of media) or smart (based on a media query, such as "all albums from 2017"). They
  name: Plex Playlist API
  slug: plex-playlist-api
- description: The Preferences API from Plex — 2 operation(s) for preferences.
  name: Plex Preferences API
  slug: plex-preferences-api
- description: 'Media providers are the starting points for the entire Plex Media Server media library API. It defines the paths for the groups of endpoints. The `/media/providers` should be the only hard-coded path '
  name: Plex Provider API
  slug: plex-provider-api
- description: The rate feature within a media provider
  name: Plex Rate API
  slug: plex-rate-api
- description: The search feature within a media provider
  name: Plex Search API
  slug: plex-search-api
- description: The status endpoints give you information about current playbacks, play history, and even terminating sessions.
  name: Plex Status API
  slug: plex-status-api
- description: Subscriptions determine which media will be recorded and the criteria for selecting an airing when multiple are available
  name: Plex Subscriptions API
  slug: plex-subscriptions-api
- description: The actions feature within a media provider
  name: Plex Timeline API
  slug: plex-timeline-api
- description: The Transcoder API from Plex — 5 operation(s) for transcoder.
  name: Plex Transcoder API
  slug: plex-transcoder-api
- description: Service provided to compute UltraBlur colors and images.
  name: Plex Ultra Blur API
  slug: plex-ultrablur-api
- description: This describes the API for searching and applying updates to the Plex Media Server. Updates to the status can be observed via the Event API.
  name: Plex Updater API
  slug: plex-updater-api
artifact_total: 68
asyncapis:
- description: ''
  name: Plex Webhooks
  slug: plex-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Plex Media Server Activities API
  slug: open-plex-activities-api
- collection_type: open
  name: Plex Media Server Butler API
  slug: open-plex-butler-api
- collection_type: open
  name: Plex Media Server Collections API
  slug: open-plex-collections-api
- collection_type: open
  name: Plex Media Server Content API
  slug: open-plex-content-api
- collection_type: open
  name: Plex Media Server Devices API
  slug: open-plex-devices-api
- collection_type: open
  name: Plex Media Server Download Queue API
  slug: open-plex-download-queue-api
- collection_type: open
  name: Plex Media Server DV Rs API
  slug: open-plex-dvrs-api
- collection_type: open
  name: Plex Media Server EPG API
  slug: open-plex-epg-api
- collection_type: open
  name: Plex Media Server Events API
  slug: open-plex-events-api
- collection_type: open
  name: Plex Media Server General API
  slug: open-plex-general-api
- collection_type: open
  name: Plex Media Server Hubs API
  slug: open-plex-hubs-api
- collection_type: open
  name: Plex Media Server Library API
  slug: open-plex-library-api
- collection_type: open
  name: Plex Media Server Library Collections API
  slug: open-plex-library-collections-api
- collection_type: open
  name: Plex Media Server Library Playlists API
  slug: open-plex-library-playlists-api
- collection_type: open
  name: Plex Media Server Live TV API
  slug: open-plex-live-tv-api
- collection_type: open
  name: Plex Media Server Log API
  slug: open-plex-log-api
- collection_type: open
  name: Plex Media Server Metadata Agents API
  slug: open-plex-metadata-agents-api
- collection_type: open
  name: Plex Media Server Play Queue API
  slug: open-plex-play-queue-api
- collection_type: open
  name: Plex Media Server Playlist API
  slug: open-plex-playlist-api
- collection_type: open
  name: Plex Media Server Preferences API
  slug: open-plex-preferences-api
- collection_type: open
  name: Plex Media Server Provider API
  slug: open-plex-provider-api
- collection_type: open
  name: Plex Media Server Rate API
  slug: open-plex-rate-api
- collection_type: open
  name: Plex Media Server Search API
  slug: open-plex-search-api
- collection_type: open
  name: Plex Media Server Status API
  slug: open-plex-status-api
- collection_type: open
  name: Plex Media Server Subscriptions API
  slug: open-plex-subscriptions-api
- collection_type: open
  name: Plex Media Server Timeline API
  slug: open-plex-timeline-api
- collection_type: open
  name: Plex Media Server Transcoder API
  slug: open-plex-transcoder-api
- collection_type: open
  name: Plex Media Server Ultra Blur API
  slug: open-plex-ultrablur-api
- collection_type: open
  name: Plex Media Server Updater API
  slug: open-plex-updater-api
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
  url: openapi/_original/plex-media-server-openapi.json
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
  name: Plex MCP Server
  slug: plex-mcp-server
modified: '2026-08-05'
name: Plex
nav: Providers
network: true
overview: 'Plex publishes 29 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Butler API, Collections API, and 26 more. Tagged areas include Company, Media, Streaming, Video, and Music.


  The Plex catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Plex''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 34 more developer resources.'
random_paper: 0
scopes:
- name: Plex Scopes
  scope_count: 7
  slug: plex-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: strong
  composite: 55.3
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 16.7
    contract_quality: 64.6
    developer_ergonomics: 58.9
    discoverability: 85.2
    governance: 16.7
    operational_transparency: 60.5
  previous_composite: 55.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 29
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/plex/refs/heads/main/screenshots/plex-2026-08-17T081305.png
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
