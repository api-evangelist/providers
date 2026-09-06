---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 17
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/american-equity-investment-life-holding-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/American-Equity-Life
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/american-equity
- group: company
  title: ''
  type: Website
  url: https://www.american-equity.com
- group: start
  title: ''
  type: Portal
  url: https://register.american-equity.com
- group: auth
  title: ''
  type: Security
  url: https://www.american-equity.com/security-disclosure
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/american-equity-investment-life-holding-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/american-equity-investment-life-holding-llms.txt
- group: start
  title: ''
  type: SignUp
  url: https://register.american-equity.com
- group: start
  title: ''
  type: Login
  url: https://myportal.american-equity.com/
- group: operate
  title: ''
  type: Support
  url: https://www.american-equity.com/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.american-equity.com/professionals/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.american-equity.com/insights/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.american-equity.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.american-equity.com/privacy
coverage:
  checked: '2026-09-02'
  detail: American Equity is an annuity carrier whose only integration surfaces are authenticated human web apps — MyPortal for contract owners and contracted agents, AppBuilder, and a product-training LMS; api.american-equity.com is a live AWS API Gateway backing MyPortal that answers 403 {"message":"Forbidden"} on every path except /ping, there is no developer portal, no /llms.txt, no /.well-known document on any host, and the American-Equity-Life GitHub org publishes zero public repositories.
  evidence:
  - status: 403
    url: https://api.american-equity.com/openapi.json
  - status: 200
    url: https://api.american-equity.com/ping
  - status: 404
    url: https://www.american-equity.com/openapi.json
  - status: 404
    url: https://www.american-equity.com/llms.txt
  - status: 404
    url: https://www.american-equity.com/.well-known/api-catalog
  - status: 200
    url: https://api.github.com/orgs/American-Equity-Life/repos
  reason: no-developer-program
  state: none
created: '2024-11-15'
description: American Equity Investment Life Holding Company is a leading provider of guaranteed income solutions, specializing in the design, development, and sale of fixed indexed and fixed-rate annuity products distributed through independent agents and broker-dealers. The company offers products including IncomeShield, AssetShield, EstateShield, and GuaranteeShield annuities, providing retirees with lifetime income, principal protection, tax-deferred growth, and legacy planning options.
features:
- description: Fixed Index Annuities (FIAs) such as IncomeShield, AssetShield, and EstateShield that provide index-linked growth potential with protection from market downside, tax-deferred growth, and guaranteed lifetime income options.
  name: Fixed Indexed Annuities
- description: GuaranteeShield fixed annuity products offering guaranteed interest rates, principal protection, tax-deferred growth, and flexible withdrawal options for conservative retirement savers.
  name: Fixed Annuities
- description: Immediate annuity contracts converting lump sums into guaranteed income payments starting within 12 months, available for lifetime or fixed periods of 5 to 25 years.
  name: Immediate Annuities
- description: Guaranteed lifetime income riders and payout options ensuring customers cannot outlive their retirement savings regardless of market performance.
  name: Lifetime Income Guarantee
- description: Multiple index crediting options including S&P 500, BlackRock Adaptive U.S. Equity, BNPP Patriot Technology Index, Nasdaq Premier, and NYSE Premier indices.
  name: Index Crediting Strategies
- description: Annuity products distributed exclusively through a network of independent insurance agents and broker-dealers, providing broad access for retirement planning clients.
  name: Independent Agent Distribution
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/american-equity-investment-life-holding.png
integrations:
- description: Integration with national and regional broker-dealer networks to distribute annuity products through registered investment advisors and insurance agents.
  name: Independent Broker-Dealer Networks
- description: Compatibility with financial planning software used by independent agents to illustrate and recommend annuity products to clients.
  name: Financial Planning Platforms
layout: provider
modified: '2026-09-02'
name: American Equity Investment Life Holding
nav: Providers
network: true
overview: 'American Equity Investment Life Holding is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Insurance, Annuities, Fixed Indexed Annuity, and Retirement.


  American Equity Investment Life Holding''s developer surface includes developer portal, signup flow, support, engineering blog, and 11 more developer resources.'
plans:
- name: American Equity Investment Life Holding Plans Pricing
  plan_count: 0
  slug: american-equity-investment-life-holding-plans-pricing
press:
- date: '2026-05-25'
  title: ael-20231231
  url: https://www.sec.gov/Archives/edgar/data/1039828/000103982824000020/ael-20231231.htm
- date: '2026-05-25'
  title: American Equity Operating Entities Upgraded To 'A
  url: https://www.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/3165704
- date: '2026-05-25'
  title: AM Best Affirms Credit Ratings of American Equity Investment ...
  url: https://news.ambest.com/newscontent.aspx?refnum=235246
- date: '2026-05-25'
  title: Brookfield Reinsurance signs deal for American Equity ...
  url: https://www.advisor.ca/industry-news/industry/brookfield-reinsurance-signs-deal-for-american-equity-investment-life-holding-co/
- date: '2026-05-25'
  title: American Equity Recognized for Award-Winning Customer ...
  url: https://www.businesswire.com/news/home/20221031005652/en/American-Equity-Recognized-for-Award-Winning-Customer-Satisfaction-Among-Annuity-Providers-in-the-U.S.-by-J.D.-Power
random_paper: 16
rate_limits:
- limit_count: 0
  name: American Equity Investment Life Holding Rate Limits
  slug: american-equity-investment-life-holding-rate-limits
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 17.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 30.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/american-equity-investment-life-holding/refs/heads/main/screenshots/american-equity-investment-life-holding-2026-06-20T171912.png
security:
- kind: domain-security
  name: American Equity Investment Life Holding Domain Security
  slug: american-equity-investment-life-holding-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: American Equity Investment Life Holding Vulnerability Disclosure
  slug: american-equity-investment-life-holding-vulnerability-disclosure
  summary_line: Hackerone
slug: american-equity-investment-life-holding
tags:
- Financial-Services
- Insurance
- Annuities
- Fixed Indexed Annuity
- Retirement
- Life Insurance
- Fortune 1000
use_cases:
- description: Creating guaranteed lifetime income streams for retirees concerned about outliving their savings, providing predictable monthly income regardless of market conditions.
  name: Retirement Income Planning
- description: Protecting retirement assets from market losses while still participating in index-linked growth during favorable market conditions.
  name: Principal Protection
- description: Accumulating retirement savings on a tax-deferred basis, allowing compound growth without annual tax liability until withdrawals begin.
  name: Tax-Deferred Growth
- description: Using EstateShield annuities to combine retirement income security with legacy planning to pass assets to heirs.
  name: Legacy and Estate Planning
- description: Providing a low-risk alternative to market investments for pre-retirees seeking guaranteed growth through fixed annuity products.
  name: Conservative Retirement Savings
website: https://www.american-equity.com
---
