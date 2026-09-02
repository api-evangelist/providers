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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: 'Real-time speech-to-speech translation over a single persistent WebSocket connection, supporting consecutive and simultaneous modes. Authenticated with a JWT bearer token or API key passed as a query '
  name: Sanas Stream API
  slug: sanas-stream-api
- description: Server-side C++17 and Python SDK for real-time speech enhancement, accent translation, and language translation. Applications initialize the SDK with an API key, create an audio processor for a chosen
  name: Sanas Speech AI SDK
  slug: sanas-speech-ai-sdk
artifact_total: 6
asyncapis:
- description: 'Real-time speech-to-speech translation over a single persistent WebSocket connection. Supports consecutive and simultaneous modes. Modeled by API Evangelist from the published Sanas WebSocket API and '
  name: Sanas Stream API
  slug: sanas-stream-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://sanas.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.sanas.ai
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sanas.ai
- group: docs
  title: ''
  type: APIReference
  url: https://developer.sanas.ai/API-Reference/Overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.sanas.ai/Docs/Getting-Started/Quick-Start
- group: company
  title: ''
  type: Blog
  url: https://sanas.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://support.sanas.ai/support/home
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.sanas.ai/Docs/Resources/Pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.sanas.ai/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sanas.ai/legal-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sanas.ai/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.sanas.ai
- group: auth
  title: ''
  type: Compliance
  url: https://developer.sanas.ai/Docs/Enterprise/Compliance-and-Data-Residency
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.sanas.ai/Docs/Resources/Changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sanas-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/sanas-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sanas-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sanas-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sanas-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sanas-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sanas-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/sanas-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sanas-problem-types.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sanas-changelog.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/sanas-stream-asyncapi.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sanas-domain-security.yml
created: '2026-07-17'
description: Sanas is a real-time speech AI platform that removes communication barriers through accent translation, language translation, speech enhancement, and speech intelligence. Its developer platform exposes these capabilities as a server-side SDK (C++17 and Python) plus a persistent WebSocket Stream API for real-time speech-to-speech translation, letting teams add real-time speech processing to voice-agent and contact-center pipelines they already run. Models are billed per minute and run on Sanas Cloud or self-hosted infrastructure, serving healthcare, financial services, retail, travel, and telecommunications customers.
image: https://www.sanas.ai/static-image.jpg
layout: provider
modified: '2026-07-21'
name: Sanas
nav: Providers
network: true
overview: 'Sanas publishes 1 API on the [APIs.io](https://apis.io/) network: Stream API. Tagged areas include Company, Speech AI, Voice AI, Accent Translation, and Language Translation.


  The Sanas catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sanas'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 19 more developer resources.'
random_paper: 9
score:
  band: developing
  composite: 46.4
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 44.8
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 46.6
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sanas/refs/heads/main/screenshots/sanas-2026-08-17T081721.png
security:
- kind: authentication
  name: Sanas Authentication
  slug: sanas-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Sanas Domain Security
  slug: sanas-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Sanas Trust Center
  slug: sanas-trust-center
  summary_line: SOC 2 Type II, ISO 27001:2022, HIPAA, GDPR, PCI DSS, CCPA
slug: sanas
tags:
- Company
- Speech AI
- Voice AI
- Accent Translation
- Language Translation
- Speech Enhancement
- Real-Time Audio
- SDK
- WebSocket
- Contact Center
website: https://sanas.ai
---
