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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: 'The AIS Client Portal provides investment analytics, portfolio management, and reporting tools for financial advisors and individual investors. The portal enables access to AIS investment strategies, '
  name: AIS Client Portal
  slug: ais-client-portal
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ais-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aisgroup.com
- group: operate
  title: ''
  type: Contact
  url: https://www.aisgroup.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aisgroup.com/privacy-policy
created: '2025-01-01'
description: AIS Group is an analytics and investment management firm providing independent, data-driven insights across global financial markets. The firm combines macroeconomic research with quantitative analytics to deliver non-correlated investment strategies for financial advisors and institutional clients, with a focus on commodity, currency, equity, and fixed-income market analysis.
features:
- description: Quantitative analysis across commodity, currency, equity, and fixed-income markets to identify investment opportunities.
  name: Global Investment Analytics
- description: Investment strategies designed to provide diversifying return streams with low correlations to traditional and alternative investments.
  name: Non-Correlated Strategies
- description: Independent macroeconomic and intermarket analysis supporting tactical asset allocation and risk management decisions.
  name: Macroeconomic Research
- description: Comprehensive portfolio reporting and performance analytics accessible via the secure client portal.
  name: Client Portfolio Reporting
- description: Risk-adjusted return analysis and portfolio risk metrics to support investment decision-making.
  name: Risk Management Analytics
finops:
- name: Ais Finops
  service_category: API
  slug: ais-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ais.png
layout: provider
modified: '2026-04-19'
name: AIS Group
nav: Providers
network: true
overview: AIS Group publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Finance, Insurance, Investment Analytics, and Risk Management.
plans:
- name: Ais Plans Pricing
  plan_count: 3
  slug: ais-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 5
  name: Ais Rate Limits
  slug: ais-rate-limits
score:
  band: minimal
  composite: 12.7
  delta: -6.6
  facets:
    commercial_clarity: 26.3
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 19.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 15.2
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/ais/refs/heads/main/screenshots/ais-2026-06-20T171439.png
security:
- kind: domain-security
  name: Ais Domain Security
  slug: ais-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ais
tags:
- Analytics
- Finance
- Insurance
- Investment Analytics
- Risk Management
use_cases:
- description: Financial advisors use AIS analytics to identify non-correlated investment strategies that reduce portfolio concentration risk.
  name: Portfolio Diversification
- description: Institutional investors leverage AIS macroeconomic research to inform tactical shifts across asset classes.
  name: Tactical Asset Allocation
- description: Investment professionals access AIS quantitative models to evaluate alternative and global investment opportunities.
  name: Alternative Investment Research
- description: Clients use the portal's reporting tools to benchmark portfolio performance against relevant indices and peer groups.
  name: Performance Benchmarking
website: https://www.aisgroup.com
---
