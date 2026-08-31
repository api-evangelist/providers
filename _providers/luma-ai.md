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
  band: agent-aware
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
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Luma Ai Agentic Access
  operation_count: 13
  slug: luma-ai-agentic-access
  summary_line: 13 operations · 8 acting
api_count: 1
apis:
- description: REST API for video (Ray series) and image (Photon) generation. Submit a generation request, then poll for status. Documentation at https://docs.lumalabs.ai/. Auth via API key from https://lumalabs.ai/
  name: Luma Dream Machine API
  slug: dream-machine
- description: Agent-style image generation/editing with a reasoning endpoint and a generation endpoint. Uses /v1/generations submit and /v1/generations/{generation_id} polling pattern at https://agents.lumalabs.ai/
  name: Luma Agents API (uni-1)
  slug: agents-uni
- description: The Concepts API from Luma AI — 1 operation(s) for concepts.
  name: Luma AI Concepts API
  slug: luma-ai-concepts-api
- description: The Credits API from Luma AI — 1 operation(s) for credits.
  name: Luma AI Credits API
  slug: luma-ai-credits-api
- description: The Generations API from Luma AI — 4 operation(s) for generations.
  name: Luma AI Generations API
  slug: luma-ai-generations-api
- description: The Image API from Luma AI — 2 operation(s) for image.
  name: Luma AI Image API
  slug: luma-ai-image-api
- description: The System API from Luma AI — 1 operation(s) for system.
  name: Luma AI System API
  slug: luma-ai-system-api
- description: The Video API from Luma AI — 3 operation(s) for video.
  name: Luma AI Video API
  slug: luma-ai-video-api
artifact_total: 24
asyncapis:
- description: Server-to-server callback delivered by the Luma Dream Machine API when an asynchronous generation transitions between states. Luma POSTs a JSON document carrying the `Generation` object to a customer-
  name: Luma Dream Machine API Callback
  slug: luma-ai-callback-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Luma Dream Machine Concepts API
  slug: open-luma-ai-concepts-api
- collection_type: open
  name: Luma Dream Machine Concepts Credits API
  slug: open-luma-ai-credits-api
- collection_type: open
  name: Luma Dream Machine Concepts Generations API
  slug: open-luma-ai-generations-api
- collection_type: open
  name: Luma Dream Machine Concepts Image API
  slug: open-luma-ai-image-api
- collection_type: open
  name: Luma Dream Machine Concepts System API
  slug: open-luma-ai-system-api
- collection_type: open
  name: Luma Dream Machine Concepts Video API
  slug: open-luma-ai-video-api
- collection_type: open
  name: Luma Dream Machine API
  slug: open-luma-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/luma-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/luma-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/luma-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lumalabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/luma-ai
- group: company
  title: ''
  type: Website
  url: https://lumalabs.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lumalabs.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/luma-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/luma-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/luma-ai-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.lumalabs.ai/llms.txt
created: '2026-05-08'
description: Luma AI builds generative video (Dream Machine / Ray) and image (Photon) models, plus agent and 3D capture products. The Dream Machine API exposes REST endpoints for video and image generation with submit + poll semantics, an agent uni-1 model, and SDKs for Python, JavaScript, Go, and a CLI. Pricing is per-second for video and per-request or per-pixel for images.
finops:
- name: Luma Ai Finops
  service_category: AI
  slug: luma-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/luma-ai.png
layout: provider
modified: '2026-05-30'
name: Luma AI
nav: Providers
network: true
overview: 'Luma AI publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Luma Dream Machine API, Concepts API, Credits API, and 4 more. Tagged areas include Artificial Intelligence, Video Generation, Image-Generation, 3D, and Dream Machine.


  The Luma AI catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Luma AI''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Luma Ai Plans Pricing
  plan_count: 3
  slug: luma-ai-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Luma Ai Rate Limits
  slug: luma-ai-rate-limits
rules:
- effective_rule_count: 30
  extends:
  - spectral:asyncapi
  name: Luma AI API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: luma-ai-asyncapi-spectral-rules
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 12
    catalog_gap: 66.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 11.4
    contract_quality: 57.2
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 11.4
    operational_transparency: 7.9
  previous_composite: 37.0
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
screenshot: https://raw.githubusercontent.com/api-evangelist/luma-ai/refs/heads/main/screenshots/luma-ai-2026-06-20T184752.png
security:
- kind: authentication
  name: Luma Ai Authentication
  slug: luma-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Luma Ai Domain Security
  slug: luma-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: luma-ai
tags:
- Artificial Intelligence
- Video Generation
- Image-Generation
- 3D
- Dream Machine
- Multimodal
website: https://lumalabs.ai/
---
