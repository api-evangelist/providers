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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 3
apis:
- description: Zions Treasury Internet Banking provides businesses with a secure online platform for managing treasury operations including ACH payments, domestic and international wire transfers, account transfers,
  name: Zions Treasury Internet Banking
  slug: treasury-internet-banking
- description: Zions ACH Payments is a payment disbursement solution enabling businesses to pay employees, suppliers, vendors, and tax agencies via ACH. Supports import and export file formats for integration with a
  name: Zions ACH Payments
  slug: ach-payments
- description: Zions Wire Transfer Services enables businesses to send domestic and international wire transfers efficiently. Supports foreign currency transfers to more than 60 countries worldwide. Available throug
  name: Zions Wire Transfer Services
  slug: wire-transfers
artifact_total: 17
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zions-bancorp-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zions-bancorporation
- group: company
  title: ''
  type: Website
  url: https://www.zionsbank.com
- group: start
  title: ''
  type: Portal
  url: https://treasurygateway.zionsbank.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zionsbank.com/business/treasury/
- group: start
  title: ''
  type: Login
  url: https://www.zionsbank.com/personal/sign-in/
- group: operate
  title: ''
  type: Support
  url: https://www.zionsbank.com/personal/customer-service/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zionsbank.com/disclosure-documents/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zionsbank.com/about/privacy/
created: '2026-05-03'
description: Zions Bancorporation is one of the nation's premier financial services companies, operating under local management teams and distinct brands in 11 western U.S. states. The company offers a comprehensive suite of banking, treasury management, lending, and wealth management services for individuals, businesses, and public sector clients. Zions provides ERP-to-bank integration capabilities, ACH payment origination, wire transfers, and cash management tools for corporate treasury operations. The company does not currently publish a public REST API developer portal; integrations are delivered via Treasury Internet Banking import/export, NACHA-compliant ACH files, and direct file-transfer arrangements with corporate customers.
features:
- description: Online treasury management platform with payment origination and reporting.
  name: Treasury Internet Banking
- description: NACHA-compliant ACH payment file origination for payroll, vendor, and tax payments.
  name: ACH Origination
- description: Domestic and international wire transfers including foreign currency.
  name: Wire Transfers
- description: Check fraud prevention with issued-check matching and exception review.
  name: Positive Pay
- description: File import/export integration with accounting and ERP systems.
  name: ERP Integration
- description: Real-time visibility into account balances, transactions, and check images.
  name: Account Reporting
finops:
- name: Zions Bancorp Finops
  service_category: API
  slug: zions-bancorp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zions-bancorp.png
layout: provider
modified: '2026-05-03'
name: Zions Bancorporation
nav: Providers
network: true
overview: 'Zions Bancorporation publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Financial Services, Treasury Management, Payments, and Fortune 1000.


  Zions Bancorporation''s developer surface includes developer portal, documentation, support, and 6 more developer resources.'
plans:
- name: Zions Bancorp Plans Pricing
  plan_count: 3
  slug: zions-bancorp-plans-pricing
press:
- date: '2026-05-25'
  title: Zions Profit 'Marred' by Charge Tied to Bad Loans
  url: https://www.wsj.com/finance/banking/zions-logs-higher-third-quarter-profit-despite-50-million-charge-8d38e852
- date: '2026-05-25'
  title: Zions Bancorporation, National Association Reports First ...
  url: https://finance.yahoo.com/markets/stocks/articles/zions-bancorporation-national-association-reports-201000841.html
- date: '2026-05-25'
  title: Zions Bancorporation Q1 2026 earnings jump 38%
  url: https://www.stocktitan.net/sec-filings/ZION/8-k-zions-bancorporation-national-association-ut-reports-material-eve-c88df85228fc.html
- date: '2026-05-25'
  title: Zions Bancorp. - Latest News
  url: https://www.americanbanker.com/organization/zions-bancorp
- date: '2026-05-25'
  title: Zions Bancorporation, National Association Reports Fourth ...
  url: https://zionsbancorp.com/news-events/press-releases/news-details/2024/Zions-Bancorporation-National-Association-Reports-Fourth-Quarter-Financial-Results/default.aspx
random_paper: 8
rate_limits:
- limit_count: 5
  name: Zions Bancorp Rate Limits
  slug: zions-bancorp-rate-limits
score:
  band: emerging
  composite: 21.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 21.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zions-bancorp/refs/heads/main/screenshots/zions-bancorp-2026-06-20T201911.png
security:
- kind: domain-security
  name: Zions Bancorp Domain Security
  slug: zions-bancorp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zions-bancorp
tags:
- Banking
- Financial Services
- Treasury Management
- Payments
- Fortune 1000
use_cases:
- description: Cash management and payment origination for corporate treasurers.
  name: Corporate Treasury Operations
- description: Treasury and payment services for state, county, and municipal governments.
  name: Public Sector Banking
- description: Banking and payment services for small and mid-sized businesses.
  name: Small Business Banking
- description: Trust, investment, and wealth advisory services.
  name: Wealth Management
website: https://www.zionsbank.com
---
