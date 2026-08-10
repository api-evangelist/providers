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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Art Agentic Access
  operation_count: 46
  slug: art-agentic-access
  summary_line: 46 operations · 1 acting
api_count: 25
apis:
- description: The Applications API from Artsy — 2 operation(s) for applications.
  name: Artsy Applications API
  slug: art-applications-api
- description: The Artists API from Artsy — 2 operation(s) for artists.
  name: Artsy Artists API
  slug: art-artists-api
- description: The Artworks API from Artsy — 2 operation(s) for artworks.
  name: Artsy Artworks API
  slug: art-artworks-api
- description: The Authentication API from Artsy — 1 operation(s) for authentication.
  name: Artsy Authentication API
  slug: art-authentication-api
- description: The Bidder Positions API from Artsy — 2 operation(s) for bidder positions.
  name: Artsy Bidder Positions API
  slug: art-bidder-positions-api
- description: The Bidders API from Artsy — 2 operation(s) for bidders.
  name: Artsy Bidders API
  slug: art-bidders-api
- description: The Collection Items API from Artsy — 2 operation(s) for collection items.
  name: Artsy Collection Items API
  slug: art-collection-items-api
- description: The Collections API from Artsy — 2 operation(s) for collections.
  name: Artsy Collections API
  slug: art-collections-api
- description: The Collector Profiles API from Artsy — 2 operation(s) for collector profiles.
  name: Artsy Collector Profiles API
  slug: art-collector-profiles-api
- description: The Devices API from Artsy — 2 operation(s) for devices.
  name: Artsy Devices API
  slug: art-devices-api
- description: The Editions API from Artsy — 1 operation(s) for editions.
  name: Artsy Editions API
  slug: art-editions-api
- description: The Fairs API from Artsy — 2 operation(s) for fairs.
  name: Artsy Fairs API
  slug: art-fairs-api
- description: The Genes API from Artsy — 2 operation(s) for genes.
  name: Artsy Genes API
  slug: art-genes-api
- description: The Images API from Artsy — 1 operation(s) for images.
  name: Artsy Images API
  slug: art-images-api
- description: The Partner Communications API from Artsy — 2 operation(s) for partner communications.
  name: Artsy Partner Communications API
  slug: art-partner-communications-api
- description: The Partner Contacts API from Artsy — 2 operation(s) for partner contacts.
  name: Artsy Partner Contacts API
  slug: art-partner-contacts-api
- description: The Partners API from Artsy — 2 operation(s) for partners.
  name: Artsy Partners API
  slug: art-partners-api
- description: The Profiles API from Artsy — 2 operation(s) for profiles.
  name: Artsy Profiles API
  slug: art-profiles-api
- description: The Sale Artworks API from Artsy — 2 operation(s) for sale artworks.
  name: Artsy Sale Artworks API
  slug: art-sale-artworks-api
- description: The Sales API from Artsy — 2 operation(s) for sales.
  name: Artsy Sales API
  slug: art-sales-api
- description: The Search API from Artsy — 1 operation(s) for search.
  name: Artsy Search API
  slug: art-search-api
- description: The Shows API from Artsy — 2 operation(s) for shows.
  name: Artsy Shows API
  slug: art-shows-api
- description: The Status API from Artsy — 1 operation(s) for status.
  name: Artsy Status API
  slug: art-status-api
- description: The User Fair Actions API from Artsy — 2 operation(s) for user fair actions.
  name: Artsy User Fair Actions API
  slug: art-user-fair-actions-api
- description: The Users API from Artsy — 3 operation(s) for users.
  name: Artsy Users API
  slug: art-users-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Mint an XApp token, search for an artist, then list that artist's artworks.
  name: Find an artist and list their artworks
  slug: art-find-artist-artworks
artifact_total: 32
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.artsy.net/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.artsy.net/v2/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.artsy.net/v2
- group: auth
  title: ''
  type: Authentication
  url: authentication/art-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/art-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/art-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/art-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/art-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://api.artsy.net/api/status/
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.artsy.net/v2/docs
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/art-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/art-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/art-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/art-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/art-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/art-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/art-find-artist-artworks.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/art-domain-security.yml
- group: docs
  title: ''
  type: GraphQL
  url: https://github.com/artsy/metaphysics
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/artsy
- group: company
  title: ''
  type: Blog
  url: https://artsy.github.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.artsy.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.artsy.net/privacy
- group: company
  title: ''
  type: Website
  url: https://www.artsy.net
created: '2026-07-17'
description: 'Artsy (art.sy) is the online marketplace and platform for discovering, buying, and selling fine art, connecting collectors with galleries, museums, art fairs, and auction houses worldwide. Artsy operates a public developer program: the Artsy Public API (v2) is a HAL hypermedia REST API exposing Artsy''s database of artists, artworks, genes (the Art Genome Project''s classification of artistic characteristics), gallery and museum shows, partners, art fairs, and auction sales. Authentication uses an application-level X-Xapp-Token minted by exchanging a client_id and client_secret. Artsy also runs the Metaphysics GraphQL API that powers its own web and mobile apps. Artsy has announced that the public REST API is being retired and may be taken down without notice; the Partner API remains available to approved partners. Surfaced as a slow-ventures portfolio company and enriched by the API Evangelist pipeline from Artsy''s live API and docs.'
image: https://github.com/artsy.png
layout: provider
mcp_servers:
- description: ''
  name: art-mcp.yml
  slug: art-mcpyml
modified: '2026-07-18'
name: Artsy
nav: Providers
network: true
overview: 'Artsy publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Artists API, Artworks API, and 22 more. Tagged areas include Art, Marketplace, Culture, Museums, and Galleries.


  Artsy''s developer surface includes documentation, API reference, authentication, engineering blog, and 21 more developer resources.'
random_paper: 95
rate_limits:
- limit_count: 1
  name: Art Rate Limits
  slug: art-rate-limits
score:
  band: developing
  composite: 44.8
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 61.0
    developer_ergonomics: 40.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 50.0
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/art/refs/heads/main/screenshots/art-2026-07-25T201312.png
security:
- kind: authentication
  name: Art Authentication
  slug: art-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Art Domain Security
  slug: art-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: art
tags:
- Art
- Marketplace
- Culture
- Museums
- Galleries
- Auctions
- Media
- Hypermedia
- Company
website: https://www.artsy.net
---
