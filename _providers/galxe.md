---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.1
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: Galxe's public GraphQL API for building web3 experiences — query credentials and eligibility, quests, spaces, loyalty-points leaderboards, and Starboard social/onchain influence metrics, and push cred
  name: Galxe Integration API
  slug: galxe-integration-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://galxe.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.galxe.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.galxe.com/galxe-integration/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.galxe.com/galxe-integration/api-reference/quest
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.galxe.com/galxe-integration/getting-started/quick-start
- group: operate
  title: ''
  type: Support
  url: https://docs.galxe.com/galxe-integration/resources/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.galxe.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Galxe
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.galxe.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.galxe.com/about/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.galxe.com/about/legal/privacy-policy
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/galxe/refs/heads/main/changelog/galxe-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/galxe-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/galxe/refs/heads/main/authentication/galxe-authentication.yml
  title: ''
  type: Authentication
  url: authentication/galxe-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/galxe/refs/heads/main/scopes/galxe-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/galxe-scopes.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/galxe/refs/heads/main/packages/galxe-packages.yml
  title: ''
  type: Packages
  url: packages/galxe-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/galxe/refs/heads/main/packages/galxe-packages.yml
  title: ''
  type: SDKs
  url: packages/galxe-packages.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/galxe/refs/heads/main/rate-limits/galxe-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/galxe-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/galxe/refs/heads/main/errors/galxe-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/galxe-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/galxe/refs/heads/main/conventions/galxe-conventions.yml
  title: ''
  type: Conventions
  url: conventions/galxe-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/galxe/refs/heads/main/conventions/galxe-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/galxe-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/galxe/refs/heads/main/lifecycle/galxe-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/galxe-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/galxe/refs/heads/main/data-model/galxe-data-model.yml
  title: ''
  type: DataModel
  url: data-model/galxe-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/galxe/refs/heads/main/conformance/galxe-conformance.yml
  title: ''
  type: Conformance
  url: conformance/galxe-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/galxe/refs/heads/main/mcp/galxe-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/galxe-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/galxe/refs/heads/main/llms/galxe-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/galxe-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/galxe/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/galxe/refs/heads/main/security/galxe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/galxe-domain-security.yml
created: '2026-07-17'
description: Galxe is a decentralized super app and one of web3's largest onchain distribution platforms, serving 14M+ Galxe ID users across a product suite of Quest, Passport, Score, Compass, and the Galxe Identity Protocol. For developers, Galxe exposes a public Integration GraphQL API (https://graphigo-business.prd.galaxy.eco/query) to query credentials, quests, spaces, loyalty-points leaderboards, and Starboard social metrics, plus a Credential API for pushing eligibility data, "Sign in with Galxe" OAuth 2.0 for identity, and a TypeScript SDK for the zero-knowledge Galxe Identity Protocol. API access uses a dashboard-issued access-token header with per-second rate limits and monthly quotas. Originally surfaced as a portfolio company of Multicoin Capital and enriched from Galxe's public developer documentation.
image: https://framerusercontent.com/assets/VIwrglmv5dnewbKhEV0KdBzBSAk.jpg
layout: provider
modified: '2026-07-19'
name: Galxe
nav: Providers
network: true
overview: 'Galxe publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto Web3, Digital Identity, Credentials, and Quests.


  Galxe''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, changelog, authentication, and 20 more developer resources.'
plans:
- name: Galxe Plans
  plan_count: 2
  slug: galxe-plans
random_paper: 1
rate_limits:
- limit_count: 2
  name: Galxe Rate Limits
  slug: galxe-rate-limits
scopes:
- name: Galxe Scopes
  scope_count: 12
  slug: galxe-scopes
  summary_line: 12 scopes · authorizationCode
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 53.0
    catalog_earned_first_party: 16.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 63.7
    discoverability: 75.9
    operational_transparency: 39.5
  previous_composite: 36.1
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/galxe/refs/heads/main/screenshots/galxe-2026-07-25T215406.png
security:
- kind: authentication
  name: Galxe Authentication
  slug: galxe-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Galxe Domain Security
  slug: galxe-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: galxe
tags:
- Company
- Crypto Web3
- Digital Identity
- Credentials
- Quests
- Loyalty
- GraphQL
- Authentication
- Blockchain
website: https://galxe.com
---
