---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - '{''url'': ''https://gretel.ai/'', ''status'': 301, ''note'': ''declared website redirects to https://www.nvidia.com/en-us/use-cases/synthetic-data-generation-for-agentic-ai/ — a different registrable domain (gretel.ai -> nvidia.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
api_count: 2
apis:
- description: REST API for Gretel's synthetic data platform. Lets you ingest data, manage projects, train models, run record handlers, and pull artifacts. Used as the backend for the gretel-client Python SDK and CL
  name: Gretel REST API
  slug: rest-api
- description: Python SDK and CLI (gretel-client) for interacting with Gretel APIs. Provides a high-level Gretel interface plus lower-level Projects, Models, and Record Handler SDKs.
  name: Gretel Python Client SDK
  slug: python-sdk
artifact_total: 6
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/gretelai/gretel-python-client/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/gretelai/gretel-python-client/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/gretelai/gretel-python-client/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gretel-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gretel.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gretel.ai/
- group: docs
  title: ''
  type: APIDocs
  url: https://api.docs.gretel.ai/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/gretelai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gretelai
- group: commercial
  title: ''
  type: Plans
  url: plans/gretel-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gretel-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gretel-ai-finops.yml
created: '2026-05-23'
description: Gretel is a synthetic data platform for tabular, text, and time-series data. It pairs a REST API and Python client (gretel-client) with Gretel Navigator and a library of model recipes for generating, transforming, and de-identifying data. The platform exposes ingestion, project, model, and record-handler endpoints over HTTPS.
finops:
- name: Gretel Ai Finops
  service_category: API
  slug: gretel-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gretel-ai.png
layout: provider
modified: '2026-05-23'
name: Gretel
nav: Providers
network: true
overview: 'Gretel publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Synthetic Data, Privacy Engineering, Tabular, Text, and Time Series.


  Gretel''s developer surface includes documentation, GitHub presence, and 10 more developer resources.'
plans:
- name: Gretel Ai Plans Pricing
  plan_count: 1
  slug: gretel-ai-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Gretel Ai Rate Limits
  slug: gretel-ai-rate-limits
score:
  band: emerging
  composite: 20.9
  coverage:
    artifact_dirs: 5
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  open_source:
    applies: true
    score: 25.0
  previous_composite: 20.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gretel-ai/refs/heads/main/screenshots/gretel-ai-2026-06-20T182404.png
security:
- kind: domain-security
  name: Gretel Ai Domain Security
  slug: gretel-ai-domain-security
  summary_line: TLSv1.2 · DMARC
slug: gretel-ai
tags:
- Synthetic Data
- Privacy Engineering
- Tabular
- Text
- Time Series
- REST
- Python SDK
- Ai Data
website: https://gretel.ai/
---
