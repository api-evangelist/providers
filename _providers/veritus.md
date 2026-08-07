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
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-08-06'
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
random_paper: 108
score:
  band: developing
  composite: 46.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 65.2
    developer_ergonomics: 29.9
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 23.7
  previous_composite: 46.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
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
