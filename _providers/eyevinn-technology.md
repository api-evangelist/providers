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
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: true
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 18.3
  scored_at: '2026-07-27'
api_count: 8
apis:
- description: The Eyevinn Open Source Cloud (OSC) REST API is the management plane for provisioning and operating service instances on the OSC platform. The API uses Personal Access Tokens (PATs) issued from app.os
  name: Eyevinn Open Source Cloud REST API
  slug: osc-rest-api
- description: Channel Engine is an open source JavaScript/TypeScript library for producing 24/7 HLS FAST (Free Ad-Supported Streaming Television) linear channels from already-transcoded HLS VOD assets using VOD2Liv
  name: Eyevinn Channel Engine
  slug: channel-engine
- description: Open source TypeScript implementations of the IETF WebRTC HTTP Ingestion Protocol (WHIP) and WebRTC HTTP Egress Protocol (WHEP). Used to ingest and distribute low-latency WebRTC media over standard HT
  name: Eyevinn WHIP and WHEP Modules
  slug: whip-whep
- description: EPAS is an open specification and SDK suite for collecting video player analytics in real time across web and native players. Eyevinn maintains the client SDK for web (`player-analytics-client-sdk-web
  name: Eyevinn Player Analytics Specification (EPAS)
  slug: player-analytics
- description: Open Intercom is a low-latency, web-based VoIP broadcast intercom system built on WebRTC. It is composed of `intercom-manager` (the server and management API) and `intercom-frontend` (the browser-base
  name: Eyevinn Open Intercom
  slug: intercom
- description: A Rust service that ingests SRT (Secure Reliable Transport) contribution feeds and re-publishes them as WebRTC playback streams via WHEP, enabling sub-second latency playback of SRT contributions in a
  name: Eyevinn SRT to WHEP Bridge
  slug: srt-whep
- description: Open source TypeScript framework for orchestrating media supply chain workflows — ingest, transcoding, packaging, QC, and distribution — across cloud-native components. Pairs with the Eyevinn Open Sou
  name: Eyevinn Media Supply Orchestrator
  slug: media-supply-orchestrator
- description: A suite of experimental tools tracking the IETF Media Over QUIC working group, including `moqlivemock` (a Go publisher simulator) and `warp-player` (a CMAF media player over MoQ transport).
  name: Eyevinn Media Over QUIC (MoQ) Tools
  slug: moq-tools
artifact_total: 44
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eyevinn-technology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eyevinn.se/
- group: company
  title: ''
  type: ProductWebsite
  url: https://www.osaas.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.osaas.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.osaas.io/osaas-api-docs/docs/index.html
- group: start
  title: ''
  type: Console
  url: https://app.osaas.io/
- group: start
  title: ''
  type: Console
  url: https://app.se.osaas.io/
- group: start
  title: ''
  type: Signup
  url: https://app.osaas.io/
- group: start
  title: ''
  type: Login
  url: https://app.osaas.io/
- group: other
  title: ''
  type: ServiceCatalog
  url: https://www.osaas.io/catalog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.osaas.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://app.osaas.io/status
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Eyevinn
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EyevinnOSC
- group: operate
  title: ''
  type: Slack
  url: https://slack.osaas.io
- group: operate
  title: ''
  type: CommunityForum
  url: https://github.com/EyevinnOSC/community/discussions
- group: company
  title: ''
  type: Blog
  url: https://eyevinntechnology.medium.com/
- group: company
  title: ''
  type: DeveloperBlog
  url: https://dev.to/video
- group: other
  title: ''
  type: Email
  url: mailto:osc@eyevinn.se
- group: operate
  title: ''
  type: ContactEmail
  url: mailto:info@eyevinn.se
- group: build
  title: ''
  type: SDKs
  url: https://github.com/EyevinnOSC/client-ts
- group: build
  title: ''
  type: SDKs
  url: https://github.com/EyevinnOSC/client-go
- group: build
  title: ''
  type: CLI
  url: https://www.npmjs.com/package/@osaas/cli
- group: other
  title: ''
  type: TerraformProvider
  url: https://github.com/EyevinnOSC/terraform-provider-osc
- group: build
  title: ''
  type: GitHubAction
  url: https://github.com/EyevinnOSC/action
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/EyevinnOSC/mcp-server
- group: build
  title: ''
  type: VSCodeExtension
  url: https://github.com/EyevinnOSC/vscode-chat-extension
- group: build
  title: ''
  type: Examples
  url: https://github.com/EyevinnOSC/solutions
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/EyevinnOSC/onboarding
created: '2026-05-25'
description: Eyevinn Technology is a Stockholm, Sweden based video streaming consultancy and open source company specializing in cloud-native video infrastructure, HLS and MPEG-DASH packaging, FAST channels, WebRTC ingest (WHIP/WHEP), server-side ad insertion (SSAI), broadcast intercom, and player analytics. The company operates one of the largest video-focused open source portfolios on GitHub (300+ repositories across the Eyevinn and EyevinnOSC orgs) and runs Eyevinn Open Source Cloud (OSC), a managed multi-tenant SaaS platform that packages 180+ open source projects (databases, media tools, developer tools, AI runtimes, productivity apps) into one-click deployments with a token-based consumption model, a Personal Access Token (PAT) authenticated REST API, and client SDKs for TypeScript, Go, and Terraform. Eyevinn shares OSC revenue with the maintainers of the open source projects hosted on the platform, positioning OSC as a "Builder Economy" distribution channel for open source rather
  than a vendor-lock-in PaaS.
features:
- description: Outcome-based video streaming engineering services delivered by Stockholm-based experts rather than billable hours.
  name: Builder Economy Consultancy
- description: Managed multi-tenant SaaS hosting 180+ unmodified open source services with one-click deployment and a token-based consumption model.
  name: Open Source Cloud (OSC)
- description: REST API authenticated via PAT JWTs from app.osaas.io that mint per-service Service Access Tokens for fine-grained authorization.
  name: Personal Access Token API
- description: First-party SDKs in TypeScript and Go, plus a Terraform provider and a GitHub Action for CI/CD integration.
  name: Polyglot Client SDKs
- description: OSC ships an MCP server so AI agents can browse the catalog and provision open source services on a developer's behalf.
  name: Model Context Protocol Server
- description: OSC shares platform revenue with the upstream open source authors whose projects are hosted on the cloud.
  name: Revenue Sharing With Maintainers
- description: VOD2Live engine producing 24/7 personalized HLS linear channels from an existing VOD library.
  name: FAST Channel Engine
- description: WHIP/WHEP modules, SRT-to-WHEP bridge, and the Open Intercom system cover the WebRTC ingest and distribution surface.
  name: WebRTC Contribution and Distribution
- description: Open EPAS event schema and SDKs for vendor-neutral video QoE analytics.
  name: Player Analytics Specification
- description: Reference publishers, players, and simulators tracking the IETF MoQ working group's evolving transport.
  name: Media Over QUIC Tooling
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eyevinn-technology.png
integrations:
- description: Official Terraform provider (terraform-provider-osc) lets users declare OSC service instances as infrastructure-as-code.
  name: Terraform
- description: Official GitHub Action provisions OSC service instances from CI pipelines.
  name: GitHub Actions
- description: MCP server exposes OSC catalog and provisioning tools to AI agents over the MCP standard.
  name: Model Context Protocol
- description: OSC Architect VS Code extension integrates OSC into Copilot Chat sessions.
  name: VS Code Copilot Chat
- description: FFmpeg is offered as a first-class managed service in the OSC catalog.
  name: FFmpeg
- description: Google's Shaka Packager is available as a managed OSC service for HLS/DASH packaging.
  name: Shaka Packager
- description: The Owncast self-hosted streaming server is a managed service in the OSC catalog.
  name: Owncast
- description: PostgreSQL is one of many managed database services on OSC.
  name: PostgreSQL
- description: Valkey (the open source Redis fork) and Redis-compatible engines are available as managed services and used by Channel Engine for HA.
  name: Redis / Valkey
- description: ClickHouse is offered as a managed OLAP database service on OSC.
  name: ClickHouse
- description: n8n workflow automation is available as a managed OSC service.
  name: n8n
- description: Grafana dashboards can be deployed on OSC in a single click.
  name: Grafana
- description: Self-hosted Git via Gitea is part of the OSC developer-tools catalog.
  name: Gitea
- description: Nextcloud is offered as a managed productivity service on OSC.
  name: Nextcloud
layout: provider
mcp_servers:
- description: ''
  name: mcp-server
  slug: mcp-server
modified: '2026-05-25'
name: Eyevinn Technology
nav: Providers
network: true
overview: 'Eyevinn Technology publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Ad Insertion, Broadcast Intercom, Channel Engine, CMAF, and DASH.


  Eyevinn Technology''s developer surface includes documentation, API reference, developer console, signup flow, pricing, GitHub presence, engineering blog, and 22 more developer resources.'
random_paper: 59
score:
  band: emerging
  composite: 27.5
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 56.5
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 27.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eyevinn-technology/refs/heads/main/screenshots/eyevinn-technology-2026-06-20T180953.png
security:
- kind: domain-security
  name: Eyevinn Technology Domain Security
  slug: eyevinn-technology-domain-security
  summary_line: TLSv1.3 · DMARC
slug: eyevinn-technology
solutions:
- description: Outcome-based consulting on cloud-native video infrastructure, packaging, ad insertion, and live production.
  name: Streaming Engineering Services
- description: Tiered token-based plans (Basic free, Personal EUR 15/mo, Professional EUR 69/mo) for self-service open source deployment.
  name: Open Source Cloud Subscription
- description: AI-powered companion product that turns plain-language prompts into deployed OSC-hosted applications.
  name: Liivo No-Code AI App Deployment
tags:
- Ad Insertion
- Broadcast Intercom
- Channel Engine
- CMAF
- DASH
- FAST Channels
- FFmpeg
- HLS
- Live Streaming
- Media Over QUIC
- Open Source
- Open Source Cloud
- OSC
- Player Analytics
- REST
- SRT
- SSAI
- Sweden
- Transcoding
- Video Infrastructure
- VOD2Live
- WebRTC
- WHEP
- WHIP
use_cases:
- description: Spin up 24/7 ad-supported linear channels from a VOD catalog using Channel Engine, either self-hosted or managed on OSC.
  name: Linear FAST Channel Production
- description: Use WHIP/WHEP and the SRT-to-WHEP bridge to deliver sub-second contribution and playback experiences.
  name: Low-Latency WebRTC Distribution
- description: Replace hardware intercom panels in live production with the Open Intercom WebRTC system.
  name: Browser-Based Broadcast Intercom
- description: Use OSC to provision PostgreSQL, ClickHouse, Owncast, Gitea, n8n, Grafana, and dozens of other open source services without DevOps.
  name: Managed Open Source PaaS
- description: Expose OSC to Claude, Copilot, and other LLM agents via the MCP server and VS Code Chat extension.
  name: AI Agent Driven DevOps
- description: Adopt EPAS to ship player QoE telemetry to a self-controlled sink rather than a closed analytics vendor.
  name: Vendor-Neutral Player Analytics
- description: Compose ingest, transcode, package, and distribute steps with the Media Supply Orchestrator framework.
  name: Media Supply Chain Orchestration
website: https://www.eyevinn.se/
---
