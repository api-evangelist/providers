---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Galxe's public GraphQL API for building web3 experiences — query credentials and eligibility, quests, spaces, loyalty-points leaderboards, and Starboard social/onchain influence metrics, and push cred
  name: Galxe Integration API
  slug: galxe-integration-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/galxe/plans/galxe-plans.yml
  title: ''
  type: Plans
  url: plans/galxe-plans.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.galxe.com/galxe-integration/resources/rate-limits
- group: company
  title: ''
  type: Blog
  url: https://www.galxe.com/press
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
  href: https://artifacts.apis.io/galxe/changelog/galxe-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/galxe-changelog.yml
- group: auth
  href: https://artifacts.apis.io/galxe/authentication/galxe-authentication.yml
  title: ''
  type: Authentication
  url: authentication/galxe-authentication.yml
- group: auth
  href: https://artifacts.apis.io/galxe/scopes/galxe-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/galxe-scopes.yml
- group: build
  href: https://artifacts.apis.io/galxe/packages/galxe-packages.yml
  title: ''
  type: Packages
  url: packages/galxe-packages.yml
- group: build
  href: https://artifacts.apis.io/galxe/packages/galxe-packages.yml
  title: ''
  type: SDKs
  url: packages/galxe-packages.yml
- group: operate
  href: https://artifacts.apis.io/galxe/rate-limits/galxe-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/galxe-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/galxe/errors/galxe-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/galxe-error-codes.yml
- group: design
  href: https://artifacts.apis.io/galxe/conventions/galxe-conventions.yml
  title: ''
  type: Conventions
  url: conventions/galxe-conventions.yml
- group: design
  href: https://artifacts.apis.io/galxe/conventions/galxe-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/galxe-conventions.yml
- group: design
  href: https://artifacts.apis.io/galxe/lifecycle/galxe-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/galxe-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/galxe/data-model/galxe-data-model.yml
  title: ''
  type: DataModel
  url: data-model/galxe-data-model.yml
- group: design
  href: https://artifacts.apis.io/galxe/conformance/galxe-conformance.yml
  title: ''
  type: Conformance
  url: conformance/galxe-conformance.yml
- group: agent
  href: https://artifacts.apis.io/galxe/mcp/galxe-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/galxe-mcp.yml
- group: agent
  href: https://artifacts.apis.io/galxe/llms/galxe-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/galxe-llms.txt
- group: agent
  href: https://artifacts.apis.io/galxe/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/galxe/security/galxe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/galxe-domain-security.yml
created: '2026-07-17'
description: Galxe is a decentralized super app and one of web3's largest onchain distribution platforms, serving 14M+ Galxe ID users across a product suite of Quest, Passport, Score, Compass, and the Galxe Identity Protocol. For developers, Galxe exposes a public Integration GraphQL API (https://graphigo-business.prd.galaxy.eco/query) to query credentials, quests, spaces, loyalty-points leaderboards, and Starboard social metrics, plus a Credential API for pushing eligibility data, "Sign in with Galxe" OAuth 2.0 for identity, and a TypeScript SDK for the zero-knowledge Galxe Identity Protocol. API access uses a dashboard-issued access-token header with per-second rate limits and monthly quotas. Originally surfaced as a portfolio company of Multicoin Capital and enriched from Galxe's public developer documentation.
finops:
- has_sources: true
  method: derived
  name: Galxe Finops
  primary_unit: ''
  service_category: ''
  slug: galxe-finops
  template: true
image: https://framerusercontent.com/assets/VIwrglmv5dnewbKhEV0KdBzBSAk.jpg
layout: provider
modified: '2026-10-06'
name: Galxe
nav: Providers
network: true
overview: 'Galxe is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Web3, Digital Identity, Credentials, and Quests.


  Galxe''s developer surface includes pricing, engineering blog, documentation, API reference, getting-started guide, support, signup flow, and 23 more developer resources.'
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
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 53.0
    catalog_earned_first_party: 16.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 39.5
  previous_composite: 41.3
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/galxe/galxe-2026-07-25T215406.png
security:
- kind: authentication
  name: Galxe Authentication
  slug: galxe-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Galxe Domain Security
  slug: galxe-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: Check user eligibility for a Galxe credential
  slug: galxe-check-user-eligibility
- name: Push members into a Galxe API credential
  slug: galxe-push-credential-items
- name: Read Galxe quest status and space leaderboard
  slug: galxe-quest-leaderboard
slug: galxe
tags:
- Company
- Web3
- Digital Identity
- Credentials
- Quests
- Loyalty
- GraphQL
- OAuth
- Blockchain
- Authentication
website: https://galxe.com
---
