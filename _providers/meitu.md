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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: Web API (OpenAPI) exposing 100+ Meitu AI vision capabilities — image generation/editing, portrait beautification, face/body analysis, cutout, virtual try-on, and image/text-to-video — via an async sub
  name: Meitu AI Open Platform
  slug: meitu-ai-open-platform
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://meitu.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ai.meitu.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ai.meitu.com/doc/?id=92&type=api
- group: docs
  title: ''
  type: APIReference
  url: https://api.meitu.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/meitu
- group: build
  title: ''
  type: Packages
  url: packages/meitu-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/meitu-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/meitu-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/meitu-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/meitu-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/meitu-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/meitu-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/meitu-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meitu-domain-security.yml
created: '2026-07-17'
description: Meitu (美图) is a Chinese visual-technology company best known for its photo- and video-editing apps (Meitu, BeautyCam, Meitu Xiuxiu). It operates the Meitu AI Open Platform, which exposes 100+ image and video AI capabilities as a Web API (OpenAPI) plus native/mobile SDKs — image generation and editing, portrait beautification, face and body analysis, cutout and segmentation, virtual try-on, and image/text-to-video. Access uses a per-application access key and secret key signature; an official Node.js CLI (meitu-cli) wraps the OpenAPI. Surfaced as a portfolio company of Qiming and enriched by the API Evangelist pipeline.
image: https://ai.meitu.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: meitu-mcp.yml
  slug: meitu-mcpyml
modified: '2026-07-20'
name: Meitu
nav: Providers
network: true
overview: 'Meitu publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Image Processing, Computer Vision, and Video.


  Meitu''s developer surface includes documentation, API reference, CLI, authentication, and 10 more developer resources.'
random_paper: 101
score:
  band: emerging
  composite: 18.3
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 18.3
  provenance:
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/meitu/refs/heads/main/screenshots/meitu-2026-08-07T172444.png
security:
- kind: authentication
  name: Meitu Authentication
  slug: meitu-authentication
  summary_line: apiKey/custom-signature · 2 schemes
- kind: domain-security
  name: Meitu Domain Security
  slug: meitu-domain-security
  summary_line: TLSv1.3 · DMARC
slug: meitu
tags:
- Company
- Artificial Intelligence
- Image Processing
- Computer Vision
- Video
- Generative AI
- Photo Editing
website: https://meitu.com
---
