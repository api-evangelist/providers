---
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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 49.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Artlist Agentic Access
  operation_count: 5
  slug: artlist-agentic-access
  summary_line: 5 operations
api_count: 3
apis:
- description: Search and retrieve the Artlist music catalog — songs (with mood, genre, instrument and video-theme category filters, BPM, duration, vocal type and free-text query), artists and albums. Returns AAC st
  name: Artlist Enterprise Search API
  slug: search
- description: Mint a downloadable URL for a licensed Artlist asset. Takes the asset type (currently song), the asset id (numeric or UUID) and the desired format (mp3 or wave), and returns the URL of the downloadabl
  name: Artlist Enterprise Download API
  slug: download
- description: Hosted Model Context Protocol server for the Artlist Enterprise API documentation. Exposes a single anonymous read-only tool, searchDocs, that searches developer.artlist.io and returns documentation p
  name: Artlist Developer Docs MCP Server
  slug: docs-mcp
artifact_total: 8
common:
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
- description: ''
  name: artlist-mcp.yml
  slug: artlist-mcpyml
modified: '2026-08-02'
name: Artlist
nav: Providers
network: true
overview: 'Artlist publishes 2 APIs on the [APIs.io](https://apis.io/) network: Enterprise Search API and Enterprise Download API. Tagged areas include Company, Music, Audio, Media, and Stock Media.


  Artlist''s developer surface includes documentation, API reference, developer console, getting-started guide, support, engineering blog, pricing, and 25 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 3
  name: Artlist Rate Limits
  slug: artlist-rate-limits
score:
  band: developing
  composite: 53.1
  facets:
    commercial_clarity: 52.6
    contract_quality: 48.8
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 36.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
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
