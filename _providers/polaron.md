---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://polaron.ai
- group: other
  title: ''
  type: Platform
  url: https://polaron.ai/platform
- group: company
  title: ''
  type: About
  url: https://polaron.ai/about-us
- group: company
  title: ''
  type: Blog
  url: https://polaron.ai/newsroom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Polaron-AI
- group: commercial
  title: ''
  type: TermsOfService
  url: https://polaron.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://polaron.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:info@polaron.ai
- group: start
  title: ''
  type: Login
  url: https://app.polaron.ai
- group: auth
  title: ''
  type: DomainSecurity
  url: security/polaron-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/polaron-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/polaron-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/polaron-rate-limits.yml
coverage:
  checked: '2026-08-17'
  detail: Polaron ships no developer surface at all on its marketing site — the 22-URL sitemap has no /developers, /docs or /pricing entry — and the product's own backend at https://app.polaron.ai/api/ answers every path, including /api/openapi.json and /api/docs, with a blanket HTTP 401 {"detail":"Unauthorized"}, so the contract is reachable only with an active tenant account.
  evidence:
  - status: 401
    url: https://app.polaron.ai/api/openapi.json
  - status: 401
    url: https://app.polaron.ai/api/docs
  - status: 404
    url: https://www.polaron.ai/pricing
  - status: 404
    url: https://polaron.ai/.well-known/security.txt
  - status: 200
    url: https://api.github.com/orgs/Polaron-AI
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: 'Polaron is a London-based AI software company that builds "the intelligence layer for materials science." Its platform applies machine learning to microscopy and image data to automate microstructure analysis, connecting process, structure, and performance so materials engineering teams can characterise, design, and manufacture materials faster and with less uncertainty. The platform centers on three core model families: Segmentation (identifying and measuring microstructural features), Reconstruction (converting 2D micrographs into 3D representations), and Design (optimising microstructural parameters). It is applied across batteries, metals and alloys, composites, ceramics, additive manufacturing, and pharmaceuticals, spanning R&D, quality and qualification, and modelling and simulation workflows. Polaron is backed by Speedinvest and research institutions including Imperial College London, Manchester, Oxford, and Cambridge.'
image: https://cdn.prod.website-files.com/66dacfc633b8a155263481fd/69813922f2dab1f63b99d94c_Frame%201707484013.png
layout: provider
modified: '2026-08-17'
name: Polaron
nav: Providers
network: true
overview: 'Polaron is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Materials Science, Artificial Intelligence, Machine Learning, and Microscopy.


  Polaron''s developer surface includes engineering blog, support, and 11 more developer resources.'
plans:
- name: Polaron Plans Pricing
  plan_count: 0
  slug: polaron-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Polaron Rate Limits
  slug: polaron-rate-limits
score:
  band: emerging
  composite: 13.0
  delta: 1.1
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Polaron Domain Security
  slug: polaron-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: polaron
tags:
- Company
- Materials Science
- Artificial Intelligence
- Machine Learning
- Microscopy
- Microstructure
- Batteries
- Additive Manufacturing
- Deep Tech
- Simulation
website: https://polaron.ai
---
