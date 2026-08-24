---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 4
apis:
- description: TIAA's retirement plan services for individual participants, covering 403(b), 457(b), 401(k), and IRA accounts. Products include TIAA Traditional fixed annuity, CREF variable annuities (stock, bond, m
  name: TIAA Retirement Plans
  slug: tiaa-retirement-plans
- description: 'TIAA''s flagship annuity products for retirement income, including TIAA Traditional (a participating fixed annuity with guaranteed minimum plus historical above-floor credits), CREF variable annuities '
  name: TIAA Annuities
  slug: tiaa-annuities
- description: Nuveen is TIAA's wholly owned institutional asset management subsidiary with $1.5 trillion AUM (as of March 2026). Nuveen provides mutual funds, ETFs, closed-end funds, target-date series with embedde
  name: Nuveen Investments
  slug: nuveen-investments
- description: TIAA's wealth management services for individuals, including managed accounts, brokerage services, financial advisory services, life insurance, educational savings (529 plans), and banking products.
  name: TIAA Wealth Management
  slug: tiaa-wealth-management
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tiaa-cref-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tiaa
- group: company
  title: ''
  type: Website
  url: https://www.tiaa.org/public
- group: company
  title: ''
  type: About
  url: https://www.tiaa.org/public/about-tiaa
- group: commercial
  title: ''
  type: Plan Sponsors
  url: https://www.tiaa.org/public/plansponsors
- group: company
  title: ''
  type: Individual Investors
  url: https://www.tiaa.org/public
- group: start
  title: ''
  type: Login
  url: https://auth.tiaa.org/public/authentication/login
- group: other
  title: ''
  type: Nuveen
  url: https://www.nuveen.com/
- group: other
  title: ''
  type: Annual Report
  url: https://www.tiaa.org/public/about-tiaa/corporate-governance
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/TIAA
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/tiaa-cref/refs/heads/main/json-schema/tiaa-cref-retirement-account-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/tiaa-cref/refs/heads/main/json-structure/tiaa-cref-retirement-account-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/tiaa-cref/refs/heads/main/json-ld/tiaa-cref-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/tiaa-cref/refs/heads/main/vocabulary/tiaa-cref-vocabulary.yml
created: '2026-03-24'
description: TIAA (Teachers Insurance and Annuity Association of America, formerly TIAA-CREF) is a Fortune 100 leading provider of financial services for people in the academic, research, medical, cultural, and government fields. With $1.5 trillion in assets under management, TIAA serves over 4.7 million individual customers and more than 12,000 institutional clients. Founded in 1918, TIAA invented the variable annuity in 1952 via the College Retirement Equities Fund (CREF) and is known for its TIAA Traditional fixed annuity and lifetime income solutions. TIAA wholly owns Nuveen Investments, a major institutional asset management firm. TIAA serves primarily non-profit organizations, universities, hospitals, and government entities with retirement plans including 403(b), 457(b), and 401(k) plans.
finops:
- name: Tiaa Cref Finops
  service_category: Financial Services
  slug: tiaa-cref-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tiaa-cref.png
json_schemas:
- name: TIAA Retirement Account
  property_count: 10
  slug: tiaa-cref-retirement-account
json_structures:
- name: Tiaa Cref Retirement Account Structure
  property_count: 0
  slug: tiaa-cref-retirement-account-structure
jsonld:
- class_count: 21
  name: Tiaa Cref Context
  property_count: 22
  slug: tiaa-cref-context
layout: provider
modified: '2026-05-03'
name: TIAA-CREF
nav: Providers
network: true
overview: 'TIAA-CREF publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include 403b, Annuities, Asset Management, Fortune 100, and Higher Education.


  The TIAA-CREF catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Tiaa Cref Plans Pricing
  plan_count: 1
  slug: tiaa-cref-plans-pricing
press:
- date: '2026-05-25'
  title: TIAA Teams Up with Google Cloud to Enhance Client ...
  url: https://www.tiaa.org/public/about-tiaa/news-press/news/2022/09-07
- date: '2026-05-25'
  title: TIAA Launches TIAA gAIt to Delight Clients and Deliver ...
  url: https://www.tiaa.org/public/about-tiaa/news-press/news/2024/07-17
- date: '2026-05-25'
  title: SEC Announces $97 Million Enforcement Action Against ...
  url: https://www.sec.gov/newsroom/press-releases/2021-123
- date: '2026-05-25'
  title: TIAA's Digital, Data, And AI Transformation
  url: https://www.forbes.com/sites/randybean/2023/06/11/tackling-retirement-inequality-tiaas-digital-data-and-ai-transformation/
- date: '2026-05-25'
  title: Participation in TIAA's Lifetime Income Solutions ...
  url: https://www.prnewswire.com/news-releases/participation-in-tiaas-lifetime-income-solutions-accelerates-as-plan-sponsors-embrace-annuity-embedded-defaults-302730672.html
random_paper: 15
rate_limits:
- limit_count: 1
  name: Tiaa Cref Rate Limits
  slug: tiaa-cref-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: TIAA-CREF API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tiaa-cref-jsonschema-spectral-rules
score:
  band: emerging
  composite: 16.9
  delta: 0.0
  facets:
    access_clarity: 19.7
    commercial_clarity: 19.7
    contract_governance: 25.0
    contract_quality: 15.5
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 5.3
  previous_composite: 16.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tiaa-cref/refs/heads/main/screenshots/tiaa-cref-2026-06-20T195327.png
security:
- kind: domain-security
  name: Tiaa Cref Domain Security
  slug: tiaa-cref-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tiaa-cref
tags:
- 403b
- Annuities
- Asset Management
- Fortune 100
- Higher Education
- Institutional
- Insurance
- Investments
- Non-Profit
- Nuveen
- Retirement
- TIAA
website: https://www.tiaa.org/public
---
