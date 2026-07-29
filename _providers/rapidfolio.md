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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Runner API and Dashboard API for programmatically running procedures, managing runs, submitting human-review decisions, managing API keys, and subscribing to run events via webhooks.
  name: Rapidfolio API
  slug: rapidfolio-api
artifact_total: 5
asyncapis:
- description: ''
  name: Rapidfolio Webhooks
  slug: rapidfolio-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rapidfolio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/rapidfolio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rapidfolio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rapidfolio.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.rapidfolio.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rapidfolio.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.rapidfolio.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rapidfolio.com/docs/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://app.rapidfolio.com/signin
- group: operate
  title: ''
  type: Support
  url: https://rapidfolio.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rapidfolio.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rapidfolio.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rapidfolio
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rapidfolio-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rapidfolio-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/rapidfolio-security.txt
- group: build
  title: ''
  type: Packages
  url: packages/rapidfolio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rapidfolio-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rapidfolio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rapidfolio-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/rapidfolio-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/rapidfolio-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/rapidfolio-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rapidfolio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/rapidfolio-conformance.yml
created: '2026-07-17'
description: Rapidfolio is an AI operations platform for financial-services companies that automates back-office workflows — KYC/KYB and identity verification, lending underwriting, payment-dispute and fraud investigation, reconciliation, and OFAC/sanctions and regulatory reviews. Teams define procedures as visual workflow graphs (Tool Call, Human Review, Wait, and Condition nodes) and Rapidfolio's AI agent executes them with deterministic, auditable outputs and a complete per-run step log. It ships isolated Sandbox and Live environments, a Runner API and Dashboard API (API-key auth), HMAC-SHA256-signed webhooks, human-review approvals with idempotency keys, a Node.js Connection SDK for private connections to internal services, and 20+ built-in integrations (Slack, Jira, Linear, Stripe, GoCardless, Onfido, Alloy, Flagright, Xero). A Y Combinator (Summer 2026) company based in San Francisco.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rapidfolio.png
layout: provider
modified: '2026-07-20'
name: Rapidfolio
nav: Providers
network: true
overview: 'Rapidfolio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Fintech, Workflow Automation, and Artificial Intelligence.


  The Rapidfolio catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Rapidfolio''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, sandbox, and 18 more developer resources.'
random_paper: 64
score:
  band: developing
  composite: 46.3
  delta: 8.5
  facets:
    commercial_clarity: 42.1
    contract_quality: 51.6
    developer_ergonomics: 63.0
    discoverability: 77.8
    governance: 12.5
    operational_transparency: 23.7
  previous_composite: 37.8
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
security:
- kind: authentication
  name: Rapidfolio Authentication
  slug: rapidfolio-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Rapidfolio Domain Security
  slug: rapidfolio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rapidfolio Vulnerability Disclosure
  slug: rapidfolio-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: rapidfolio
tags:
- Company
- Financial Services
- Fintech
- Workflow Automation
- Artificial Intelligence
- Agents
- Compliance
- KYC
- Fraud
- Back Office
website: https://rapidfolio.com
---
