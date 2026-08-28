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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Real-time identity verification (Verify) and modular identity intelligence (Signals) over a shared multi-field request model. Bearer-authenticated REST endpoints POST /verify and POST /signals at api.
  name: Fideo Verify & Signals API
  slug: fideo-verify-signals-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fideo-intelligence-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fideo.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.fideo.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fideo.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fideo.ai/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/fideo-intelligence-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.fideo.ai/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fideo.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.fideo.ai/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.fideo.ai/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://www.fideo.ai/tryverify/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fideo.ai/products/verify/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fideo.ai/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fideo.ai/privacy/privacy-policy/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fideo-intelligence-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fideo-intelligence-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fideo-intelligence-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fideo-intelligence-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fideo-intelligence-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fideo-intelligence-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fideo-intelligence-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fideo-intelligence-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fideo-intelligence-changelog.yml
created: '2026-07-17'
description: 'Fideo Intelligence is an identity intelligence platform that helps banks, fintechs, and financial institutions detect fraud and financial crime in real time. Fideo screens billions of transactions annually against an identity graph of billions of identities and hundreds of billions of identifiers and relationships. Its developer-ready APIs expose two products: Fideo Verify, a real-time, AI-powered identity verification and risk-scoring endpoint that consolidates many identity and risk checks into a single call for account origination, onboarding, account-takeover prevention, and loan-origination fraud; and Fideo Signals, modular identity intelligence that enriches existing fraud models, risk scoring, investigations, and link analysis. Both products share one multi-field request schema and are reached over a bearer-authenticated REST API at api.fideo.ai, with date-versioned responses and platform integrations for FusionAuth, Auth0, and Maltego.'
image: https://www.fideo.ai/wp-content/uploads/2024/10/preview-thumb-fideo-1200px.png
layout: provider
mcp_servers:
- description: ''
  name: Fideo Intelligence MCP Server
  slug: fideo-intelligence-mcp-server
modified: '2026-07-19'
name: Fideo Intelligence
nav: Providers
network: true
overview: 'Fideo Intelligence publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity, Identity Verification, Fraud Prevention, and Financial Crime.


  Fideo Intelligence''s developer surface includes documentation, getting-started guide, authentication, changelog, engineering blog, support, signup flow, and 17 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 26.8
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 43.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 26.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fideo-intelligence/refs/heads/main/screenshots/fideo-intelligence-2026-07-25T214416.png
security:
- kind: authentication
  name: Fideo Intelligence Authentication
  slug: fideo-intelligence-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fideo Intelligence Domain Security
  slug: fideo-intelligence-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fideo-intelligence
tags:
- Company
- Identity
- Identity Verification
- Fraud Prevention
- Financial Crime
- KYC
- Risk Scoring
- Identity Intelligence
- Fintech
website: https://fideo.ai/
---
