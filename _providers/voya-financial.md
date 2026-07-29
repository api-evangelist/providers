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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voya-financial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.voya.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.voya.com/
- group: other
  title: ''
  type: DataFeed
  url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001535778&type=&dateb=&owner=include&count=40
- group: other
  title: ''
  type: MarketData
  url: https://finance.yahoo.com/quote/VOYA/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/voya-financial
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/voya-financial
created: '2025-02-08'
description: 'Voya Financial (NYSE: VOYA) is a leading health, wealth, and investment company serving approximately 14.7 million individual, workplace, and institutional clients. Voya specializes in retirement plans, group employee benefits, health savings accounts (HSAs), and investment management. Their myVoyage platform integrates financial wellness tools to help participants plan, invest, and protect their financial futures. Voya does not offer a public developer API but provides account connectivity through open banking aggregators such as Plaid.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/voya-financial.png
json_schemas:
- name: Voya Retirement Account
  property_count: 13
  slug: voya-retirement-account
jsonld:
- class_count: 0
  name: Voya Financial Context
  property_count: 6
  slug: voya-financial-context
layout: provider
modified: '2026-05-03'
name: Voya Financial
nav: Providers
network: true
overview: 'Voya Financial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Benefits, Finance, Fortune 500, Health Savings, and Investment Management.


  The Voya Financial catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
press:
- date: '2026-05-25'
  title: Learn how Voya Financial used AI and machine
  url: https://www.facebook.com/MicrosoftinBusiness/posts/learn-how-voya-financial-used-ai-and-machine-learning-to-transform-its-investmen/10159673606868393/
- date: '2026-05-25'
  title: Voya celebrates success of 24/7 chatbot and emerging ...
  url: https://www.theglobeandmail.com/investing/markets/stocks/VOYA/pressreleases/12061687/
- date: '2026-05-25'
  title: Voya Financial joins the Workday Wellness Partner ...
  url: https://www.businesswire.com/news/home/20250911276055/en/Voya-Financial-joins-the-Workday-Wellness-Partner-Program-to-enhance-employee-wellness-through-AI-powered-benefits
- date: '2026-05-25'
  title: Machine Intelligence Dynamic Global Equity
  url: https://institutional.voya.com/investment-capabilities/machine-intelligence-ai-driven/machine-intelligence-dynamic-global-equity
- date: '2026-05-25'
  title: Voya celebrates success of 24/7 chatbot and emerging ...
  url: https://www.voya.com/news/2022/11/voya-celebrates-success-247-chatbot-and-emerging-artificial-intelligence-capabilities
random_paper: 39
rules:
- name: Voya Financial API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: voya-financial-jsonschema-spectral-rules
score:
  band: emerging
  composite: 14.7
  delta: -3.9
  facets:
    commercial_clarity: 0.0
    contract_quality: 8.1
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 18.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/voya-financial/refs/heads/main/screenshots/voya-financial-2026-06-20T201145.png
security:
- kind: domain-security
  name: Voya Financial Domain Security
  slug: voya-financial-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: voya-financial
tags:
- Benefits
- Finance
- Fortune 500
- Health Savings
- Investment Management
- Retirement
website: https://www.voya.com/
---
