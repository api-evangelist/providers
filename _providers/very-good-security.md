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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.3
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Unique IDs that retain all the essential information about the data without compromising its security.
  name: Very Good Security aliases API
  slug: very-good-security-aliases-api
artifact_total: 8
asyncapis:
- description: ''
  name: Very Good Security Webhooks
  slug: very-good-security-webhooks
collections:
- collection_type: postman
  name: Vault HTTP aliases API
  slug: postman-very-good-security-aliases-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/very-good-security/overview
- group: build
  title: ''
  type: Packages
  url: packages/very-good-security-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/very-good-security-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/very-good-security-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/very-good-security-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/very-good-security-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/very-good-security-vault-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/very-good-security-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/very-good-security-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/very-good-security-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/very-good-security-scopes.yml
- group: build
  title: ''
  type: CLI
  url: cli/very-good-security-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/very-good-security-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/very-good-security-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/very-good-security-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/very-good-security-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/very-good-security-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/very-good-security-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/very-good-security-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/very-good-security-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/very-good-security-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.verygoodsecurity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.verygoodsecurity.com/
- group: docs
  title: ''
  type: APIReference
  url: https://www.verygoodsecurity.com/docs/vault/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.verygoodsecurity.com/docs/tokenization/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.verygoodsecurity.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/verygoodsecurity
- group: operate
  title: ''
  type: Support
  url: mailto:support@verygoodsecurity.com
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.verygoodsecurity.com/tokenization
- group: start
  title: ''
  type: Login
  url: https://dashboard.verygoodsecurity.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.verygoodsecurity.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.verygoodsecurity.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.verygoodsecurity.com/privacy-notice
- group: operate
  title: ''
  type: StatusPage
  url: https://status.verygoodsecurity.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.verygoodsecurity.com/
- group: auth
  title: ''
  type: Compliance
  url: https://security.verygoodsecurity.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.verygoodsecurity.com/overview/release-notes
created: '2026-07-17'
description: Very Good Security (VGS) is a data security and payments infrastructure company that lets organizations operate on sensitive data — payment card numbers, bank accounts, PII, and other regulated information — without the cost or liability of storing it themselves. Its core Vault tokenization platform substitutes sensitive values with format-preserving aliases so customer systems never touch raw data, dramatically reducing PCI DSS, SOC 2, HIPAA, and GDPR compliance scope. VGS also offers Zero Data (a proxy that keeps the customer environment entirely out of PCI scope), a Card Management Platform (network tokens, account updater, 3D Secure), and VGS Control for compliance automation. The developer surface includes the Vault HTTP API for aliases/tokenization, VGS Collect and VGS Show client SDKs, a Terraform provider, and the vgs-cli command line tool. Founded in 2015, VGS is backed by a16z and stores over 5 billion tokens.
image: https://www.verygoodsecurity.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: very-good-security-mcp.yml
  slug: very-good-security-mcpyml
modified: '2026-07-21'
name: Very Good Security
nav: Providers
network: true
overview: 'Very Good Security publishes 1 API on the [APIs.io](https://apis.io/) network: aliases API. Tagged areas include Company, Data Security, Tokenization, Payments, and Vault.


  The Very Good Security catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Very Good Security''s developer surface includes CLI, sandbox, changelog, authentication, documentation, API reference, getting-started guide, and 31 more developer resources.'
random_paper: 57
scopes:
- name: Very Good Security Scopes
  scope_count: 3
  slug: very-good-security-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: strong
  composite: 62.4
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 68.4
    developer_ergonomics: 86.4
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 62.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Very Good Security Authentication
  slug: very-good-security-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Very Good Security Domain Security
  slug: very-good-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Very Good Security Trust Center
  slug: very-good-security-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: very-good-security
tags:
- Company
- Data Security
- Tokenization
- Payments
- Vault
- PCI Compliance
- Data Privacy
- Card Management
- Network Tokens
- Security
website: https://docs.verygoodsecurity.com/
---
