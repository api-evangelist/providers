---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 247
  human_in_the_loop: 6
  name: Clarifai Agentic Access
  operation_count: 466
  slug: clarifai-agentic-access
  summary_line: 466 operations · 247 acting · 6 human-in-the-loop
api_count: 1
apis:
- description: The V2 API from Clarifai — 297 operation(s) for v2.
  name: Clarifai V2 API
  slug: clarifai-v2-api
artifact_total: 40
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clarifai-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/clarifai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clarifai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clarifai.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.clarifai.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Clarifai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clarifai
- group: company
  title: ''
  type: Blog
  url: https://www.clarifai.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clarifai.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clarifai.com/
- group: other
  title: ''
  type: X
  url: https://x.com/clarifai
- group: commercial
  title: ''
  type: Plans
  url: plans/clarifai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clarifai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/clarifai-finops.yml
created: '2026-06-13'
description: Clarifai is an AI computer vision and NLP platform providing REST and gRPC APIs for image recognition, object detection, text analysis, visual search, and custom model training. The platform enables teams to build, deploy, and manage AI across shared cloud, on-premise, and edge infrastructure with support for model inference, workflow orchestration, vector search, and dataset management.
examples:
- key_count: 8
  name: List Concepts
  slug: list-concepts
- key_count: 8
  name: List Inputs
  slug: list-inputs
- key_count: 8
  name: List Models
  slug: list-models
- key_count: 8
  name: Post Inputs
  slug: post-inputs
- key_count: 8
  name: Post Model Outputs
  slug: post-model-outputs
- key_count: 8
  name: Post Searches
  slug: post-searches
- key_count: 8
  name: Post Workflow Results
  slug: post-workflow-results
finops:
- name: Clarifai Finops
  service_category: ''
  slug: clarifai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clarifai.png
json_schemas:
- name: apiAnnotationFilter
  property_count: 6
  slug: apiAnnotationFilter
- name: apiApp
  property_count: 21
  slug: apiApp
- name: apiConcept
  property_count: 14
  slug: apiConcept
- name: apiDataset
  property_count: 16
  slug: apiDataset
- name: apiDatasetVersion
  property_count: 17
  slug: apiDatasetVersion
- name: apiInput
  property_count: 7
  slug: apiInput
- name: apiKey
  property_count: 10
  slug: apiKey
- name: apiModel
  property_count: 36
  slug: apiModel
- name: apiModelVersion
  property_count: 25
  slug: apiModelVersion
- name: apiOutput
  property_count: 9
  slug: apiOutput
- name: apiPipeline
  property_count: 10
  slug: apiPipeline
- name: apiPipelineVersion
  property_count: 11
  slug: apiPipelineVersion
- name: apiPostInputsRequest
  property_count: 4
  slug: apiPostInputsRequest
- name: apiPostModelOutputsRequest
  property_count: 8
  slug: apiPostModelOutputsRequest
- name: apiPostWorkflowResultsResponse
  property_count: 4
  slug: apiPostWorkflowResultsResponse
- name: apiRunner
  property_count: 14
  slug: apiRunner
- name: apiSearch
  property_count: 13
  slug: apiSearch
- name: apiTask
  property_count: 23
  slug: apiTask
- name: apiUpload
  property_count: 8
  slug: apiUpload
- name: apiUser
  property_count: 24
  slug: apiUser
- name: apiWorkflow
  property_count: 17
  slug: apiWorkflow
- name: apiWorkflowVersion
  property_count: 12
  slug: apiWorkflowVersion
- name: Annotation
  property_count: 15
  slug: clarifaiapiAnnotation
jsonld:
- class_count: 0
  name: Clarifai Api Context
  property_count: 0
  slug: clarifai-api
- class_count: 40
  name: Clarifai Context
  property_count: 5
  slug: clarifai-context
layout: provider
modified: '2026-06-13'
name: Clarifai
nav: Providers
network: true
overview: 'Clarifai publishes 1 API on the [APIs.io](https://apis.io/) network: V2 API. Tagged areas include AI, Computer Vision, NLP, Image Recognition, and Object Detection.


  The Clarifai catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Clarifai''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Clarifai Plans Pricing
  plan_count: 4
  slug: clarifai-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 2
  name: Clarifai Rate Limits
  slug: clarifai-rate-limits
rules:
- name: Clarifai API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: clarifai-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.8
  delta: -6.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 45.2
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/clarifai/refs/heads/main/screenshots/clarifai-2026-06-20T174436.png
security:
- kind: domain-security
  name: Clarifai Domain Security
  slug: clarifai-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Clarifai Vulnerability Disclosure
  slug: clarifai-vulnerability-disclosure
  summary_line: disclosure policy published
slug: clarifai
tags:
- AI
- Computer Vision
- NLP
- Image Recognition
- Object Detection
- Text Analysis
- Visual Search
- Machine Learning
- Custom Model Training
- gRPC
website: https://www.clarifai.com
---
