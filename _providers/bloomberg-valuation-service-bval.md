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
  scored_at: '2026-08-17'
api_count: 3
apis:
- description: Access BVAL evaluated prices, yield curves, spread data, and pricing transparency metadata for fixed income securities via BLPAPI and Data License. Supports corporate bonds, municipal bonds, governmen
  name: Bloomberg BVAL Pricing API
  slug: bval-api
- description: Evaluated pricing for US municipal bonds with BVAL's deep munis coverage providing independent prices for general obligation, revenue, and specialty municipal securities. Widely used for NAV calculati
  name: Bloomberg BVAL Municipal Bond Pricing
  slug: bval-muni
- description: Evaluated pricing for complex structured finance instruments including ABS, MBS, CMBS, CLOs, and other securitized products using market-consistent models and observable market data inputs.
  name: Bloomberg BVAL Structured Product Pricing
  slug: bval-structured-products
artifact_total: 19
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-valuation-service-bval-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.bloomberg.com/professional/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bloomberg.com/professional/solution/bval/
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
description: Bloomberg Valuation Service (BVAL) is Bloomberg's evaluated pricing service providing independent fair value prices for over 2.5 million fixed income securities including corporate bonds, municipal bonds, government securities, structured products, and derivatives. BVAL prices are designed for portfolio valuation, NAV calculation, regulatory reporting, and risk management, with full transparency on pricing methodology and inputs.
features:
- description: Third-party evaluated prices for over 2.5 million fixed income securities.
  name: Independent Fair Value Prices
- description: Full transparency on pricing methodology, comparable securities, and model inputs.
  name: Price Transparency
- description: Pricing coverage for corporate, government, municipal, and structured products globally.
  name: Coverage Breadth
- description: BVAL prices designed to meet ASC 820/IFRS 13 fair value hierarchy requirements.
  name: Regulatory-Grade Prices
- description: Bloomberg yield curves and spread surfaces used in BVAL pricing.
  name: Yield Curve Data
- description: Full audit trail and pricing justification for regulatory and compliance review.
  name: Audit Trail
finops:
- name: Bloomberg Valuation Service Bval Finops
  service_category: API
  slug: bloomberg-valuation-service-bval-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-valuation-service-bval.png
layout: provider
modified: '2026-04-21'
name: Bloomberg Valuation Service (BVAL)
nav: Providers
network: true
overview: 'Bloomberg Valuation Service (BVAL) publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include BVAL, Evaluated Pricing, Fixed Income, Fair Value, and Bond Pricing.


  Bloomberg Valuation Service (BVAL)''s developer surface includes developer portal, documentation, support, and 3 more developer resources.'
plans:
- name: Bloomberg Valuation Service Bval Plans Pricing
  plan_count: 3
  slug: bloomberg-valuation-service-bval-plans-pricing
random_paper: 112
rate_limits:
- limit_count: 5
  name: Bloomberg Valuation Service Bval Rate Limits
  slug: bloomberg-valuation-service-bval-rate-limits
score:
  band: emerging
  composite: 20.2
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 20.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 25.9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-valuation-service-bval/refs/heads/main/screenshots/bloomberg-valuation-service-bval-2026-07-25T203407.png
security:
- kind: domain-security
  name: Bloomberg Valuation Service Bval Domain Security
  slug: bloomberg-valuation-service-bval-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bloomberg-valuation-service-bval
tags:
- BVAL
- Evaluated Pricing
- Fixed Income
- Fair Value
- Bond Pricing
- Municipal Bonds
- Structured Products
- Bloomberg
use_cases:
- description: Use BVAL prices for end-of-day NAV calculation for fixed income funds.
  name: NAV Calculation
- description: Value fixed income portfolios at fair value for reporting and analytics.
  name: Portfolio Valuation
- description: Meet fair value measurement requirements for ASC 820 and IFRS 13 reporting.
  name: Regulatory Reporting
- description: Use BVAL prices for mark-to-market and risk analytics.
  name: Risk Management
- description: Value fixed income collateral for repo, lending, and margin purposes.
  name: Collateral Valuation
- description: Calculate accurate returns and attribution using BVAL evaluated prices.
  name: Performance Attribution
website: https://www.bloomberg.com/professional/
---
