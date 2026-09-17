---
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.9
  scored_at: '2026-09-16'
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
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://adanos.org
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adanos-market-sentiment-api/refs/heads/main/security/adanos-market-sentiment-api-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/adanos-market-sentiment-api-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adanos-market-sentiment-api/refs/heads/main/security/adanos-market-sentiment-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adanos-market-sentiment-api-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adanos-market-sentiment-api/refs/heads/main/authentication/adanos-market-sentiment-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adanos-market-sentiment-api-authentication.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adanos-market-sentiment-api/refs/heads/main/packages/adanos-market-sentiment-api-packages.yml
  title: ''
  type: Packages
  url: packages/adanos-market-sentiment-api-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adanos-market-sentiment-api/refs/heads/main/packages/adanos-market-sentiment-api-packages.yml
  title: ''
  type: SDKs
  url: packages/adanos-market-sentiment-api-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adanos-market-sentiment-api/refs/heads/main/cli/adanos-market-sentiment-api-cli.yml
  title: ''
  type: CLI
  url: cli/adanos-market-sentiment-api-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adanos-market-sentiment-api/refs/heads/main/well-known/adanos-market-sentiment-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adanos-market-sentiment-api-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adanos-market-sentiment-api/refs/heads/main/well-known/adanos-market-sentiment-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/adanos-market-sentiment-api-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adanos-market-sentiment-api/refs/heads/main/security/adanos-market-sentiment-api-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/adanos-market-sentiment-api-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adanos-market-sentiment-api/refs/heads/main/conformance/adanos-market-sentiment-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adanos-market-sentiment-api-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adanos-market-sentiment-api/refs/heads/main/errors/adanos-market-sentiment-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adanos-market-sentiment-api-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adanos-market-sentiment-api/refs/heads/main/lifecycle/adanos-market-sentiment-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/adanos-market-sentiment-api-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adanos.org/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/adanos-market-sentiment-api/refs/heads/main/lifecycle/adanos-market-sentiment-api-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/adanos-market-sentiment-api-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adanos-market-sentiment-api/refs/heads/main/conventions/adanos-market-sentiment-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/adanos-market-sentiment-api-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/adanos-market-sentiment-api/refs/heads/main/changelog/adanos-market-sentiment-api-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/adanos-market-sentiment-api-changelog.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/adanos-market-sentiment-api/refs/heads/main/plans/adanos-market-sentiment-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adanos-market-sentiment-api-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/adanos-market-sentiment-api/refs/heads/main/rate-limits/adanos-market-sentiment-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/adanos-market-sentiment-api-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adanos-market-sentiment-api/refs/heads/main/data-model/adanos-market-sentiment-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adanos-market-sentiment-api-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adanos-market-sentiment-api/refs/heads/main/components/adanos-market-sentiment-api-components.yml
  title: ''
  type: Components
  url: components/adanos-market-sentiment-api-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adanos-market-sentiment-api/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adanos-market-sentiment-api/refs/heads/main/overlays/adanos-market-sentiment-api-openapi-overlay.yaml
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
layout: provider
modified: '2026-09-03'
name: Adanos Market Sentiment API
nav: Providers
network: true
overview: 'Adanos Market Sentiment API publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Finance Sentiment API, Health Check API, News Stocks API, and 4 more. Tagged areas include Markets, Sentiment, Stocks, Crypto, and Finance.


  Adanos Market Sentiment API''s developer surface includes authentication, CLI, changelog, pricing, signup flow, support, engineering blog, and 24 more developer resources.'
plans:
- name: Adanos Market Sentiment Api Plans Pricing
  plan_count: 3
  slug: adanos-market-sentiment-api-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 6
  name: Adanos Market Sentiment Api Rate Limits
  slug: adanos-market-sentiment-api-rate-limits
score:
  band: strong
  composite: 63.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 62.0
    catalog_earned_first_party: 24.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.9
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 60.1
    developer_ergonomics: 57.1
    discoverability: 77.8
    operational_transparency: 76.3
  previous_composite: 54.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 61.7
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/adanos-market-sentiment-api/refs/heads/main/screenshots/adanos-market-sentiment-api-2026-07-25T181547.png
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
- Crypto
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
- llms-txt
- Agent Skills
website: https://adanos.org
---
