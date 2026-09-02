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
  scored_at: '2026-09-01'
api_count: 5
apis:
- description: Comprehensive financial planning and advisory services from Thrivent Financial, offering personalized advice across investments, insurance, estate planning, and retirement. Services include free Money
  name: Thrivent Financial Planning
  slug: thrivent-financial-planning
- description: Insurance products from Thrivent Financial including life insurance, disability income insurance, and long-term care strategies, designed to protect members and their families.
  name: Thrivent Insurance
  slug: thrivent-insurance
- description: 'Investment products from Thrivent Financial including mutual funds, actively managed ETFs, annuities, and managed accounts. Includes the Thrivent Managed Accounts Program (minimum $25,000 investment) '
  name: Thrivent Investments
  slug: thrivent-investments
- description: Thrivent Bank is a Utah-chartered industrial bank offering savings and banking products including high-yield savings, church loans, and other banking services to Thrivent members.
  name: Thrivent Bank
  slug: thrivent-bank
- description: Charitable giving and generosity programs from Thrivent including Thrivent Action Teams (190,000 teams with 2.4M volunteers in 2025), donor-advised funds, and member giving programs designed to connec
  name: Thrivent Charitable
  slug: thrivent-charitable
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thrivent-financial-for-lutherans-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thrivent
- group: company
  title: ''
  type: Website
  url: https://www.thrivent.com/
- group: other
  title: ''
  type: Products and Services
  url: https://www.thrivent.com/product-overview
- group: build
  title: ''
  type: Client Resources
  url: https://www.thrivent.com/client-resources
- group: company
  title: ''
  type: About
  url: https://www.thrivent.com/about-us/support
- group: start
  title: ''
  type: Login
  url: https://login.apps.thrivent.com/
- group: other
  title: ''
  type: Mobile App
  url: https://play.google.com/store/apps/details?id=com.thrivent.mobileapp
- group: other
  title: ''
  type: Financial Advisor Network
  url: https://www.thriventadvisornetwork.com/
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/thrivent-financial-for-lutherans/refs/heads/main/json-ld/thrivent-financial-for-lutherans-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/thrivent-financial-for-lutherans/refs/heads/main/vocabulary/thrivent-financial-for-lutherans-vocabulary.yml
created: '2026-03-21'
description: Thrivent Financial is a not-for-profit, membership-owned Fortune 500 financial services organization headquartered in Minneapolis, Minnesota, that helps Christians be wise with money and live generously. With more than $212 billion in assets under management and advisement, over 4,500 employees, and 2.4 million members and clients, Thrivent provides comprehensive financial advice, insurance, investments, banking, and generosity programs. The organization is distinguished by connecting financial planning with charitable giving, community impact, and values-based decision making.
finops:
- name: Thrivent Financial For Lutherans Finops
  service_category: API
  slug: thrivent-financial-for-lutherans-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thrivent-financial-for-lutherans.png
jsonld:
- class_count: 20
  name: Thrivent Financial For Lutherans Context
  property_count: 21
  slug: thrivent-financial-for-lutherans-context
layout: provider
modified: '2026-05-03'
name: Thrivent Financial
nav: Providers
network: true
overview: 'Thrivent Financial publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Annuities, Banking, ETFs, Financial Advice, and Financial Planning.


  The Thrivent Financial catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Thrivent Financial For Lutherans Plans Pricing
  plan_count: 3
  slug: thrivent-financial-for-lutherans-plans-pricing
press:
- date: '2026-05-25'
  title: Parents' Retirement Threatened as High Costs Drive Adult ...
  url: https://newsroom.thrivent.com/2025-04-30-Parents-Retirement-Threatened-as-High-Costs-Drive-Adult-Children-Home,-Thrivents-Annual-Boomerang-Kids-Survey-Shows
- date: '2026-05-25'
  title: Thrivent Financial for Lutherans Boosts Holdings in Equity ...
  url: https://www.marketbeat.com/instant-alerts/filing-thrivent-financial-for-lutherans-boosts-holdings-in-equity-lifestyle-properties-inc-els-2026-05-17/
- date: '2026-05-25'
  title: Thrivent to Add 600 New Financial Advisers in 2026 as Part of ...
  url: https://news.ambest.com/newscontent.aspx?refnum=273194&altsrc=23
- date: '2026-05-25'
  title: Thrivent Receives A++ (Superior) Rating, Stable Outlook ...
  url: https://www.prnewswire.com/news-releases/thrivent-receives-a-superior-rating-stable-outlook-from-am-best-302609261.html
- date: '2026-05-25'
  title: 'Research Update: Thrivent Financial for Lutherans'
  url: https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/12298853
random_paper: 6
rate_limits:
- limit_count: 5
  name: Thrivent Financial For Lutherans Rate Limits
  slug: thrivent-financial-for-lutherans-rate-limits
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 15.2
    contract_quality: 14.7
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 15.2
    operational_transparency: 7.9
  previous_composite: 20.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 16.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thrivent-financial-for-lutherans/refs/heads/main/screenshots/thrivent-financial-for-lutherans-2026-06-20T195319.png
security:
- kind: domain-security
  name: Thrivent Financial For Lutherans Domain Security
  slug: thrivent-financial-for-lutherans-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: thrivent-financial-for-lutherans
tags:
- Annuities
- Banking
- ETFs
- Financial Advice
- Financial Planning
- Fortune 500
- Generosity
- Insurance
- Investments
- Mutual Funds
- Non-Profit
website: https://www.thrivent.com/
---
