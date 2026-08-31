---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Ludo Ai Agentic Access
  operation_count: 20
  slug: ludo-ai-agentic-access
  summary_line: 20 operations · 14 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The Ludo.ai MCP Server exposes the platform's asset generation tools via the Model Context Protocol, allowing AI assistants like Claude and Cursor to generate game assets through natural language conv
  name: Ludo.ai MCP Server
  slug: mcp-server
- description: 'The Ludo.ai Unity Plugin integrates AI-powered asset generation directly into the Unity game engine. It provides a native interface for Unity developers to access Ludo.ai''s image generation, 3D model '
  name: Ludo.ai Unity Plugin
  slug: unity-plugin
- description: Convert 2D images into textured 3D GLB models with PBR textures and configurable quality settings.
  name: Ludo.ai 3D Models API
  slug: ludo-ai-3d-models-api
- description: Create animated spritesheets from static sprites, transfer motion from videos or presets, and list available animation presets.
  name: Ludo.ai Animation API
  slug: ludo-ai-animation-api
- description: Generate sound effects, background music, character voices, and text-to-speech audio for games.
  name: Ludo.ai Audio API
  slug: ludo-ai-audio-api
- description: Generate, edit, and manipulate game-ready images including sprites, icons, UI assets, textures, and backgrounds.
  name: Ludo.ai Images API
  slug: ludo-ai-images-api
- description: Retrieve previously generated assets using request IDs or browse recent API-generated content.
  name: Ludo.ai Results API
  slug: ludo-ai-results-api
- description: Generate short videos from images with motion prompts, suitable for cinematics, trailers, and dynamic backgrounds.
  name: Ludo.ai Video API
  slug: ludo-ai-video-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ludo.ai REST 3D Models API
  slug: open-ludo-ai-3d-models-api
- collection_type: open
  name: Ludo.ai REST 3D Models Animation API
  slug: open-ludo-ai-animation-api
- collection_type: open
  name: Ludo.ai REST 3D Models Audio API
  slug: open-ludo-ai-audio-api
- collection_type: open
  name: Ludo.ai REST 3D Models Images API
  slug: open-ludo-ai-images-api
- collection_type: open
  name: Ludo.ai REST API
  slug: open-ludo-ai-rest-api
- collection_type: open
  name: Ludo.ai REST 3D Models Results API
  slug: open-ludo-ai-results-api
- collection_type: open
  name: Ludo.ai REST 3D Models Video API
  slug: open-ludo-ai-video-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ludo-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ludo-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ludo-ai-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ludoai
- group: design
  title: ''
  type: JSONLD
  url: json-ld/ludo-ai-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/ludo-ai-game-asset-schema.json
- group: company
  title: ''
  type: Website
  url: https://ludo.ai/
- group: start
  title: ''
  type: Portal
  url: https://ludo.ai/api-mcp-integration
- group: docs
  title: ''
  type: Documentation
  url: https://ludo.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://ludo.ai/blog/introducing-ludo-ai-api-mcp-integration
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ludo-AI
- group: start
  title: ''
  type: Login
  url: https://ludo.ai/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Ludo-AI/ludo-mcp
created: '2026-03-24'
description: Ludo.ai is a game design hub that uses artificial intelligence to help developers generate production-ready game assets including images, 3D models, audio, and animations. The platform entered beta for its Model Context Protocol (MCP) integration, exposing its asset generation suite as a headless API that enables vibe coding where developers can trigger asset creation directly from AI assistants like Claude or Cursor.
finops:
- name: Ludo Ai Finops
  service_category: AI Infrastructure
  slug: ludo-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ludo-ai.png
json_schemas:
- name: Ludo.ai Game Asset
  property_count: 10
  slug: ludo-ai-game-asset
jsonld:
- class_count: 0
  name: Ludo Ai Context
  property_count: 7
  slug: ludo-ai-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Ludo.ai
nav: Providers
network: true
overview: 'Ludo.ai publishes 6 APIs on the [APIs.io](https://apis.io/) network, including 3D Models API, Animation API, Audio API, and 3 more. Tagged areas include Artificial Intelligence, Asset Generation, Game Design, and Game Development.


  The Ludo.ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ludo.ai''s developer surface includes authentication, developer portal, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Ludo Ai Plans Pricing
  plan_count: 4
  slug: ludo-ai-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 7
  name: Ludo Ai Rate Limits
  slug: ludo-ai-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Ludo.ai API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: ludo-ai-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 13
    catalog_gap: 65.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 9.8
    contract_quality: 61.9
    developer_ergonomics: 33.3
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/screenshots/ludo-ai-2026-06-20T184746.png
security:
- kind: authentication
  name: Ludo Ai Authentication
  slug: ludo-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ludo Ai Domain Security
  slug: ludo-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ludo-ai
tags:
- Artificial Intelligence
- Asset Generation
- Game Design
- Game Development
website: https://ludo.ai/
---
