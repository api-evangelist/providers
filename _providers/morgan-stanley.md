---
access_model:
  confidence: medium
  label: Invitation-only institutional platform + public E*TRADE brokerage API
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
  score: 11.2
  scored_at: '2026-08-26'
api_count: 6
apis:
- description: 'The institutional REST APIs on the Morgan Stanley API Platform let onboarded clients and third-party partners integrate Morgan Stanley data and services directly into their own systems and processes. '
  name: Morgan Stanley API Platform (REST)
  slug: api-platform-rest
- description: Alongside its REST APIs, the Morgan Stanley API Platform exposes streaming WebSocket APIs for onboarded institutional clients who need low-latency, event-driven data feeds rather than request/response
  name: Morgan Stanley API Platform (WebSocket Streaming)
  slug: api-platform-websocket
- description: E*TRADE from Morgan Stanley operates a genuinely public, self-service developer platform whose REST Accounts API gives an authenticated E*TRADE user's authorized application access to detailed account
  name: E*TRADE from Morgan Stanley - Accounts API
  slug: etrade-accounts
- description: The E*TRADE from Morgan Stanley Market Data API is the market-data module of the public E*TRADE V1 REST platform. It provides real-time and delayed equity and option quotes, option chains, and product
  name: E*TRADE from Morgan Stanley - Market Data API
  slug: etrade-market-data
- description: The E*TRADE from Morgan Stanley Order API is the trading module of the public E*TRADE V1 REST platform, letting an authorized application list an account's orders and preview, place, change, and cance
  name: E*TRADE from Morgan Stanley - Order API
  slug: etrade-orders
- description: The E*TRADE from Morgan Stanley Alerts API is the notifications module of the public E*TRADE V1 REST platform. It lets an authorized application list the alerts E*TRADE has generated for the authentic
  name: E*TRADE from Morgan Stanley - Alerts API
  slug: etrade-alerts
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://www.morganstanley.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.morganstanley.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.morganstanley.com/apis
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.morganstanley.com/terms
- group: build
  title: ''
  type: SampleCode
  url: https://github.com/morganstanley/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/morganstanley
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/morgan-stanley
- group: company
  title: ''
  type: Blog
  url: https://morganstanley.github.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.etrade.com/getting-started
- group: auth
  title: ''
  type: DomainSecurity
  url: security/morgan-stanley-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/morgan-stanley-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.morganstanley.com/vulnerability-disclosure
- group: auth
  title: ''
  type: Authentication
  url: authentication/morgan-stanley-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/morgan-stanley-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/morgan-stanley-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/morgan-stanley-etrade-error-codes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/morgan-stanley-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/morgan-stanley-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/morgan-stanley-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/morgan-stanley-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/morgan-stanley-llms.txt
created: '2025-03-01'
description: Morgan Stanley is a global financial services firm that offers a wide range of services to individuals, corporations, and governments. The firm is known for its investment banking and wealth management services, helping clients raise capital, make strategic acquisitions, and manage their assets. Morgan Stanley also provides services in areas such as asset management, trading, research, and risk management. Its public developer surface is split between an invitation-only institutional API Platform at developer.morganstanley.com (OAuth 2.0 with certificate-based token exchange, REST and WebSocket, built to the OpenAPI Specification) and the genuinely public E*TRADE from Morgan Stanley brokerage API at developer.etrade.com (OAuth 1.0a, REST, with a sandbox).
finops:
- name: Morgan Stanley Finops
  service_category: Financial Services
  slug: morgan-stanley-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/morgan-stanley.png
layout: provider
modified: '2026-07-23'
name: Morgan Stanley
nav: Providers
network: true
overview: 'Morgan Stanley publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial, Investment Banking, Wealth Management, Brokerage, and Market Data.


  Morgan Stanley''s developer surface includes documentation, engineering blog, getting-started guide, authentication, sandbox, and 16 more developer resources.'
plans:
- name: Morgan Stanley Plans Pricing
  plan_count: 2
  slug: morgan-stanley-plans-pricing
press:
- date: '2026-05-25'
  title: Launch of AI @ Morgan Stanley Debrief
  url: https://www.morganstanley.com/press-releases/ai-at-morgan-stanley-debrief-launch
- date: '2026-05-25'
  title: Morgan Stanley uses AI evals to shape the future of ...
  url: https://openai.com/index/morgan-stanley/
- date: '2026-05-25'
  title: 'Artificial Intelligence: Firmwide Team'
  url: https://www.morganstanley.com/about-us/technology/artificial-intelligence-firmwide-team
- date: '2026-05-25'
  title: Morgan Stanley Research Announces AskResearchGPT
  url: https://www.morganstanley.com/press-releases/morgan-stanley-research-announces-askresearchgpt
- date: '2026-05-25'
  title: Research
  url: https://www.morganstanley.com/what-we-do/research
random_paper: 8
rate_limits:
- limit_count: 2
  name: Morgan Stanley Rate Limits
  slug: morgan-stanley-rate-limits
score:
  band: thin
  composite: 29.3
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 29.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 55.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/morgan-stanley/refs/heads/main/screenshots/morgan-stanley-2026-06-20T185816.png
security:
- kind: authentication
  name: Morgan Stanley Authentication
  slug: morgan-stanley-authentication
  summary_line: oauth1/oauth2 · 2 schemes
- kind: domain-security
  name: Morgan Stanley Domain Security
  slug: morgan-stanley-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Morgan Stanley Vulnerability Disclosure
  slug: morgan-stanley-vulnerability-disclosure
  summary_line: disclosure policy published
slug: morgan-stanley
tags:
- Financial
- Investment Banking
- Wealth Management
- Brokerage
- Market Data
- Trading
- Fortune 100
- United States
website: https://www.morganstanley.com/
---
