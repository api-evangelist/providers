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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 61.5
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Search and retrieve regulatory and clinical documents.
  name: Rhizome Ai Documents API
  slug: rhizome-ai-documents-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rhizome-ai-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rhizome-ai-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rhizome-ai-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rhizome-ai-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rhizome-ai-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rhizome-ai-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rhizome-ai-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/rhizome-ai-openapi-overlay.yaml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/rhizome-ai-openapi.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rhizomeai.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rhizomeai.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.rhizomeai.com/api-reference/search
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rhizomeai.com/introduction
- group: auth
  title: ''
  type: Authentication
  url: authentication/rhizome-ai-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rhizome-ai-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rhizome-ai-llms.txt
- group: operate
  title: ''
  type: Support
  url: mailto:support@rhizomeai.com
- group: commercial
  title: ''
  type: Pricing
  url: https://rhizomeai.com
- group: start
  title: ''
  type: SignUp
  url: https://rhizomeai.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://rhizomeai.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rhizomeai.com/termsofservice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rhizomeai.com/privacypolicy
- group: company
  title: ''
  type: Website
  url: https://rhizomeai.com
created: '2026-07-17'
description: Rhizome AI is an AI-powered regulatory research platform for pharmaceutical and medical device companies. It lets regulatory affairs teams ask questions and receive cited answers grounded in primary-source documents from health authorities worldwide (FDA, EMA, Health Canada, Swissmedic, MHRA, TGA and others across 10+ agencies), retrieving from up to a thousand documents without hallucinating. Beyond the web application, Rhizome AI publishes an enterprise HTTP API that exposes BM25 keyword search across the regulatory document corpus and full-text, page-by-page document retrieval, authenticated with an x-api-key header. A YC-backed company, Rhizome AI was surfaced as a portfolio-company lead and enriched from its public developer documentation.
image: https://rhizomeai.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: rhizome-ai-mcp.yml
  slug: rhizome-ai-mcpyml
modified: '2026-07-21'
name: Rhizome Ai
nav: Providers
network: true
overview: 'Rhizome Ai publishes 1 API on the [APIs.io](https://apis.io/) network: Documents API. Tagged areas include Company, Regulatory, Pharmaceutical, Medical Devices, and Life Sciences.


  Rhizome Ai''s developer surface includes documentation, API reference, getting-started guide, authentication, support, pricing, signup flow, and 17 more developer resources.'
random_paper: 61
rate_limits:
- limit_count: 0
  name: Rhizome Ai Rate Limits
  slug: rhizome-ai-rate-limits
score:
  band: developing
  composite: 48.2
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 63.7
    developer_ergonomics: 65.2
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 48.2
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Rhizome Ai Authentication
  slug: rhizome-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rhizome Ai Domain Security
  slug: rhizome-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rhizome-ai
tags:
- Company
- Regulatory
- Pharmaceutical
- Medical Devices
- Life Sciences
- Document Search
- Artificial Intelligence
- Compliance
website: https://rhizomeai.com
---
