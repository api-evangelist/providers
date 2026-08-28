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
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-08-26'
api_count: 9
apis:
- description: Provides programmatic access to Bloomberg's comprehensive financial data including pricing, reference data, fundamentals, and historical information. Content can be accessed via a REST API, SFTP, or n
  name: Bloomberg Data License API
  slug: bloomberg-data-license-api
- description: Desktop API enabling custom applications to access Bloomberg data and functionality programmatically through the Bloomberg Terminal. Supports development in C++, Java, C# (.NET), Python, and other lan
  name: Bloomberg API (BLPAPI)
  slug: bloomberg-api-blpapi
- description: Server-side API delivering the same real-time market data, historical data, premium reference data, and calculation tools available with the Bloomberg Terminal for seamless use in proprietary and Bloo
  name: Bloomberg SAPI (Server API)
  slug: bloomberg-sapi-server-api
- description: Real-time streaming market data feed providing access to 35 million instruments across all asset classes, aggregated from 330+ exchanges and 5,000+ contributors. Supports Bloomberg composite tickers a
  name: Bloomberg B-PIPE
  slug: bloomberg-b-pipe
- description: 'Provides programmatic access to Data License content with a combination of request-response and subscription-based services. Available content includes reference, pricing, regulatory, and alternative '
  name: Bloomberg Hypermedia API (HAPI)
  slug: bloomberg-hypermedia-api-hapi
- description: HTTP wrapper making the Bloomberg Open API available via HTTP and WebSockets, allowing clients to access reference and historical request/response data as well as make subscriptions for live data with
  name: Bloomberg HTTP API
  slug: bloomberg-http-api
- description: Enables synchronization of actions across third-party applications and the Bloomberg Terminal. Allows developers to initiate Bloomberg functions within external applications and synchronize with Bloom
  name: Bloomberg Terminal Connect API
  slug: bloomberg-terminal-connect-api
- description: Platform for building, connecting, and scaling third-party applications within the Bloomberg Terminal ecosystem. Developers can create extensions published and distributed to Bloomberg Terminal subscr
  name: Bloomberg App Portal
  slug: bloomberg-app-portal
- description: Fully managed, public cloud-based data management solution that brings Bloomberg data together in a centralized platform for easier and more consistent delivery to downstream systems.
  name: Bloomberg Data License Plus (DL+)
  slug: bloomberg-data-license-plus-dl
artifact_total: 35
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/bloomberg/blpapi-http/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/bloomberg/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/bloomberg/blpapi-http/blob/develop/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/bloomberg/blpapi-http/blob/develop/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-professional-service-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/bloomberg-professional-service
- group: start
  title: ''
  type: Portal
  url: https://www.bloomberg.com/professional/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bloomberg.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bloomberg.com/professional/solutions/asset-management/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://bloomberg.github.io/blpapi-docs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bloomberg.com/professional/support/api-library/
- group: operate
  title: ''
  type: Support
  url: https://www.bloomberg.com/professional/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.bloomberg.com/professional/support/software-updates/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bloomberg
- group: other
  title: ''
  type: Resources
  url: https://bloomberg.github.io/
- group: other
  title: ''
  type: Resources
  url: https://www.bloomberg.com/professional/products/data/data-connectivity/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/notices/
- group: operate
  title: ''
  type: Contact
  url: https://www.bloomberg.com/professional/request-demo/
created: 2024-01-20 00:00:00+00:00
description: Bloomberg Professional Service is a comprehensive financial data, news, and analytics platform serving investment professionals worldwide. It provides real-time and historical market data, trading capabilities, news, research, and analytical tools for financial markets.
features:
- Real-time and historical market data access
- Desktop API for Bloomberg Terminal integration
- Server-side API for enterprise applications
- B-PIPE low-latency streaming data feed
- Hypermedia API for Data License content
- HTTP/WebSocket wrapper for BLPAPI
- Terminal Connect for third-party app synchronization
- App Portal for Terminal ecosystem extensions
finops:
- name: Bloomberg Professional Service Finops
  service_category: API
  slug: bloomberg-professional-service-finops
image: https://www.bloomberg.com/company/press/wp-content/uploads/sites/40/2018/02/Bloomberg_Logo_2018.png
integrations:
- Bloomberg Terminal
- AWS
- Microsoft Azure
- Python
- Java
- C++ / .NET
- Node.js
- Haskell
layout: provider
modified: '2026-04-18'
name: Bloomberg Professional Service
nav: Providers
network: true
overview: 'Bloomberg Professional Service publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Cloud, Data Management, Enterprise, and Financial-Services.


  Bloomberg Professional Service''s developer surface includes developer portal, documentation, support, and 16 more developer resources.'
plans:
- name: Bloomberg Professional Service Plans Pricing
  plan_count: 3
  slug: bloomberg-professional-service-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Bloomberg Professional Service Rate Limits
  slug: bloomberg-professional-service-rate-limits
score:
  band: thin
  composite: 30.5
  delta: 7.1
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 40.5
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 33.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-professional-service/refs/heads/main/screenshots/bloomberg-professional-service-2026-06-20T173510.png
security:
- kind: domain-security
  name: Bloomberg Professional Service Domain Security
  slug: bloomberg-professional-service-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bloomberg-professional-service
tags:
- Analytics
- Cloud
- Data Management
- Enterprise
- Financial-Services
- Market Data
- Open-Source
- Real-Time Data
- Trading
use_cases:
- Algorithmic and quantitative trading
- Portfolio management and risk analysis
- Financial data integration and reporting
- Real-time market data distribution
- Custom Terminal application development
- Enterprise data management and analytics
website: https://developer.bloomberg.com/
---
