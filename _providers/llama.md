---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 4
apis:
- description: Meta's hosted REST API providing access to Llama large language models for chat completions, text generation, and embeddings. Authentication is via API key issued through llama.developer.meta.com.
  name: Llama API
  slug: llama-api
- description: Open-weight Llama model family available for direct download and self-hosted inference, distributed under Meta's Llama Community License.
  name: Llama Models (open weights)
  slug: llama-models
- description: Open-source framework standardizing the building blocks for Llama-based generative AI applications, including inference, safety, agents, and evaluation, with REST and SDK access across multiple provid
  name: Llama Stack
  slug: llama-stack
- description: Open-source project providing tools and evaluations for assessing and improving the safety and security of generative AI models, including Llama Guard and CyberSecEval.
  name: PurpleLlama
  slug: purple-llama
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/llama-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.llama.com/
- group: docs
  title: ''
  type: Documentation
  url: https://llama.developer.meta.com/docs/overview/
- group: start
  title: ''
  type: Portal
  url: https://llama.developer.meta.com/
- group: docs
  title: ''
  type: Reference
  url: https://ai.meta.com/llama/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/meta-llama
- group: commercial
  title: ''
  type: License
  url: https://www.llama.com/llama3/license/
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://www.llama.com/llama3/use-policy/
created: '2024-01-15'
description: Llama is Meta's family of open-weight large language models, available for download, self-hosting, and via Meta's hosted Llama API for chat completions, text generation, and embeddings. The ecosystem also includes the open-source llama-models, llama-stack, and PurpleLlama safety projects on GitHub.
finops:
- name: Llama Finops
  service_category: API
  slug: llama-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/llama.png
layout: provider
modified: '2026-04-28'
name: Llama
nav: Providers
network: true
overview: 'Llama publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Large Language Models, Machine-Learning, Meta, and Open-Source.


  Llama''s developer surface includes documentation, developer portal, and 6 more developer resources.'
plans:
- name: Llama Plans Pricing
  plan_count: 3
  slug: llama-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Llama Rate Limits
  slug: llama-rate-limits
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 5
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 16.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/llama/refs/heads/main/screenshots/llama-2026-06-20T184621.png
security:
- kind: domain-security
  name: Llama Domain Security
  slug: llama-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: llama
tags:
- Artificial Intelligence
- Large Language Models
- Machine-Learning
- Meta
- Open-Source
- LLM
- Natural Language Processing
website: https://www.llama.com/
---
