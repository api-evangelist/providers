---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
  scored_at: '2026-07-27'
api_count: 9
apis:
- description: Cantor Fitzgerald, L.P. is a privately held global financial services firm founded in 1945. It is a U.S. Federal Reserve primary dealer in U.S. government securities and operates investment banking, f
  name: Cantor Fitzgerald
  slug: cantor-fitzgerald
- description: 'Cantor Prime Services is the firm''s multi-asset prime-brokerage platform launched in 2009, offering custody, securities lending, financing, and capital introduction to hedge funds and asset managers. '
  name: Cantor Prime Services
  slug: cantor-prime-services
- description: Cantor Commercial Real Estate, launched in 2010, originates fixed- and floating-rate commercial mortgages and operates as a CMBS issuer and special servicer. Cantor Fitzgerald Income Trust is the firm
  name: Cantor Commercial Real Estate (CCRE)
  slug: cantor-commercial-real-estate
- description: Cantor Equity Partners is Cantor Fitzgerald's blank-check / SPAC vehicle franchise (Cantor Equity Partners I, "CEP"; Cantor Equity Partners II; Cantor Fitzgerald Realty SPACs). The flagship 2025 trans
  name: Cantor Equity Partners (SPAC Platform)
  slug: cantor-equity-partners
- description: Cantor Ventures is the firm's corporate-venture and enterprise-development arm, incubating financial-services, technology, and gaming businesses (including the Hollywood Stock Exchange and TopLine Gam
  name: Cantor Ventures
  slug: cantor-ventures
- description: 'BGC Group, Inc. (NASDAQ: BGC) was formed in 2004 when Cantor Fitzgerald spun out its voice-brokerage business and remains affiliated through common ownership and leadership. BGC operates inter-dealer '
  name: BGC Group (Affiliated)
  slug: bgc-group
- description: 'Fenics Market Data (FMD) is the "exclusive distributor of data for BGC Group, Inc. (NASDAQ: BGC) and its affiliates, a global brokerage group serving the financial markets." FMD covers FX & money mark'
  name: Fenics Market Data (BGC)
  slug: fenics-market-data
- description: 'Newmark Group (NASDAQ: NMRK) is a commercial real-estate advisory and services firm acquired by BGC Partners in October 2011 and spun out as a separate public company in 2017. Services include "Capita'
  name: Newmark Group (Affiliated)
  slug: newmark-group
- description: Hollywood Stock Exchange, founded in 1996 and owned by Cantor Fitzgerald, is "the world's virtual entertainment stock market" — a play-money prediction market for movies, stars, and box-office outcome
  name: Hollywood Stock Exchange
  slug: hollywood-stock-exchange
artifact_total: 15
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cantor-fitzgerald-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cantor-fitzgerald-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cantor.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cantor-fitzgerald
created: '2026-05-19'
description: 'Cantor Fitzgerald, L.P. is a privately held global financial services firm founded in 1945 by Bernard Gerald Cantor and John Fitzgerald, headquartered in New York with more than 12,000 employees across 60+ offices in 20+ countries. The firm is a U.S. Federal Reserve primary dealer and operates investment banking, fixed-income and equities trading, prime brokerage, commercial real-estate lending (CCRE / Cantor Fitzgerald Income Trust), asset management, a SPAC franchise (Cantor Equity Partners), and corporate-venture investing (Cantor Ventures, Hollywood Stock Exchange). Cantor spun out its voice-brokerage business in 2004 to form BGC Partners (now BGC Group, NASDAQ: BGC), which in turn acquired Newmark in 2011 and spun it out as Newmark Group (NASDAQ: NMRK) in 2017. Long-time chairman/CEO Howard Lutnick became the 41st U.S. Secretary of Commerce on February 18, 2025; his sons Brandon and Kyle Lutnick assumed chairman and executive vice chairman roles, with Pascal Bandelier,
  Sage Kelly, and Christian Wall serving as co-CEOs. Cantor has no public developer portal — all electronic-trading, market-data, and prime-brokerage connectivity is delivered B2B under institutional client agreements; the closest public data surface is Fenics Market Data, sold by BGC affiliate Fenics under negotiated entitlement.'
finops:
- name: Cantor Fitzgerald Finops
  service_category: Financial Services
  slug: cantor-fitzgerald-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cantor-fitzgerald.png
jsonld:
- class_count: 8
  name: Cantor Fitzgerald Context
  property_count: 0
  slug: cantor-fitzgerald-context
layout: provider
modified: '2026-05-23'
name: Cantor Fitzgerald
nav: Providers
network: true
overview: 'Cantor Fitzgerald publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Investment Banking, Prime Brokerage, Fixed Income, and Equities.


  The Cantor Fitzgerald catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Cantor Fitzgerald Plans Pricing
  plan_count: 3
  slug: cantor-fitzgerald-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 3
  name: Cantor Fitzgerald Rate Limits
  slug: cantor-fitzgerald-rate-limits
score:
  band: emerging
  composite: 26.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 15.1
    developer_ergonomics: 0.0
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 26.4
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: domain-security
  name: Cantor Fitzgerald Domain Security
  slug: cantor-fitzgerald-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cantor Fitzgerald Vulnerability Disclosure
  slug: cantor-fitzgerald-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cantor-fitzgerald
tags:
- Financial Services
- Investment Banking
- Prime Brokerage
- Fixed Income
- Equities
- Real Estate Finance
- Market Data
- SPAC
website: https://www.cantor.com
---
