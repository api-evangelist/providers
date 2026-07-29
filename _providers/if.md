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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'Single REST API for the Integrated Finance platform — clients, users, real / virtual / shared-pool accounts, bank transfers, currency exchanges, card issuing and processing, beneficiary verification, '
  name: Integrated Finance API
  slug: integrated-finance-api
artifact_total: 6
asyncapis:
- description: ''
  name: If Webhooks
  slug: if-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://integrated.finance
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.integrated.finance
- group: docs
  title: ''
  type: Documentation
  url: https://developer.integrated.finance/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.integrated.finance/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.integrated.finance/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://integrated.finance/support
- group: company
  title: ''
  type: Blog
  url: https://integrated.finance/insights
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/integrated-finance
- group: operate
  title: ''
  type: StatusPage
  url: https://integratedfinance.statuspage.io
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.integrated.finance/docs/changes-to-the-api
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://integrated.finance/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://integrated.finance/terms-and-conditions
- group: auth
  title: ''
  type: Compliance
  url: https://integrated.finance/security-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/if-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/if-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/if-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/if-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/if-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/if-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/if-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/if-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/if-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/if-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/if-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/if-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/if-domain-security.yml
created: '2026-07-17'
description: Integrated Finance (IF) is a modular fintech infrastructure platform — a "financial operating system" — that lets companies build banking, card, and payment experiences for their users without becoming a bank. Its orchestration layers (IF API interface, IF CORE workflow, IF CONNECT integration) sit on top of multiple banking, card-issuing, FX, and compliance providers and expose a single REST API covering clients and users, real / virtual / shared-pool accounts, incoming and outgoing bank transfers, currency exchanges, card issuing and processing (including 3DS and PIN management), beneficiary verification, generic transactions, and open-banking consents. Authentication is OAuth 2.0 on Keycloak (JWT client assertion, client_credentials); the API supports idempotency on all POST endpoints, Ed25519-signed webhooks with automatic retry, and a full sandbox environment for testing.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/if.png
layout: provider
mcp_servers:
- description: ''
  name: if-mcp.yml
  slug: if-mcpyml
modified: '2026-07-19'
name: IF
nav: Providers
network: true
overview: 'IF publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Embedded Finance, Banking as a Service, and Payments.


  The IF catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  IF''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 19 more developer resources.'
random_paper: 47
scopes:
- name: If Scopes
  scope_count: 11
  slug: if-scopes
  summary_line: 11 scopes · clientCredentials
score:
  band: developing
  composite: 52.0
  delta: 4.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 51.6
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 52.6
  previous_composite: 47.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 75.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/if/refs/heads/main/screenshots/if-2026-07-25T222048.png
security:
- kind: authentication
  name: If Authentication
  slug: if-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: If Domain Security
  slug: if-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: if
tags:
- Company
- Financial Services
- Embedded Finance
- Banking as a Service
- Payments
- Cards
- Foreign Exchange
- Compliance
- Open Banking
- API
website: https://integrated.finance
---
