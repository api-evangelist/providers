---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for AIStrategyMiner tools and services as documented in the reference pages.
  name: AIStrategyMiner API
  slug: aistrategyminer-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/aistrategyminer-com/plans/aistrategyminer-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aistrategyminer-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/aistrategyminer-com/llms/aistrategyminer-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aistrategyminer-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/aistrategyminer-com/well-known/aistrategyminer-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aistrategyminer-com-security.txt
- group: agent
  href: https://artifacts.apis.io/aistrategyminer-com/well-known/aistrategyminer-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aistrategyminer-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aistrategyminer-com/hosts/aistrategyminer-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aistrategyminer-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aistrategyminer-com/vendors/aistrategyminer-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aistrategyminer-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aistrategyminer.com/en/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://aistrategyminer.com/en/legal/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aistrategyminer.com/en/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://aistrategyminer.com/en/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://aistrategyminer.com/ar/strategies/news
- group: start
  title: ''
  type: Login
  url: https://aistrategyminer.com/en/account/login
- group: docs
  title: ''
  type: Documentation
  url: https://aistrategyminer.com/en/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://aistrategyminer.com/en/docs/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://aistrategyminer.com/en/docs/reference/tools
- group: start
  title: ''
  type: GettingStarted
  url: https://aistrategyminer.com/en/docs/get-started/quickstart
- group: auth
  href: https://artifacts.apis.io/aistrategyminer-com/security/aistrategyminer-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aistrategyminer-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aistrategyminer-com/security/aistrategyminer-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aistrategyminer-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aistrategyminer.com/
created: '2026-11-01'
description: AIStrategyMiner provides AI‑powered tools for building, testing, and deploying automated trading strategies on MetaTrader 5. The platform offers a strategy generator that drafts candidate strategies using an AI assistant, a robust testing lab for stress‑testing and backtesting, and a suite of free tools for risk analysis, position sizing, and portfolio management. Users can explore guides, technical indicators, and detailed documentation to refine and export strategies to MT5 and other platforms. The service targets traders seeking data‑driven, automated solutions to enhance trading performance.
image: https://aistrategyminer.com/og/home.png
layout: provider
modified: '2026-11-01'
name: AIStrategyMiner
nav: Providers
network: true
overview: 'AIStrategyMiner is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Trading, Artificial Intelligence, Automation, MetaTrader, and Strategy.


  AIStrategyMiner''s developer surface includes pricing, documentation, changelog, API reference, getting-started guide, and 14 more developer resources.'
plans:
- name: Aistrategyminer Com Plans Pricing
  plan_count: 3
  slug: aistrategyminer-com-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 20.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.7
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 58.0
    operational_transparency: 13.2
  previous_composite: 30.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 19.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aistrategyminer Com Domain Security
  slug: aistrategyminer-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aistrategyminer Com Vulnerability Disclosure
  slug: aistrategyminer-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: aistrategyminer-com
tags:
- Trading
- Artificial Intelligence
- Automation
- MetaTrader
- Strategy
website: https://aistrategyminer.com/
---
