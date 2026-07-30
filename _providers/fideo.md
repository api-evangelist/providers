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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'Fideo''s real-time REST API for identity verification, fraud risk scoring, and identity intelligence. Two endpoints share a common multi-field request schema: POST /verify runs a comprehensive suite of'
  name: Fideo Verify & Signals API
  slug: fideo-verify-signals-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fideo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fideo.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.fideo.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fideo.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fideo.ai/docs/verify
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fideo.ai/docs/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://www.fideo.ai/tryverify/
- group: operate
  title: ''
  type: Support
  url: https://www.fideo.ai/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.fideo.ai/resources/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fideo-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fideo-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fideo-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fideo-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fideo-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/fideo-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fideo-well-known.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fideo.ai/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fideo.ai/privacy/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fideointelligence
created: '2026-07-17'
description: Fideo Intelligence is a Denver-based identity intelligence and fraud-prevention platform, spun out of FullContact in 2024 and backed by Foundry Group, Baird Capital, and Blue Note Ventures. Fideo turns fragmented personal identifiers — email, phone, SSN, name, postal address, IP address, and social handles — into real-time fraud and identity-verification signals drawn from an identity graph spanning billions of identities. Its two products, Verify (a single-call, real-time identity-verification and risk-scoring API that runs dozens of checks across breach, sanctions/watchlist, email, phone, location, device, and synthetic-identity dimensions) and Signals (modular identity-intelligence bundles that enrich existing fraud models), serve banks, credit unions, neobanks, fintechs, payments companies, and financial-crime and compliance teams for KYC, AML, onboarding, account-takeover, and payment-fraud use cases. The REST API is served at https://api.fideo.ai with bearer API-key authentication
  and JSON payloads, and is documented on a ReadMe developer hub.
image: https://www.fideo.ai/wp-content/uploads/2024/10/preview-thumb-fideo-1200px.png
layout: provider
mcp_servers:
- description: ''
  name: fideo-mcp.yml
  slug: fideo-mcpyml
modified: '2026-07-19'
name: Fideo
nav: Providers
network: true
overview: 'Fideo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Identity Verification, Fraud Prevention, and Fraud Detection.


  Fideo''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, changelog, and 12 more developer resources.'
random_paper: 27
score:
  band: thin
  composite: 31.1
  delta: 0.9
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 30.2
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fideo/refs/heads/main/screenshots/fideo-2026-07-25T214416.png
security:
- kind: authentication
  name: Fideo Authentication
  slug: fideo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fideo Domain Security
  slug: fideo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fideo
tags:
- Company
- AI
- Identity Verification
- Fraud Prevention
- Fraud Detection
- Identity Intelligence
- KYC
- AML
- Financial Crime
- Compliance
- Fintech
- Sanctions Screening
- Risk Scoring
website: https://www.fideo.ai
---
