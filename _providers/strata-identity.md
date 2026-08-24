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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Public management API for the Maverics platform, automated with confidential OAuth 2.0 client-credentials API clients (private_key_jwt / JWT client assertion, ES256). Region-specific auth surfaces are
  name: Maverics Console Management API
  slug: maverics-console-management-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://strata.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.strata.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.strata.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.strata.io/reference/console/api-clients
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.strata.io/guides/getting-started/quick-start
- group: operate
  title: ''
  type: Support
  url: https://www.strata.io/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.strata.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/strata-io
- group: operate
  title: ''
  type: StatusPage
  url: https://status.strata.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rubrik.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.strata.io/privacy-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.strata.io/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.strata.io/
- group: auth
  title: ''
  type: Security
  url: https://trust.strata.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.strata.io/changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/strata-identity-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/strata-identity-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/strata-identity-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/strata-identity-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/strata-identity-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/strata-identity-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/strata-identity-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/strata-identity-changelog.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/strata-identity-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/strata-identity-domain-security.yml
created: '2026-07-17'
description: Strata Identity is a multi-cloud identity orchestration and agentic AI security company whose Maverics platform lets organizations unify authentication and authorization across multiple clouds, identity providers, and applications, and govern AI agent access at runtime, without rewriting apps or consolidating identity providers. The platform pairs the Maverics Orchestrator, a lightweight identity abstraction layer that routes auth between apps and any IdP (SAML, OIDC, LDAP, Active Directory), with a hosted Maverics Console for visual configuration, policy, and lifecycle management. It adds SSO, MFA, and authorization policy to legacy and modern apps, provides identity continuity during IdP outages, and now secures MCP servers and AI agents through an AI Identity Gateway. The Console exposes a public management API automated with OAuth 2.0 client-credentials clients. Founded by CEO Eric Olden, co-author of the SAML standard and creator of the Identity Query Language (IDQL) and
  the open-source Hexa project; Strata is now part of Rubrik.
image: https://www.strata.io/wp-content/uploads/2025/07/Strata_Preview_Agentic.jpg
layout: provider
modified: '2026-07-21'
name: Strata Identity
nav: Providers
network: true
overview: 'Strata Identity publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity, Identity Orchestration, Authentication, and Authorization.


  Strata Identity''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 18 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 36.9
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 36.9
  provenance:
    conformance: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Strata Identity Authentication
  slug: strata-identity-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Strata Identity Domain Security
  slug: strata-identity-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Strata Identity Trust Center
  slug: strata-identity-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, CSA STAR
slug: strata-identity
tags:
- Company
- Identity
- Identity Orchestration
- Authentication
- Authorization
- Single Sign-On
- IAM
- SAML
- OpenID Connect
- AI Identity
- Security
website: https://strata.io
---
