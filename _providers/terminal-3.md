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
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Terminal 3 Agentic Access
  operation_count: 24
  slug: terminal-3-agentic-access
  summary_line: 24 operations · 13 acting
api_count: 7
apis:
- description: Decentralized identifier (DID) operations.
  name: Terminal 3 DID V1 API
  slug: terminal-3-did-v1-api
- description: OpenID Connect authorization, token, userinfo, and credential operations (v1).
  name: Terminal 3 OpenID Connect V1 API
  slug: terminal-3-openid-connect-v1-api
- description: OpenID Connect token and userinfo operations (v2).
  name: Terminal 3 OpenID Connect V2 API
  slug: terminal-3-openid-connect-v2-api
- description: Manage sub-clients under a Terminal 3 tenant.
  name: Terminal 3 Sub Client V1 API
  slug: terminal-3-sub-client-v1-api
- description: Create, update, and send transactional email templates.
  name: Terminal 3 Transactional Email Template V1 API
  slug: terminal-3-transactional-email-template-v1-api
- description: User creation and user data (social data, wallet addresses).
  name: Terminal 3 User V1 API
  slug: terminal-3-user-v1-api
- description: Verifiable Credential issuer operations.
  name: Terminal 3 VC V1 API
  slug: terminal-3-vc-v1-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Terminal 3 DID V1 API
  slug: open-terminal-3-did-v1-api
- collection_type: open
  name: Terminal 3 DID V1 OpenID Connect V1 API
  slug: open-terminal-3-openid-connect-v1-api
- collection_type: open
  name: Terminal 3 DID V1 OpenID Connect V2 API
  slug: open-terminal-3-openid-connect-v2-api
- collection_type: open
  name: Terminal 3 DID V1 Sub Client V1 API
  slug: open-terminal-3-sub-client-v1-api
- collection_type: open
  name: Terminal 3 DID V1 Transactional Email Template V1 API
  slug: open-terminal-3-transactional-email-template-v1-api
- collection_type: open
  name: Terminal 3 DID V1 User V1 API
  slug: open-terminal-3-user-v1-api
- collection_type: open
  name: Terminal 3 DID V1 VC V1 API
  slug: open-terminal-3-vc-v1-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/terminal-3-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/terminal-3-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/terminal-3-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/terminal-3-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://terminal3.io/security
- group: auth
  title: ''
  type: Compliance
  url: https://terminal3.io/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/terminal-3-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/terminal-3-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/terminal-3-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/terminal-3-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/terminal-3-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/terminal-3-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/terminal-3-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/terminal-3-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/terminal-3-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.terminal3.io
- group: design
  title: ''
  type: Conventions
  url: conventions/terminal-3-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/terminal-3-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/terminal-3-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/terminal-3-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.terminal3.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.terminal3.io
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.terminal3.io/developers/adk/get-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://t.me/terminal3developer
- group: company
  title: ''
  type: Blog
  url: https://blog.terminal3.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Terminal-3
- group: start
  title: ''
  type: SignUp
  url: https://docs.terminal3.io/developers/adk/get-started/prerequisites/request-test-tokens
- group: commercial
  title: ''
  type: TermsOfService
  url: https://terminal3.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://terminal3.io/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://terminal3.io
created: '2026-07-17'
description: Terminal 3 (T3) is a data-freedom and decentralized-identity company (founded 2023, Hong Kong) building privacy-preserving identity, verifiable credentials, and confidential computing infrastructure. Its products include T3 Verify (enterprise KYC/AML with real-time identity and liveness verification across 190+ countries and reusable verifiable credentials), T3 Identity (full-stack digital identity with passwordless auth, OpenID Connect SSO, decentralized identifiers, and verifiable credentials), Agent Command (secure, cryptographically verifiable AI-agent identity, permissions, and audit), and the T3 Network (T3N) — a hardware-secured confidential-computing network running tenant TEE contracts inside Intel TDX enclaves. Terminal 3 publishes a REST API (DID, OpenID Connect, verifiable credentials, sub-clients, transactional email, and user data) and an Agent Developer Kit (ADK) with a first-party TypeScript SDK family. Backed by 500 Global, ConsenSys Mesh, CMCC Global, Bixin
  Ventures, and Cherubic Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/terminal-3.png
layout: provider
mcp_servers:
- description: ''
  name: terminal-3-mcp.yml
  slug: terminal-3-mcpyml
modified: '2026-07-21'
name: Terminal 3
nav: Providers
network: true
overview: 'Terminal 3 publishes 7 APIs on the [APIs.io](https://apis.io/) network, including DID V1 API, OpenID Connect V1 API, OpenID Connect V2 API, and 4 more. Tagged areas include Company, Identity, Decentralized Identity, Verifiable Credentials, and OpenID Connect.


  Terminal 3''s developer surface includes authentication, changelog, sandbox, documentation, getting-started guide, support, engineering blog, and 24 more developer resources.'
random_paper: 62
score:
  band: developing
  composite: 42.6
  delta: 1.1
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 16.7
    contract_quality: 13.6
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 44.7
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Terminal 3 Authentication
  slug: terminal-3-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Terminal 3 Domain Security
  slug: terminal-3-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Terminal 3 Vulnerability Disclosure
  slug: terminal-3-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Terminal 3 Trust Center
  slug: terminal-3-trust-center
  summary_line: SOC 2, SOC 2 Type 1, ISO 27001
slug: terminal-3
tags:
- Company
- Identity
- Decentralized Identity
- Verifiable Credentials
- OpenID Connect
- KYC
- AML
- Confidential Computing
- AI Agents
- Privacy
- Web3
- DID
website: https://terminal3.io
---
