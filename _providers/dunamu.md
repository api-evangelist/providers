---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
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
  schema_version: 0.2
  score: 14.7
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dunamu-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/dunamu-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dunamu-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/dunamu-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dunamu-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dunamu-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dunamu-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.dunamu.com/en/about/company
- group: auth
  title: ''
  type: Authentication
  url: authentication/dunamu-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dunamu-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/dunamu-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dunamu-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dunamu-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dunamu-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dunamu-llms.txt
- group: company
  title: ''
  type: Website
  url: https://dunamu.com/
- group: company
  title: ''
  type: About
  url: https://dunamu.com/about/company
- group: start
  title: ''
  type: DeveloperPortal
  url: https://global-docs.upbit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://global-docs.upbit.com/reference
- group: docs
  title: ''
  type: APIReference
  url: https://global-docs.upbit.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://global-docs.upbit.com/docs/first-exchange-api-call
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/upbit-official
- group: company
  title: ''
  type: Blog
  url: https://blog.naver.com/dunamupr
- group: company
  title: ''
  type: News
  url: https://dunamu.com/news
- group: operate
  title: ''
  type: Support
  url: https://upbitcare.com
- group: company
  title: ''
  type: Careers
  url: https://dunamu.com/careers/jobs
- group: company
  title: ''
  type: InvestorRelations
  url: https://dunamu.com/ir/announcement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://upbit.com/terms_of_service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://upbit.com/privacy_policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://global-docs.upbit.com/changelog
- group: auth
  title: ''
  type: Authentication
  url: https://global-docs.upbit.com/reference/auth
- group: operate
  title: ''
  type: RateLimits
  url: https://global-docs.upbit.com/reference/rate-limits
- group: start
  title: ''
  type: SignUp
  url: https://sg.upbit.com/signup
- group: agent
  title: ''
  type: LLMsTxt
  url: https://global-docs.upbit.com/llms.txt
created: '2026-08-12'
description: Dunamu Inc. (두나무 주식회사) is a South Korean fintech and blockchain company founded in April 2012 and headquartered at 369 Gangnam-daero, Seocho-gu, Seoul. Dunamu operates Upbit, Korea's largest digital asset exchange (launched 2017, the country's first registered VASP), and Stockplus, a securities trading application launched in 2014, alongside Stockplus Unlisted for pre-IPO share trading. The group also spun out Lambda256 (blockchain infrastructure, now trading as Nodit) in 2019 and runs the Dunamu & Partners venture arm. Dunamu itself publishes no developer program at dunamu.com — its entire public API surface is served under the Upbit brand through the Upbit Developer Center, which offers REST and WebSocket APIs for market data, orders, accounts, deposits, withdrawals and Travel Rule compliance, plus first-party Python, TypeScript and Go SDKs, a CLI and packaged agent skills published from the upbit-official GitHub organization. That API surface is catalogued separately at the
  Upbit provider profile; this record profiles the corporate parent.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-08-12'
name: Dunamu
nav: Providers
network: true
overview: 'Dunamu is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Cryptocurrency, Digital Assets, Exchange, and Securities.


  Dunamu''s developer surface includes CLI, changelog, authentication, documentation, API reference, getting-started guide, engineering blog, and 28 more developer resources.'
plans:
- name: Dunamu Plans Pricing
  plan_count: 1
  slug: dunamu-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 11
  name: Dunamu Rate Limits
  slug: dunamu-rate-limits
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 47.0
    catalog_earned_first_party: 20.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 53.6
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 31.6
  provenance:
    conformance: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 46.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dunamu/refs/heads/main/screenshots/dunamu-2026-08-17T080906.png
security:
- kind: authentication
  name: Dunamu Authentication
  slug: dunamu-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dunamu Domain Security
  slug: dunamu-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dunamu
tags:
- Fintech
- Cryptocurrency
- Digital Assets
- Exchange
- Securities
- Trading
- Blockchain
- South Korea
- Company
website: https://dunamu.com/
---
