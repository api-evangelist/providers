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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 5
apis:
- description: Electronic trading API for executing trades across fixed income, derivatives, and ETF markets. Supports RFQ (Request for Quote), click-to-trade, and automated execution via AiEX (Automated Intelligent
  name: Tradeweb Trading API
  slug: trading-api
- description: Python API enabling seamless integration between trading strategies and Tradeweb execution. Allows direct connection between Python-coded trading models and Tradeweb for solicited workflows and Automa
  name: Tradeweb Python API
  slug: python-api
- description: FIX protocol connectivity for electronic trading integration with order management systems, risk systems, and third-party trading platforms. Industry-standard FIX messaging for trade execution and str
  name: Tradeweb FIX API
  slug: fix-api
- description: Real-time and historical market data API providing independent pricing information and benchmark OTC pricing data across more than 20 asset classes including government bonds, credit, swaps, and ETFs.
  name: Tradeweb Market Data API
  slug: market-data-api
- description: Approved Publication Arrangement (APA) API enabling market participants to meet MiFID II post-trade transparency requirements. Supports real-time trade reporting across all mandated instrument classes
  name: Tradeweb APA Trade Reporting API
  slug: apa-api
artifact_total: 38
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tradeweb-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tradeweb
- group: start
  title: ''
  type: Portal
  url: https://www.tradeweb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tradeweb.com/our-markets/institutional/integration/
- group: operate
  title: ''
  type: Support
  url: https://www.tradeweb.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.tradeweb.com/newsroom/media-center/insights/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tradeweb.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tradeweb.com/privacy-policy/
- group: design
  title: ''
  type: Spectral
  url: rules/tradeweb-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tradeweb-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tradeweb-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tradeweb-trade-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tradeweb-rfq-schema.json
created: '2026-03-16'
description: Tradeweb Markets is a leading global operator of electronic marketplaces for rates, credit, equities, and money markets. The platform provides APIs for electronic trading execution, straight-through processing, market data, trade reporting, and integration with order management and risk systems across more than 40 fixed income and derivatives products.
examples:
- key_count: 13
  name: Tradeweb Rfq Example
  slug: tradeweb-rfq-example
features:
- description: Send RFQs to multiple dealers simultaneously for competitive pricing on fixed income and derivatives.
  name: Request for Quote (RFQ)
- description: Automated trade execution with pre-defined rules for straight-through processing.
  name: Automated Intelligent Execution (AiEX)
- description: One-click trade execution on streaming dealer prices.
  name: Click-to-Trade
- description: Real-time and historical pricing data across 20+ asset classes as an independent benchmark source.
  name: Market Data
- description: MiFID II compliant post-trade transparency reporting via Approved Publication Arrangement.
  name: Trade Reporting (APA)
- description: Automated post-trade processing from execution to settlement with STP vendor integration.
  name: Straight-Through Processing
- description: Direct connection between Python trading models and Tradeweb execution.
  name: Python API
- description: Industry-standard FIX protocol integration with OMS, EMS, and risk systems.
  name: FIX Connectivity
- description: Trading across rates, credit, equities, ETFs, and money markets on a single platform.
  name: Multi-Asset Coverage
- description: Transaction cost analysis and liquidity analytics before trade execution.
  name: Pre-Trade Analytics
finops:
- name: Tradeweb Finops
  service_category: API
  slug: tradeweb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tradeweb.png
json_schemas:
- name: Tradeweb RFQ
  property_count: 11
  slug: tradeweb-rfq
- name: Tradeweb Trade
  property_count: 16
  slug: tradeweb-trade
json_structures:
- name: Tradeweb Trade Structure
  property_count: 0
  slug: tradeweb-trade-structure
jsonld:
- class_count: 29
  name: Tradeweb Context
  property_count: 0
  slug: tradeweb-context
layout: provider
modified: '2026-05-03'
name: Tradeweb
nav: Providers
network: true
overview: 'Tradeweb publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Electronic Trading, Financial Markets, Fixed Income, Market Data, and OTC Trading.


  The Tradeweb catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tradeweb''s developer surface includes developer portal, documentation, support, engineering blog, and 9 more developer resources.'
plans:
- name: Tradeweb Plans Pricing
  plan_count: 3
  slug: tradeweb-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Tradeweb Rate Limits
  slug: tradeweb-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tradeweb API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tradeweb-jsonschema-spectral-rules
- effective_rule_count: 17
  extends: []
  name: Tradeweb API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 2
  slug: tradeweb-spectral-rules
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 12
    catalog_gap: 49.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 10.7
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 20.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: domain-security
  name: Tradeweb Domain Security
  slug: tradeweb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tradeweb
solutions:
- description: Electronic marketplace for buy-side institutional trading across fixed income and derivatives.
  name: Tradeweb Institutional
- description: Inter-dealer marketplace for wholesale fixed income and derivatives trading.
  name: Tradeweb Wholesale (Dealerweb)
- description: Electronic marketplace for retail-sized fixed income trading.
  name: Tradeweb Retail
- description: Market data, pricing, and analytics services including APA trade reporting.
  name: Tradeweb Data & Analytics
tags:
- Electronic Trading
- Financial Markets
- Fixed Income
- Market Data
- OTC Trading
use_cases:
- description: Execute government bond, corporate bond, and municipal bond trades electronically.
  name: Institutional Fixed Income Trading
- description: Trade interest rate swaps, credit default swaps, and other OTC derivatives.
  name: Derivatives Execution
- description: Access institutional ETF liquidity with RFQ and portfolio trading workflows.
  name: ETF Trading
- description: Connect Python-based algo strategies directly to Tradeweb execution via API.
  name: Algorithmic Trading
- description: Integrate Tradeweb execution with order management and portfolio management systems.
  name: OMS Integration
- description: Meet MiFID II post-trade transparency requirements via APA trade reporting.
  name: Regulatory Reporting
- description: Access independent OTC pricing data for valuation, risk, and compliance.
  name: Market Data Analytics
- description: Execute US Treasury and government bond trades across CLOB and RFQ protocols.
  name: Treasury Management
website: https://www.tradeweb.com/
---
