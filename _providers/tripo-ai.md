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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 9
apis:
- description: 'Unified task API for all Tripo generative 3D operations. A single POST creates an asynchronous task keyed by task_type (text_to_model, image_to_model, multiview_to_model, texture_model, refine_model, '
  name: Tripo OpenAPI Task API
  slug: openapi-task
- description: Upload endpoint for source assets (reference images, multi-view image sets, base meshes) consumed by downstream tasks. Returns a handle that is passed into subsequent task creation calls.
  name: Tripo OpenAPI Upload API
  slug: openapi-upload
- description: Returns the calling API key's remaining credit balance and any frozen credits held against in-flight tasks. Used by client integrations to surface usage and gate expensive operations.
  name: Tripo OpenAPI User Balance API
  slug: openapi-balance
- description: Server-to-server webhook delivery of task lifecycle events. Customers register a callback URL and receive notifications when a Tripo task transitions to a terminal state, removing the need to poll tas
  name: Tripo Webhook
  slug: webhook
- description: Official Python SDK wrapping the Tripo OpenAPI. Provides synchronous and asynchronous clients, typed task helpers, balance retrieval, and file-upload utilities. Auth via TRIPO_API_KEY environment vari
  name: Tripo Python SDK
  slug: python-sdk
- description: Official Model Context Protocol server that exposes Tripo generation tasks as MCP tools, allowing MCP-aware AI clients (Claude Desktop, IDEs, agents) to invoke text-to-3D, image-to-3D, and related wor
  name: Tripo MCP Server
  slug: mcp-server
- description: Official Blender extension that wraps the Tripo API so Blender users can generate, texture, refine, and import 3D models directly into a Blender scene from inside the editor.
  name: Tripo Blender Plugin
  slug: blender-plugin
- description: Official ComfyUI custom node pack that exposes Tripo task types as composable nodes inside ComfyUI graphs for AI-driven 3D pipelines.
  name: Tripo ComfyUI Custom Nodes
  slug: comfyui-nodes
- description: Open-source single-image 3D reconstruction model released by VAST AI Research in collaboration with Stability AI. Distributed as model weights and inference code; complementary to the hosted Tripo API
  name: TripoSR (Open Source)
  slug: triposr
artifact_total: 13
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/VAST-AI-Research/tripo-python-sdk/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/VAST-AI-Research/tripo-python-sdk/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/VAST-AI-Research/tripo-python-sdk/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tripo-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tripo3d.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://platform.tripo3d.ai/docs
- group: other
  title: ''
  type: Developer
  url: https://www.tripo3d.ai/api
- group: start
  title: ''
  type: Signup
  url: https://platform.tripo3d.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tripo3d.ai/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/VAST-AI-Research
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/tripoai
- group: company
  title: ''
  type: Blog
  url: https://www.tripo3d.ai/blog
created: '2026-05-23'
description: Tripo AI (VAST AI Research) is an AI 3D content platform that converts text, images, and multi-view photographs into production-ready 3D assets. The platform exposes a REST API at api.tripo3d.ai that orchestrates a unified "task" abstraction across text-to-3D, image-to-3D, multi-view-to-3D, AI texturing, mesh segmentation, model refinement, stylization, format conversion, automatic rigging, retargeting, and one-shot animation. An official Python SDK, an MCP server, and engine plugins for Blender, Unity, Unreal Engine, ComfyUI, Cocos, and Godot wrap the API for creative and game pipelines. Open-source research artifacts (TripoSR, TripoSG, UniRig) ship separately on GitHub under the VAST-AI-Research organization.
finops:
- name: Tripo Ai Finops
  service_category: API
  slug: tripo-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tripo-ai.png
layout: provider
modified: '2026-05-23'
name: Tripo AI
nav: Providers
network: true
overview: 'Tripo AI publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include 3D, Generative AI, 3D Modeling, Text-to-3D, and Image-to-3D.


  Tripo AI''s developer surface includes documentation, signup flow, pricing, GitHub presence, engineering blog, and 7 more developer resources.'
plans:
- name: Tripo Ai Plans Pricing
  plan_count: 1
  slug: tripo-ai-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Tripo Ai Rate Limits
  slug: tripo-ai-rate-limits
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 7
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  open_source:
    applies: true
    score: 25.0
  previous_composite: 24.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tripo-ai/refs/heads/main/screenshots/tripo-ai-2026-06-20T195733.png
security:
- kind: domain-security
  name: Tripo Ai Domain Security
  slug: tripo-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tripo-ai
tags:
- 3D
- Generative AI
- 3D Modeling
- Text-to-3D
- Image-to-3D
- Rigging
- Animation
- Texturing
- Game Development
- Creative Tools
website: https://www.tripo3d.ai/
---
