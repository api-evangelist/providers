---
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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'National Bank of Canada exposes no public, self-serve first-party developer API. Consumer financial-data access is consent-based and aggregator-mediated: when a customer links a fintech app, National '
  name: National Bank Consumer Data Access (Aggregator-Mediated)
  slug: consumer-data-access-aggregator
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-bank-of-canada-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/national-bank-of-canada-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.nbc.ca/
- group: company
  title: ''
  type: About
  url: https://www.nbc.ca/about-us.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/national-bank-of-canada
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.nbc.ca/about-us/investors.html
- group: company
  title: ''
  type: Newsroom
  url: https://www.nbc.ca/about-us/news-media/press-release.html
- group: company
  title: ''
  type: Careers
  url: https://emplois.bnc.ca/en_CA/careers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nbc.ca/privacy-policy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nbc.ca/terms-of-use.html
- group: other
  title: ''
  type: DataAccess
  url: https://www.flinks.com/go/open-banking-api
created: '2026-07-23'
description: 'National Bank of Canada (Banque Nationale du Canada, TSX: NA) is a Schedule I chartered bank headquartered in Montreal, Quebec, founded in 1859. It is the sixth-largest of Canada''s Big Six banks and the leading bank in Quebec, serving personal, commercial, wealth-management, and financial-markets clients. On open finance, National Bank is a notable first-mover: it was the first major Canadian bank to launch a secure, consent-based data-sharing API for retail customers, but it does NOT operate a public self-serve first-party developer portal. Programmatic access to customer financial data is delivered through aggregators rather than a downloadable public API — principally Flinks, the Montreal aggregator in which National Bank holds an ~80% stake, via its Open Banking Environment (OBE), and also through Plaid. National Bank and Flinks are founding participants of the FDX Canada working group, aligning their data-sharing on the FDX technical standard, and the bank is positioning
  ahead of Canada''s forthcoming, legislated-but-not-yet-operational Consumer-Driven Banking framework (Budget 2024 / FCAC oversight). Today access is voluntary and aggregator-mediated; there is no operational open-banking mandate and no public first-party API surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: National Bank of Canada
nav: Providers
network: true
overview: National Bank of Canada publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, Canada, Big Six, and Open Banking.
random_paper: 9
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 3
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-bank-of-canada/refs/heads/main/screenshots/national-bank-of-canada-2026-08-07T184639.png
security:
- kind: domain-security
  name: National Bank Of Canada Domain Security
  slug: national-bank-of-canada-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: national-bank-of-canada
tags:
- Financial-Services
- Banking
- Canada
- Big Six
- Open Banking
- Consumer-Driven Banking
- FDX
- Data Aggregation
- Payments
website: https://www.nbc.ca/
---
