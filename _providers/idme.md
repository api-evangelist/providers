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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.7
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: ID.me's OpenID Connect and OAuth 2.0 identity provider. Supports the authorization code flow (with PKCE), refresh tokens, encrypted ID tokens and userinfo, and returns verified identity attributes and
  name: ID.me OpenID Connect & OAuth 2.0 API
  slug: idme-openid-connect-oauth-20-api
- description: 'ID.me''s REST Services API for orchestrating identity verification: create and manage verifications, verify phone possession and identity via telecom endpoints, and verify identity documents (driver''s '
  name: ID.me Services API
  slug: idme-services-api
artifact_total: 8
asyncapis:
- description: ''
  name: Idme Services Webhooks
  slug: idme-services-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.id.me
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.id.me
- group: docs
  title: ''
  type: Documentation
  url: https://docs.id.me
- group: docs
  title: ''
  type: APIReference
  url: https://docs.id.me/services-api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.id.me/home
- group: operate
  title: ''
  type: Support
  url: https://docs.id.me/integrations/deploy-and-monitor/help
- group: operate
  title: ''
  type: StatusPage
  url: https://status.id.me
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/IDme
- group: start
  title: ''
  type: SignUp
  url: https://developers.id.me
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/idme-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/idme-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/idme-security.txt
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/idme-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/idme-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/idme-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/idme-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/idme-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/idme-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/idme-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/idme-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.id.me/guides/learn-more/digital-wallet/nist-ial-2
- group: start
  title: ''
  type: Sandbox
  url: sandbox/idme-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/idme-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/idme-packages.yml
- group: design
  title: ''
  type: Components
  url: components/idme-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/idme-services-webhooks.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/idme-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/idme-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.id.me/.well-known/security.txt
created: '2026-07-17'
description: ID.me is a digital identity network that provides NIST 800-63-3 IAL2/AAL2 identity verification, single sign-on, and group affiliation (community) verification for government agencies, healthcare, and commercial partners. For developers, ID.me exposes an OpenID Connect and OAuth 2.0 identity provider (authorization code flow with PKCE, plus SAML 2.0 federation), a REST Services API for telecom and document verification, an Applications API, a Document Passback API, and a Shared Signals Framework (SSF) event stream for fraud and verification signals. Native iOS and Android SDKs, a button widget, conversion tracking, and multi-language sample code round out the developer surface, letting relying parties add strong identity proofing and attribute exchange to any application or IAM platform (Okta, Keycloak, Entra, PingOne, AWS Cognito).
image: https://avatars.githubusercontent.com/u/295660?v=4
layout: provider
mcp_servers:
- description: ''
  name: idme-mcp.yml
  slug: idme-mcpyml
modified: '2026-07-19'
name: ID.me
nav: Providers
network: true
overview: 'ID.me publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity, Identity Verification, Authentication, and OpenID Connect.


  The ID.me catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ID.me''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, sandbox, and 22 more developer resources.'
random_paper: 67
scopes:
- name: Idme Scopes
  scope_count: 11
  slug: idme-scopes
  summary_line: 11 scopes · authorizationCode
score:
  band: developing
  composite: 50.3
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 51.6
    developer_ergonomics: 71.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 39.5
  previous_composite: 50.3
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 70.4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Idme Authentication
  slug: idme-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Idme Domain Security
  slug: idme-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Idme Vulnerability Disclosure
  slug: idme-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: idme
tags:
- Company
- Identity
- Identity Verification
- Authentication
- OpenID Connect
- OAuth 2.0
- SAML
- Single Sign-On
- Digital Identity
- KYC
- Fraud Prevention
- Government
website: https://www.id.me
---
