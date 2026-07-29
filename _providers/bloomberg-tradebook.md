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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: FIX protocol connectivity to Bloomberg Tradebook for electronic order routing, execution reporting, and position updates across equities, futures, options, and FX markets. Supports FIX 4.2, 4.4, and 5
  name: Bloomberg Tradebook FIX API
  slug: tradebook-fix-api
- description: Integration between Bloomberg's Electronic Order Management System (EMSX) and Tradebook for seamless order routing from the Bloomberg Terminal to Tradebook execution desks and algorithms.
  name: Bloomberg EMSX-Tradebook Integration
  slug: emsx-tradebook-integration
- description: Bloomberg Tradebook's foreign exchange marketplace for electronic FX spot, forward, and swap execution. Launched in 2007, providing competitive FX pricing and execution from major liquidity providers.
  name: Bloomberg Tradebook FX Marketplace
  slug: tradebook-fx
artifact_total: 17
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-tradebook-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bloomberg-tradebook
- group: start
  title: ''
  type: Portal
  url: https://www.bloomberg.com/professional/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bloomberg.com/professional/product/tradebook/
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
description: Bloomberg Tradebook is an electronic brokerage and agency trading platform offering execution services across global equities, futures, options, and foreign exchange. Founded in 1996 as a Bloomberg LP subsidiary, Tradebook provides algorithmic trading, direct market access, and transaction cost analysis (TCA) via FIX protocol connectivity and integration with Bloomberg Terminal workflows.
features:
- description: Access to Tradebook's proprietary and third-party trading algorithms.
  name: Algorithmic Trading
- description: DMA connectivity to global equity and futures exchanges.
  name: Direct Market Access
- description: TCA reporting for evaluating execution quality and broker performance.
  name: Transaction Cost Analysis
- description: Standard FIX protocol integration for order routing and execution.
  name: FIX Connectivity
- description: Electronic FX marketplace for competitive spot and forward execution.
  name: FX Execution
- description: Access to global equity, futures, options, and FX markets through one platform.
  name: Global Execution
finops:
- name: Bloomberg Tradebook Finops
  service_category: API
  slug: bloomberg-tradebook-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-tradebook.png
layout: provider
modified: '2026-04-21'
name: Bloomberg Tradebook
nav: Providers
network: true
overview: 'Bloomberg Tradebook publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Tradebook, Electronic Trading, Equities, Futures, and Options.


  Bloomberg Tradebook''s developer surface includes developer portal, documentation, support, and 4 more developer resources.'
plans:
- name: Bloomberg Tradebook Plans Pricing
  plan_count: 3
  slug: bloomberg-tradebook-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 5
  name: Bloomberg Tradebook Rate Limits
  slug: bloomberg-tradebook-rate-limits
score:
  band: thin
  composite: 28.0
  delta: -1.3
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 29.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 33.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-tradebook/refs/heads/main/screenshots/bloomberg-tradebook-2026-07-25T203405.png
security:
- kind: domain-security
  name: Bloomberg Tradebook Domain Security
  slug: bloomberg-tradebook-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bloomberg-tradebook
tags:
- Tradebook
- Electronic Trading
- Equities
- Futures
- Options
- FX
- Agency Brokerage
- Bloomberg
use_cases:
- description: Execute equity orders globally with algorithmic and DMA strategies.
  name: Equity Execution
- description: Trade global futures contracts through Tradebook's electronic platform.
  name: Futures Trading
- description: Execute FX transactions competitively through Tradebook's FX marketplace.
  name: FX Execution
- description: Analyze execution quality and broker performance with TCA reporting.
  name: Execution Quality Measurement
website: https://www.bloomberg.com/professional/
---
