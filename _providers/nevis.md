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
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: REST API to automate the Nevis Authentication Cloud — passwordless registration, authentication and transaction signing (FIDO2 / passkeys, Access App, OATH TOTP, SMS OTP, recovery codes), user and aut
  name: Nevis Authentication Cloud REST API
  slug: nevis-authentication-cloud-rest-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nevis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nevis.net
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.nevis.net
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nevis.net/authcloud/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nevis.net/authcloud/api-doc/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nevis.net/authcloud/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://www.nevis.net/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nevissecurity
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nevis.net/en/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nevis.net/en/legal
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nevis.net
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.nevis.net/authcloud/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.nevis.net/authcloud/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nevis-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nevis-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/nevis-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nevis-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nevis-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nevis-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nevis-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nevis-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/nevis-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nevis-llms.txt
created: '2026-07-17'
description: Nevis (Nevis Security AG) is a Swiss customer identity and access management (CIAM) and passwordless authentication provider. Its Authentication Cloud adds passwordless login and transaction signing to applications using FIDO2 passkeys, the Nevis Access App device authenticator, OATH TOTP, SMS OTP and recovery codes, exposed through a versioned REST API and native iOS / Android Mobile Authentication SDKs. Nevis also offers the on-premises Identity Suite and Nevis ID, serving banks, insurers and government with secure, standards-based (FIDO2 / WebAuthn) authentication.
image: https://www.nevis.net/hubfs/Nevis/images/logotype.svg
layout: provider
mcp_servers:
- description: ''
  name: nevis-mcp.yml
  slug: nevis-mcpyml
modified: '2026-07-20'
name: Nevis
nav: Providers
network: true
overview: 'Nevis publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Authentication, Identity, Passwordless, and FIDO2.


  Nevis'' developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, authentication, sandbox, and 16 more developer resources.'
random_paper: 97
score:
  band: thin
  composite: 32.8
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 63.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 44.7
  previous_composite: 32.8
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Nevis Authentication
  slug: nevis-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nevis Domain Security
  slug: nevis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nevis
tags:
- Company
- Authentication
- Identity
- Passwordless
- FIDO2
- Passkeys
- CIAM
- Transaction Signing
- Security
website: https://www.nevis.net
---
