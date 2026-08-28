---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: 'Speechly''s gRPC API surface: Identity (access tokens), SLU (streaming spoken language understanding), WLU (written language understanding), Batch audio processing, Config/Model management, Analytics, '
  name: Speechly API
  slug: speechly-api
artifact_total: 4
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/speechly/api/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: http://speechly.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/speechly
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/speechly/api
- group: build
  title: ''
  type: Packages
  url: packages/speechly-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/speechly-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/speechly-cli.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/speechly-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/speechly-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/speechly-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/speechly-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/speechly-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/speechly-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/speechly-data-model.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/speechly-conventions.yml
created: '2026-07-17'
description: Speechly was a real-time spoken language understanding (SLU) and streaming speech recognition platform from a Finnish startup, offering low-latency voice transcription, intent/entity parsing, written language understanding (WLU), batch audio processing, and audio/text moderation through a gRPC API with browser, React, iOS, Unity/.NET, Python and Go client SDKs and a command-line interface. Speechly was acquired by Roblox; the standalone product and hosted API have since been discontinued — speechly.com now redirects to roblox.com, the api.speechly.com and docs.speechly.com hosts no longer resolve, and the github.com/speechly organization was archived on 2025-01-07. Its open-source client SDKs and protobuf/gRPC API definitions remain publicly available and are cataloged here by the API Evangelist enrichment pipeline.
image: https://avatars.githubusercontent.com/u/25465412?v=4
layout: provider
mcp_servers:
- description: ''
  name: Speechly MCP Server
  slug: speechly-mcp-server
modified: '2026-07-21'
name: Speechly
nav: Providers
network: true
overview: 'Speechly publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Speech Recognition, Voice, Spoken Language Understanding, and Speech-to-Text.


  Speechly''s developer surface includes CLI, authentication, and 14 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 19.6
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 26.7
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 19.6
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Speechly Authentication
  slug: speechly-authentication
  summary_line: oauth2-like/bearer · 1 scheme
- kind: domain-security
  name: Speechly Domain Security
  slug: speechly-domain-security
  summary_line: TLSv1.3 · DMARC
slug: speechly
tags:
- Company
- Speech Recognition
- Voice
- Spoken Language Understanding
- Speech-to-Text
- Content Moderation
- Machine-Learning
- gRPC
- Artificial Intelligence
website: http://speechly.com
---
