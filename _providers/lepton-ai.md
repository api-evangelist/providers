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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Managed AI platform API exposing model endpoints (HTTP server with OpenAI-compatible chat surface), dev sessions with managed GPUs, distributed training jobs, and batch processing. Endpoints are deplo
  name: NVIDIA DGX Cloud Lepton API
  slug: dgx-cloud-lepton
artifact_total: 5
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/nvidia/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lepton-ai-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/leptonai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lepton-ai
- group: company
  title: ''
  type: Website
  url: https://www.nvidia.com/en-us/data-center/dgx-cloud-lepton/
- group: company
  title: ''
  type: LegacyWebsite
  url: https://www.lepton.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nvidia.com/dgx-cloud/lepton/
- group: commercial
  title: ''
  type: Plans
  url: plans/lepton-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lepton-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lepton-ai-finops.yml
created: '2026-05-08'
description: Lepton AI was acquired by NVIDIA in 2025 and the platform is now branded NVIDIA DGX Cloud Lepton. It is a fully managed AI platform that connects developers to global GPU compute across a federated network of cloud providers, with managed endpoints, dev sessions, distributed training, and batch processing.
finops:
- name: Lepton Ai Finops
  service_category: AI
  slug: lepton-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lepton-ai.png
layout: provider
modified: '2026-08-21'
name: Lepton AI
nav: Providers
network: true
overview: 'Lepton AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, ML, Inference, Cloud, and GPU.


  Lepton AI''s developer surface includes documentation and 9 more developer resources.'
plans:
- name: Lepton Ai Plans Pricing
  plan_count: 1
  slug: lepton-ai-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Lepton Ai Rate Limits
  slug: lepton-ai-rate-limits
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 5
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 14.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lepton-ai/refs/heads/main/screenshots/lepton-ai-2026-06-20T184428.png
security:
- kind: domain-security
  name: Lepton Ai Domain Security
  slug: lepton-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lepton-ai
tags:
- Artificial Intelligence
- ML
- Inference
- Cloud
- GPU
- NVIDIA
- DGX Cloud
website: https://www.nvidia.com/en-us/data-center/dgx-cloud-lepton/
---
