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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for creating contracts, sending them to signers over WhatsApp/SMS/email, running biometric identity verification, generating documents from templates, sending and verifying OTPs, and register
  name: Keynua API
  slug: keynua-api
artifact_total: 5
asyncapis:
- description: ''
  name: Keynua Webhooks
  slug: keynua-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keynua-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.keynua.com/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://keynua.github.io/slate
- group: docs
  title: ''
  type: Documentation
  url: https://keynua.github.io/slate
- group: docs
  title: ''
  type: APIReference
  url: https://keynua.github.io/slate
- group: start
  title: ''
  type: GettingStarted
  url: https://keynua.github.io/slate/#introduction
- group: commercial
  title: ''
  type: Pricing
  url: https://www.keynua.com/en/plans/
- group: start
  title: ''
  type: SignUp
  url: https://www.keynua.com/en/account-request/
- group: start
  title: ''
  type: Login
  url: https://app.keynua.com?lang=en
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.keynua.com/en/legal/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.keynua.com/en/legal/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Keynua
- group: operate
  title: ''
  type: StatusPage
  url: https://status.keynua.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/keynua-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/keynua-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/keynua-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/keynua-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/keynua-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/keynua-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/keynua-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/keynua-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/keynua-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Keynua is a Latin American digital identity and electronic signature platform that lets businesses design signing flows combining video, drawn, OTP, and digital signatures with biometric identity verification — liveness detection, facial matching, 3D and selfie identification, and geopositioning. Its REST API covers contracts, document templates, identity verification, OTP, and Deceval promissory notes, delivering requests to signers over WhatsApp, SMS, or email and emitting webhooks for asynchronous processing events. It supports 20+ Latin American identity documents across 20 countries and serves financial services, real estate, human resources, commercial contracts, and sports betting.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keynua.png
layout: provider
mcp_servers:
- description: ''
  name: keynua-mcp.yml
  slug: keynua-mcpyml
modified: '2026-07-19'
name: Keynua
nav: Providers
network: true
overview: 'Keynua publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Electronic Signature, Digital Signature, Identity Verification, and Biometrics.


  The Keynua catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Keynua''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, authentication, sandbox, and 16 more developer resources.'
random_paper: 37
score:
  band: developing
  composite: 44.4
  delta: 3.3
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 56.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 41.1
  provenance:
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/keynua/refs/heads/main/screenshots/keynua-2026-07-25T223656.png
security:
- kind: authentication
  name: Keynua Authentication
  slug: keynua-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Keynua Domain Security
  slug: keynua-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: keynua
tags:
- Company
- Electronic Signature
- Digital Signature
- Identity Verification
- Biometrics
- KYC
- Onboarding
- OTP
- Webhooks
- Latin America
website: https://www.keynua.com/en
---
