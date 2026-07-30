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
- acting_count: 2
  human_in_the_loop: 0
  name: Determined Ai Agentic Access
  operation_count: 10
  slug: determined-ai-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 8
apis:
- description: Log in to and out of the cluster
  name: Determined AI Authentication API
  slug: determined-ai-authentication-api
- description: Manage checkpoints
  name: Determined AI Checkpoints API
  slug: determined-ai-checkpoints-api
- description: Manage cluster components
  name: Determined AI Cluster API
  slug: determined-ai-cluster-api
- description: Manage experiments
  name: Determined AI Experiments API
  slug: determined-ai-experiments-api
- description: Manage models
  name: Determined AI Models API
  slug: determined-ai-models-api
- description: Manage templates
  name: Determined AI Templates API
  slug: determined-ai-templates-api
- description: Manage tokens
  name: Determined AI Tokens API
  slug: determined-ai-tokens-api
- description: Manage users
  name: Determined AI Users API
  slug: determined-ai-users-api
artifact_total: 15
collections:
- collection_type: open
  name: Determined AI REST API
  slug: open-determined-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/determined-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/determined-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/determined-ai-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/determined-ai
- group: company
  title: ''
  type: Website
  url: https://www.determined.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.determined.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/determined-ai
- group: commercial
  title: ''
  type: License
  url: https://github.com/determined-ai/determined/blob/main/LICENSE
created: '2024-07-02'
description: Determined helps deep learning teams train models more quickly, easily share GPU resources, and effectively collaborate. Determined allows deep learning engineers to focus on building and training models at scale, without needing to worry about DevOps or writing custom code for common tasks like fault tolerance or experiment tracking. It bridges the gap between tools like TensorFlow and PyTorch for single researchers to the challenges that arise when doing deep learning at scale.
finops:
- name: Determined Ai Finops
  service_category: API
  slug: determined-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/determined-ai.png
layout: provider
modified: '2026-05-19'
name: Determined AI
nav: Providers
network: true
overview: 'Determined AI publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Checkpoints API, Cluster API, and 5 more. Tagged areas include Artificial Intelligence, Deep Learning, Machine Learning, and MLOps.


  Determined AI''s developer surface includes authentication, documentation, and 6 more developer resources.'
plans:
- name: Determined Ai Plans Pricing
  plan_count: 3
  slug: determined-ai-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 5
  name: Determined Ai Rate Limits
  slug: determined-ai-rate-limits
score:
  band: thin
  composite: 34.0
  delta: -2.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 47.5
    developer_ergonomics: 19.6
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/determined-ai/refs/heads/main/screenshots/determined-ai-2026-07-25T211812.png
security:
- kind: authentication
  name: Determined Ai Authentication
  slug: determined-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Determined Ai Domain Security
  slug: determined-ai-domain-security
  summary_line: DMARC
slug: determined-ai
tags:
- Artificial Intelligence
- Deep Learning
- Machine Learning
- MLOps
website: https://www.determined.ai/
---
