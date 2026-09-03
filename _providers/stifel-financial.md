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
api_count: 3
apis:
- description: Stifel Bank account data accessible via Finicity (Mastercard) open banking aggregation API, enabling third-party applications to retrieve account balances, transaction history, and investment portfoli
  name: Stifel Bank Finicity Integration
  slug: stifel-bank-finicity
- description: Stifel Trust Company account data accessible via Plaid open banking aggregation API, enabling third-party applications to access financial account data through standardized connectivity.
  name: Stifel Bank Plaid Integration
  slug: stifel-bank-plaid
- description: Stifel Wealth Tracker is a client-facing portfolio management portal enabling investors to monitor account performance, holdings, and financial activity online.
  name: Stifel Wealth Tracker
  slug: stifel-wealth-tracker
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stifel-financial-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stifel-financial
- group: company
  title: ''
  type: Website
  url: https://www.stifel.com
- group: other
  title: ''
  type: Technology
  url: https://www.choosestifel.com/technology/
- group: other
  title: ''
  type: Open Banking Tracker
  url: https://www.openbankingtracker.com/provider/stifel-bank-personal/apis
- group: company
  title: ''
  type: Blog
  url: https://www.stifel.com/rss/headlines
created: '2026-05-02'
description: Stifel Financial is a financial services holding company whose subsidiaries provide securities brokerage, investment banking, trading, investment advisory, and related financial services to individual investors, corporations, and government entities. Stifel bank accounts are accessible via open banking data aggregators including Plaid and Finicity (Mastercard) for third-party financial applications.
finops:
- name: Stifel Financial Finops
  service_category: Financial Services
  slug: stifel-financial-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stifel-financial.png
jsonld:
- class_count: 13
  name: Stifel Financial Context
  property_count: 0
  slug: stifel-financial-context
layout: provider
modified: '2026-05-02'
name: Stifel Financial
nav: Providers
network: true
overview: 'Stifel Financial publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Wealth Management, Investment Banking, Open Banking, and Financial-Services.


  The Stifel Financial catalog on APIs.io includes 1 JSON-LD context.


  Stifel Financial''s developer surface includes engineering blog and 5 more developer resources.'
plans:
- name: Stifel Financial Plans Pricing
  plan_count: 1
  slug: stifel-financial-plans-pricing
press:
- date: '2026-05-25'
  title: 2025 Annual Report
  url: https://www.stifel.com/docs/pdf/investorrelations/annualreports/annual2025.pdf
- date: '2026-05-25'
  title: Chen X. Na - Stifel Financial Corp.
  url: https://www.linkedin.com/in/chen-x-na-26b9867
- date: '2026-05-25'
  title: Schwab, Raymond James, Stifel drop as AI stirs concerns ...
  url: https://www.investing.com/news/stock-market-news/schwab-raymond-james-stifel-drop-as-ai-stirs-concerns-over-advisory-models-4497514
- date: '2026-05-25'
  title: Autonomy 2.0
  url: https://stifelinstitutional.com/iris/autonomy-2-0/
- date: '2026-05-25'
  title: Stifel CEO 'not comfortable' with AI replacing advisor ...
  url: https://www.investmentnews.com/independent-broker-dealers/stifel-ceo-not-comfortable-with-ai-replacing-advisor-judgement/266281
random_paper: 8
rate_limits:
- limit_count: 1
  name: Stifel Financial Rate Limits
  slug: stifel-financial-rate-limits
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 10
    catalog_gap: 65.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 12.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 13.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stifel-financial/refs/heads/main/screenshots/stifel-financial-2026-06-20T194550.png
security:
- kind: domain-security
  name: Stifel Financial Domain Security
  slug: stifel-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: stifel-financial
tags:
- Finance
- Wealth Management
- Investment Banking
- Open Banking
- Financial-Services
- Fortune 1000
website: https://www.stifel.com
---
