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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: 'Swan''s Partner API is a GraphQL API for embedding banking: accounts and account holders, memberships, cards, SEPA credit transfers and direct debits, standing orders, merchant payments, onboarding, an'
  name: Swan Partner API
  slug: swan-partner-api
artifact_total: 6
asyncapis:
- description: ''
  name: Swan Webhooks
  slug: swan-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.swan.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.swan.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api-reference.swan.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.swan.io/developers
- group: start
  title: ''
  type: Console
  url: https://explorer.swan.io/
- group: operate
  title: ''
  type: Support
  url: https://support.swan.io/hc/en-150
- group: company
  title: ''
  type: Blog
  url: https://swan.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/swan-io
- group: commercial
  title: ''
  type: Pricing
  url: https://swan.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://swan.io/start-now
- group: start
  title: ''
  type: Login
  url: https://swan.io/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://swan.io/termsandconditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://swan.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.swan.io
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.swan.io/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.swan.io/
- group: build
  title: ''
  type: Packages
  url: packages/swan-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/swan-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/swan-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/swan-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/swan-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/swan-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/swan-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/swan-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/swan-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/swan-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/swan-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/swan-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/swan-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/swan-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swan-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/swan-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/swan-llms.txt
created: '2026-07-17'
description: Swan is a European banking-as-a-service (BaaS) and embedded-finance platform that lets software companies embed banking features -- business accounts with native IBANs, physical and virtual card programs, SEPA payments, direct debits, and white-labelled onboarding -- directly into their products through a single GraphQL API. Swan operates as a licensed electronic money institution authorised by France's ACPR (identifier 86245); client deposits are safeguarded with BNP Paribas and covered by the French FGDR deposit guarantee. Developers integrate via an OAuth 2.0 protected Partner GraphQL API (sandbox and live), a Testing API and Event Simulator for end-to-end sandbox testing, webhooks for external events, and first-party React/React Native tooling. Swan has issued over one million cards and serves platforms across accounting, treasury, proptech, HR-tech and travel.
image: https://avatars.githubusercontent.com/u/47886602?v=4
layout: provider
mcp_servers:
- description: ''
  name: swan-mcp.yml
  slug: swan-mcpyml
modified: '2026-07-21'
name: Swan
nav: Providers
network: true
overview: 'Swan publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking as a Service, Embedded Finance, Fintech, and Payments.


  The Swan catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Swan''s developer surface includes documentation, API reference, getting-started guide, developer console, support, engineering blog, pricing, and 26 more developer resources.'
random_paper: 143
scopes:
- name: Swan Scopes
  scope_count: 5
  slug: swan-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials/refreshToken
score:
  band: strong
  composite: 56.6
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 67.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 52.6
  previous_composite: 56.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Swan Authentication
  slug: swan-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Swan Domain Security
  slug: swan-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: swan
tags:
- Company
- Banking as a Service
- Embedded Finance
- Fintech
- Payments
- Cards
- SEPA
- GraphQL
- Europe
- Accounts
website: https://docs.swan.io/
---
