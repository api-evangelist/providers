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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cibc-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cibc-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.cibc.com
- group: company
  title: ''
  type: About
  url: https://www.cibc.com/en/about-cibc.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cibc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cibc
- group: docs
  title: ''
  type: Documentation
  url: https://www.cibc.com/en/commercial/business-solutions/managing-cash-flow/cash-management-services.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cibc.com/en/privacy-security/privacy-policy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cibc.com/en/legal.html
- group: other
  title: ''
  type: DataAggregator
  url: https://plaid.com/institutions/cibc/
created: '2026-07-23'
description: 'Canadian Imperial Bank of Commerce (CIBC) is a Schedule I domestic chartered bank and one of Canada''s Big Six, formed in 1961 through the merger of the Canadian Bank of Commerce and the Imperial Bank of Canada and headquartered in Toronto, Ontario. Serving roughly eleven million personal, business, commercial, wealth, and capital-markets clients across Personal & Business Banking, Wealth Management, and Capital Markets, CIBC is a participant in the shared Canadian rails, including Interac e-Transfer and Payments Canada settlement systems. Canada has no operational open-banking mandate today: the federal Consumer-Driven Banking framework legislated in Budget 2024 and the 2024 Fall Economic Statement, overseen by the Financial Consumer Agency of Canada (FCAC), is not yet live, so access remains voluntary and fragmented. CIBC runs no first-party public developer portal (developer.cibc.com does not resolve) and publishes no downloadable OpenAPI or Swagger specifications. Consumer-permissioned
  data access is aggregator-mediated: CIBC signed a tokenized data-access agreement with U.S. aggregator MX (announced August 2022, MX''s first in Canada) to let clients share financial data with third-party apps without exposing banking credentials, and its accounts are also reachable through Plaid (Assets, Auth, Balance). Corporate connectivity is offered through CIBC SWIFT Corporate Access (SCA) file exchange rather than a public REST API, so CIBC''s honest public API surface today is aggregator-mediated only, pending the coming Consumer-Driven Banking regime.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: CIBC
nav: Providers
network: true
overview: 'CIBC is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, Canada, Big Six, and Schedule I Bank.


  CIBC''s developer surface includes documentation and 9 more developer resources.'
random_paper: 103
score:
  band: minimal
  composite: 10.2
  delta: -3.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 13.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cibc/refs/heads/main/screenshots/cibc-2026-07-25T205336.png
security:
- kind: domain-security
  name: Cibc Domain Security
  slug: cibc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cibc
tags:
- Financial Services
- Banking
- Canada
- Big Six
- Schedule I Bank
- Open Finance
- Consumer-Driven Banking
- Interac
- Payments
- Data Aggregation
website: https://www.cibc.com
---
