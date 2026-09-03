---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Pika Agentic Access
  operation_count: 8
  slug: pika-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 2
apis:
- baseURL: https://fal.run/fal-ai/pika
  baseurl_source: declared
  description: The Fal Ai API from Pika — 8 operation(s) for fal ai.
  name: Pika Fal Ai API
  slug: pika-fal-ai-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pika 2.2 Image-to-Video Fal Ai API
  slug: open-pika-fal-ai-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pika-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pika-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pika-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://pika.art
- group: docs
  title: ''
  type: Documentation
  url: https://fal.ai/models/fal-ai/pika/v2.2/text-to-video
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Pika-Labs
- group: company
  title: ''
  type: Blog
  url: https://pika.art/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://pika.art/pricing
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pika-labs
- group: other
  title: ''
  type: X
  url: https://x.com/pika_labs
- group: commercial
  title: ''
  type: Plans
  url: plans/pika-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pika-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pika-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/pika-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/pika-context.jsonld
created: '2026-06-12'
description: Pika is an AI-powered video generation platform that allows users and developers to create, edit, and transform video content using natural language prompts, images, and existing video clips. The platform employs advanced diffusion models to produce short-form videos with realistic motion, smooth camera transitions, and detailed scene composition. Pika offers a suite of AI video tools including text-to-video, image-to-video, scene building (Pikascenes), keyframe interpolation (Pikaframes), and specialized transformation features such as Pikaffects, Pikaswaps, and Pikadditions. Developer API access is provided through a partnership with fal.ai, enabling programmatic integration of Pika's Pika 2.2 video models into applications and workflows.
examples:
- key_count: 5
  name: Pika Image To Video Example
  slug: pika-image-to-video-example
- key_count: 5
  name: Pika Text To Video Example
  slug: pika-text-to-video-example
finops:
- name: Pika Finops
  service_category: ''
  slug: pika-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pika.png
json_schemas:
- name: PikaVideoRequest
  property_count: 7
  slug: pika-video-request
- name: PikaVideoResponse
  property_count: 1
  slug: pika-video-response
jsonld:
- class_count: 5
  name: Pika Context
  property_count: 23
  slug: pika-context
layout: provider
modified: '2026-06-12'
name: Pika
nav: Providers
network: true
overview: 'Pika publishes 1 API on the [APIs.io](https://apis.io/) network: Fal Ai API. Tagged areas include Artificial Intelligence, Video Generation, Text-to-Video, Image-to-Video, and Diffusion Models.


  The Pika catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Pika''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Pika Plans Pricing
  plan_count: 5
  slug: pika-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Pika Rate Limits
  slug: pika-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Pika API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: pika-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.7
  coverage:
    artifact_dirs: 15
    catalog_gap: 25.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 70.1
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 23.7
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pika/refs/heads/main/screenshots/pika-2026-06-20T191705.png
security:
- kind: authentication
  name: Pika Authentication
  slug: pika-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pika Domain Security
  slug: pika-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pika
tags:
- Artificial Intelligence
- Video Generation
- Text-to-Video
- Image-to-Video
- Diffusion Models
- Generative AI
- Media
- Creative Tools
website: https://pika.art
---
