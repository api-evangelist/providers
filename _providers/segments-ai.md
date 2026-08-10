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
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Segments Ai Agentic Access
  operation_count: 23
  slug: segments-ai-agentic-access
  summary_line: 23 operations · 13 acting
api_count: 5
apis:
- description: The Datasets API from Segments.ai — 4 operation(s) for datasets.
  name: Segments.ai Datasets API
  slug: segments-ai-datasets-api
- description: The Labels API from Segments.ai — 1 operation(s) for labels.
  name: Segments.ai Labels API
  slug: segments-ai-labels-api
- description: The Labelsets API from Segments.ai — 2 operation(s) for labelsets.
  name: Segments.ai Labelsets API
  slug: segments-ai-labelsets-api
- description: The Releases API from Segments.ai — 2 operation(s) for releases.
  name: Segments.ai Releases API
  slug: segments-ai-releases-api
- description: The Samples API from Segments.ai — 2 operation(s) for samples.
  name: Segments.ai Samples API
  slug: segments-ai-samples-api
artifact_total: 12
collections:
- collection_type: open
  name: Segments.ai API
  slug: open-segments-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/segments-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/segments-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/segments-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/segments-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/segments-ai
- group: company
  title: ''
  type: Website
  url: https://segments.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.segments.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/segments-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/segments-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/segments-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://segments.ai/blog/
created: '2026-06-21'
description: Segments.ai is a data-labeling platform for computer vision, supporting 2D image segmentation and vectors as well as 3D point cloud and multi-sensor fusion annotation. Its REST API and Python SDK let teams manage datasets, samples, labels, labelsets, and versioned releases programmatically for building training data pipelines.
finops:
- name: Segments Ai Finops
  service_category: AI and Machine Learning
  slug: segments-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/segments-ai.png
layout: provider
modified: '2026-06-21'
name: Segments.ai
nav: Providers
network: true
overview: 'Segments.ai publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Datasets API, Labels API, Labelsets API, and 2 more. Tagged areas include Data Labeling, Computer Vision, Point Cloud, Annotation, and Machine Learning.


  Segments.ai''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Segments Ai Plans Pricing
  plan_count: 3
  slug: segments-ai-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 3
  name: Segments Ai Rate Limits
  slug: segments-ai-rate-limits
score:
  band: thin
  composite: 38.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Segments Ai Authentication
  slug: segments-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Segments Ai Domain Security
  slug: segments-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: segments-ai
tags:
- Data Labeling
- Computer Vision
- Point Cloud
- Annotation
- Machine Learning
website: https://segments.ai
---
