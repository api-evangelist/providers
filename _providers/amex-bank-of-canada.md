---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amex-bank-of-canada-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.americanexpress.com/en-ca/
- group: company
  title: ''
  type: About
  url: https://www.americanexpress.com/en-ca/company/about-american-express/
- group: auth
  title: ''
  type: RegulatoryDisclosures
  url: https://www.americanexpress.com/ca/en/company/legal/pillar-iii.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.americanexpress.com/en-ca/company/legal/online-terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.americanexpress.com/en-ca/company/legal/privacy-centre/privacy-statement/
- group: operate
  title: ''
  type: Support
  url: https://www.americanexpress.com/ca/en/customer-service/contact-us.html
created: '2026-07-23'
description: Amex Bank of Canada is the Canadian banking subsidiary of the American Express Company (United States), incorporated in 1990 and headquartered in the Toronto area (Markham, Ontario). It is a Schedule II bank under Canada's Bank Act — a foreign-bank subsidiary regulated by the Office of the Superintendent of Financial Institutions (OSFI) and treated as a Category II small-and-medium-sized deposit-taking institution — and it issues American Express charge and credit cards to Canadian consumers and businesses. As a card-centric Schedule II bank, Amex Bank of Canada runs no first-party developer portal of its own; the global American Express developer platform at developer.americanexpress.com is operated by the U.S. parent (a separate profile), not by this Canadian entity. Canada's federal Consumer-Driven Banking (open-banking) framework, legislated in Budget 2024 and the 2024 Fall Economic Statement with the Financial Consumer Agency of Canada (FCAC) as overseer, is not yet operational,
  so consumer data access to Amex-Canada accounts today is voluntary and largely aggregator-based rather than served by a public first-party API. This is an identity/provider record; no public Canadian API surface is documented.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Amex Bank of Canada
nav: Providers
network: true
overview: 'Amex Bank of Canada is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, Canada, Schedule II Bank, and Foreign Bank Subsidiary.


  Amex Bank of Canada''s developer surface includes support and 6 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amex-bank-of-canada/refs/heads/main/screenshots/amex-bank-of-canada-2026-07-25T200104.png
security:
- kind: domain-security
  name: Amex Bank Of Canada Domain Security
  slug: amex-bank-of-canada-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amex-bank-of-canada
tags:
- Financial-Services
- Banking
- Canada
- Schedule II Bank
- Foreign Bank Subsidiary
- Credit Cards
- Payments
- Consumer-Driven Banking
website: https://www.americanexpress.com/en-ca/
---
