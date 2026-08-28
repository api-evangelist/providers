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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Charles Schwab Agentic Access
  operation_count: 18
  slug: charles-schwab-agentic-access
  summary_line: 18 operations · 2 acting
api_count: 10
apis:
- description: Linked brokerage accounts, balances, and positions
  name: Charles Schwab Accounts API
  slug: charles-schwab-accounts-api
- description: Instrument metadata search
  name: Charles Schwab Instruments API
  slug: charles-schwab-instruments-api
- description: Market hours by product
  name: Charles Schwab Market Hours API
  slug: charles-schwab-market-hours-api
- description: Top movers within indexes
  name: Charles Schwab Movers API
  slug: charles-schwab-movers-api
- description: Option chain and expiration data
  name: Charles Schwab Options API
  slug: charles-schwab-options-api
- description: Place, retrieve, and cancel orders
  name: Charles Schwab Orders API
  slug: charles-schwab-orders-api
- description: Historical price candles
  name: Charles Schwab Price History API
  slug: charles-schwab-price-history-api
- description: Real-time and delayed quote data
  name: Charles Schwab Quotes API
  slug: charles-schwab-quotes-api
- description: Account transaction history
  name: Charles Schwab Transactions API
  slug: charles-schwab-transactions-api
- description: User account preferences and metadata
  name: Charles Schwab User Preferences API
  slug: charles-schwab-user-preferences-api
artifact_total: 37
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Charles Schwab Market Data Accounts API
  slug: open-charles-schwab-accounts-api
- collection_type: open
  name: Charles Schwab Market Data Accounts Instruments API
  slug: open-charles-schwab-instruments-api
- collection_type: open
  name: Charles Schwab Market Data API
  slug: open-charles-schwab-market-data-api
- collection_type: open
  name: Charles Schwab Market Data Accounts Market Hours API
  slug: open-charles-schwab-market-hours-api
- collection_type: open
  name: Charles Schwab Market Data Accounts Movers API
  slug: open-charles-schwab-movers-api
- collection_type: open
  name: Charles Schwab Market Data Accounts Options API
  slug: open-charles-schwab-options-api
- collection_type: open
  name: Charles Schwab Market Data Accounts Orders API
  slug: open-charles-schwab-orders-api
- collection_type: open
  name: Charles Schwab Market Data Accounts Price History API
  slug: open-charles-schwab-price-history-api
- collection_type: open
  name: Charles Schwab Market Data Accounts Quotes API
  slug: open-charles-schwab-quotes-api
- collection_type: open
  name: Charles Schwab Trader API
  slug: open-charles-schwab-trader-api
- collection_type: open
  name: Charles Schwab Market Data Accounts Transactions API
  slug: open-charles-schwab-transactions-api
- collection_type: open
  name: Charles Schwab Market Data Accounts User Preferences API
  slug: open-charles-schwab-user-preferences-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/charles-schwab-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/charles-schwab-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/charles-schwab-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/charles-schwab-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/charles-schwab-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/charles-schwab
- group: company
  title: ''
  type: Website
  url: https://www.schwab.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.schwab.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.schwab.com/user-guides
- group: auth
  title: ''
  type: Authentication
  url: https://developer.schwab.com/user-guides/get-started/authenticate-with-oauth
- group: start
  title: ''
  type: Signup
  url: https://developer.schwab.com/register
- group: other
  title: ''
  type: Dashboard
  url: https://developer.schwab.com/dashboard
- group: operate
  title: ''
  type: Support
  url: https://developer.schwab.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.schwab.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.schwab.com/legal/online-privacy
- group: design
  title: ''
  type: JSONLD
  url: json-ld/charles-schwab-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/charles-schwab-account-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/charles-schwab-order-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/charles-schwab-quote-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.schwab.com/llms.txt
created: '2026-03-21'
description: Charles Schwab is a financial services company providing brokerage, banking, asset management, and financial advisory services to individual investors and independent investment advisors. The Schwab Developer Portal exposes Trader APIs that let registered applications access account balances, positions, and orders, place equity and option trades, and consume real-time and historical market data through OAuth 2.0-secured REST endpoints.
finops:
- name: Charles Schwab Finops
  service_category: Financial Services / Brokerage
  slug: charles-schwab-finops
graphqls:
- description: This conceptual GraphQL schema represents the Charles Schwab Trader API and Market Data API surface. Charles Schwab operates one of the largest retail brokerage platforms in the United States, offerin
  name: Charles Schwab GraphQL Schema
  slug: charles-schwab-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/charles-schwab.png
json_schemas:
- name: Schwab Account
  property_count: 7
  slug: charles-schwab-account
- name: Schwab Order
  property_count: 12
  slug: charles-schwab-order
- name: Schwab Quote
  property_count: 11
  slug: charles-schwab-quote
jsonld:
- class_count: 0
  name: Charles Schwab Context
  property_count: 5
  slug: charles-schwab-context
layout: provider
modified: '2026-05-19'
name: Charles Schwab
nav: Providers
network: true
overview: 'Charles Schwab publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Instruments API, Market Hours API, and 7 more. Tagged areas include Account, Banking, Brokerage, Financial-Services, and Investing.


  The Charles Schwab catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Charles Schwab''s developer surface includes authentication, documentation, signup flow, support, and 16 more developer resources.'
plans:
- name: Charles Schwab Plans Pricing
  plan_count: 2
  slug: charles-schwab-plans-pricing
press:
- date: '2026-05-25'
  title: Charles Schwab Launches AI-Powered Capability That Helps ...
  url: https://pressroom.aboutschwab.com/press-releases/press-release/2026/Charles-Schwab-Launches-AI-Powered-Capability-That-Helps-Investors-Understand-Portfolio-Performance-and-Market-Activity/default.aspx
- date: '2026-05-25'
  title: Charles Schwab credits increased AI use with cost savings
  url: https://www.ciodive.com/news/charles-schwab-AI-cost-savings-knowledge-assistant/738188/
- date: '2026-05-25'
  title: Charles Schwab
  url: https://www.facebook.com/CharlesSchwab/posts/we-are-rolling-out-an-exciting-ai-powered-capability-for-investors-it-delivers-i/1364267489081281/
- date: '2026-05-25'
  title: Charles Schwab Corp. is planning to use artificial ...
  url: https://www.facebook.com/bloombergbusiness/posts/charles-schwab-corp-is-planning-to-use-artificial-intelligence-to-extend-benefit/1397432698909486/
- date: '2026-05-25'
  title: What to Know About Artificial Intelligence (AI)
  url: https://www.schwab.com/learn/story/what-to-know-about-artificial-intelligence-ai
random_paper: 8
rate_limits:
- limit_count: 3
  name: Charles Schwab Rate Limits
  slug: charles-schwab-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Charles Schwab API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: charles-schwab-jsonschema-spectral-rules
scopes:
- name: Charles Schwab Scopes
  scope_count: 1
  slug: charles-schwab-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 44.9
  delta: 2.3
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 9.8
    contract_quality: 59.0
    developer_ergonomics: 47.6
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 42.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 55.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/charles-schwab/refs/heads/main/screenshots/charles-schwab-2026-06-20T174236.png
security:
- kind: authentication
  name: Charles Schwab Authentication
  slug: charles-schwab-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Charles Schwab Domain Security
  slug: charles-schwab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Charles Schwab Vulnerability Disclosure
  slug: charles-schwab-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: charles-schwab
tags:
- Account
- Banking
- Brokerage
- Financial-Services
- Investing
- Market Data
- Authentication
- Order
- Trading
- Fortune 500
website: https://www.schwab.com
---
