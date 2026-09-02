---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Export Import Bank Of The United States Agentic Access
  operation_count: 3
  slug: export-import-bank-of-the-united-states-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: EXIM Bank publishes open government datasets through the federal Data.gov catalog. Datasets include export authorization records from 2006 onward, accessible programmatically via the Socrata Open Data
  name: EXIM Open Data API
  slug: open-data
- description: The Resource API from Export-Import Bank of the United States — 2 operation(s) for resource.
  name: Export-Import Bank of the United States Resource API
  slug: export-import-bank-of-the-united-states-resource-api
- description: The Views API from Export-Import Bank of the United States — 1 operation(s) for views.
  name: Export-Import Bank of the United States Views API
  slug: export-import-bank-of-the-united-states-views-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: EXIM Bank Open Data API (Socrata SODA) Resource API
  slug: open-export-import-bank-of-the-united-states-resource-api
- collection_type: open
  name: EXIM Bank Open Data API (Socrata SODA) Resource Views API
  slug: open-export-import-bank-of-the-united-states-views-api
- collection_type: open
  name: EXIM Bank Open Data API (Socrata SODA)
  slug: open-export-import-bank-of-the-united-states
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/export-import-bank-of-the-united-states-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/export-import-bank-of-the-united-states-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/export-import-bank-of-the-united-states-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.exim.gov/
- group: start
  title: ''
  type: Portal
  url: https://eximonline.exim.gov/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.exim.gov/open-government-data
- group: company
  title: ''
  type: Blog
  url: https://grow.exim.gov/blog
- group: operate
  title: ''
  type: Contact
  url: https://www.exim.gov/contact/contact-form
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.exim.gov/privacy-and-security-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/export-import-bank-of-the-united-states/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/EximBank
created: '2024-07-11'
description: The U.S. Export-Import Bank (EXIM) is the official export credit agency of the United States federal government. It assists in financing and facilitating U.S. exports of goods and services by providing export credit insurance, working capital guarantees, and direct loans to help American businesses compete in the global marketplace. EXIM publishes open government data including authorization records accessible via the federal Data.gov catalog using the Socrata Open Data API (SODA).
features:
- description: Insurance products protecting US exporters against non-payment by foreign buyers due to commercial or political risks.
  name: Export Credit Insurance
- description: Loan guarantees enabling US businesses to obtain working capital financing from commercial lenders for export activities.
  name: Working Capital Guarantees
- description: Guarantees on loans made by private lenders to foreign buyers for purchases of US goods and services.
  name: Loan Guarantees
- description: Fixed-rate loans provided directly to foreign buyers to finance purchases of US exports.
  name: Direct Loans
- description: Public datasets including authorization records accessible via Data.gov and the Socrata Open Data API.
  name: Open Government Data
- description: Interactive tool to verify export eligibility and financing availability by country.
  name: Country Limitation Schedule
- description: Online portal for submitting and managing export financing applications electronically.
  name: EXIM Online Portal
finops:
- name: About Exim Exim Gov Export Import Bank Of The United States Finops
  service_category: API
  slug: about-exim-exim-gov-export-import-bank-of-the-united-states-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/export-import-bank-of-the-united-states.png
integrations:
- description: EXIM datasets are published through the federal Data.gov catalog for public access.
  name: Data.gov
- description: EXIM open data is accessible via the Socrata Open Data API (SODA) for programmatic data access.
  name: Socrata SODA API
layout: provider
modified: '2026-04-19'
name: Export-Import Bank of the United States
nav: Providers
network: true
overview: 'Export-Import Bank of the United States publishes 2 APIs on the [APIs.io](https://apis.io/) network: Resource API and Views API. Tagged areas include Export, Federal-Government, Finance, Import, and Trade Finance.


  Export-Import Bank of the United States'' developer surface includes authentication, developer portal, getting-started guide, engineering blog, YouTube channel, and 6 more developer resources.'
plans:
- name: About Exim Exim Gov Export Import Bank Of The United States Plans Pricing
  plan_count: 3
  slug: about-exim-exim-gov-export-import-bank-of-the-united-states-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: About Exim Exim Gov Export Import Bank Of The United States Rate Limits
  slug: about-exim-exim-gov-export-import-bank-of-the-united-states-rate-limits
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 52.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 29.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/export-import-bank-of-the-united-states/refs/heads/main/screenshots/export-import-bank-of-the-united-states-2026-06-20T180939.png
security:
- kind: authentication
  name: Export Import Bank Of The United States Authentication
  slug: export-import-bank-of-the-united-states-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Export Import Bank Of The United States Domain Security
  slug: export-import-bank-of-the-united-states-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: export-import-bank-of-the-united-states
tags:
- Export
- Federal-Government
- Finance
- Import
- Trade Finance
use_cases:
- description: Enable small and medium-sized US businesses to compete globally with access to export credit and working capital.
  name: Export Financing for Small Businesses
- description: Help foreign buyers finance purchases of US goods and services with EXIM-backed loans.
  name: Foreign Buyer Financing
- description: Protect US exporters against non-payment risk in international transactions.
  name: Export Risk Mitigation
- description: Use EXIM open data to analyze US export financing trends, authorized amounts, and industry distributions.
  name: Market Research and Data Analysis
- description: Access authorization records for policy analysis, academic research, and government oversight.
  name: Policy and Compliance Research
website: https://www.exim.gov/
---
