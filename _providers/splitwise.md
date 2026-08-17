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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-08-17'
api_count: 7
apis:
- description: The comments API from Splitwise — 3 operation(s) for comments.
  name: Splitwise comments API
  slug: splitwise-comments-api
- description: The expenses API from Splitwise — 6 operation(s) for expenses.
  name: Splitwise expenses API
  slug: splitwise-expenses-api
- description: The friends API from Splitwise — 5 operation(s) for friends.
  name: Splitwise friends API
  slug: splitwise-friends-api
- description: 'A Group represents a collection of users who share expenses together. For example, some users use a Group to aggregate expenses related to a home. Others use it to represent a trip. Expenses assigned '
  name: Splitwise groups API
  slug: splitwise-groups-api
- description: The notifications API from Splitwise — 1 operation(s) for notifications.
  name: Splitwise notifications API
  slug: splitwise-notifications-api
- description: The other API from Splitwise — 2 operation(s) for other.
  name: Splitwise other API
  slug: splitwise-other-api
- description: Resources to access and modify user information.
  name: Splitwise users API
  slug: splitwise-users-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Splitwise comments API
  slug: open-splitwise-comments-api
- collection_type: open
  name: Splitwise comments expenses API
  slug: open-splitwise-expenses-api
- collection_type: open
  name: Splitwise comments friends API
  slug: open-splitwise-friends-api
- collection_type: open
  name: Splitwise comments groups API
  slug: open-splitwise-groups-api
- collection_type: open
  name: Splitwise comments notifications API
  slug: open-splitwise-notifications-api
- collection_type: open
  name: Splitwise comments other API
  slug: open-splitwise-other-api
- collection_type: open
  name: Splitwise comments users API
  slug: open-splitwise-users-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/splitwise-api-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/splitwise-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/splitwise-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/splitwise-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/splitwise-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/splitwise-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/splitwise-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/splitwise-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.splitwise.com/
- group: build
  title: ''
  type: Packages
  url: packages/splitwise-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/splitwise-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/splitwise-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/splitwise-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/splitwise-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/splitwise-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/splitwise-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/splitwise-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.splitwise.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.splitwise.com/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.splitwise.com/
- group: start
  title: ''
  type: SignUp
  url: https://secure.splitwise.com/apps
- group: company
  title: ''
  type: Blog
  url: https://blog.splitwise.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.splitwise.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.splitwise.com/privacy
- group: company
  title: ''
  type: Website
  url: https://www.splitwise.com
created: '2026-07-17'
description: Splitwise is an expense-sharing and bill-splitting service that helps roommates, travel groups, couples, and friends track shared costs and settle up fairly. Its public Self-Serve REST API (v3.0) lets third-party applications read and manage a user's groups, friends, expenses, comments, and notifications on that user's behalf, authenticating with OAuth 2.0 or a personal API key. Splitwise was added to the API Evangelist network from a venture-capital portfolio lead and has been enriched from its public developer documentation and OpenAPI specification.
image: https://www.splitwise.com/assets/press/logos/sw.svg
layout: provider
mcp_servers:
- description: ''
  name: splitwise-mcp.yml
  slug: splitwise-mcpyml
modified: '2026-07-21'
name: Splitwise
nav: Providers
network: true
overview: 'Splitwise publishes 7 APIs on the [APIs.io](https://apis.io/) network, including comments API, expenses API, friends API, and 4 more. Tagged areas include Company, Consumer, Expense Management, Personal Finance, and Bill Splitting.


  Splitwise''s developer surface includes authentication, documentation, API reference, signup flow, engineering blog, and 21 more developer resources.'
random_paper: 102
scopes:
- name: Splitwise Scopes
  scope_count: 0
  slug: splitwise-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.2
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.2
    developer_ergonomics: 40.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 26.3
  previous_composite: 45.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 64.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Splitwise Authentication
  slug: splitwise-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Splitwise Domain Security
  slug: splitwise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Splitwise Vulnerability Disclosure
  slug: splitwise-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: splitwise
tags:
- Company
- Consumer
- Expense Management
- Personal Finance
- Bill Splitting
- Payments
- REST API
- OAuth
website: https://www.splitwise.com
---
