---
access_model:
  confidence: high
  label: No public API program
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
api_count: 2
apis:
- description: The investor-facing digital channel for Core Natural Resources, the company Arch Coal / Arch Resources became after the January 2025 merger with CONSOL Energy. It publishes SEC filings, quarterly earn
  name: Core Natural Resources Investor Relations
  slug: core-investor-relations
- description: Machine-readable filing data for Core Natural Resources is available from the U.S. Securities and Exchange Commission, not from the company. The SEC EDGAR submissions API returns the full filing histo
  name: SEC EDGAR Filings (Core Natural Resources, CIK 1710366)
  slug: sec-edgar-filings
artifact_total: 19
common:
- group: company
  title: ''
  type: Website
  url: https://corenaturalresources.com/
- group: start
  title: ''
  type: Portal
  url: https://corenaturalresources.com/
- group: company
  title: ''
  type: Legacy Website
  url: https://archresources.com/
- group: company
  title: ''
  type: Investors
  url: https://corenaturalresources.com/investors/
- group: company
  title: ''
  type: News
  url: https://corenaturalresources.com/news-media/
- group: other
  title: ''
  type: Sustainability
  url: https://corenaturalresources.com/sustainability/
- group: other
  title: ''
  type: Suppliers
  url: https://corenaturalresources.com/suppliers/
- group: company
  title: ''
  type: Careers
  url: https://corenaturalresources.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://corenaturalresources.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://corenaturalresources.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://corenaturalresources.com/arch-terms-and-conditions/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/core-natural-resources
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arch-coal-domain-security.yml
created: '2026-03-23'
description: 'Arch Coal was a St. Louis-based producer and marketer of metallurgical and thermal coal, renamed Arch Resources in 2020. In January 2025 Arch Resources merged with CONSOL Energy in a merger of equals to form Core Natural Resources, Inc. (NYSE: CNR), headquartered in Canonsburg, Pennsylvania. The combined company operates the Pennsylvania Mining Complex, Leer, Leer South, West Elk, Black Thunder, and other mines across six U.S. states with 5,000+ employees, and holds stakes in East Coast marine export terminals. Core Natural Resources does not publish a public developer API. Its external digital surface is a corporate website at corenaturalresources.com plus a separate investor relations portal; machine-readable company data is available only through third-party channels such as the SEC EDGAR APIs.'
features:
- description: Low-Vol (Beckley, Itmann), High-Vol A (Leer, Leer South), and High-Vol B (Mountain Laurel) metallurgical coals for blast furnace steelmaking — roughly 12 million tons annually.
  name: Metallurgical Coal
- description: High CV thermal coal from the Pennsylvania Mining Complex and West Elk mine for power generation, cement, and industrial use — roughly 30 million tons annually.
  name: High Calorific Value Thermal Coal
- description: PRB sub-bituminous coal from Black Thunder and Coal Creek mines in Wyoming.
  name: Powder River Basin Thermal Coal
- description: Ownership stakes in East Coast marine export terminals, with roughly 25 million tons of owned annual export capacity.
  name: Marine Export Terminals
- description: Advanced materials and critical mineral extraction research turning coal-based carbon into products for aerospace and other industries.
  name: CONSOL Innovations
- description: Quarterly earnings, production and sales volume reporting, and SEC filings published as HTML and PDF through the investor relations portal and EDGAR.
  name: SEC Filings and Investor Reporting
finops:
- name: Arch Coal Finops
  service_category: Industrial / Mining
  slug: arch-coal-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arch-coal.png
integrations:
- description: All filings for CIK 0001710366 are available through EDGAR and the SEC's public JSON APIs at data.sec.gov.
  name: SEC EDGAR
- description: Shares trade on the New York Stock Exchange under the ticker CNR; market data flows through standard exchange and market data providers.
  name: NYSE
layout: provider
modified: '2026-07-25'
name: Arch Coal
nav: Providers
network: true
overview: 'Arch Coal publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Mining, Coal, Metallurgical Coal, Thermal Coal, and Energy.


  Arch Coal''s developer surface includes developer portal, product news, and 11 more developer resources.'
plans:
- name: Arch Coal Plans Pricing
  plan_count: 1
  slug: arch-coal-plans-pricing
press:
- date: '2026-05-25'
  title: About Core Natural Resources
  url: https://corenaturalresources.com/about-core/
- date: '2026-05-25'
  title: Press Releases
  url: https://www.ftc.gov/news-events/news/press-releases?initialSessionID=144-1670540-8490742&page=379
- date: '2026-05-25'
  title: Arch Resources winding down massive US coal mine as ...
  url: https://www.spglobal.com/market-intelligence/en/news-insights/articles/2021/2/arch-resources-winding-down-massive-us-coal-mine-as-customer-base-dwindles-62788531
- date: '2026-05-25'
  title: Q4 2018 Arch Coal Inc Earnings Call Transcript
  url: https://www.gurufocus.com/news/2231894/q4-2018-arch-coal-inc-earnings-call-transcript?mobile=true
- date: '2026-05-25'
  title: Despite a strong quarter for its Powder River Basin ...
  url: https://www.facebook.com/cowboystatedaily/posts/despite-a-strong-quarter-for-its-powder-river-basin-operations-arch-resources-in/500718778737496/
random_paper: 48
rate_limits:
- limit_count: 1
  name: Arch Coal Rate Limits
  slug: arch-coal-rate-limits
security:
- kind: domain-security
  name: Arch Coal Domain Security
  slug: arch-coal-domain-security
  summary_line: HSTS · DMARC
slug: arch-coal
tags:
- Mining
- Coal
- Metallurgical Coal
- Thermal Coal
- Energy
- Core Natural Resources
- Investor Relations
- Fortune 500
use_cases:
- description: Analyze Core Natural Resources (NYSE:CNR) financial performance, production volumes, and market position through EDGAR filings and investor materials.
  name: Investment Research
- description: Follow the Arch Coal → Arch Resources → Core Natural Resources lineage, including the CONSOL Energy merger of equals completed January 2025.
  name: Merger and Lineage Tracking
- description: Access environmental, safety, and governance disclosures published through the corporate sustainability section.
  name: ESG and Safety Reporting
- description: Steel producers, utilities, and suppliers reference product specifications, terms and conditions, and the Supplier Code of Conduct.
  name: Supply Chain and Procurement
- description: Track metallurgical and thermal coal production, export capacity, and sales volumes for commodity market research.
  name: Commodity Market Analysis
website: https://corenaturalresources.com/
---
