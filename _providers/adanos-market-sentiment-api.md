---
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
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: RESTful JSON API grouping five sentiment services (Reddit Stocks, X.com Stocks, Stock News, Polymarket Stocks, Reddit Crypto) with 41 base endpoints plus PRO raw-mention endpoints. Authenticated via X
  name: Adanos Market Sentiment API
  slug: adanos-market-sentiment-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://adanos.org
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/adanos-market-sentiment-api-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adanos-market-sentiment-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adanos-market-sentiment-api-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/adanos-market-sentiment-api-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/adanos-market-sentiment-api-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/adanos-market-sentiment-api-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/adanos-market-sentiment-api-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/adanos-market-sentiment-api-security.txt
- group: auth
  title: ''
  type: Security
  url: security/adanos-market-sentiment-api-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adanos-market-sentiment-api-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/adanos-market-sentiment-api-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/adanos-market-sentiment-api-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adanos.org/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/adanos-market-sentiment-api-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/adanos-market-sentiment-api-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/adanos-market-sentiment-api-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adanos-market-sentiment-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adanos-market-sentiment-api-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/adanos-market-sentiment-api-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/adanos-market-sentiment-api-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
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
overview: 'Adanos Market Sentiment API publishes 1 API on the [APIs.io](https://apis.io/) network: Adanos Market Sentiment API. Tagged areas include Market, Sentiment, Stocks, Crypto, and Finance.


  Adanos Market Sentiment API''s developer surface includes authentication, CLI, changelog, pricing, signup flow, support, engineering blog, and 24 more developer resources.'
plans:
- name: Adanos Market Sentiment Api Plans Pricing
  plan_count: 3
  slug: adanos-market-sentiment-api-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 6
  name: Adanos Market Sentiment Api Rate Limits
  slug: adanos-market-sentiment-api-rate-limits
score:
  band: strong
  composite: 58.0
  coverage:
    artifact_dirs: 20
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 48.8
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 26.7
    developer_ergonomics: 57.1
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 86.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 9.2
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 61.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: rising
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
slug: adanos-market-sentiment-api
tags:
- Market
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
