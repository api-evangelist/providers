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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Mux Agentic Access
  operation_count: 12
  slug: mux-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 4
apis:
- description: Manage video on-demand assets.
  name: Mux Assets API
  slug: mux-assets-api
- description: Create direct upload URLs and inspect upload status.
  name: Mux Direct Uploads API
  slug: mux-direct-uploads-api
- description: Create and manage live streams.
  name: Mux Live Streams API
  slug: mux-live-streams-api
- description: Manage playback IDs for assets.
  name: Mux Playback IDs API
  slug: mux-playback-ids-api
artifact_total: 11
collections:
- collection_type: open
  name: Mux Video API
  slug: open-mux
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mux-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mux-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mux-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mux-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mux-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mux
- group: company
  title: ''
  type: Website
  url: https://www.mux.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.mux.com/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/muxinc
- group: docs
  title: ''
  type: OpenAPI
  url: https://www.mux.com/api-spec.json
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mux.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://dashboard.mux.com/signup
- group: company
  title: ''
  type: Blog
  url: https://www.mux.com/blog/rss.xml
created: '2026-05-11'
description: 'Mux is an API-first video platform that provides developer tools for video streaming, on-demand video, live streaming, real-time video, and video analytics, used to ingest, transcode, store, deliver, and measure video inside applications without managing video infrastructure. The Mux platform is delivered through two product families: Mux Video (ingest, asset management, live streams, playback IDs, signed URLs, and Mux Player) and Mux Data (QoE analytics for any HTML5 video player). All Mux REST APIs are served from https://api.mux.com, authenticated via HTTP Basic auth using a Mux Access Token ID and Secret, and fully described by an OpenAPI specification.'
graphqls:
- description: Mux does not currently offer a public GraphQL API. All Mux Video and Mux Data operations are available exclusively through the Mux REST API, served from `https://api.mux.com` and authenticated via HTT
  name: Mux GraphQL
  slug: mux-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mux.png
layout: provider
modified: '2026-05-11'
name: Mux
nav: Providers
network: true
overview: 'Mux publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Direct Uploads API, Live Streams API, and 1 more. Tagged areas include Video, Streaming, Live Streaming, Video Analytics, and QoE.


  Mux''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 8 more developer resources.'
random_paper: 38
score:
  band: thin
  composite: 29.6
  delta: -1.1
  facets:
    commercial_clarity: 18.4
    contract_quality: 54.0
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 30.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mux/refs/heads/main/screenshots/mux-2026-06-20T185912.png
security:
- kind: authentication
  name: Mux Authentication
  slug: mux-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mux Domain Security
  slug: mux-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mux Vulnerability Disclosure
  slug: mux-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Mux Trust Center
  slug: mux-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: mux
tags:
- Video
- Streaming
- Live Streaming
- Video Analytics
- QoE
- Video On Demand
- Transcoding
- Mux Player
website: https://www.mux.com
---
