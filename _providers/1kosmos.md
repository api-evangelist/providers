---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.9
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: 1Kosmos Agentic Access
  operation_count: 29
  slug: 1kosmos-agentic-access
  summary_line: 29 operations · 24 acting
api_count: 1
apis:
- description: 'The tenant-scoped REST surface of the 1Kosmos BlockID platform: identity verification (IDVerify) document-share sessions, identity assurance level (IAL) lookup, one-time passcode generation and verifi'
  name: 1Kosmos BlockID Platform API
  slug: 1kosmos-blockid
artifact_total: 6
asyncapis:
- description: ''
  name: 1Kosmos Idverify Events
  slug: 1kosmos-idverify-events
common:
- group: company
  title: ''
  type: Website
  url: https://www.1kosmos.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.1kosmos.com/devportal
- group: docs
  title: ''
  type: Documentation
  url: https://docs.1kosmos.com/productdocs/
- group: docs
  title: ''
  type: APIReference
  url: https://documenter.getpostman.com/view/50203634/2sB3dHWZ1n
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.1kosmos.com/devportal/docs/
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/50203634/2sB3dHWZ1n
- group: start
  title: ''
  type: SignUp
  url: https://developer.1kosmos.com/devportal/register/
- group: start
  title: ''
  type: Login
  url: https://developer.1kosmos.com/devportal/login/
- group: operate
  title: ''
  type: Support
  url: https://www.1kosmos.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.1kosmos.com/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/1Kosmos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.1kosmos.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.1kosmos.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.1kosmos.com/compliance
- group: start
  title: ''
  type: Sandbox
  url: sandbox/1kosmos-sandbox.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/1kosmos-blockid-openapi.yml
- group: build
  title: ''
  type: Packages
  url: packages/1kosmos-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/1kosmos-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/1kosmos-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/1kosmos-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/1kosmos-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/1kosmos-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/1kosmos-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/1kosmos-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/1kosmos-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/1kosmos-data-model.yml
- group: other
  title: ''
  type: EventCatalog
  url: asyncapi/1kosmos-idverify-events.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/1kosmos-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/1kosmos-blockid-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/1kosmos-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/1kosmos-agentic-access.yml
created: '2026-08-05'
description: 1Kosmos is a digital identity company whose BlockID platform combines identity proofing, document and biometric verification, and passwordless / FIDO2 authentication into a single tenant-scoped platform used across workforce, customer and citizen identity. The platform is delivered as a REST API surface (identity verification sessions, identity assurance level lookup, one-time passcodes, user management, access codes, W3C Verifiable Credentials and Verifiable Presentations, IAL2 identity-proofing workflows and reporting/metrics) plus first-party helper SDKs for NodeJS, Java, PHP, .NET, .NET Core and Go, and native Android/iOS mobile SDKs. 1Kosmos is Kantara-approved as a full-service credential service provider conformant with NIST SP 800-63-3 at IAL2/AAL2, is FIDO2 certified, holds SOC 2 Type II and ISO 27001, and holds a FedRAMP High authorization.
image: https://framerusercontent.com/images/CaZExN3h34OiuPCO41bzrgwhVc.png
layout: provider
modified: '2026-08-05'
name: 1Kosmos
nav: Providers
network: true
overview: '1Kosmos publishes 1 API on the [APIs.io](https://apis.io/) network: BlockID Platform API. Tagged areas include Identity, Authentication, Identity Verification, Passwordless, and Biometrics.


  The 1Kosmos catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  1Kosmos'' developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, sandbox, and 25 more developer resources.'
random_paper: 39
scopes:
- name: 1Kosmos Scopes
  scope_count: 3
  slug: 1kosmos-scopes
  summary_line: 3 scopes · authorizationCode/refreshToken
score:
  band: developing
  composite: 54.9
  facets:
    commercial_clarity: 31.6
    contract_quality: 73.5
    developer_ergonomics: 71.2
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 36.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: 1Kosmos Authentication
  slug: 1kosmos-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: 1Kosmos Domain Security
  slug: 1kosmos-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: 1kosmos
tags:
- Identity
- Authentication
- Identity Verification
- Passwordless
- Biometrics
- Verifiable Credentials
- FIDO2
- Security
- Company
website: https://www.1kosmos.com/
---
