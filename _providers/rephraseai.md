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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: OAuth2 text-to-video generation API — list supported actors and voices, create and export videos of speaking digital avatars, and poll video status. Legacy surface; company acquired by Adobe (Nov 2023
  name: Rephrase Studio API
  slug: rephrase-studio-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://rephrase.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://studio-rephrase-api.readme.io/reference/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://studio-rephrase-api.readme.io/reference/documentation
- group: auth
  title: ''
  type: Authentication
  url: authentication/rephraseai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/rephraseai-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rephraseai-conventions.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rephraseai-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rephraseai-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rephraseai-llms.txt
created: '2026-07-17'
description: Rephrase.ai is a Bengaluru-based generative-AI startup whose text-to-video platform, Rephrase Studio, turns plain text scripts into videos of digital human avatars ("actors") that speak the script with lip-synced, natural voices. It exposed a Rephrase Studio API for programmatic video generation (list actors and voices, create and export videos, poll video status) secured with OAuth2 bearer tokens. Backed by Techstars, Rephrase.ai was acquired by Adobe in November 2023 and its technology folded into Adobe's video and generative-AI offerings; the standalone product hosts have since been decommissioned, though the legacy API reference remains hosted on ReadMe. This profile is maintained by API Evangelist for historical and enrichment purposes.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rephraseai.png
layout: provider
mcp_servers:
- description: ''
  name: rephraseai-mcp.yml
  slug: rephraseai-mcpyml
modified: '2026-07-20'
name: Rephrase.ai
nav: Providers
network: true
overview: 'Rephrase.ai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Generative AI, Video, and Text to Video.


  Rephrase.ai''s developer surface includes documentation, API reference, authentication, and 6 more developer resources.'
random_paper: 59
scopes:
- name: Rephraseai Scopes
  scope_count: 1
  slug: rephraseai-scopes
  summary_line: 1 scope
score:
  band: emerging
  composite: 14.4
  delta: -1.8
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.3
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.2
  provenance:
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Rephraseai Authentication
  slug: rephraseai-authentication
  summary_line: oauth2 · 1 scheme
slug: rephraseai
tags:
- Company
- Artificial Intelligence
- Generative AI
- Video
- Text to Video
- Avatars
- Media
- Content Creation
website: https://rephrase.ai/
---
