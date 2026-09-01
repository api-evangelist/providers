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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/laurentian-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.laurentianbank.ca/en
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.laurentianbank.ca/en/about-us/investor-relations
- group: company
  title: ''
  type: Blog
  url: https://news.laurentianbank.ca/
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/company/banque-laurentienne
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.laurentianbank.ca/en/personal/privacy-and-security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.laurentianbank.ca/en/personal/legal-notice
- group: auth
  title: ''
  type: Security
  url: https://www.laurentianbank.ca/en/personal/ways-to-bank/security
- group: operate
  title: ''
  type: Support
  url: https://www.laurentianbank.ca/en/contact-us
created: '2026-07-23'
description: Laurentian Bank of Canada (Banque Laurentienne du Canada) is a Montreal-headquartered Schedule I chartered bank, founded in 1846 as the Montreal City and District Savings Bank and listed on the Toronto Stock Exchange as LB. With roughly CA$47 billion in assets, about 3,000 employees, and approximately 1.5 million clients, it serves personal, commercial, and capital-markets customers - concentrated in Quebec with commercial offices across Canada - through subsidiaries including B2B Bank, Laurentian Bank Securities, and LBC Capital. The bank operates no public developer portal and exposes no first-party or FDX-style data-access API; consumer data access is aggregator-mediated today (screen-scraping via providers such as Flinks and Plaid), and Canada's federal Consumer-Driven Banking framework remains legislated but not yet operational, so participation is voluntary. In December 2025 the bank announced a proposed sale to Fairstone Bank of Canada, with National Bank of Canada acquiring
  its retail operations.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Laurentian Bank of Canada
nav: Providers
network: true
overview: 'Laurentian Bank of Canada is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, Canada, Schedule I Bank, and Retail Banking.


  Laurentian Bank of Canada''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 2.0
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/laurentian-bank/refs/heads/main/screenshots/laurentian-bank-2026-07-25T224628.png
security:
- kind: domain-security
  name: Laurentian Bank Domain Security
  slug: laurentian-bank-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: laurentian-bank
tags:
- Financial-Services
- Banking
- Canada
- Schedule I Bank
- Retail Banking
- Quebec
- Interac
- Data Aggregation
website: https://www.laurentianbank.ca/en
---
