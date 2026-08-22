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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'Real-time consumer-insights and decisioning API. Accepts consumer identifiers (phone, email, device, name, address) and returns enriched, AI-ready insights used for onboarding/KYC-AML, fraud and risk '
  name: Monnai Insights API
  slug: monnai-insights-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://monnai.com
- group: start
  title: ''
  type: Portal
  url: https://dev.monnai.com
- group: start
  title: ''
  type: SignUp
  url: https://www.monnai.com/get-started
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/monnai/
- group: auth
  title: ''
  type: Authentication
  url: authentication/monnai-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/monnai-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/monnai-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/monnai-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/monnai-llms.txt
created: '2026-07-17'
description: Monnai is a global consumer-insights infrastructure company that delivers real-time, AI-ready data for decisioning across the entire customer lifecycle. Its Insights API unifies fragmented identity, device, phone, email, and behavioral signals from a proprietary data consortium into clean, contextual 360-degree profiles, enabling financial institutions, fintechs, ecommerce, and marketplaces to power acquisition, onboarding (KYC/AML), risk assessment and fraud detection, credit decisioning, and collections. Monnai provides localized coverage across 190+ countries with a privacy-first, encryption-backed approach. The API is secured with OAuth 2.0. Monnai is backed by 500 Global.
image: https://cdn.prod.website-files.com/675348f1c32d2b2d94ca4ff7/6779efb03e354eaf71050a44_apple-touch-icon%20(1).webp
layout: provider
modified: '2026-07-20'
name: Monnai
nav: Providers
network: true
overview: 'Monnai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Insights, Fintech, Financial Services, and Fraud Detection.


  Monnai''s developer surface includes developer portal, signup flow, authentication, and 6 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 16.7
  delta: 1.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 15.7
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/monnai/refs/heads/main/screenshots/monnai-2026-08-07T184208.png
security:
- kind: authentication
  name: Monnai Authentication
  slug: monnai-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Monnai Domain Security
  slug: monnai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: monnai
tags:
- Company
- Consumer Insights
- Fintech
- Financial Services
- Fraud Detection
- Identity Verification
- KYC
- AML
- Credit Decisioning
- Risk Assessment
- Collections
- Emerging Markets
- Decisioning
- OAuth2
website: https://monnai.com
---
