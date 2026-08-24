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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Search and retrieve regulatory and clinical documents.
  name: Rhizome Ai Documents API
  slug: rhizome-ai-documents-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rhizome AI Documents API
  slug: open-rhizome-ai-documents-api
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
  url: openapi/_original/rhizome-ai-openapi.yml
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
  name: Rhizome Ai MCP Server
  slug: rhizome-ai-mcp-server
modified: '2026-07-21'
name: Rhizome Ai
nav: Providers
network: true
overview: 'Rhizome Ai publishes 1 API on the [APIs.io](https://apis.io/) network: Documents API. Tagged areas include Company, Regulatory, Pharmaceuticals, Medical Devices, and Life Sciences.


  Rhizome Ai''s developer surface includes documentation, API reference, getting-started guide, authentication, support, pricing, signup flow, and 17 more developer resources.'
random_paper: 5
rate_limits:
- limit_count: 1
  name: Rhizome Ai Rate Limits
  slug: rhizome-ai-rate-limits
score:
  band: developing
  composite: 50.2
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 16.7
    contract_quality: 63.6
    developer_ergonomics: 56.5
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 21.1
  previous_composite: 50.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rhizome-ai/refs/heads/main/screenshots/rhizome-ai-2026-08-17T081552.png
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
- Pharmaceuticals
- Medical Devices
- Life Sciences
- Document Search
- Artificial Intelligence
- Compliance
website: https://rhizomeai.com
---
