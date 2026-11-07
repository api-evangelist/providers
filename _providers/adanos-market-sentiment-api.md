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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.4
  scored_at: '2026-11-06'
api_count: 7
apis:
- baseURL: https://api.adanos.org
  baseurl_source: declared
  description: Direct finance-tuned sentiment analysis for client-provided trading, market and investment text.
  name: Adanos Market Sentiment API Finance Sentiment API
  slug: adanos-market-sentiment-api-finance-sentiment-api
- baseURL: https://api.adanos.org
  baseurl_source: declared
  description: Operational health and freshness checks. Useful for monitoring, not required for normal client integrations.
  name: Adanos Market Sentiment API Health Check API
  slug: adanos-market-sentiment-api-health-check-api
- baseURL: https://api.adanos.org
  baseurl_source: declared
  description: Editorial/news sentiment with source breadth. Use `source` on supported endpoints to isolate a publisher or canonical source id.
  name: Adanos Market Sentiment API News Stocks API
  slug: adanos-market-sentiment-api-news-stocks-api
- baseURL: https://api.adanos.org
  baseurl_source: declared
  description: Prediction-market based stock sentiment and attention from Polymarket prices, trades, liquidity and orderbook signals. Metrics are market-centric rather than mention-based.
  name: Adanos Market Sentiment API Polymarket Stocks API
  slug: adanos-market-sentiment-api-polymarket-stocks-api
- baseURL: https://api.adanos.org
  baseurl_source: declared
  description: Crypto sentiment on Reddit with the same discovery/search/compare pattern as the stock APIs.
  name: Adanos Market Sentiment API Reddit Crypto API
  slug: adanos-market-sentiment-api-reddit-crypto-api
- baseURL: https://api.adanos.org
  baseurl_source: declared
  description: Retail stock discussion data from Reddit. Start with `/trending`, then drill into `/stock/{ticker}` or build watchlists with `/compare`.
  name: Adanos Market Sentiment API Reddit Stocks API
  slug: adanos-market-sentiment-api-reddit-stocks-api
- baseURL: https://api.adanos.org
  baseurl_source: declared
  description: Fast-moving stock attention from X/Twitter cashtags and tweet engagement, useful for momentum discovery and validation.
  name: Adanos Market Sentiment API X/Twitter Stocks API
  slug: adanos-market-sentiment-api-x-twitter-stocks-api
artifact_total: 16
common:
- group: other
  href: https://artifacts.apis.io/adanos-market-sentiment-api/capabilities/adanos-market-sentiment-api-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/adanos-market-sentiment-api-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://adanos.org
- group: auth
  href: https://artifacts.apis.io/adanos-market-sentiment-api/security/adanos-market-sentiment-api-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/adanos-market-sentiment-api-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/adanos-market-sentiment-api/security/adanos-market-sentiment-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adanos-market-sentiment-api-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/adanos-market-sentiment-api/authentication/adanos-market-sentiment-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adanos-market-sentiment-api-authentication.yml
- group: build
  href: https://artifacts.apis.io/adanos-market-sentiment-api/packages/adanos-market-sentiment-api-packages.yml
  title: ''
  type: Packages
  url: packages/adanos-market-sentiment-api-packages.yml
- group: build
  href: https://artifacts.apis.io/adanos-market-sentiment-api/packages/adanos-market-sentiment-api-packages.yml
  title: ''
  type: SDKs
  url: packages/adanos-market-sentiment-api-packages.yml
- group: build
  href: https://artifacts.apis.io/adanos-market-sentiment-api/cli/adanos-market-sentiment-api-cli.yml
  title: ''
  type: CLI
  url: cli/adanos-market-sentiment-api-cli.yml
- group: agent
  href: https://artifacts.apis.io/adanos-market-sentiment-api/well-known/adanos-market-sentiment-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adanos-market-sentiment-api-well-known.yml
- group: auth
  href: https://artifacts.apis.io/adanos-market-sentiment-api/well-known/adanos-market-sentiment-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/adanos-market-sentiment-api-security.txt
- group: auth
  href: https://artifacts.apis.io/adanos-market-sentiment-api/security/adanos-market-sentiment-api-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/adanos-market-sentiment-api-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/adanos-market-sentiment-api/conformance/adanos-market-sentiment-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adanos-market-sentiment-api-conformance.yml
- group: design
  href: https://artifacts.apis.io/adanos-market-sentiment-api/errors/adanos-market-sentiment-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adanos-market-sentiment-api-problem-types.yml
- group: design
  href: https://artifacts.apis.io/adanos-market-sentiment-api/lifecycle/adanos-market-sentiment-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/adanos-market-sentiment-api-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adanos.org/
- group: operate
  href: https://artifacts.apis.io/adanos-market-sentiment-api/lifecycle/adanos-market-sentiment-api-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/adanos-market-sentiment-api-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/adanos-market-sentiment-api/conventions/adanos-market-sentiment-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/adanos-market-sentiment-api-conventions.yml
- group: operate
  href: https://artifacts.apis.io/adanos-market-sentiment-api/changelog/adanos-market-sentiment-api-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/adanos-market-sentiment-api-changelog.yml
- group: commercial
  href: https://artifacts.apis.io/adanos-market-sentiment-api/plans/adanos-market-sentiment-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adanos-market-sentiment-api-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/adanos-market-sentiment-api/rate-limits/adanos-market-sentiment-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/adanos-market-sentiment-api-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/adanos-market-sentiment-api/data-model/adanos-market-sentiment-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adanos-market-sentiment-api-data-model.yml
- group: design
  href: https://artifacts.apis.io/adanos-market-sentiment-api/components/adanos-market-sentiment-api-components.yml
  title: ''
  type: Components
  url: components/adanos-market-sentiment-api-components.yml
- group: agent
  href: https://artifacts.apis.io/adanos-market-sentiment-api/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/adanos-market-sentiment-api/overlays/adanos-market-sentiment-api-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adanos-market-sentiment-api-openapi-overlay.yaml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adanos-software
- group: commercial
  title: ''
  type: Pricing
  url: https://adanos.org/pricing
- group: start
  title: ''
  type: SignUp
  url: https://adanos.org/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adanos.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adanos.org/privacy
- group: operate
  title: ''
  type: Support
  url: https://adanos.org/contact
- group: company
  title: ''
  type: Blog
  url: https://adanos.org/insights/
- group: docs
  title: ''
  type: APIReference
  url: https://api.adanos.org/docs
created: '2026-07-17'
description: Key-authenticated REST/JSON API for financial market sentiment analytics across Reddit, X.com, news, and Polymarket, plus stock news and crypto sentiment. Provides Buzz Score, Trend Detection, and directional Sentiment signals for traders, fintech, quant/research teams, and AI agents.
finops:
- has_sources: true
  method: derived
  name: Adanos Market Sentiment Api Finops
  primary_unit: subscription
  service_category: ''
  slug: adanos-market-sentiment-api-finops
  template: false
layout: provider
modified: '2026-09-03'
name: Adanos Market Sentiment API
nav: Providers
network: true
overview: 'Adanos Market Sentiment API publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Finance Sentiment API, Health Check API, News Stocks API, and 4 more. Tagged areas include Markets, Sentiment, Stocks, Cryptocurrency, and Finance.


  The Adanos Market Sentiment API catalog on APIs.io includes 1 Spectral governance ruleset.


  Adanos Market Sentiment API''s developer surface includes authentication, CLI, changelog, pricing, signup flow, support, engineering blog, and 25 more developer resources.'
plans:
- name: Adanos Market Sentiment Api Plans Pricing
  plan_count: 6
  slug: adanos-market-sentiment-api-plans-pricing
- name: Adanos Market Sentiment Api Price Estimates
  plan_count: 0
  slug: adanos-market-sentiment-api-price-estimates
random_paper: 18
rate_limits:
- limit_count: 6
  name: Adanos Market Sentiment Api Rate Limits
  slug: adanos-market-sentiment-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 125
  extends:
  - spectral:oas
  name: Adanos Market Sentiment API API Rules
  rule_count: 84
  severity_counts:
    error: 70
    hint: 0
    info: 1
    warn: 13
  slug: adanos-market-sentiment-api-rules
score:
  band: strong
  composite: 63.9
  coverage:
    artifact_dirs: 29
    catalog_earned: 69.5
    catalog_earned_first_party: 24.0
    catalog_gap: 45.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 58.6
    developer_ergonomics: 57.1
    discoverability: 75.0
    operational_transparency: 76.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 63.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 57.1
      total: 7
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/adanos-market-sentiment-api/adanos-market-sentiment-api-2026-07-25T181547.png
security:
- kind: authentication
  name: Adanos Market Sentiment Api Authentication
  slug: adanos-market-sentiment-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Adanos Market Sentiment Api Domain Security
  slug: adanos-market-sentiment-api-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Adanos Market Sentiment Api Vulnerability Disclosure
  slug: adanos-market-sentiment-api-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: adanos-market-sentiment
  slug: adanos-market-sentiment
slug: adanos-market-sentiment-api
tags:
- Markets
- Sentiment
- Stocks
- Cryptocurrency
- Finance
- Trading
- Social Data
- News
- Prediction Markets
- Reddit
- X / Twitter
- Polymarket
- AI Agents
- REST API
- OpenAPI
- Llms.txt
- Agent Skills
website: https://adanos.org
---
