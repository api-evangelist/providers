---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.0
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: Digital platform providing financial advisors and their clients access to independent investment managers with differentiated investment solutions. Offers access to mutual funds, separately managed ac
  name: AMG Wealth Platform
  slug: affiliated-managers-group-wealth-platform
- description: Investor relations platform providing shareholders, analysts, and institutional investors access to AMG's financial performance data, earnings releases, SEC filings, governance documents, and corporat
  name: AMG Investor Relations
  slug: affiliated-managers-group-investor-relations
- baseURL: https://wealth.amg.com/wp-json/amgfundsdata/v1
  baseurl_source: declared
  description: 'Undocumented, anonymously callable JSON API on wealth.amg.com that backs the AMG Wealth Platform product pages. Exposed as the AMG-authored WordPress REST namespace amgfundsdata/v1, whose route table '
  name: AMG Funds Data API
  slug: affiliated-managers-group-funds-data
- baseURL: https://www.amg.com/wp-json/amginc/v1
  baseurl_source: declared
  description: Undocumented, anonymously callable JSON API on www.amg.com that backs the AMG Affiliate directory. Exposed as the AMG-authored WordPress REST namespace amginc/v1. A single POST-only route, /amginc/v1/
  name: AMG Corporate Content API
  slug: affiliated-managers-group-corporate-content
artifact_total: 26
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/affiliated-managers-group-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/affiliated-managers-group-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/affiliated-managers-group-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/affiliated-managers-group-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/affiliated-managers-group-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/affiliated-managers-group-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/affiliated-managers-group-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/affiliated-managers-group-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/affiliated-managers-group-packages.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/affiliated-managers-group-vocabulary.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/affiliated-managers-group-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/affiliated-managers-group-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/affiliated-managers-group-finops.yml
- group: operate
  title: ''
  type: Support
  url: https://www.amg.com/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/affiliated-managers-group
- group: company
  title: ''
  type: Website
  url: https://www.amg.com
- group: start
  title: ''
  type: Portal
  url: https://wealth.amg.com
- group: start
  title: ''
  type: Login
  url: https://wealth.amg.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amg.com/privacy-notices/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amg.com/terms-and-conditions/
created: '2026-04-19'
description: Affiliated Managers Group (AMG) is a global asset management company that partners with outstanding independent investment management firms. With approximately $813 billion in assets under management across roughly 40 affiliate firms and 500+ investment strategies, AMG provides capital, distribution, and operational support while preserving each affiliate's investment autonomy. AMG operates a Wealth Platform for financial advisors and an Institutional Platform for global institutional investors, offering mutual funds, separately managed accounts, and alternative investment strategies.
features:
- description: Partners with independent investment managers while preserving their autonomy and investment culture.
  name: Affiliate Partnership Model
- description: Access to 500+ investment strategies across equity, fixed income, alternative, and sustainability-focused asset classes.
  name: Multi-Asset Investment Strategies
- description: Exclusive access to customized investment strategies through separately managed accounts for wealth clients.
  name: Separately Managed Accounts
- description: Global distribution platform extending affiliate reach to institutional investors in key markets worldwide.
  name: Global Institutional Distribution
- description: Wealth platform providing financial advisors curated access to independent manager strategies and client account tools.
  name: Financial Advisor Platform
- description: Comprehensive investor relations platform with financial data, SEC filings, and earnings information for public shareholders.
  name: Investor Relations Portal
finops:
- name: Affiliated Managers Group Finops
  service_category: Investment Management
  slug: affiliated-managers-group-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/affiliated-managers-group.png
integrations:
- description: Network of ~40 independent boutique investment managers including Yacktman, Tweedy Browne, and other established firms.
  name: AMG Affiliate Network
- description: Private markets investment vehicle providing access to private equity strategies through an AMG-sponsored fund.
  name: AMG Pantheon Fund
- description: AMG is publicly traded on the New York Stock Exchange under the ticker symbol AMG.
  name: NYSE
- description: Integration with broker-dealer and RIA custodial platforms for seamless separately managed account delivery.
  name: Financial Advisor Platforms
- description: Relationships with institutional investment consultants facilitating mandate sourcing for affiliate managers.
  name: Institutional Consultant Networks
layout: provider
modified: '2026-08-30'
name: Affiliated Managers Group
nav: Providers
network: true
overview: 'Affiliated Managers Group publishes 2 APIs on the [APIs.io](https://apis.io/) network: AMG Funds Data API and AMG Corporate Content API. Tagged areas include Asset Management, Investment Management, Financial-Services, Wealth Management, and Institutional Investing.


  Affiliated Managers Group''s developer surface includes authentication, support, developer portal, and 18 more developer resources.'
plans:
- name: Affiliated Managers Group Plans Pricing
  plan_count: 1
  slug: affiliated-managers-group-plans-pricing
press:
- date: '2026-05-25'
  title: AMG 2026 proxy details board, pay and auditors
  url: https://www.stocktitan.net/sec-filings/AMG/def-14a-affiliated-managers-group-inc-definitive-proxy-statement-43ab713fa48d.html
- date: '2026-05-25'
  title: A Look at Affiliated Managers Group (AMG) Valuation After ...
  url: https://finance.yahoo.com/news/look-affiliated-managers-group-amg-021044341.html
- date: '2026-05-25'
  title: 2023 Annual Report - Investor Relations
  url: https://ir.amg.com/static-files/2dab9faa-964c-4998-bb0b-6ce967ae754a
- date: '2026-05-25'
  title: AMG and Parnassus Investments Announce Partnership
  url: https://www.parnassus.com/updates/article/amg_and_parnassus_investments_announce_partnership
- date: '2026-05-25'
  title: AFFILIATED MANAGERS GROUP, INC. - Investor Relations
  url: https://ir.amg.com/static-files/8a2c2594-42c3-4f8f-95dd-222c6272344c
random_paper: 6
rate_limits:
- limit_count: 0
  name: Affiliated Managers Group Rate Limits
  slug: affiliated-managers-group-rate-limits
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 43.0
    catalog_earned_first_party: 8.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 15.2
    contract_quality: 13.3
    developer_ergonomics: 37.5
    discoverability: 57.4
    governance: 15.2
    operational_transparency: 0.0
  previous_composite: 31.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/affiliated-managers-group/refs/heads/main/screenshots/affiliated-managers-group-2026-06-20T165600.png
security:
- kind: authentication
  name: Affiliated Managers Group Authentication
  slug: affiliated-managers-group-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Affiliated Managers Group Domain Security
  slug: affiliated-managers-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: affiliated-managers-group
tags:
- Asset Management
- Investment Management
- Financial-Services
- Wealth Management
- Institutional Investing
- Fortune 1000
use_cases:
- description: Boutique investment firms partner with AMG to receive growth capital while maintaining investment independence.
  name: Independent Manager Capital Partnerships
- description: Financial advisors use AMG Wealth Platform to access differentiated investment strategies for client portfolios.
  name: Financial Advisor Diversification
- description: Institutional investors access AMG's affiliate network for specialized investment mandates across asset classes.
  name: Institutional Mandate Sourcing
- description: Wealth clients access alternative investment strategies including hedge funds and private markets through AMG affiliates.
  name: Alternative Investment Access
- description: Investors access sustainability-focused strategies from AMG affiliate managers across multiple asset classes.
  name: ESG and Sustainable Investing
- description: NYSE shareholders and analysts track AMG's financial performance and governance through the investor relations portal.
  name: Public Shareholder Engagement
website: https://www.amg.com
---
