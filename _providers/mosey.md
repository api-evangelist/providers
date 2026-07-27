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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 65.4
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Mosey Agentic Access
  operation_count: 52
  slug: mosey-agentic-access
  summary_line: 52 operations · 29 acting
api_count: 12
apis:
- description: The Accounts API from Mosey — 7 operation(s) for accounts.
  name: Mosey Accounts API
  slug: mosey-accounts-api
- description: The Agency Accounts API from Mosey — 2 operation(s) for agency accounts.
  name: Mosey Agency Accounts API
  slug: mosey-agency-accounts-api
- description: The Auth API from Mosey — 2 operation(s) for auth.
  name: Mosey Auth API
  slug: mosey-auth-api
- description: The Documents API from Mosey — 1 operation(s) for documents.
  name: Mosey Documents API
  slug: mosey-documents-api
- description: The Handbook API from Mosey — 3 operation(s) for handbook.
  name: Mosey Handbook API
  slug: mosey-handbook-api
- description: The Legal Entity API from Mosey — 2 operation(s) for legal entity.
  name: Mosey Legal Entity API
  slug: mosey-legal-entity-api
- description: The Locations API from Mosey — 7 operation(s) for locations.
  name: Mosey Locations API
  slug: mosey-locations-api
- description: The Logins API from Mosey — 4 operation(s) for logins.
  name: Mosey Logins API
  slug: mosey-logins-api
- description: The Mail API from Mosey — 2 operation(s) for mail.
  name: Mosey Mail API
  slug: mosey-mail-api
- description: The Regions API from Mosey — 2 operation(s) for regions.
  name: Mosey Regions API
  slug: mosey-regions-api
- description: The Signup API from Mosey — 3 operation(s) for signup.
  name: Mosey Signup API
  slug: mosey-signup-api
- description: The Tasks API from Mosey — 9 operation(s) for tasks.
  name: Mosey Tasks API
  slug: mosey-tasks-api
artifact_total: 16
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mosey-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.mosey.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mosey.com/api-reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mosey.com/api-reference/introduction
- group: company
  title: ''
  type: Blog
  url: https://mosey.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://mosey.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.mosey.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.mosey.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mosey.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mosey.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mosey-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/mosey-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mosey-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mosey-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/mosey-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/mosey-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mosey-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mosey-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mosey-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/mosey-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mosey-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Mosey is a business compliance platform that helps multi-state companies open and manage state and local tax, HR, payroll, insurance, and registration accounts. The Mosey API is a composable set of OpenAPI 3.1 endpoints that let software platforms embed state compliance into their own products: sign up or authenticate a legal entity, register the states it operates in, generate and resolve compliance tasks, receive physical mail, and securely manage state-agency logins via short-lived hosted sessions. Authentication is OAuth2 (password grant). Mosey partnered with Gusto, Stripe, and Sequoia Consulting Group and was subsequently acquired by Gusto. This profile was surfaced as a Canaan Partners portfolio company and enriched by the API Evangelist pipeline from Mosey''s public OpenAPI and developer documentation.'
image: https://mosey.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: mosey-mcp.yml
  slug: mosey-mcpyml
modified: '2026-07-20'
name: Mosey
nav: Providers
network: true
overview: 'Mosey publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Agency Accounts API, Auth API, and 9 more. Tagged areas include Company, Compliance, Regulatory Technology, State Compliance, and Tax.


  Mosey''s developer surface includes documentation, API reference, engineering blog, pricing, signup flow, authentication, and 16 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 41.9
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 50.1
    developer_ergonomics: 52.2
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 41.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Mosey Authentication
  slug: mosey-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Mosey Domain Security
  slug: mosey-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mosey
tags:
- Company
- Compliance
- Regulatory Technology
- State Compliance
- Tax
- Payroll
- HR
- Business Operations
website: https://docs.mosey.com
---
