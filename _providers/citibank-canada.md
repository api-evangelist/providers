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
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Citigroup's group-level institutional API platform (Citi Developer Experience / CitiConnect, from Treasury and Trade Solutions) that Citi Canada's corporate and institutional clients integrate with fo
  name: Citi Institutional (CitiConnect) API Platform
  slug: citi-institutional-citiconnect-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/citibank-canada-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.citigroup.com/citi/about/countries-and-jurisdictions/canada.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.citi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.citi.com/apis/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Citi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/citi
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.citigroup.com/global/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/citibank-canada-llms.txt
created: '2026-07-23'
description: Citibank Canada (Citi Canada) is the Canadian arm of Citigroup, chartered under Canada's Bank Act as a Schedule II (foreign bank subsidiary) deposit-taking institution, established in 1919 in Toronto and headquartered at Citigroup Place, 123 Front Street West. It is a member of the Canadian Bankers Association and the Canada Deposit Insurance Corporation (CDIC). Citi Canada is an institutional and corporate bank only — securities trading, cash management, treasury, trade finance, custody, clearing, securities financing and private banking — having exited Canadian consumer retail banking years ago (its MasterCard portfolio was sold to CIBC in 2010 and CitiFinancial Canada, now Fairstone, was divested in 2017). It runs no Canada-specific developer portal; its corporate and institutional clients integrate through Citigroup's group-level Citi Developer Experience and CitiConnect API platform for payments, statements/reporting, balance inquiry and FX. Canada has no operational open-banking
  mandate — the federal Consumer-Driven Banking framework (Budget 2024 / FES 2024, overseen by the FCAC) is legislated but not yet live — and because Citi Canada holds no retail consumer accounts here, consumer data-aggregation access is not applicable to this entity.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Citibank Canada
nav: Providers
network: true
overview: 'Citibank Canada publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, Canada, Schedule II Bank, and Institutional Banking.


  Citibank Canada''s developer surface includes documentation and 7 more developer resources.'
random_paper: 90
score:
  band: minimal
  composite: 12.9
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 12.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 12.7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/citibank-canada/refs/heads/main/screenshots/citibank-canada-2026-07-25T205424.png
security:
- kind: domain-security
  name: Citibank Canada Domain Security
  slug: citibank-canada-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: citibank-canada
tags:
- Financial Services
- Banking
- Canada
- Schedule II Bank
- Institutional Banking
- Treasury and Trade
- Corporate Banking
- Payments
website: https://www.citigroup.com/citi/about/countries-and-jurisdictions/canada.html
---
