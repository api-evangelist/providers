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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Cvat Agentic Access
  operation_count: 36
  slug: cvat-agentic-access
  summary_line: 36 operations · 20 acting
api_count: 8
apis:
- description: Shapes, tracks, and tags attached to tasks and jobs.
  name: CVAT annotations API
  slug: cvat-annotations-api
- description: External object-storage connections used as data sources.
  name: CVAT cloudstorages API
  slug: cvat-cloudstorages-api
- description: Assignable annotation units that subdivide a task.
  name: CVAT jobs API
  slug: cvat-jobs-api
- description: Label taxonomy shared across projects, tasks, and jobs.
  name: CVAT labels API
  slug: cvat-labels-api
- description: Membership of users within organizations.
  name: CVAT memberships API
  slug: cvat-memberships-api
- description: Organizations scoping resources for teams.
  name: CVAT organizations API
  slug: cvat-organizations-api
- description: Annotation projects that group tasks and share a label set.
  name: CVAT projects API
  slug: cvat-projects-api
- description: Annotation tasks holding media data and annotations.
  name: CVAT tasks API
  slug: cvat-tasks-api
artifact_total: 15
collections:
- collection_type: open
  name: CVAT REST API
  slug: open-cvat
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cvat-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cvat-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cvat-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cvat-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cvat-ai
- group: company
  title: ''
  type: Website
  url: https://www.cvat.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cvat.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/cvat-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cvat-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cvat-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.cvat.ai/resources/blog
created: '2026-06-21'
description: CVAT (Computer Vision Annotation Tool) is an open-source platform for annotating images, video, and 3D point clouds for vision AI. The CVAT REST API exposes projects, tasks, jobs, annotations, labels, organizations, memberships, and cloud storage integrations, available both self-hosted (MIT-licensed) and as the hosted CVAT Online service at app.cvat.ai.
finops:
- name: Cvat Finops
  service_category: Machine Learning and Data Annotation
  slug: cvat-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cvat.png
layout: provider
modified: '2026-06-21'
name: CVAT
nav: Providers
network: true
overview: 'CVAT publishes 8 APIs on the [APIs.io](https://apis.io/) network, including annotations API, cloudstorages API, jobs API, and 5 more. Tagged areas include Computer Vision, Data Annotation, Labeling, Datasets, and Open Source.


  CVAT''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Cvat Plans Pricing
  plan_count: 5
  slug: cvat-plans-pricing
random_paper: 82
rate_limits:
- limit_count: 6
  name: Cvat Rate Limits
  slug: cvat-rate-limits
score:
  band: thin
  composite: 37.3
  delta: -0.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cvat/refs/heads/main/screenshots/cvat-2026-07-25T211022.png
security:
- kind: authentication
  name: Cvat Authentication
  slug: cvat-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Cvat Domain Security
  slug: cvat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cvat
tags:
- Computer Vision
- Data Annotation
- Labeling
- Datasets
- Open Source
website: https://www.cvat.ai
---
