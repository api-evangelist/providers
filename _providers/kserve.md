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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Kserve Agentic Access
  operation_count: 10
  slug: kserve-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 1
apis:
- description: KServe's standardized model inference protocol for serving predictions across multiple ML frameworks on Kubernetes.
  name: KServe Inference API
  slug: inference-api
- baseURL_template: http://{host}
  baseurl_source: spec_template
  description: The Health API from KServe — 2 operation(s) for health.
  name: KServe Health API
  slug: kserve-health-api
- baseURL_template: http://{host}
  baseurl_source: spec_template
  description: The KServe Inference Protocol API from KServe — 1 operation(s) for kserve inference protocol.
  name: KServe KServe Inference Protocol API
  slug: kserve-kserve-inference-protocol-api
- baseURL_template: http://{host}
  baseurl_source: spec_template
  description: The Models API from KServe — 7 operation(s) for models.
  name: KServe Models API
  slug: kserve-models-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: KServe Inference Protocol Health API
  slug: open-kserve-health-api
- collection_type: open
  name: Health KServe Inference Protocol API
  slug: open-kserve-kserve-inference-protocol-api
- collection_type: open
  name: KServe Inference Protocol Health Models API
  slug: open-kserve-models-api
- collection_type: open
  name: KServe Inference Protocol
  slug: open-kserve
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kserve-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kserve-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kserve-project
- group: company
  title: ''
  type: Website
  url: https://kserve.github.io/website/
- group: docs
  title: ''
  type: Documentation
  url: https://kserve.github.io/website/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://kserve.github.io/website/latest/get_started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kserve/kserve
- group: company
  title: ''
  type: Blog
  url: https://kserve.github.io/website/blog/atom.xml
created: '2025-01-01'
description: KServe is a standard model inference platform on Kubernetes, built for highly scalable use cases. It provides performant, standardized inference protocol across ML frameworks including TensorFlow, PyTorch, scikit-learn, XGBoost, and more.
finops:
- name: Kserve Finops
  service_category: API
  slug: kserve-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kserve.png
layout: provider
modified: '2026-04-28'
name: KServe
nav: Providers
network: true
overview: 'KServe publishes 3 APIs on the [APIs.io](https://apis.io/) network: Health API, KServe Inference Protocol API, and Models API. Tagged areas include Inference, Kubernetes, Machine-Learning, MLOps, and Model Serving.


  KServe''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 4 more developer resources.'
plans:
- name: Kserve Plans Pricing
  plan_count: 3
  slug: kserve-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Kserve Rate Limits
  slug: kserve-rate-limits
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 9
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 44.9
    developer_ergonomics: 42.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 30.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kserve/refs/heads/main/screenshots/kserve-2026-06-20T184201.png
security:
- kind: authentication
  name: Kserve Authentication
  slug: kserve-authentication
  summary_line: http · 1 scheme
slug: kserve
tags:
- Inference
- Kubernetes
- Machine-Learning
- MLOps
- Model Serving
website: https://kserve.github.io/website/
---
