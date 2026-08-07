---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Limitless Ai Agentic Access
  operation_count: 8
  slug: limitless-ai-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 7
apis:
- description: Wearable AI pendant that captures ambient audio, transcribes it, and stores it as Lifelogs in the user's Limitless account.
  name: Limitless Pendant
  slug: pendant
- description: Software assistant for meetings — transcripts, summaries, and Ask AI chat over personal memory. Available across desktop and mobile.
  name: Limitless Meeting Assistant
  slug: meeting-assistant
- description: Hosted Model Context Protocol endpoint that connects Claude and other MCP-compatible clients to the user's Limitless memory.
  name: Limitless MCP Server
  slug: mcp-server
- description: The Chats API from Limitless — 2 operation(s) for chats.
  name: Limitless Chats API
  slug: limitless-ai-chats-api
- description: The Download Audio API from Limitless — 1 operation(s) for download audio.
  name: Limitless Download Audio API
  slug: limitless-ai-download-audio-api
- description: The Lifelogs API from Limitless — 2 operation(s) for lifelogs.
  name: Limitless Lifelogs API
  slug: limitless-ai-lifelogs-api
- description: The Limitless Developer API API from Limitless — 1 operation(s) for limitless developer api.
  name: Limitless Limitless Developer API API
  slug: limitless-ai-limitless-developer-api-api
artifact_total: 13
collections:
- collection_type: open
  name: Limitless Developer API
  slug: open-limitless-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/limitless-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/limitless-ai-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/limitless-ai
- group: company
  title: ''
  type: Website
  url: https://www.limitless.ai/
- group: other
  title: ''
  type: Developers
  url: https://www.limitless.ai/developers
- group: build
  title: ''
  type: GitHub
  url: https://github.com/limitless-ai-inc
- group: docs
  title: ''
  type: OpenAPI
  url: https://api.limitless.ai/v1/openapi.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/limitless-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/limitless-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/limitless-ai-finops.yml
created: '2026-05-23'
description: Limitless is a personalized AI for meetings with a software assistant and the Limitless Pendant wearable that captures conversations as Lifelogs. The Limitless Developer API gives users programmatic access to their own Lifelogs, Ask AI chat history, and audio downloads, with an MCP endpoint that lets Claude and other MCP-compatible tools query Limitless memory directly. The OpenAPI spec is published and example code is hosted on GitHub.
finops:
- name: Limitless Ai Finops
  service_category: API
  slug: limitless-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/limitless-ai.png
layout: provider
modified: '2026-05-23'
name: Limitless
nav: Providers
network: true
overview: 'Limitless publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Chats API, Download Audio API, Lifelogs API, and 1 more. Tagged areas include AI, Wearable, Pendant, Meeting Notes, and Lifelogs.


  Limitless'' developer surface includes GitHub presence and 9 more developer resources.'
plans:
- name: Limitless Ai Plans Pricing
  plan_count: 1
  slug: limitless-ai-plans-pricing
random_paper: 99
rate_limits:
- limit_count: 2
  name: Limitless Ai Rate Limits
  slug: limitless-ai-rate-limits
score:
  band: thin
  composite: 28.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 47.1
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 28.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/limitless-ai/refs/heads/main/screenshots/limitless-ai-2026-06-20T184530.png
security:
- kind: domain-security
  name: Limitless Ai Domain Security
  slug: limitless-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: limitless-ai
tags:
- AI
- Wearable
- Pendant
- Meeting Notes
- Lifelogs
- Personal AI
- API
- MCP
- OpenAPI
website: https://www.limitless.ai/
---
