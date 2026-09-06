---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Single GraphQL endpoint (Elixir/Absinthe, introspection enabled) covering datasets, submissions, models, leaderboards, staking, and Compute webhooks for Numerai Classic, Signals, and Crypto Signals. A
  name: Numerai GraphQL API
  slug: numerai-graphql-api
artifact_total: 7
asyncapis:
- description: ''
  name: Numerai Webhooks
  slug: numerai-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://numer.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.numer.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.numer.ai
- group: docs
  title: ''
  type: APIReference
  url: https://api-tournament.numer.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.numer.ai/tournament/learn
- group: operate
  title: ''
  type: Support
  url: https://forum.numer.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/numerai
- group: start
  title: ''
  type: SignUp
  url: https://numer.ai/signup
- group: start
  title: ''
  type: Login
  url: https://numer.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://numer.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://numer.ai/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://numerai.statuspage.io
- group: auth
  title: ''
  type: Security
  url: https://docs.numer.ai/numerai-tournament/bounties
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/numerai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/numerai-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/numerai-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/numerai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/numerai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/numerai-scopes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/numerai-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/numerai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/numerai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/numerai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/numerai-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/numerai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/numerai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/numerai-cli.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/numerai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/numerai-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/numerai-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/numerai-data-model.yml
created: '2026-07-17'
description: Numerai is a San Francisco hedge fund that crowdsources its stock-market trading models from a global community of data scientists. Participants download obfuscated, regularized financial datasets, train machine-learning models, and submit predictions each weekly round through a single GraphQL API at api-tournament.numer.ai. Models are staked with the Ethereum-based NMR token and earn performance-based payouts for accurate, original signals. The platform spans Numerai Classic, Numerai Signals (bring-your-own stock signals), and Crypto Signals, with official Python tooling (numerapi, numerai-cli, numerai-tools) and cloud Compute Prediction Nodes for fully automated round submissions.
image: https://numer.ai/img/social-card.jpg
layout: provider
modified: '2026-07-20'
name: Numerai
nav: Providers
network: true
overview: 'Numerai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Machine-Learning, Data Science, and Hedge Fund.


  The Numerai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Numerai''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, CLI, and 25 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 150
  name: Numerai Rate Limits
  slug: numerai-rate-limits
scopes:
- name: Numerai Scopes
  scope_count: 8
  slug: numerai-scopes
  summary_line: 8 scopes
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 68.4
  previous_composite: 47.0
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/numerai/refs/heads/main/screenshots/numerai-2026-08-07T185729.png
security:
- kind: authentication
  name: Numerai Authentication
  slug: numerai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Numerai Domain Security
  slug: numerai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Numerai Vulnerability Disclosure
  slug: numerai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: numerai
tags:
- Company
- Fintech
- Machine-Learning
- Data Science
- Hedge Fund
- GraphQL
- Crypto
- Quantitative Finance
- Tournament
website: https://numer.ai
---
