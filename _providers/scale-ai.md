---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    asyncapi_events: false
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Scale Ai Agentic Access
  operation_count: 14
  slug: scale-ai-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 9
apis:
- description: The Scale REST API is the unified programmatic surface for Scale's data engine. It is built on REST principles with resource-oriented URLs, form-encoded request bodies, JSON responses, and standard HT
  name: Scale REST API
  slug: scale-rest-api
- description: The GenAI Data Engine is Scale's product surface for generating, curating, and reviewing data used to train and tune generative-AI foundation models, including RLHF, SFT, evaluation, and red-team data
  name: Scale GenAI Data Engine
  slug: scale-genai-data-engine
- description: The Scale GenAI Platform is the deployment and orchestration product for generative-AI applications, used by enterprise and public-sector customers to deliver agentic and generative workflows on top o
  name: Scale GenAI Platform
  slug: scale-genai-platform
- description: Scale's Automotive Data Engine covers autonomy-grade data needs including LiDAR labeling, sensor fusion, multi-stage annotation, the customer dashboard, data hosting, and Nucleus for dataset managemen
  name: Scale Automotive Data Engine
  slug: scale-automotive-data-engine
- description: Nucleus is Scale's dataset management product for browsing, querying, and curating ML datasets at scale.
  name: Scale Nucleus
  slug: scale-nucleus
- description: Donovan is Scale's AI platform for defense and public-sector use cases, delivering decision-support and analytic capabilities to U.S. and allied government customers.
  name: Scale Donovan
  slug: scale-donovan
- description: The Batches API from Scale AI — 4 operation(s) for batches.
  name: Scale AI Batches API
  slug: scale-ai-batches-api
- description: The Projects API from Scale AI — 3 operation(s) for projects.
  name: Scale AI Projects API
  slug: scale-ai-projects-api
- description: The Tasks API from Scale AI — 5 operation(s) for tasks.
  name: Scale AI Tasks API
  slug: scale-ai-tasks-api
artifact_total: 39
collections:
- collection_type: open
  name: Scale AI REST API
  slug: open-scale-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scale-ai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/scale-ai-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/scale-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scale-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scale-ai-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://scale.com
- group: docs
  title: ''
  type: Documentation
  url: https://scale.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api-reference.scale.com
- group: start
  title: ''
  type: GettingStarted
  url: https://api-reference.scale.com/docs/api-reference/introduction-to-scale-api.md
- group: auth
  title: ''
  type: Authentication
  url: https://api-reference.scale.com/docs/api-reference/authentication.md
- group: company
  title: ''
  type: Blog
  url: https://scale.com/blog
- group: start
  title: ''
  type: Signup
  url: https://dashboard.scale.com
- group: start
  title: ''
  type: Console
  url: https://dashboard.scale.com
- group: commercial
  title: ''
  type: Pricing
  url: https://scale.com
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/scaleapi/
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/scaleapi
- group: operate
  title: ''
  type: Support
  url: https://scale.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/scaleai
created: '2026-05-23'
description: Scale AI is the data engine for AI. The company turns raw data into training data by combining ML-powered pre-labeling with multi-tier human review, and ships an extensive REST API and SDKs for managing labeling, evaluation, and generative-AI data pipelines. The product portfolio spans the Scale Data Engine (foundational labeling and review), the GenAI Data Engine (data for foundation-model training and tuning), the Scale GenAI Platform (deployment and orchestration for generative AI), the Automotive Data Engine (LiDAR, sensor fusion, customer dashboards, Nucleus), and Donovan (Scale's defense / public-sector AI product). The REST API lives at api.scale.com/v1, supports live and sandbox modes, and is wrapped by official Python (scaleapi) and JavaScript (scaleapi) SDKs. The company serves enterprise, insurance, healthcare, and U.S. and global public-sector verticals.
features:
- description: Resource-oriented REST API with JSON responses, live and sandbox modes, and versioned v1 endpoints.
  name: REST API at api.scale.com/v1
- description: Create, retrieve, cancel, and tag individual labeling tasks with unique identifiers and metadata.
  name: Tasks API
- description: Create, finalize, prioritize, list, and retrieve status for batches of tasks.
  name: Batches API
- description: Create and manage labeling projects, including taxonomy service management.
  name: Projects API
- description: Image and video, sensor fusion, LiDAR, and multi-stage annotation task types.
  name: Specialized Annotation
- description: RLHF, SFT, evaluation, and red-team data for generative AI foundation models.
  name: GenAI Data Engine
- description: Deployment and orchestration product for enterprise and public-sector generative-AI workflows.
  name: GenAI Platform
- description: Scale's defense and public-sector AI product line.
  name: Donovan
- description: Dataset management for browsing, querying, and curating ML datasets.
  name: Nucleus
- description: Integrates with AWS S3, Azure, and Google Cloud Storage for data ingest and delivery.
  name: Cloud Storage Integration
- description: Asynchronous task completion callbacks and secure result URLs.
  name: Callbacks
finops:
- name: Scale Ai Finops
  service_category: API
  slug: scale-ai-finops
graphqls:
- description: Scale AI provides data labeling, RLHF, and AI evaluation services. The API covers task creation for labeling, annotation retrieval, workforce management, evaluation datasets, and model improvement pip
  name: Scale AI GraphQL API
  slug: scale-ai-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scale-ai.png
integrations:
- description: Cloud storage ingest and delivery for labeling jobs.
  name: AWS S3, Azure Blob, Google Cloud Storage
- description: Official Python client published on PyPI.
  name: Python SDK (scaleapi)
- description: Official Node.js client published on npm.
  name: JavaScript SDK (scaleapi)
- description: Test integrations safely against a sandbox environment that mirrors live behavior.
  name: Sandbox Mode
layout: provider
modified: '2026-05-23'
name: Scale AI
nav: Providers
network: true
overview: 'Scale AI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Batches API, Projects API, and Tasks API. Tagged areas include Data Engine, Labeling, RLHF, GenAI Platform, and Donovan.


  Scale AI''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, engineering blog, signup flow, and 11 more developer resources.'
plans:
- name: Scale Ai Plans Pricing
  plan_count: 1
  slug: scale-ai-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 2
  name: Scale Ai Rate Limits
  slug: scale-ai-rate-limits
score:
  band: developing
  composite: 46.0
  delta: -0.8
  facets:
    commercial_clarity: 47.4
    contract_quality: 56.9
    developer_ergonomics: 65.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 46.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scale-ai/refs/heads/main/screenshots/scale-ai-2026-06-20T193601.png
security:
- kind: authentication
  name: Scale Ai Authentication
  slug: scale-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Scale Ai Domain Security
  slug: scale-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Scale Ai Vulnerability Disclosure
  slug: scale-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Scale Ai Trust Center
  slug: scale-ai-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP
slug: scale-ai
tags:
- Data Engine
- Labeling
- RLHF
- GenAI Platform
- Donovan
- Defense AI
- LiDAR
- Sensor Fusion
- REST API
use_cases:
- description: RLHF, SFT, evaluation, and red-team datasets for frontier model labs.
  name: Foundation Model Training Data
- description: LiDAR, camera, and sensor-fusion labeling for AV programs.
  name: Autonomous Vehicle Data
- description: Build and deploy generative-AI applications on the GenAI Platform.
  name: Enterprise GenAI Deployment
- description: Deliver Donovan-based analytic and decision-support workflows to defense and government customers.
  name: Public Sector Decision Support
- description: Browse, query, and curate ML datasets at scale with Nucleus.
  name: Dataset Curation
website: https://scale.com
---
