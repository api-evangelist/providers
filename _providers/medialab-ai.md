---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.1
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: 'The Genius API exposes the music knowledge community behind genius.com: annotations (crowd-sourced explanations attached to a fragment of a document), referents (the fragments annotations attach to), '
  name: Genius API
  slug: genius-api
- description: 'The Imgur API (version 3) exposes the Imgur image-sharing and community platform over a RESTful HTTPS interface: image upload and retrieval, albums, the public gallery and its tags, comments, and acco'
  name: Imgur API
  slug: imgur-api
artifact_total: 9
collections:
- collection_type: postman
  name: Imgur API
  slug: postman-medialab-ai-imgur-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/medialab-ai-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medialab-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://medialab.la/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/medialab-ai_stock/
- group: other
  title: ''
  type: Brands
  url: https://medialab.la/brands
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.imgur.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.genius.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.imgur.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.genius.com/#getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.imgur.com/hc/en-us
- group: commercial
  title: ''
  type: Pricing
  url: https://rapidapi.com/imgur/api/imgur-9/pricing
- group: start
  title: ''
  type: SignUp
  url: https://api.imgur.com/oauth2/addclient
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/medialab-ai
- group: company
  title: ''
  type: Careers
  url: https://medialab.la/careers
- group: operate
  title: ''
  type: Contact
  url: https://medialab.la/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://medialab.la/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://medialab.la/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/medialab-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/medialab-ai-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/medialab-ai-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/medialab-ai-genius-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/medialab-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://bugcrowd.com/engagements/Genius-VDP
- group: auth
  title: ''
  type: Authentication
  url: authentication/medialab-ai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/medialab-ai-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/medialab-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/medialab-ai-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/medialab-ai-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/medialab-ai-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.imgur.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/medialab-ai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/medialab-ai-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/medialab-ai-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/medialab-ai-components.yml
- group: build
  title: ''
  type: Examples
  url: examples/medialab-ai-imgur-examples.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/medialab-ai-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Postman
  url: postman/medialab-ai-imgur-api.postman_collection.json
created: '2026-08-01'
description: MediaLab.AI Inc. is a Santa Monica, California holding company for consumer internet brands. Rather than building products from scratch, MediaLab acquires and operates established community and media properties, and monetizes them through advertising across an owned-and-operated portfolio that reaches roughly one in three US internet users each month. The portfolio includes Genius (music knowledge, lyrics and annotations), Imgur (image sharing and community), Kik (messaging), WorldStarHipHop (hip hop media), Whisper (anonymous sharing), Amino (interest communities) and DatPiff (mixtapes). MediaLab also operates Assembly Exchange, its owned-and-operated programmatic ad exchange. The company itself publishes no corporate developer portal; its public API surface is carried by two portfolio brands - the Genius API (docs.genius.com, OAuth 2.0, annotations/songs/artists/search) and the Imgur API v3 (apidocs.imgur.com, OAuth 2.0, images/albums/galleries/comments/accounts), the latter
  documented as a public Postman collection.
image: https://cdn.prod.website-files.com/6434b7d63112666081bedeb0/643591619f8e24bf570e827e_medialab-webclip.jpg
layout: provider
mcp_servers:
- description: ''
  name: MediaLab.AI MCP Server
  slug: medialabai-mcp-server
modified: '2026-08-01'
name: MediaLab.AI
nav: Providers
network: true
overview: 'MediaLab.AI publishes 1 API on the [APIs.io](https://apis.io/) network: Imgur API. Tagged areas include Company, Media, Social, Advertising, and Content.


  MediaLab.AI''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 31 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 3
  name: Medialab Ai Rate Limits
  slug: medialab-ai-rate-limits
scopes:
- name: Medialab Ai Scopes
  scope_count: 4
  slug: medialab-ai-scopes
  summary_line: 4 scopes · authorizationCode/implicit
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 18
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 6.7
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 68.4
  previous_composite: 38.9
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/medialab-ai/refs/heads/main/screenshots/medialab-ai-2026-08-07T172332.png
security:
- kind: authentication
  name: Medialab Ai Authentication
  slug: medialab-ai-authentication
  summary_line: oauth2/http · 4 schemes
- kind: domain-security
  name: Medialab Ai Domain Security
  slug: medialab-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Medialab Ai Vulnerability Disclosure
  slug: medialab-ai-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: medialab-ai
tags:
- Company
- Media
- Social
- Advertising
- Content
- Image
- Music
- Messaging
- Communities
- Holding Company
website: https://medialab.la/
---
