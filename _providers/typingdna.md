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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 46.2
  scored_at: '2026-08-03'
api_count: 3
apis:
- description: Advanced routes for customisation
  name: TypingDNA advanced API
  slug: typingdna-advanced-api
- description: Optional routes
  name: TypingDNA optional API
  slug: typingdna-optional-api
- description: Main routes
  name: TypingDNA standard API
  slug: typingdna-standard-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/typingdna-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/typingdna-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/typingdna-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://typingdna.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.typingdna.com/clients/login
- group: docs
  title: ''
  type: Documentation
  url: https://api.typingdna.com/docs/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://api.typingdna.com/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.typingdna.com/docs/tutorials.html
- group: operate
  title: ''
  type: Support
  url: https://www.typingdna.com/contact
- group: company
  title: ''
  type: Blog
  url: https://blog.typingdna.com
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.typingdna.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TypingDNA
- group: commercial
  title: ''
  type: Pricing
  url: https://www.typingdna.com/pricing/auth-api
- group: start
  title: ''
  type: SignUp
  url: https://www.typingdna.com/clients/signup
- group: start
  title: ''
  type: Login
  url: https://www.typingdna.com/clients/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.typingdna.com/legal/authentication-API-standard-service-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.typingdna.com/legal/website-privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.typingdna.com
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/collections/48c757074b638c64b350
- group: auth
  title: ''
  type: Compliance
  url: https://www.typingdna.com/pricing/auth-api
- group: build
  title: ''
  type: Packages
  url: packages/typingdna-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/typingdna-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/typingdna-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/typingdna-verify-openid-configuration.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/typingdna-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/typingdna-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/typingdna-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/typingdna-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/typingdna-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/typingdna-scopes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/typingdna-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/typingdna-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/typingdna-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/typingdna-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: TypingDNA provides AI-based typing biometrics authentication, recognizing people by how they type on desktop and mobile keyboards. Its RESTful Authentication API enrolls and verifies typing patterns for fraud prevention, account-sharing detection and passwordless second factors, while Verify 2FA replaces SMS/email one-time codes with typing verification — standalone or as an OIDC authentication method for Okta, Ping Identity and Microsoft Entra ID. TypingDNA is certified for ISO 27001, ISO 27017 and ISO 27018.
image: https://www.typingdna.com/assets/images/default-meta-image.jpg
layout: provider
mcp_servers:
- description: ''
  name: typingdna-mcp.yml
  slug: typingdna-mcpyml
modified: '2026-07-21'
name: TypingDNA
nav: Providers
network: true
overview: 'TypingDNA publishes 3 APIs on the [APIs.io](https://apis.io/) network: advanced API, optional API, and standard API. Tagged areas include Company, Authentication, Biometrics, Typing Biometrics, and Two-Factor Authentication.


  TypingDNA''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 28 more developer resources.'
random_paper: 24
scopes:
- name: Typingdna Scopes
  scope_count: 3
  slug: typingdna-scopes
  summary_line: 3 scopes · authorizationCode/refreshToken/deviceCode/jwtBearer
score:
  band: strong
  composite: 56.0
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 58.9
    developer_ergonomics: 73.4
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 21.1
  previous_composite: 56.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Typingdna Authentication
  slug: typingdna-authentication
  summary_line: apiKey/http/openIdConnect · 4 schemes
- kind: domain-security
  name: Typingdna Domain Security
  slug: typingdna-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Typingdna Trust Center
  slug: typingdna-trust-center
  summary_line: ISO 27001, ISO 27017, ISO 27018
slug: typingdna
tags:
- Company
- Authentication
- Biometrics
- Typing Biometrics
- Two-Factor Authentication
- Identity
- Security
- Fraud Prevention
website: https://typingdna.com/
---
