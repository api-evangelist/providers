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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Conga Advantage Platform REST API exposes Conga's Revenue Lifecycle Management services - Contract Lifecycle Management (CLM), cart/CPQ, catalog, user management, X-Author authoring, document- and
  name: Conga Advantage Platform REST API
  slug: conga-advantage-platform-rest-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/conga-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://conga.com/vulnerability-disclosure
- group: company
  title: ''
  type: Website
  url: https://www.conga.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.conga.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.conga.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.conga.com/platform/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.conga.com/revenue/docs/user-authentication-to-conga-platform
- group: auth
  title: ''
  type: Authentication
  url: authentication/conga-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/conga-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/conga-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/conga-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/conga-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/conga-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.conga.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/conga-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/conga-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://conga.com/trust-compliance-center
- group: auth
  title: ''
  type: TrustCenter
  url: security/conga-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/conga-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/conga-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/conga-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/conga-sandbox.yml
- group: operate
  title: ''
  type: Support
  url: https://conga.com/support
- group: company
  title: ''
  type: Blog
  url: https://conga.com/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://conga.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://conga.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://conga.com/privacy
created: '2026-07-17'
description: Conga (formerly Apttus + Conga) is an enterprise Revenue Lifecycle Management vendor whose Conga Advantage Platform unifies Configure-Price-Quote (CPQ), Contract Lifecycle Management (CLM), document generation and e-signature, X-Author authoring, and AI-assisted contract intelligence. The platform exposes a broad RESTful API surface (CLM, cart/CPQ, catalog, user-management, document- and conversion-management, e-sign, search, scheduler, and extensibility services) documented on a public ReadMe-hosted developer portal at developer.conga.com. APIs use OAuth 2.0 bearer tokens minted through region-specific Conga login services, JSON request/response bodies, cursor-free page/limit pagination with Content-Range headers, URI filtering, and a JSON:API error envelope. Conga is backed by ICONIQ Capital and Insight Partners.
image: https://conga.com/sites/default/files/styles/large/public/image/2026-03/Social%20Share%20%281%29%20%281%29.png?itok=uH7gF5iu
layout: provider
modified: '2026-07-18'
name: Conga
nav: Providers
network: true
overview: 'Conga publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise Software, Contract Lifecycle Management, CPQ, and Revenue Lifecycle Management.


  Conga''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, support, and 20 more developer resources.'
random_paper: 28
rate_limits:
- limit_count: 0
  name: Conga Rate Limits
  slug: conga-rate-limits
scopes:
- name: Conga Scopes
  scope_count: 11
  slug: conga-scopes
  summary_line: 11 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 36.9
  delta: 1.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 42.1
  previous_composite: 35.9
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/conga/refs/heads/main/screenshots/conga-2026-07-25T210254.png
security:
- kind: authentication
  name: Conga Authentication
  slug: conga-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Conga Domain Security
  slug: conga-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Conga Vulnerability Disclosure
  slug: conga-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Conga Trust Center
  slug: conga-trust-center
  summary_line: SOC 1 Type 2, SOC 2 Type 2, ISO 27001, ISO 27701, HIPAA, GDPR, CCPA, PCI
slug: conga
tags:
- Company
- Enterprise Software
- Contract Lifecycle Management
- CPQ
- Revenue Lifecycle Management
- Document Automation
- E-Signature
- Contract Intelligence
- CRM
website: https://www.conga.com/
---
