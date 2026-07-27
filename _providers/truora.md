---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 77.9
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 6
  human_in_the_loop: 4
  name: Truora Agentic Access
  operation_count: 12
  slug: truora-agentic-access
  summary_line: 12 operations · 6 acting · 4 human-in-the-loop
api_count: 5
apis:
- description: API-key and web integration token management.
  name: Truora Account API
  slug: truora-account-api
- description: Background checks on persons, vehicles, and companies across LatAm.
  name: Truora Checks API
  slug: truora-checks-api
- description: Recurring re-checks of previously verified subjects.
  name: Truora Continuous Monitoring API
  slug: truora-continuous-monitoring-api
- description: Web and WhatsApp identity verification processes.
  name: Truora Digital Identity API
  slug: truora-digital-identity-api
- description: Document, facial, email, and phone validation (KYC).
  name: Truora Validators API
  slug: truora-validators-api
artifact_total: 16
asyncapis:
- description: ''
  name: Truora Webhooks
  slug: truora-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/truora-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/truora-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/truora-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/truora-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/truora-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/truora
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/truora
- group: company
  title: ''
  type: Website
  url: https://www.truora.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.truora.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/truora-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/truora-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/truora-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.truora.com/en
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/truora-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/truora-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/truora-packages.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/truora-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/truora-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/truora-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/truora-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/truora-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.truora.com/en/iso-27001-certification
- group: design
  title: ''
  type: DataModel
  url: data-model/truora-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/truora-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/truora-overlay.yaml
- group: design
  title: ''
  type: Components
  url: components/truora-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/truora-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://www.truora.com/es/politica-de-seguridad
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.truora.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.truora.com/guides/api_integration_guide/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.truora.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.truora.com/en/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://account.truora.com/account#/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.truora.com/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.truora.com/en/integral-privacy-notice
- group: operate
  title: ''
  type: Support
  url: https://www.truora.com/en/contact-sales
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/truora-api-docs/workspace/truora-api-docs
created: '2026-07-17'
description: Truora is a Latin American identity verification and fraud-prevention platform. Its REST APIs run background checks on people, vehicles, and companies across LatAm, validate documents/faces/email/phone for KYC, and orchestrate web and WhatsApp conversational onboarding flows. All requests authenticate with a Truora-API-Key header.
finops:
- name: Truora Finops
  service_category: Identity and Fraud Prevention
  slug: truora-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/truora.png
layout: provider
mcp_servers:
- description: ''
  name: truora-mcp.yml
  slug: truora-mcpyml
modified: '2026-07-17'
name: Truora
nav: Providers
network: true
overview: 'Truora publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account API, Checks API, Continuous Monitoring API, and 2 more. Tagged areas include Identity Verification, KYC, Background Checks, Fraud Prevention, and LatAm.


  The Truora catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Truora''s developer surface includes authentication, documentation, engineering blog, getting-started guide, API reference, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Truora Plans Pricing
  plan_count: 3
  slug: truora-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 2
  name: Truora Rate Limits
  slug: truora-rate-limits
scopes:
- name: Truora Scopes
  scope_count: 14
  slug: truora-scopes
  summary_line: 14 scopes · authorizationCode/ciba/refreshToken
score:
  band: strong
  composite: 68.5
  delta: 0.0
  facets:
    commercial_clarity: 100.0
    contract_quality: 68.3
    developer_ergonomics: 78.3
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 68.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Truora Authentication
  slug: truora-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Truora Domain Security
  slug: truora-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Truora Vulnerability Disclosure
  slug: truora-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Truora Trust Center
  slug: truora-trust-center
  summary_line: ISO 27001, ISO 30107, GDPR
slug: truora
tags:
- Identity Verification
- KYC
- Background Checks
- Fraud Prevention
- LatAm
- WhatsApp
website: https://www.truora.com/
---
