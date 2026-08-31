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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/b2b-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://b2bbank.com/en/index
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/company/b2b-bank
- group: operate
  title: ''
  type: Support
  url: https://b2bbank.com/en/contacts/index
- group: company
  title: ''
  type: Careers
  url: https://b2bbank.com/en/careers/careers-at-b2b-bank
- group: commercial
  title: ''
  type: TermsOfService
  url: https://b2bbank.com/en/legal/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.laurentianbank.ca/en/personal/privacy-and-security
created: '2026-07-23'
description: 'B2B Bank is a Schedule I Canadian bank, headquartered in Toronto and wholly owned by Laurentian Bank of Canada (Laurentian Bank Financial Group). It operates a business-to-business, intermediary-only model: rather than serving retail consumers directly, it manufactures and distributes banking products through a network of roughly 27,000 financial professionals — financial advisors and their dealerships, deposit and mortgage brokers and their firms, mutual fund and insurance manufacturers, and CIRO (formerly MFDA/IIROC) members. Its product lines include investment loans, RSP and TFSA loans, broker deposits (GICs and high-interest savings/investment accounts), broker mortgages, and investment and banking accounts. The bank became a Schedule I bank and adopted the B2B Bank name in 2012, consolidating predecessor trust businesses (North American Trust, Sun Life Trust), and its deposits are CDIC insured. On open finance, B2B Bank publishes no first-party developer portal or public
  API: developer.b2bbank.com and api.b2bbank.com do not resolve, and the public site exposes only gated advisor/broker applications (Advisor Access, EASE online loans, Group Access, Investor Access, online banking). Canada''s Consumer-Driven Banking framework is legislated but not yet operational, and the bank documents no FDX participation, Interac data-sharing API, or aggregator program of its own — consistent with an intermediary bank whose digital surface is partner-gated rather than developer-facing.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: B2B Bank
nav: Providers
network: true
overview: 'B2B Bank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, Canada, Schedule I Bank, and Broker Bank.


  B2B Bank''s developer surface includes support and 6 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 1.5
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 1.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/b2b-bank/refs/heads/main/screenshots/b2b-bank-2026-07-25T202139.png
security:
- kind: domain-security
  name: B2B Bank Domain Security
  slug: b2b-bank-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: b2b-bank
tags:
- Financial-Services
- Banking
- Canada
- Schedule I Bank
- Broker Bank
- Deposits
- Mortgages
- Lending
website: https://b2bbank.com/en/index
---
