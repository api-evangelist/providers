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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/personal-capital-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.personalcapital.com/
- group: start
  title: ''
  type: Login
  url: https://home.personalcapital.com/page/login/goHome
- group: start
  title: ''
  type: SignUp
  url: https://www.personalcapital.com/sign-up/onboarding-v2
- group: operate
  title: ''
  type: Support
  url: https://support-personalwealth.empower.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.personalcapital.com/blog/
created: '2026-07-17'
description: Personal Capital is a digital wealth management and personal finance company, now operating as an Empower company, that pairs free online money-management tools with paid registered-investment-adviser services. Its Personal Capital / Empower Personal Dashboard app lets individuals link bank, brokerage, retirement, and loan accounts to track net worth, analyze investment fees, plan for retirement, and manage cash flow, while Personal Capital Advisors Corporation (an SEC-registered investment adviser) offers human financial advisors and managed portfolios for clients who link at least $100,000 in investable assets. Personal Capital was acquired by Empower Retirement (Great-West Lifeco / Power Corporation) in 2020. The company is consumer-facing and, as of this enrichment pass, does not publish a public developer API, OpenAPI, or developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/personal-capital.png
layout: provider
modified: '2026-07-20'
name: Personal Capital
nav: Providers
network: true
overview: 'Personal Capital is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Wealth Management, Personal Finance, and Financial Planning.


  Personal Capital''s developer surface includes signup flow, support, engineering blog, and 3 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/personal-capital/refs/heads/main/screenshots/personal-capital-2026-09-02T151106.png
security:
- kind: domain-security
  name: Personal Capital Domain Security
  slug: personal-capital-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: personal-capital
tags:
- Company
- Fintech
- Wealth Management
- Personal Finance
- Financial Planning
- Investing
- Retirement
- Financial Advisor
website: https://www.personalcapital.com/
---
