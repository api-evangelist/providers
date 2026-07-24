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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 3
apis:
- description: Cross-platform API providing access to the full Bloomberg data ecosystem including real-time, reference, and historical data with SDKs for Python, Java, C++, and other languages.
  name: Bloomberg Open API (BLPAPI)
  slug: blpapi
- description: Enterprise data distribution platform for delivering Bloomberg data at scale to multiple applications and users within an institution using a managed entitlement and authorization framework.
  name: Bloomberg B-PIPE
  slug: bpipe
- description: Bloomberg's Electronic Order Management System (EMSX) enabling electronic order routing to brokers across equities, fixed income, FX, and derivatives. Provides FIX connectivity, algorithmic trading, a
  name: Bloomberg EMSX (Electronic Order Management)
  slug: emsx
artifact_total: 17
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bloomberg-products-and-platforms-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-products-and-platforms-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.bloomberg.com/professional/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bloomberg.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bloomberg
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.bloomberg.com/professional/support/
created: '2024-01-01'
description: Bloomberg Products and Platforms covers the breadth of Bloomberg's integrated offerings spanning the Bloomberg Terminal, Enterprise data products, API platforms, trading systems, analytics, messaging, media, and government intelligence solutions. Bloomberg serves financial professionals with an interconnected ecosystem of products and platforms for data, analytics, and communication.
features:
- description: Professional workstation integrating data, analytics, news, and messaging.
  name: Bloomberg Terminal
- description: B-PIPE for institution-wide Bloomberg data sharing.
  name: Enterprise Data Distribution
- description: EMSX for electronic order routing and execution management.
  name: Electronic Trading
- description: Cloud-native Bloomberg data and analytics via cloud connectivity.
  name: Cloud Products
- description: Bloomberg Anywhere for mobile and remote product access.
  name: Mobile Access
finops:
- name: Bloomberg Products And Platforms Finops
  service_category: API
  slug: bloomberg-products-and-platforms-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-products-and-platforms.png
layout: provider
modified: '2026-04-21'
name: Bloomberg Products and Platforms
nav: Providers
network: true
overview: 'Bloomberg Products and Platforms publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Products, Platforms, Terminal, Enterprise, and Financial Data.


  Bloomberg Products and Platforms'' developer surface includes developer portal, documentation, support, and 5 more developer resources.'
plans:
- name: Bloomberg Products And Platforms Plans Pricing
  plan_count: 3
  slug: bloomberg-products-and-platforms-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 5
  name: Bloomberg Products And Platforms Rate Limits
  slug: bloomberg-products-and-platforms-rate-limits
score:
  band: thin
  composite: 30.0
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 30.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-products-and-platforms/refs/heads/main/screenshots/bloomberg-products-and-platforms-2026-06-20T173513.png
security:
- kind: domain-security
  name: Bloomberg Products And Platforms Domain Security
  slug: bloomberg-products-and-platforms-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Bloomberg Products And Platforms Vulnerability Disclosure
  slug: bloomberg-products-and-platforms-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bloomberg-products-and-platforms
tags:
- Products
- Platforms
- Terminal
- Enterprise
- Financial Data
- Analytics
- Bloomberg
use_cases:
- description: End-to-end data, analytics, and trading workflow for asset managers.
  name: Buy-Side Investment Workflows
- description: Data and trading tools for bank trading desks and market makers.
  name: Sell-Side Market Making
- description: Bloomberg Intelligence and data for research teams.
  name: Financial Research
- description: Risk data and analytics integration for risk management operations.
  name: Risk Operations
website: https://www.bloomberg.com/professional/
---
