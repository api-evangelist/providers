---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
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
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liquidity-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.liquidity.com/
- group: company
  title: ''
  type: About
  url: https://www.liquidity.com/who-we-are
- group: other
  title: ''
  type: Portfolio
  url: https://www.liquidity.com/portfolio
- group: company
  title: ''
  type: Blog
  url: https://www.liquidity.com/news-insights
- group: operate
  title: ''
  type: Support
  url: https://www.liquidity.com/contact
- group: start
  title: ''
  type: Login
  url: https://app.liquiditygroup.com/v2/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.liquidity.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.liquidity.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/liquidity-capital
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/liquidity-group/
- group: company
  title: ''
  type: Careers
  url: https://www.liquidity.com/careers
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/liquidity-group-llms.txt
coverage:
  checked: '2026-08-25'
  detail: LIQUiDITY Group is a private credit lender whose software, the DYNAMiCs decision-science platform, is shipped only as an end-user product to its own analysts, borrowers, fund investors and distributors at app.liquiditygroup.com — the SPA's own bundle names a private /graphql and /api/v3/ backend, but there is no developer program, no API reference, no published spec and no public repository anywhere on liquidity.com, liquiditygroup.com, marsgrowth.com or the company's own GitHub org.
  evidence:
  - status: 404
    url: https://www.liquidity.com/openapi.json
  - status: 404
    url: https://www.liquidity.com/.well-known/security.txt
  - status: 404
    url: https://www.liquidity.com/llms.txt
  - status: 200
    url: https://www.liquidity.com/sitemap.xml
  - status: 400
    url: https://app.liquiditygroup.com/graphql
  - status: 200
    url: https://github.com/liquidity-capital
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: 'LIQUiDITY Group (branded simply "Liquidity") is an AI-native private credit lender and alternative asset manager founded in 2018, headquartered in New York with offices in Tel Aviv, London, Singapore, Tokyo and Abu Dhabi. It underwrites and deploys non-dilutive debt and growth capital — typically $10M to $200M — to late-stage technology and mid-market companies across 35+ countries, using its proprietary DYNAMiCs decision-science platform to compress due diligence from months to days. The firm manages several billion dollars across multiple debt and equity funds, including Mars Growth Capital, a joint venture with MUFG Bank, and is backed by MUFG, Apollo Asset Management, Spark Capital and Meitav Dash. Liquidity is a lender that runs on software rather than a software vendor: its DYNAMiCs platform is operated for its own analysts, borrowers and fund investors at app.liquiditygroup.com and is not offered as a public developer product. No public developer portal, API reference,
  OpenAPI/GraphQL schema, SDK or machine-readable contract is published on any host the company controls.'
image: https://cdn.prod.website-files.com/692473d30dce37720b06615a/6a1ead70262b4f5eccc6226e_logo.png
layout: provider
modified: '2026-08-25'
name: LIQUiDITY Group
nav: Providers
network: true
overview: 'LIQUiDITY Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Private Credit, Lending, and Asset Management.


  LIQUiDITY Group''s developer surface includes engineering blog, support, and 11 more developer resources.'
plans:
- name: Liquidity Group Plans Pricing
  plan_count: 0
  slug: liquidity-group-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Liquidity Group Rate Limits
  slug: liquidity-group-rate-limits
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 13.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/liquidity-group/refs/heads/main/screenshots/liquidity-group-2026-09-02T150546.png
security:
- kind: domain-security
  name: Liquidity Group Domain Security
  slug: liquidity-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: liquidity-group
tags:
- Company
- Financial-Services
- Private Credit
- Lending
- Asset Management
- Venture Debt
- Fintech
- Artificial Intelligence
- Growth Capital
website: https://www.liquidity.com/
---
