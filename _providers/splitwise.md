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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://secure.splitwise.com/api/v3.0
  baseurl_source: declared
  description: The comments API from Splitwise — 3 operation(s) for comments.
  name: Splitwise Comments API
  slug: splitwise-comments-api
- baseURL: https://secure.splitwise.com/api/v3.0
  baseurl_source: declared
  description: The expenses API from Splitwise — 6 operation(s) for expenses.
  name: Splitwise Expenses API
  slug: splitwise-expenses-api
- baseURL: https://secure.splitwise.com/api/v3.0
  baseurl_source: declared
  description: The friends API from Splitwise — 5 operation(s) for friends.
  name: Splitwise Friends API
  slug: splitwise-friends-api
- baseURL: https://secure.splitwise.com/api/v3.0
  baseurl_source: declared
  description: 'A Group represents a collection of users who share expenses together. For example, some users use a Group to aggregate expenses related to a home. Others use it to represent a trip. Expenses assigned '
  name: Splitwise Groups API
  slug: splitwise-groups-api
- baseURL: https://secure.splitwise.com/api/v3.0
  baseurl_source: declared
  description: The notifications API from Splitwise — 1 operation(s) for notifications.
  name: Splitwise Notifications API
  slug: splitwise-notifications-api
- baseURL: https://secure.splitwise.com/api/v3.0
  baseurl_source: declared
  description: The other API from Splitwise — 2 operation(s) for other.
  name: Splitwise Other API
  slug: splitwise-other-api
- baseURL: https://secure.splitwise.com/api/v3.0
  baseurl_source: declared
  description: Resources to access and modify user information.
  name: Splitwise Users API
  slug: splitwise-users-api
artifact_total: 20
collections:
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
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.splitwise.com/feed/
- group: other
  href: https://artifacts.apis.io/splitwise/overlays/splitwise-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/splitwise-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/splitwise/authentication/splitwise-authentication.yml
  title: ''
  type: Authentication
  url: authentication/splitwise-authentication.yml
- group: auth
  href: https://artifacts.apis.io/splitwise/scopes/splitwise-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/splitwise-scopes.yml
- group: design
  href: https://artifacts.apis.io/splitwise/conventions/splitwise-conventions.yml
  title: ''
  type: Conventions
  url: conventions/splitwise-conventions.yml
- group: design
  href: https://artifacts.apis.io/splitwise/errors/splitwise-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/splitwise-problem-types.yml
- group: design
  href: https://artifacts.apis.io/splitwise/data-model/splitwise-data-model.yml
  title: ''
  type: DataModel
  url: data-model/splitwise-data-model.yml
- group: design
  href: https://artifacts.apis.io/splitwise/conformance/splitwise-conformance.yml
  title: ''
  type: Conformance
  url: conformance/splitwise-conformance.yml
- group: design
  href: https://artifacts.apis.io/splitwise/lifecycle/splitwise-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/splitwise-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.splitwise.com/
- group: build
  href: https://artifacts.apis.io/splitwise/packages/splitwise-packages.yml
  title: ''
  type: Packages
  url: packages/splitwise-packages.yml
- group: agent
  href: https://artifacts.apis.io/splitwise/mcp/splitwise-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/splitwise-mcp.yml
- group: agent
  href: https://artifacts.apis.io/splitwise/llms/splitwise-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/splitwise-llms.txt
- group: agent
  href: https://artifacts.apis.io/splitwise/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/splitwise/well-known/splitwise-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/splitwise-well-known.yml
- group: auth
  href: https://artifacts.apis.io/splitwise/well-known/splitwise-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/splitwise-security.txt
- group: auth
  href: https://artifacts.apis.io/splitwise/security/splitwise-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/splitwise-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/splitwise/security/splitwise-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/splitwise-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/splitwise/security/splitwise-domain-security.yml
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
modified: '2026-10-06'
name: Splitwise
nav: Providers
network: true
overview: 'Splitwise publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Comments API, Expenses API, Friends API, and 4 more. Tagged areas include Company, Consumer, Expense Management, Personal Finance, and Bill Splitting.


  Splitwise''s developer surface includes authentication, documentation, API reference, signup flow, engineering blog, and 22 more developer resources.'
random_paper: 12
scopes:
- name: Splitwise Scopes
  scope_count: 0
  slug: splitwise-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 45.7
    developer_ergonomics: 42.3
    discoverability: 66.1
    operational_transparency: 26.3
  previous_composite: 39.9
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
    score: 36.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/splitwise/splitwise-2026-08-17T082029.png
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
skill_count: 2
skills:
- name: splitwise-check-group-balances
  slug: splitwise-check-group-balances
- name: splitwise-log-shared-expense
  slug: splitwise-log-shared-expense
slug: splitwise
tags:
- Company
- Consumer
- Expense Management
- Personal Finance
- Bill Splitting
- Payments
- REST API
- Authentication
website: https://www.splitwise.com
---
