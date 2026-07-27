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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 26.9
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: Real-time WebSocket session API used by the Web SDK to connect a browser client to a Digital Person running on the Soul Machines session server. A session is authenticated with either an API key (conf
  name: Soul Machines Digital Person Session
  slug: soul-machines-digital-person-session
- description: REST/callback contract for building web services ("skills") that respond to a Digital Person's conversational user input — NLP-adapter skills, intent matching, and pre/post processing stages. Skills a
  name: Soul Machines Skills API
  slug: soul-machines-skills-api
artifact_total: 6
asyncapis:
- description: ''
  name: Soul Machines Skills Webhooks
  slug: soul-machines-skills-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soul-machines-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.soulmachines.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.soulmachines.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.soulmachines.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.soulmachines.com/web-sdk/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.soulmachines.com/web-sdk/
- group: operate
  title: ''
  type: Support
  url: https://support.soulmachines.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/soulmachines
- group: commercial
  title: ''
  type: Pricing
  url: https://www.soulmachines.com/studio-pricing
- group: start
  title: ''
  type: SignUp
  url: https://workforce.soulmachines.com/auth/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.soulmachines.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.soulmachines.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.soulmachines.com/trust-safety
- group: auth
  title: ''
  type: Compliance
  url: https://www.soulmachines.com/trust-safety
- group: build
  title: ''
  type: Packages
  url: packages/soul-machines-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/soul-machines-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/soul-machines-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/soul-machines-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/soul-machines-components.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/soul-machines-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/soul-machines-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/soul-machines-skills-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/soul-machines-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/soul-machines-llms.txt
created: '2026-07-17'
description: Soul Machines builds autonomously animated "Digital People" — AI-driven interactive avatars that combine a real-time facial/gesture animation engine with conversational AI so brands can deploy human-like agents for customer experience, sales, education, and health. Developers integrate Digital People through the Web SDK (a JavaScript library that renders and drives a Digital Person in the browser over a WebSocket session to the dh.soulmachines.cloud session server) and the Skills API (a REST/callback contract for building web services that supply the conversational responses a Digital Person speaks). Personas, API keys, and content are configured in DDNA Studio. Soul Machines was founded in Auckland, New Zealand and is a portfolio company of the SoftBank Vision Fund.
image: https://github.com/soulmachines.png
layout: provider
mcp_servers:
- description: ''
  name: soul-machines-mcp.yml
  slug: soul-machines-mcpyml
modified: '2026-07-21'
name: Soul Machines
nav: Providers
network: true
overview: 'Soul Machines publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Artificial Intelligence, Digital Humans, and Avatars.


  The Soul Machines catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Soul Machines'' developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 17 more developer resources.'
random_paper: 44
score:
  band: thin
  composite: 43.8
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 22.6
    developer_ergonomics: 65.2
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 43.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Soul Machines Authentication
  slug: soul-machines-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Soul Machines Domain Security
  slug: soul-machines-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: soul-machines
tags:
- Company
- Enterprise
- Artificial Intelligence
- Digital Humans
- Avatars
- Conversational AI
- Customer Experience
- SDK
- Web SDK
website: https://www.soulmachines.com
---
