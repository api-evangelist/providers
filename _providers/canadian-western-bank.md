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
  url: security/canadian-western-bank-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/canadian-western-bank-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.cwbank.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.nbc.ca/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/canadian-western-bank
- group: company
  title: ''
  type: Twitter
  url: https://x.com/cwbank
created: '2026-07-23'
description: 'Canadian Western Bank (CWB) is a Schedule I domestic chartered bank founded in 1988 (through the merger of the Bank of Alberta and Western & Pacific Bank) and headquartered in Edmonton, Alberta at Canadian Western Bank Place. Historically the largest publicly traded Schedule I bank headquartered in Western Canada and listed on the Toronto Stock Exchange (TSX: CWB), it held roughly CA$43 billion in assets and focused on full-service business and commercial banking, personal banking, equipment financing and leasing, trust services, and wealth management across a network of affiliated entities. In June 2024 National Bank of Canada agreed to acquire CWB in an all-share deal valued at roughly CA$5 billion, and the acquisition closed in early 2025; CWB now operates as a subsidiary of National Bank of Canada and its branches and brand are being wound down and rebranded under National Bank. Consistent with Canada''s voluntary and still fragmented open-finance landscape — the federal
  Consumer-Driven Banking framework was legislated in 2024 (Budget 2024 / Fall Economic Statement, overseen by the FCAC) but is not yet operational — CWB publishes no first-party public developer portal and no documented public API. Its developer and API hostnames do not resolve, and the entire cwbank.com domain now 301-redirects to National Bank of Canada (nbc.ca). Consumer-permissioned account and transaction data is reached only indirectly through third-party data aggregators (Plaid is confirmed via aggregator coverage directories). No first-party FDX-conformant data-access API was found. This is an honest identity-only, aggregator-only record for an institution now absorbed into National Bank of Canada.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Canadian Western Bank
nav: Providers
network: true
overview: Canadian Western Bank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, Canada, Schedule I Bank, and Business Banking.
random_paper: 7
score:
  band: minimal
  composite: 6.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/canadian-western-bank/refs/heads/main/screenshots/canadian-western-bank-2026-07-25T204330.png
security:
- kind: domain-security
  name: Canadian Western Bank Domain Security
  slug: canadian-western-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: canadian-western-bank
tags:
- Financial Services
- Banking
- Canada
- Schedule I Bank
- Business Banking
- Alberta
- Open Finance
- Consumer-Driven Banking
- Data Aggregation
website: https://www.cwbank.com/
---
