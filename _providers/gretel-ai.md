---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
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
overview: 'Gretel publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Synthetic Data, Privacy Engineering, Tabular, Text, and Time-Series.


  Gretel''s developer surface includes documentation, GitHub presence, and 7 more developer resources.'
plans:
- name: Gretel Ai Plans Pricing
  plan_count: 1
  slug: gretel-ai-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 2
  name: Gretel Ai Rate Limits
  slug: gretel-ai-rate-limits
score:
  band: emerging
  composite: 17.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 17.8
  schema_version: 0.9
  scored_at: '2026-08-03'
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
- Time-Series
- REST
- Python SDK
- AI Data
website: https://gretel.ai/
---
