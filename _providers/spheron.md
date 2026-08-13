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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: REST API for programmatically managing GPU deployments across the Spheron marketplace. Covers provider and GPU-offer discovery, deployment lifecycle (create, list, get, rename, terminate, can-terminat
  name: Spheron GPU Cloud API
  slug: spheron-gpu-cloud-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spheron-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.spheron.network
- group: other
  title: ''
  type: Marketplace
  url: https://www.spheron.network
- group: commercial
  title: ''
  type: Pricing
  url: https://www.spheron.network/pricing
- group: other
  title: ''
  type: GPUs
  url: https://www.spheron.network/gpus
- group: start
  title: ''
  type: Console
  url: https://app.spheron.ai
- group: start
  title: ''
  type: Signup
  url: https://app.spheron.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spheron.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.spheron.ai/api-reference
- group: other
  title: ''
  type: Protocol
  url: https://docs.spheron.network
- group: docs
  title: ''
  type: ProtocolDocumentation
  url: https://docs.spheron.network/overview
- group: company
  title: ''
  type: Blog
  url: https://blog.spheron.network
- group: build
  title: ''
  type: GitHub
  url: https://github.com/spheron-core
- group: build
  title: ''
  type: LegacyGitHub
  url: https://github.com/spheronFdn
- group: build
  title: ''
  type: SDKs
  url: https://github.com/spheron-core/protocol-sdk
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/spheron-core/spheron-mcp-plugin
- group: other
  title: ''
  type: SkyPilot
  url: https://github.com/spheron-core/skypilot
- group: other
  title: ''
  type: HelmCharts
  url: https://github.com/spheron-core/spheron-stack
- group: other
  title: ''
  type: ProviderInstallation
  url: https://github.com/spheron-core/provider-installation
- group: other
  title: ''
  type: Templates
  url: https://github.com/spheron-core/awesome-spheron
- group: other
  title: ''
  type: ICLGenie
  url: https://github.com/spheron-core/icl-genie-api
- group: other
  title: ''
  type: Foundation
  url: https://github.com/spheron-core/.github
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/SpheronFDN
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spheron
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@SpheronFdn
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/spheron
- group: other
  title: ''
  type: Telegram
  url: https://t.me/SpheronFdn
created: '2026-05-25'
description: Spheron Network is a decentralized GPU and cloud compute marketplace that aggregates enterprise-grade NVIDIA GPU capacity from certified Tier 3/4 data centers worldwide and exposes it through a single on-demand, per-minute billed interface. The marketplace covers H100, H200, B200, B300, A100, GH200, L40S, RTX PRO 6000, RTX 5090, RTX 4090, and pre-order GB200/GB300/ R100 inventory, priced 40-60% below hyperscaler rates with spot, reserved, and custom-cluster (8-512+ GPU) options. Teams access the platform through a web dashboard, a documented REST API at app.spheron.ai/api, a TypeScript Protocol SDK, an MCP plugin for Claude, SkyPilot integration, and Helm charts for self-hosted provider nodes. The Spheron Foundation also maintains an open compute protocol with Fizz nodes, provider nodes, ICL YAML configuration, and an on-chain payment system supporting both traditional payment rails and USDC/USDT stablecoin settlement. The company is transitioning from a pure decentralized protocol
  model toward an enterprise GPU procurement and aggregation marketplace while keeping the underlying provider network open and community-operated.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spheron.png
layout: provider
modified: '2026-05-25'
name: Spheron
nav: Providers
network: true
overview: 'Spheron publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Compute, GPU, GPU Cloud, Decentralized Compute, and AI Infrastructure.


  Spheron''s developer surface includes pricing, developer console, signup flow, documentation, API reference, engineering blog, GitHub presence, and 20 more developer resources.'
random_paper: 47
score:
  band: emerging
  composite: 17.8
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 17.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spheron/refs/heads/main/screenshots/spheron-2026-06-20T194308.png
security:
- kind: domain-security
  name: Spheron Domain Security
  slug: spheron-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spheron
tags:
- Compute
- GPU
- GPU Cloud
- Decentralized Compute
- AI Infrastructure
- NVIDIA
- H100
- B200
- Kubernetes
- Bare Metal
- Marketplace
- DePIN
- Web3
- Stablecoin Payments
- MCP
website: https://www.spheron.network
---
