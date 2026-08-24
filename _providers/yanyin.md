---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Yanyin Webhooks
  slug: yanyin-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.yanyin.tech
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.yanyin.tech/product/mega-open-platform
- group: docs
  title: ''
  type: Documentation
  url: https://www.yanyin.tech/product/mega-open-platform
- group: commercial
  title: ''
  type: Pricing
  url: https://www.yanyin.tech/price
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.yanyin.tech/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.yanyin.tech/register
- group: start
  title: ''
  type: Login
  url: https://app.yanyin.tech/login
- group: company
  title: ''
  type: Blog
  url: https://www.yanyin.tech/news
- group: operate
  title: ''
  type: Support
  url: https://www.yanyin.tech/company#contact-us
- group: auth
  title: ''
  type: Authentication
  url: authentication/yanyin-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/yanyin-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/yanyin-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/yanyin-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/yanyin-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/yanyin-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yanyin-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yanyin-domain-security.yml
created: '2026-07-17'
description: Yanyin Technology (衍因科技) is a Shanghai-based biomedical AI company building 衍因智研云 (Yanyin Zhiyun), a digital research-collaboration platform for life-sciences R&D. Its product suite spans an electronic lab notebook (Yan Note), molecular biology tools (Yan Molecule), a LIMS (Yan LIMS), AI literature and experiment assistants (Yan Research, Yan Reviewer, Yan Advisor), and the enterprise AI MEGASphere platform, whose Mega Open Platform exposes an API gateway (API Key and OAuth2 client-credentials authentication, rate limiting, request signing, idempotency and retries, versioning), a developer center with online docs, SDKs and a sandbox, and webhook callback management with HMAC signing and event replay. Yanyin serves 80+ pharma companies, 280+ research institutions and hospitals, and 430+ universities, and holds ISO 9001, ISO 27001 and ISO 20000 certifications plus China MLPS Level 3. Backed by Qiming Venture Partners.
image: https://www.yanyin.tech/website2/apple-touch-icon.sxr5Uh9x.png
layout: provider
modified: '2026-07-21'
name: Yanyin Technology
nav: Providers
network: true
overview: 'Yanyin Technology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Artificial Intelligence, and Research.


  The Yanyin Technology catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Yanyin Technology''s developer surface includes documentation, pricing, signup flow, engineering blog, support, authentication, and 11 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 34.9
  delta: 0.0
  facets:
    access_clarity: 25.0
    commercial_clarity: 25.0
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 38.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 34.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Yanyin Authentication
  slug: yanyin-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Yanyin Domain Security
  slug: yanyin-domain-security
  summary_line: TLSv1.3
slug: yanyin
tags:
- Company
- Biotechnology
- Life Sciences
- Artificial Intelligence
- Research
- Electronic Lab Notebook
- LIMS
- Software-as-a-Service
- China
website: https://www.yanyin.tech
---
