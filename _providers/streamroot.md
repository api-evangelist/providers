---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/streamroot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://streamroot.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/streamroot
- group: build
  title: ''
  type: Packages
  url: packages/streamroot-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/streamroot-packages.yml
created: '2026-07-17'
description: Streamroot was a Paris-founded video-delivery company (backed by Partech and Techstars) that built a peer-to-peer / multi-CDN "Mesh Delivery" and DNA SDK to offload live and on-demand video traffic onto a hybrid CDN+WebRTC peer mesh, reducing bandwidth cost and improving scale for broadcasters and OTT platforms. The developer surface was a client-side (browser and native player) delivery SDK distributed as video-player plugins (video.js, Clappr, hls.js, AVPlayer) rather than a server-side REST API. Streamroot was acquired by CenturyLink — now Lumen Technologies — in 2019 and folded into Lumen's CDN / Mesh Delivery product line. The standalone streamroot.io website and developer docs are offline; the surviving public assets are the (now Lumen-operated) GitHub organization and a set of official but deprecated npm player-plugin packages.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/streamroot.png
layout: provider
modified: '2026-07-21'
name: Streamroot
nav: Providers
network: true
overview: Streamroot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure Saas, Video, Streaming, and CDN.
random_paper: 12
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 6.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Streamroot Domain Security
  slug: streamroot-domain-security
  summary_line: DNSSEC
slug: streamroot
tags:
- Company
- Infrastructure Saas
- Video
- Streaming
- CDN
- Peer-to-Peer
- WebRTC
- Media Delivery
- SDK
- Acquired
website: https://streamroot.io/
---
