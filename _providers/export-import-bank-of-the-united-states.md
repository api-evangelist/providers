---
access_model:
  confidence: high
  label: Free public data · No signup, no key
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - data-catalog
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: true
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Export Import Bank Of The United States Agentic Access
  operation_count: 4
  slug: export-import-bank-of-the-united-states-agentic-access
  summary_line: 4 operations
api_count: 2
apis:
- description: 'EXIM''s entire programmatic open-data footprint: a Project Open Data v1.1 (DCAT-US) catalog at data.json listing one public dataset — every EXIM authorization approved from 10/01/2006 to the current re'
  name: EXIM Open Data Catalog
  slug: open-data
- description: 26 collections of EXIM's historical record — annual reports, press releases, board materials, executive orders, oral histories, reports to Congress — served over anonymous JSON endpoints and IIIF Pres
  name: EXIM Digital Archives (CONTENTdm / IIIF)
  slug: digital-archives
artifact_total: 25
common:
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
- group: agent
  href: https://artifacts.apis.io/export-import-bank-of-the-united-states/llms/export-import-bank-of-the-united-states-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/export-import-bank-of-the-united-states-llms.txt
- group: design
  href: https://artifacts.apis.io/export-import-bank-of-the-united-states/conformance/export-import-bank-of-the-united-states-conformance.yml
  title: ''
  type: Conformance
  url: conformance/export-import-bank-of-the-united-states-conformance.yml
- group: design
  href: https://artifacts.apis.io/export-import-bank-of-the-united-states/lifecycle/export-import-bank-of-the-united-states-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/export-import-bank-of-the-united-states-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/export-import-bank-of-the-united-states/plans/export-import-bank-of-the-united-states-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/export-import-bank-of-the-united-states-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/export-import-bank-of-the-united-states/rate-limits/export-import-bank-of-the-united-states-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/export-import-bank-of-the-united-states-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/export-import-bank-of-the-united-states/authentication/export-import-bank-of-the-united-states-authentication.yml
  title: ''
  type: Authentication
  url: authentication/export-import-bank-of-the-united-states-authentication.yml
- group: auth
  href: https://artifacts.apis.io/export-import-bank-of-the-united-states/security/export-import-bank-of-the-united-states-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/export-import-bank-of-the-united-states-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/export-import-bank-of-the-united-states/security/export-import-bank-of-the-united-states-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/export-import-bank-of-the-united-states-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.exim.gov/vulnerability-disclosure-policy
- group: agent
  href: https://artifacts.apis.io/export-import-bank-of-the-united-states/agentic-access/export-import-bank-of-the-united-states-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/export-import-bank-of-the-united-states-agentic-access.yml
- group: company
  title: ''
  type: Blog
  url: https://grow.exim.gov/blog
- group: company
  title: ''
  type: Newsroom
  url: https://www.exim.gov/news
- group: operate
  title: ''
  type: Support
  url: https://www.exim.gov/contact/contact-form
- group: operate
  title: ''
  type: Contact
  url: https://www.exim.gov/contact/contact-form
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.exim.gov/privacy-and-security-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.exim.gov/policies
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eximbankus
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/EximBankofUS
- group: company
  title: ''
  type: Twitter
  url: https://x.com/eximbankus
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/eximbankus/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/eximbankus/
coverage:
  checked: '2026-09-04'
  detail: EXIM retired its only programmatic surface — the Socrata/SODA portal at data.exim.gov — on 2023-09-14 by its own published announcement, and the host now has no DNS record at all; what replaced it is a quarterly CSV behind a Project Open Data catalog, so there is no endpoint left to document.
  evidence:
  - status: 0
    url: https://data.exim.gov/
  - status: 200
    url: https://img.exim.gov/s3fs-public/dataset/vbhv-d8am/vbhv-d8am.json
  - status: 200
    url: https://img.exim.gov/s3fs-public/dataset/vbhv-d8am/data.json
  - status: 200
    url: https://www.exim.gov/open-government-data
  - status: 404
    url: https://www.exim.gov/.well-known/security.txt
  - status: 200
    url: https://catalog.data.gov/organization/exim
  reason: no-developer-program
  state: none
created: '2024-07-11'
description: The U.S. Export-Import Bank (EXIM) is the official export credit agency of the United States federal government. It assists in financing and facilitating U.S. exports of goods and services by providing export credit insurance, working capital guarantees, loan guarantees and direct loans to help American businesses compete in the global marketplace. EXIM operates no public API. Its former Socrata/SODA open data portal at data.exim.gov was decommissioned on 2023-09-14 by EXIM's own announcement and the host no longer resolves; what remains is a Project Open Data v1.1 (DCAT-US) catalog pointing at a quarterly CSV of every authorization approved since FY2007, distributed through Data.gov. A separate OCLC CONTENTdm tenant serves EXIM's historical archives over CONTENTdm and IIIF Presentation API 2.0 endpoints at an exim.gov address.
features:
- description: Insurance products protecting US exporters against non-payment by foreign buyers due to commercial or political risks.
  name: Export Credit Insurance
- description: Loan guarantees enabling US businesses to obtain working capital financing from commercial lenders for export activities.
  name: Working Capital Guarantees
- description: Guarantees on loans made by private lenders to foreign buyers for purchases of US goods and services.
  name: Loan Guarantees
- description: Fixed-rate loans provided directly to foreign buyers to finance purchases of US exports.
  name: Direct Loans
- description: A Project Open Data v1.1 catalog and quarterly CSV of every EXIM authorization since FY2007, distributed free through Data.gov.
  name: Open Government Data
- description: Interactive tool to verify export eligibility and financing availability by country.
  name: Country Limitation Schedule
- description: Authenticated portal for submitting and managing export financing applications electronically.
  name: EXIM Online Portal
- description: 26 collections of EXIM's historical record served over CONTENTdm and IIIF endpoints, hosted by OCLC on an exim.gov address.
  name: Digital Archives
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/export-import-bank-of-the-united-states.png
integrations:
- description: EXIM's single public dataset is registered on the federal Data.gov catalog under the exim organization.
  name: Data.gov
- description: Vendor platform hosting the EXIM Digital Archives and its CONTENTdm/IIIF endpoints under www.digitalarchives.exim.gov.
  name: OCLC CONTENTdm
- description: Managed platform for EXIM's Vulnerability Disclosure Program at bugcrowd.com/exim-vdp.
  name: Bugcrowd
- description: Hosts grow.exim.gov, EXIM's exporter-education blog and content site.
  name: HubSpot
layout: provider
modified: '2026-09-04'
name: Export-Import Bank of the United States
nav: Providers
network: true
overview: 'Export-Import Bank of the United States is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Export, Federal Government, Finance, Import, and Open Data.


  Export-Import Bank of the United States'' developer surface includes developer portal, getting-started guide, authentication, engineering blog, support, YouTube channel, and 18 more developer resources.'
plans:
- name: Export Import Bank Of The United States Plans Pricing
  plan_count: 0
  slug: export-import-bank-of-the-united-states-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Export Import Bank Of The United States Rate Limits
  slug: export-import-bank-of-the-united-states-rate-limits
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 4.4
    developer_ergonomics: 57.1
    discoverability: 67.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 29.6
  provenance:
    agentic_access: first-party
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/export-import-bank-of-the-united-states/export-import-bank-of-the-united-states-2026-06-20T180939.png
security:
- kind: authentication
  name: Export Import Bank Of The United States Authentication
  slug: export-import-bank-of-the-united-states-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Export Import Bank Of The United States Domain Security
  slug: export-import-bank-of-the-united-states-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Export Import Bank Of The United States Vulnerability Disclosure
  slug: export-import-bank-of-the-united-states-vulnerability-disclosure
  summary_line: Bugcrowd
slug: export-import-bank-of-the-united-states
tags:
- Export
- Federal Government
- Finance
- Import
- Open Data
- Trade Finance
use_cases:
- description: Enable small and medium-sized US businesses to compete globally with access to export credit and working capital.
  name: Export Financing for Small Businesses
- description: Help foreign buyers finance purchases of US goods and services with EXIM-backed loans.
  name: Foreign Buyer Financing
- description: Protect US exporters against non-payment risk in international transactions.
  name: Export Risk Mitigation
- description: Bulk-download the authorization CSV to analyze US export financing trends, authorized amounts, and industry distributions.
  name: Market Research and Data Analysis
- description: Access authorization records and archival board materials for policy analysis, academic research, and government oversight.
  name: Policy and Compliance Research
website: https://www.exim.gov/
---
