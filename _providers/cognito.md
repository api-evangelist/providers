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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: REST API for identity verification, KYC, and AML watchlist/PEP screening. JSON:API media type (application/vnd.api+json), date-based versioning via the Cognito-Version header, and HTTP request-signatu
  name: Cognito Identity Verification API
  slug: cognito-identity-verification-api
artifact_total: 6
asyncapis:
- description: ''
  name: Cognito Flow Webhooks
  slug: cognito-flow-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cognitohq.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://cognitohq.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://cognitohq.com/docs/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://cognitohq.com/docs/identity/id-verification-api-quickstart
- group: company
  title: ''
  type: Blog
  url: https://cognitohq.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://plaid.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.plaid.com/signup/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cognitohq.com/privacy-statement
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cognitohq.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://cognitohq.com/docs/guides/api-changelog
- group: operate
  title: ''
  type: Deprecation
  url: https://cognitohq.com/docs/guides/breaking-changes
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cognito-flow-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cognito-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cognito-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cognito-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cognito-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cognito-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/cognito-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cognito-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cognito-problem-types.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cognito-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://cognitohq.com/docs/guides/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cognito-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cognito-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cognito-llms.txt
- group: design
  title: ''
  type: Components
  url: components/cognito-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cognito-data-model.yml
created: '2026-07-17'
description: 'Cognito (cognitohq.com, operated by BlockScore, Inc.) is an identity verification, KYC, and AML compliance API provider that was backed by Y Combinator and Battery Ventures and acquired by Plaid in 2020. Its API turns a phone number, name, or ID document into a verified identity in under a minute, covering 209 countries and thousands of document types. Three developer products sit on one REST API: Identity (phone-first, frictionless verification), Flow (an all-in-one hosted / embeddable verification experience integrated in minutes with document and selfie checks), and Screening (watchlist, sanctions, and politically-exposed-person AML screening with daily re-scans across 20+ lists). The API is JSON:API (application/vnd.api+json), date-versioned via a Cognito-Version header, and authenticated with HTTP request signatures (HMAC-SHA256 over a digest of the body). It ships a sandbox host, signed webhooks, and client SDKs for seven languages.'
image: https://cognitohq.com/wp-content/themes/cognito/images/cognito-share.jpg
layout: provider
mcp_servers:
- description: ''
  name: cognito-mcp.yml
  slug: cognito-mcpyml
modified: '2026-07-18'
name: Cognito
nav: Providers
network: true
overview: 'Cognito publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity, Identity Verification, KYC, and AML.


  The Cognito catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cognito''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 20 more developer resources.'
random_paper: 59
score:
  band: developing
  composite: 47.7
  delta: -1.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 57.9
  previous_composite: 48.8
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cognito/refs/heads/main/screenshots/cognito-2026-07-25T210011.png
security:
- kind: authentication
  name: Cognito Authentication
  slug: cognito-authentication
  summary_line: httpSignature · 1 scheme
- kind: domain-security
  name: Cognito Domain Security
  slug: cognito-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cognito Vulnerability Disclosure
  slug: cognito-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: cognito
tags:
- Company
- Identity
- Identity Verification
- KYC
- AML
- Compliance
- Fraud Prevention
- Onboarding
- Watchlist Screening
- Know Your Customer
website: https://cognitohq.com/docs
---
