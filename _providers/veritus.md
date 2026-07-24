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
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: true
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 46.2
  scored_at: '2026-07-23'
api_count: 4
apis:
- description: The Calls API from Veritus — 2 operation(s) for calls.
  name: Veritus Calls API
  slug: veritus-calls-api
- description: The Clients API from Veritus — 1 operation(s) for clients.
  name: Veritus Clients API
  slug: veritus-clients-api
- description: The Customers API from Veritus — 12 operation(s) for customers.
  name: Veritus Customers API
  slug: veritus-customers-api
- description: The Interactions API from Veritus — 1 operation(s) for interactions.
  name: Veritus Interactions API
  slug: veritus-interactions-api
artifact_total: 8
asyncapis:
- description: Outbound webhooks Veritus Agent POSTs to a subscriber-supplied URL when calls complete or drip-campaign events occur. Payloads are signed with HMAC SHA-256. Register a webhook by supplying `webhook.ur
  name: Veritus Agent Webhooks
  slug: veritus-webhooks-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://veritus.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.veritus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.veritus.com/
- group: start
  title: ''
  type: SignUp
  url: https://app.veritus.com/try
- group: start
  title: ''
  type: Login
  url: https://app.veritus.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://veritus.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://veritus.com/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/veritus-agent
- group: auth
  title: ''
  type: Authentication
  url: authentication/veritus-authentication.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/veritus-conventions.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.veritus.com/
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/veritus-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/veritus-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/veritus-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/veritus-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/veritus-domain-security.yml
created: '2026-07-17'
description: Veritus (Veritus Agent) is a San Francisco fintech (Y Combinator S2025) building compliant, voice-first AI agents for the consumer-lending lifecycle - origination, servicing, and collections. Its omnichannel platform places AI voice calls, SMS, and email to borrowers, running every contact through a built-in compliance engine (respectful hours, frequency limits, cease-and-desist, model-validation notices) before outreach. The REST API (OpenAPI 3.1, bearer auth, isolated sandbox and production environments, HMAC-signed webhooks) lets lenders, servicers, and collections agencies create customers, place compliance-checked calls, run omnichannel drip campaigns, import and analyze SMS/email interactions, and retrieve call recordings.
image: https://veritus.com/apple-touch-icon.png
layout: provider
modified: '2026-07-21'
name: Veritus
nav: Providers
network: true
overview: 'Veritus publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Calls API, Clients API, Customers API, and 1 more. Tagged areas include Company, Fintech, Consumer Lending, Collections, and AI Agents.


  The Veritus catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Veritus'' developer surface includes documentation, signup flow, authentication, and 14 more developer resources.'
random_paper: 21
score:
  band: developing
  composite: 45.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.0
    developer_ergonomics: 34.8
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 45.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Veritus Authentication
  slug: veritus-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Veritus Domain Security
  slug: veritus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Veritus Trust Center
  slug: veritus-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, PCI DSS, HIPAA, EU AI Act
slug: veritus
tags:
- Company
- Fintech
- Consumer Lending
- Collections
- AI Agents
- Voice AI
- Communications
- Compliance
website: https://veritus.com/
---
