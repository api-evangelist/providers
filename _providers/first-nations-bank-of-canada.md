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
  url: security/first-nations-bank-of-canada-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/first-nations-bank-of-canada-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://www.fnbc.ca/
- group: other
  title: ''
  type: OnlineBanking
  url: https://online.fnbc.ca/
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/company/first-nations-bank-of-canada
- group: company
  title: ''
  type: Blog
  url: https://www.fnbc.ca/about/media-centre/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fnbc.ca/about/regulatory/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fnbc.ca/about/regulatory/privacy-code
- group: operate
  title: ''
  type: Support
  url: https://www.fnbc.ca/contact-us
- group: other
  title: ''
  type: Regulatory
  url: https://www.fnbc.ca/about/regulatory/regulatory-and-CDIC
created: '2026-07-23'
description: 'First Nations Bank of Canada (FNBC) is a Schedule I federally regulated chartered bank under the Bank Act, chartered on 19 November 1996 and headquartered in Saskatoon, Saskatchewan. It is the first Canadian chartered bank to be independently controlled by Indigenous shareholders — roughly 88% Indigenous owned and controlled by 78 Indigenous shareholder groups from Nunavut, Northwest Territories, Yukon, Saskatchewan, Manitoba, Alberta and Quebec — and focuses on serving the Indigenous marketplace, with over 90% of its loans going directly to Indigenous communities, many of its branches on reserve, and CDIC-insured deposits. On the open-finance and API front, FNBC runs no first-party developer portal and publishes no public API: probes of developer.fnbc.ca, api.fnbc.ca and developers.fnbc.ca all fail to resolve, and the fnbc.ca site exposes only retail online-banking and a mobile app, not a documented API surface. Canada''s federal Consumer-Driven Banking framework (legislated
  via Budget 2024 / Fall Economic Statement 2024, with FCAC as overseer) is not yet operational, so third-party access to FNBC account data today is voluntary and effectively aggregator-mediated (Flinks, Plaid and similar), not a first-party open-banking API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: First Nations Bank of Canada
nav: Providers
network: true
overview: 'First Nations Bank of Canada is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, Canada, Schedule I Bank, and Indigenous.


  First Nations Bank of Canada''s developer surface includes engineering blog, support, and 8 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/first-nations-bank-of-canada/refs/heads/main/screenshots/first-nations-bank-of-canada-2026-07-25T214606.png
security:
- kind: domain-security
  name: First Nations Bank Of Canada Domain Security
  slug: first-nations-bank-of-canada-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: first-nations-bank-of-canada
tags:
- Financial-Services
- Banking
- Canada
- Schedule I Bank
- Indigenous
- Consumer-Driven Banking
- Data Aggregation
- Interac
website: https://www.fnbc.ca/
---
