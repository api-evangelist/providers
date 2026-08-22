---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: The Neptune REST API backs the Neptune Python client. It exposes runs, projects, fields, and metadata logging. Authentication uses an API token from the user profile.
  name: Neptune.ai REST API
  slug: neptune-rest-api
- description: Neptune Scale is the higher-throughput logging surface designed for foundation model training jobs. Same API-token authentication; SDK support in `neptune-scale`.
  name: Neptune Scale API (foundation-model tier)
  slug: neptune-scale-api
artifact_total: 6
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/neptune-ai/neptune-client/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/neptune-ai/neptune-client/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/neptune-ai/neptune-client/blob/master/.github/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/neptune-ai/neptune-client/blob/master/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/neptune-ai/neptune-client/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neptune-ai-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/neptuneai
- group: company
  title: ''
  type: Website
  url: https://neptune.ai/
- group: other
  title: ''
  type: Acquisition
  url: https://openai.com/index/openai-to-acquire-neptune/
- group: build
  title: neptune client
  type: SourceCode
  url: https://github.com/neptune-ai/neptune-client
- group: commercial
  title: ''
  type: Plans
  url: plans/neptune-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/neptune-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/neptune-ai-finops.yml
created: '2026-05-08'
description: Neptune.ai is an experiment tracker for ML and foundation-model training. As of 2025, Neptune.ai is being acquired by OpenAI and the public pricing page redirects to the OpenAI announcement. Customers continue to use the Neptune Python client and REST API during the transition.
finops:
- name: Neptune Ai Finops
  service_category: ML
  slug: neptune-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/neptune-ai.png
layout: provider
modified: '2026-05-08'
name: Neptune.ai
nav: Providers
network: true
overview: Neptune.ai publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include ML, MLOps, Experiment Tracking, Foundation Models, and Acquired.
plans:
- name: Neptune Ai Plans Pricing
  plan_count: 1
  slug: neptune-ai-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Neptune Ai Rate Limits
  slug: neptune-ai-rate-limits
score:
  band: emerging
  composite: 13.6
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 13.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/neptune-ai/refs/heads/main/screenshots/neptune-ai-2026-06-20T190137.png
security:
- kind: domain-security
  name: Neptune Ai Domain Security
  slug: neptune-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: neptune-ai
tags:
- ML
- MLOps
- Experiment Tracking
- Foundation Models
- Acquired
website: https://neptune.ai/
---
