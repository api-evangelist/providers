---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Brapi Agentic Access
  operation_count: 20
  slug: brapi-agentic-access
  summary_line: 20 operations
api_count: 12
apis:
- description: Access structured financial statement data for Brazilian listed companies including balance sheets (BP), income statements (DRE), cash flow (DFC), and value added statements (DVA). Historical data ava
  name: brapi Fundamentals API
  slug: fundamentals-api
- description: Retrieve complete dividend and earnings distribution history for B3-listed securities, enabling portfolio yield analysis and income tracking.
  name: brapi Dividends API
  slug: dividends-api
- description: Access cryptocurrency prices denominated in Brazilian Reals (BRL), supporting investment analysis and portfolio management for Brazilian digital asset investors.
  name: brapi Cryptocurrency API
  slug: crypto-api
- description: Retrieve Brazilian Real (BRL) exchange rates against major global currencies, sourced from Banco Central do Brasil data.
  name: brapi Exchange Rates API
  slug: exchange-api
- description: Access Brazilian macroeconomic indicators including IPCA (consumer price index), IGPM (market general price index), INPC, and SELIC interest rate data published by Banco Central do Brasil.
  name: brapi Economic Indicators API
  slug: indicators-api
- description: The Criptomoedas API from brapi — 2 operation(s) for criptomoedas.
  name: brapi Criptomoedas API
  slug: brapi-criptomoedas-api
- description: The Fiis API from brapi — 6 operation(s) for fiis.
  name: brapi Fiis API
  slug: brapi-fiis-api
- description: The Inflacao API from brapi — 2 operation(s) for inflacao.
  name: brapi Inflacao API
  slug: brapi-inflacao-api
- description: The Moedas API from brapi — 2 operation(s) for moedas.
  name: brapi Moedas API
  slug: brapi-moedas-api
- description: The Opcoes API from brapi — 4 operation(s) for opcoes.
  name: brapi Opcoes API
  slug: brapi-opcoes-api
- description: The Quote API from brapi — 2 operation(s) for quote.
  name: brapi Quote API
  slug: brapi-quote-api
- description: The Taxa Basica De Juros API from brapi — 2 operation(s) for taxa basica de juros.
  name: brapi Taxa Basica De Juros API
  slug: brapi-taxa-basica-de-juros-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: brapi Criptomoedas API
  slug: open-brapi-criptomoedas-api
- collection_type: open
  name: brapi Criptomoedas Fiis API
  slug: open-brapi-fiis-api
- collection_type: open
  name: brapi Criptomoedas Inflacao API
  slug: open-brapi-inflacao-api
- collection_type: open
  name: brapi Criptomoedas Moedas API
  slug: open-brapi-moedas-api
- collection_type: open
  name: brapi Criptomoedas Opcoes API
  slug: open-brapi-opcoes-api
- collection_type: open
  name: brapi Criptomoedas Quote API
  slug: open-brapi-quote-api
- collection_type: open
  name: brapi Criptomoedas Taxa Basica De Juros API
  slug: open-brapi-taxa-basica-de-juros-api
- collection_type: open
  name: brapi API
  slug: open-brapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/brapi-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/brapi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brapi-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brapi-dev
- group: company
  title: ''
  type: Website
  url: https://brapi.dev
- group: docs
  title: ''
  type: Documentation
  url: https://brapi.dev/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://brapi.dev/pricing
- group: auth
  title: ''
  type: Authentication
  url: https://brapi.dev/docs
- group: start
  title: ''
  type: Signup
  url: https://brapi.dev/register
- group: agent
  title: ''
  type: LlmsText
  url: https://brapi.dev/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://brapi.dev/blog
created: '2025-03-01'
description: brapi.dev is a Brazilian financial data REST API aggregating public market data from B3 (stock exchange), CVM (securities commission), and Banco Central (central bank). It provides real-time and historical stock quotes, fundamentals, dividends, cryptocurrency prices in BRL, foreign exchange rates, and economic indicators such as IPCA, IGPM, and SELIC. With over 20,000 active developers, brapi.dev offers tiered subscription plans from free to Pro, with up to 500,000 requests per month and data updated every 5 minutes.
finops:
- name: Brapi Finops
  service_category: API
  slug: brapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brapi.png
layout: provider
modified: '2026-05-19'
name: brapi
nav: Providers
network: true
overview: 'brapi publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Criptomoedas API, Fiis API, Inflacao API, and 4 more. Tagged areas include Finance, Brazilian Financial Data, Stock Market, Investments, and Economic Indicators.


  brapi''s developer surface includes documentation, pricing, authentication, signup flow, engineering blog, and 6 more developer resources.'
plans:
- name: Brapi Plans Pricing
  plan_count: 3
  slug: brapi-plans-pricing
random_paper: 79
rate_limits:
- limit_count: 5
  name: Brapi Rate Limits
  slug: brapi-rate-limits
score:
  band: thin
  composite: 32.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 44.0
    developer_ergonomics: 21.7
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 32.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brapi/refs/heads/main/screenshots/brapi-2026-06-20T173642.png
security:
- kind: domain-security
  name: Brapi Domain Security
  slug: brapi-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Brapi Vulnerability Disclosure
  slug: brapi-vulnerability-disclosure
  summary_line: disclosure policy published
slug: brapi
tags:
- Finance
- Brazilian Financial Data
- Stock Market
- Investments
- Economic Indicators
- Cryptocurrency
website: https://brapi.dev
---
