---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: 1Kosmos Agentic Access
  operation_count: 29
  slug: 1kosmos-agentic-access
  summary_line: 29 operations · 24 acting
api_count: 1
apis:
- description: The Access Code API from 1Kosmos — 2 operation(s) for access code.
  name: 1Kosmos Access Code API
  slug: 1kosmos-access-code-api
- description: The IAL API from 1Kosmos — 1 operation(s) for ial.
  name: 1Kosmos IAL API
  slug: 1kosmos-ial-api
- description: The IAL2 API from 1Kosmos — 2 operation(s) for ial2.
  name: 1Kosmos IAL2 API
  slug: 1kosmos-ial2-api
- description: The ID Verification API from 1Kosmos — 2 operation(s) for id verification.
  name: 1Kosmos ID Verification API
  slug: 1kosmos-id-verification-api
- description: The OTP API from 1Kosmos — 3 operation(s) for otp.
  name: 1Kosmos OTP API
  slug: 1kosmos-otp-api
- description: The Reports API from 1Kosmos — 7 operation(s) for reports.
  name: 1Kosmos Reports API
  slug: 1kosmos-reports-api
- description: The Set up API from 1Kosmos — 2 operation(s) for set up.
  name: 1Kosmos Set up API
  slug: 1kosmos-set-up-api
- description: The User Management API from 1Kosmos — 3 operation(s) for user management.
  name: 1Kosmos User Management API
  slug: 1kosmos-user-management-api
- description: The Verifiable Credentials API from 1Kosmos — 5 operation(s) for verifiable credentials.
  name: 1Kosmos Verifiable Credentials API
  slug: 1kosmos-verifiable-credentials-api
- description: The Workflow API API from 1Kosmos — 2 operation(s) for workflow api.
  name: 1Kosmos Workflow API API
  slug: 1kosmos-workflow-api-api
artifact_total: 27
asyncapis:
- description: ''
  name: 1Kosmos Idverify Events
  slug: 1kosmos-idverify-events
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: 1Kosmos BlockID Platform Access Code API
  slug: open-1kosmos-access-code-api
- collection_type: open
  name: 1Kosmos BlockID Platform IAL API
  slug: open-1kosmos-ial-api
- collection_type: open
  name: 1Kosmos BlockID Platform IAL2 API
  slug: open-1kosmos-ial2-api
- collection_type: open
  name: 1Kosmos BlockID Platform ID Verification API
  slug: open-1kosmos-id-verification-api
- collection_type: open
  name: 1Kosmos BlockID Platform OTP API
  slug: open-1kosmos-otp-api
- collection_type: open
  name: 1Kosmos BlockID Platform Reports API
  slug: open-1kosmos-reports-api
- collection_type: open
  name: 1Kosmos BlockID Platform Set up API
  slug: open-1kosmos-set-up-api
- collection_type: open
  name: 1Kosmos BlockID Platform User Management API
  slug: open-1kosmos-user-management-api
- collection_type: open
  name: 1Kosmos BlockID Platform Verifiable Credentials API
  slug: open-1kosmos-verifiable-credentials-api
- collection_type: open
  name: 1Kosmos BlockID Platform Workflow API API
  slug: open-1kosmos-workflow-api-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/1kosmos-mcp.yml
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
  url: openapi/_original/1kosmos-blockid-openapi.yml
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
mcp_servers:
- description: ''
  name: 1Kosmos MCP Server
  slug: 1kosmos-mcp-server
modified: '2026-08-05'
name: 1Kosmos
nav: Providers
network: true
overview: '1Kosmos publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Access Code API, IAL API, IAL2 API, and 7 more. Tagged areas include Identity, Authentication, Identity Verification, Passwordless, and Biometrics.


  The 1Kosmos catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  1Kosmos'' developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, sandbox, and 26 more developer resources.'
random_paper: 3
scopes:
- name: 1Kosmos Scopes
  scope_count: 3
  slug: 1kosmos-scopes
  summary_line: 3 scopes · authorizationCode/refreshToken
score:
  band: developing
  composite: 50.5
  coverage:
    artifact_dirs: 23
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 62.2
    developer_ergonomics: 72.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/1kosmos/refs/heads/main/screenshots/1kosmos-2026-08-07T160649.png
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
