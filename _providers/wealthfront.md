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
  scored_at: '2026-09-03'
api_count: 5
apis:
- description: Internal REST API powering Wealthfront's automated portfolio management service. Supports account creation, portfolio configuration, risk assessment, automated rebalancing, and tax-loss harvesting for
  name: Wealthfront Automated Investing API
  slug: automated-investing-api
- description: Automated tax optimization service providing daily tax-loss harvesting, direct indexing at the stock level for accounts over $100,000, and Smart Beta factor weighting for accounts over $500,000. The s
  name: Wealthfront Tax Optimization API
  slug: tax-optimization-api
- description: High-yield cash management account API supporting deposits, withdrawals, transfers, bill pay, and debit card management. Offers 3.30% base APY with FDIC insurance up to $8 million through deposits swe
  name: Wealthfront Cash Account API
  slug: cash-account-api
- description: External account linking and data aggregation platform that connects Wealthfront with third-party financial institutions via vendors such as Plaid and Finicity. Handles authentication on behalf of cli
  name: Wealthfront Account Linking API
  slug: account-linking-api
- description: 'Financial planning and retirement projection API powering Wealthfront''s Path product. Aggregates linked external accounts, models retirement scenarios, and provides personalized projections for goals '
  name: Wealthfront Financial Planning API (Path)
  slug: financial-planning-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wealthfront-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wealthfront-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/wealthfront/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/wealthfront/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/wealthfront/refs/heads/main/finops/finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.wealthfront.com
- group: company
  title: ''
  type: EngineeringBlog
  url: https://eng.wealthfront.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/wealthfront
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wealthfront.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.wealthfront.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.wealthfront.com
- group: operate
  title: ''
  type: Contact
  url: https://www.wealthfront.com/contact-us
- group: other
  title: ''
  type: Research
  url: https://research.wealthfront.com
- group: auth
  title: ''
  type: Security
  url: https://www.wealthfront.com/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wealthfront.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wealthfront.com/privacy
created: 2026-06-13
description: Wealthfront is an automated investment service offering REST APIs and integrations for portfolio management, financial planning, tax optimization, direct indexing, and cash account management. Founded in 2008 and headquartered in Palo Alto, California, Wealthfront manages approximately $95 billion in assets for over 1.4 million clients as of 2026. The platform provides automated investing with tax-loss harvesting, direct indexing for accounts over $100,000, high-yield cash management accounts with FDIC insurance up to $8 million, and stock investing with no advisory fees. Wealthfront went public on Nasdaq (WLTH) in December 2025.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wealthfront.png
layout: provider
modified: 2026-06-13
name: Wealthfront
nav: Providers
network: true
overview: 'Wealthfront publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Investment, Portfolio-Management, Tax Optimization, and Robo-Advisor.


  Wealthfront''s developer surface includes GitHub presence, pricing, engineering blog, support, and 12 more developer resources.'
plans:
- name: Plans
  plan_count: 6
  slug: plans
random_paper: 1
rate_limits:
- limit_count: 3
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 29.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wealthfront/refs/heads/main/screenshots/wealthfront-2026-06-20T201308.png
security:
- kind: domain-security
  name: Wealthfront Domain Security
  slug: wealthfront-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wealthfront Vulnerability Disclosure
  slug: wealthfront-vulnerability-disclosure
  summary_line: Bugcrowd
slug: wealthfront
tags:
- Finance
- Investment
- Portfolio-Management
- Tax Optimization
- Robo-Advisor
- Wealth Management
- Cash Management
- Direct Indexing
- Financial Planning
- Fintech
website: https://www.wealthfront.com
---
