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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Artlist Agentic Access
  operation_count: 5
  slug: artlist-agentic-access
  summary_line: 5 operations
api_count: 2
apis:
- description: Hosted Model Context Protocol server for the Artlist Enterprise API documentation. Exposes a single anonymous read-only tool, searchDocs, that searches developer.artlist.io and returns documentation p
  name: Artlist Developer Docs MCP Server
  slug: docs-mcp
- baseURL: https://business.artlist.io/search/v1
  baseurl_source: declared
  description: The album API from Artlist — 1 operation(s) for album.
  name: Artlist Album API
  slug: artlist-album-api
- baseURL: https://business.artlist.io/search/v1
  baseurl_source: declared
  description: The artist API from Artlist — 1 operation(s) for artist.
  name: Artlist Artist API
  slug: artlist-artist-api
- baseURL: https://business.artlist.io/search/v1
  baseurl_source: declared
  description: The downloadable API from Artlist — 1 operation(s) for downloadable.
  name: Artlist Downloadable API
  slug: artlist-downloadable-api
- baseURL: https://business.artlist.io/search/v1
  baseurl_source: declared
  description: The song API from Artlist — 2 operation(s) for song.
  name: Artlist Song API
  slug: artlist-song-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Search Album API
  slug: open-artlist-album-api
- collection_type: open
  name: Search Artist API
  slug: open-artlist-artist-api
- collection_type: open
  name: Download Downloadable API
  slug: open-artlist-downloadable-api
- collection_type: open
  name: Search Song API
  slug: open-artlist-song-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/artlist-download-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://artlist.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.artlist.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.artlist.io/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://developer.artlist.io/search/song/song-controller-get-songs
- group: start
  title: ''
  type: Console
  url: https://developer.artlist.io/search/song/song-controller-get-songs
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.artlist.io/welcome
- group: operate
  title: ''
  type: Support
  url: https://help.artlist.io/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://artlist.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Artlist-LTD
- group: commercial
  title: ''
  type: Pricing
  url: https://artlist.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://artlist.io/start-now
- group: start
  title: ''
  type: Login
  url: https://artlist.io/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://artlist.io/help-center/privacy-terms/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://artlist.io/help-center/privacy-terms/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://help.artlist.io/hc/en-us/articles/29556821619101-Privacy-at-Artlist
- group: other
  title: ''
  type: Enterprise
  url: https://artlist.io/enterprise
- group: auth
  title: ''
  type: Authentication
  url: authentication/artlist-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/artlist-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/artlist-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/artlist-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/artlist-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/artlist-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/artlist-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/artlist-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/artlist-api-catalog.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/artlist-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/artlist-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/artlist-packages.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/artlist-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/artlist-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/artlist-tool-crosswalk.yml
created: '2026-08-02'
description: 'Artlist is a creative-assets platform for video creators, marketers and brands, licensing royalty-free music, sound effects, stock footage, video templates, LUTs and editing plugins alongside a generative AI toolkit. The Artlist Enterprise API, published at developer.artlist.io, opens the company''s music catalog to partner platforms: a Search API for songs, artists and albums with mood/genre/instrument category filters plus BPM, duration, vocal-type and free-text facets, and a Download API that mints signed MP3/WAV asset URLs for licensed assets. Access is OAuth 2.0 client-credentials against an Amazon Cognito authorization server with credentials issued by an account manager, and the developer portal publishes OpenAPI 3.1 definitions, an llms.txt index, an RFC 9727 /.well-known/api-catalog linkset and a hosted MCP server for documentation search.'
image: https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/artlist.docs.buildwithfern.com/55c8148c837879232b42a92524952487559fe4e81d1d81b61c162440bdbaf680/docs/assets/artlist-light.svg
layout: provider
mcp_servers:
- description: 'Artlist publishes a hosted, anonymous MCP server for its developer documentation. It is a docs-search server, not a wrapper over the Enterprise API itself: the single tool searches developer.artlist.i'
  name: Artlist MCP Server
  slug: artlist-mcp-server
modified: '2026-08-02'
name: Artlist
nav: Providers
network: true
overview: 'Artlist publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Album API, Artist API, Downloadable API, and 1 more. Tagged areas include Company, Music, Audio, Media, and Stock Media.


  Artlist''s developer surface includes documentation, API reference, developer console, getting-started guide, support, engineering blog, pricing, and 26 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 3
  name: Artlist Rate Limits
  slug: artlist-rate-limits
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 19
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 43.4
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 44.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/artlist/refs/heads/main/screenshots/artlist-2026-08-07T161743.png
security:
- kind: authentication
  name: Artlist Authentication
  slug: artlist-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Artlist Domain Security
  slug: artlist-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: artlist
tags:
- Company
- Music
- Audio
- Media
- Stock Media
- Content Licensing
- Creative Tools
- Search
- Generative AI
- Video
website: https://artlist.io/
---
