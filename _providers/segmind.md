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
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Segmind Agentic Access
  operation_count: 12
  slug: segmind-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 5
apis:
- description: We put the AI in API, delivering top AI models for rapid prototyping and seamless deployment, ready to scale up as needed.
  name: Segmind
  slug: segmind
- description: User account and credits
  name: Segmind Account API
  slug: segmind-account-api
- description: Fine-tuning request management and data handling
  name: Segmind Fine-tuning API
  slug: segmind-fine-tuning-api
- description: Synchronous and asynchronous model inference
  name: Segmind Inference API
  slug: segmind-inference-api
- description: Upload reusable assets
  name: Segmind Storage API
  slug: segmind-storage-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Segmind Account API
  slug: open-segmind-account-api
- collection_type: open
  name: Segmind Account Fine-tuning API
  slug: open-segmind-fine-tuning-api
- collection_type: open
  name: Segmind Account Inference API
  slug: open-segmind-inference-api
- collection_type: open
  name: Segmind Account Storage API
  slug: open-segmind-storage-api
- collection_type: open
  name: Segmind API
  slug: open-segmind
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/segmind-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/segmind-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/segmind-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/segmind
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/segmind
- group: agent
  title: ''
  type: LlmsText
  url: https://www.segmind.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://blog.segmind.com/feed
created: '2025-03-01'
description: We put the AI in API, delivering top AI models for rapid prototyping and seamless deployment, ready to scale up as needed.
finops:
- name: Segmind Finops
  service_category: API
  slug: segmind-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/segmind.png
layout: provider
modified: '2026-03-16'
name: Segmind
nav: Providers
network: true
overview: 'Segmind publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account API, Fine-tuning API, Inference API, and 1 more.


  Segmind''s developer surface includes authentication, engineering blog, and 5 more developer resources.'
plans:
- name: Segmind Plans Pricing
  plan_count: 3
  slug: segmind-plans-pricing
random_paper: 147
rate_limits:
- limit_count: 5
  name: Segmind Rate Limits
  slug: segmind-rate-limits
score:
  band: emerging
  composite: 26.6
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 55.2
    developer_ergonomics: 13.0
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 26.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/segmind/refs/heads/main/screenshots/segmind-2026-06-20T193634.png
security:
- kind: authentication
  name: Segmind Authentication
  slug: segmind-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Segmind Domain Security
  slug: segmind-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: segmind
---
