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
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.8
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: HTTP RPC-style API for age gates, age verification, verifiable parental consent, k-ID sessions, and permission management. Methods take the form https://game-api.k-id.com/api/v1/{method} with bearer A
  name: k-ID API
  slug: k-id-api
artifact_total: 6
asyncapis:
- description: ''
  name: K Id Webhooks
  slug: k-id-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.k-id.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.k-id.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.k-id.com/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.k-id.com/get-started/overview
- group: operate
  title: ''
  type: Support
  url: https://k-id.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://product.k-id.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kidentify
- group: commercial
  title: ''
  type: TermsOfService
  url: https://k-id.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://k-id.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://portal.k-id.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.k-id.com
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/k-id-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.k-id.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/k-id-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/k-id-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/k-id-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/k-id-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/k-id-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/k-id-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/k-id-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/k-id-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/k-id-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/k-id-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/k-id-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/k-id-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/k-id-domain-security.yml
created: '2026-07-17'
description: k-ID is a compliance platform that lets games, social apps, AI products, and commerce deliver age-appropriate experiences across 200+ jurisdictions. Its Compliance Development Kit (CDK) encodes auto-updating regulatory logic for regimes like COPPA, GDPR-Kids, the UK Age Appropriate Design Code and Online Safety Act, Brazil's ECA Digital, and Australia's minimum-age rules, while AgeKit and AgeKit+ provide privacy-preserving age assurance (facial age estimation, ID checks, credit card, AgeKey reusable credentials) and Family Connect handles verifiable parental consent. Developers integrate through the k-ID HTTP RPC API (game-api.k-id.com) using bearer API keys, hosted widget URLs, HMAC-signed webhooks, and official Agent Skills for AI coding tools.
image: https://avatars.githubusercontent.com/kidentify
layout: provider
mcp_servers:
- description: ''
  name: k-id-mcp.yml
  slug: k-id-mcpyml
modified: '2026-07-20'
name: k-ID
nav: Providers
network: true
overview: 'k-ID publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Age Verification, Age Assurance, Compliance, and Parental Consent.


  The k-ID catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  k-ID''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 20 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 43.6
  delta: -6.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 45.1
    developer_ergonomics: 59.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 50.0
  previous_composite: 49.6
  provenance:
    conformance: derived
    mcp: derived
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/k-id/refs/heads/main/screenshots/k-id-2026-08-17T123933.png
security:
- kind: authentication
  name: K Id Authentication
  slug: k-id-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: K Id Domain Security
  slug: k-id-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: K Id Trust Center
  slug: k-id-trust-center
  summary_line: trust center published
slug: k-id
tags:
- Company
- Age Verification
- Age Assurance
- Compliance
- Parental Consent
- Child Safety
- Identity
- Privacy
- Regulatory Technology
- Gaming
website: https://portal.k-id.com
---
