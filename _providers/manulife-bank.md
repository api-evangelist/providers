---
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/manulife-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.manulifebank.ca/
- group: company
  title: ''
  type: AboutUs
  url: https://www.manulifebank.ca/support/about-us.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/manulife-bank
created: '2026-07-23'
description: Manulife Bank of Canada is a Schedule I federally chartered bank and a wholly-owned subsidiary of The Manufacturers Life Insurance Company, part of Manulife Financial Corporation. Launched in 1993 as Canada's first branchless (direct) bank — and the first federally regulated bank opened by an insurance company in Canada — it operates entirely through online banking, a mobile app, and telephone banking, with no physical branches. It is best known for the Manulife One all-in-one account, the Advantage Account, GICs, mortgages, and lines of credit that connect everyday banking and borrowing with long-term financial planning. Manulife Bank publishes no first-party public developer portal or downloadable API specifications; no developer.manulifebank.ca host resolves, and the public site is bot-protected. Canada's Consumer-Driven Banking (open-banking) framework — legislated in Budget 2024 and the Fall Economic Statement 2024, with the Financial Consumer Agency of Canada (FCAC) as
  overseer — is legislated but not yet operational, so consumer financial data access today is voluntary and occurs through financial-data aggregators (Plaid, Flinks, MX) rather than a first-party bank API. Interac e-Transfer is offered as a consumer feature but is not exposed as a documented public API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Manulife Bank
nav: Providers
network: true
overview: Manulife Bank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, Canada, Schedule I Bank, and Direct Bank.
random_paper: 114
score:
  band: minimal
  composite: 5.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/manulife-bank/refs/heads/main/screenshots/manulife-bank-2026-07-25T230113.png
security:
- kind: domain-security
  name: Manulife Bank Domain Security
  slug: manulife-bank-domain-security
  summary_line: TLSv1.3 · DMARC
slug: manulife-bank
tags:
- Financial Services
- Banking
- Canada
- Schedule I Bank
- Direct Bank
- Digital Banking
- Data Aggregation
website: https://www.manulifebank.ca/
---
