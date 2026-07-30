---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/conifer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://conifer.build
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ConiferKit
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ConiferKit/sage
- group: other
  title: ''
  type: Download
  url: https://github.com/ConiferKit/sage/releases/latest
- group: other
  title: ''
  type: X
  url: https://x.com/coniferbuild
- group: build
  title: ''
  type: Packages
  url: packages/conifer-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/conifer-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/conifer-llms.txt
created: '2026-07-17'
description: Conifer (YC S26) builds Sage, a local-first AI runtime and workspace that runs models entirely on your own machine. Its inference engine is written from scratch in Rust, reaching up to 60% faster decode than llama.cpp on Apple Silicon, and pairs an editor, integrated terminal, file viewers, and an agent runtime inside a kernel-level sandbox so tool calls only touch what you allow. Conifer routes each request to the cheapest capable model, starting with free on-device inference and falling back to cloud only when needed, cutting AI spend by up to 80%. The desktop app ships as Juniper for macOS, Windows, and Linux with no accounts, no telemetry, and no cloud dependency. Conifer is proprietary and distributed as compiled binaries; it currently exposes no public web API.
image: https://raw.githubusercontent.com/ConiferKit/sage/main/assets/sage-banner-light.png
layout: provider
modified: '2026-07-18'
name: Conifer
nav: Providers
network: true
overview: 'Conifer is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Local AI, Inference, and Large Language Models.


  Conifer''s developer surface includes changelog and 8 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 8.5
  delta: -1.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 9.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/conifer/refs/heads/main/screenshots/conifer-2026-07-25T210259.png
security:
- kind: domain-security
  name: Conifer Domain Security
  slug: conifer-domain-security
  summary_line: TLSv1.3 · DMARC
slug: conifer
tags:
- Company
- Artificial Intelligence
- Local AI
- Inference
- Large Language Models
- Developer Tools
- Model Routing
- Desktop Application
- Privacy
- Rust
website: https://conifer.build
---
