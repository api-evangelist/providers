---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: Green Button Connect My Data is the OAuth2-based ESPI service that lets Con Edison customers authorize a registered third party to receive their interval energy usage and account data on a recurring b
  name: Green Button Connect My Data
  slug: green-button-connect
- description: 'Customer-driven file export that lets Con Edison residential and small commercial accounts download up to one year of smart-meter interval data as CSV or ESPI XML directly from the My Account portal. '
  name: Green Button Download My Data
  slug: green-button-download
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/consolidated-edison-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Con-Edison
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/con-edison
- group: company
  title: ''
  type: Website
  url: https://www.coned.com
- group: start
  title: ''
  type: Customer Portal
  url: https://www.coned.com/en/accounts-billing
- group: other
  title: ''
  type: Become a Third Party
  url: https://www.coned.com/en/accounts-billing/share-energy-usage-data/become-a-third-party
- group: other
  title: ''
  type: Share My Data Overview
  url: https://www.coned.com/en/accounts-billing/share-energy-usage-data/share-my-data
- group: company
  title: ''
  type: Investor Relations
  url: https://investor.conedison.com
- group: company
  title: ''
  type: Careers
  url: https://www.conedjobs.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coned.com/en/about-us/privacy-statement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coned.com/en/about-us/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.coned.com/en/contact-us
created: '2026-03-21'
description: Consolidated Edison, Inc. (Con Edison) is a Fortune 500 holding company that, through its subsidiaries, provides electric, natural gas, and steam service to customers in New York City and Westchester County. Con Edison does not publish a general-purpose developer portal; programmatic data access is delivered through the Green Button Connect My Data (GBC) program, which lets authorized third parties retrieve customer energy usage data via the NAESB Energy Services Provider Interface (ESPI) standard once the customer grants consent through Con Edison's authorization portal.
finops:
- name: Consolidated Edison Finops
  service_category: Regulated Utility / Energy
  slug: consolidated-edison-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/consolidated-edison.png
layout: provider
modified: '2026-04-28'
name: Consolidated Edison
nav: Providers
network: true
overview: 'Consolidated Edison publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Fortune 500, Green Button, Natural Gas, and New York.


  Consolidated Edison''s developer surface includes support and 11 more developer resources.'
plans:
- name: Consolidated Edison Plans Pricing
  plan_count: 1
  slug: consolidated-edison-plans-pricing
press:
- date: '2026-05-25'
  title: 'Document 2 - file: ed-20251231xexx991.htm'
  url: https://www.sec.gov/Archives/edgar/data/1047862/000104786226000028/ed-20251231xexx991.htm
- date: '2026-05-25'
  title: CON EDISON REPORTS 2026 FIRST QUARTER EARNINGS
  url: https://www.prnewswire.com/news-releases/con-edison-reports-2026-first-quarter-earnings-302766258.html
- date: '2026-05-25'
  title: CON EDISON REPORTS 2026 FIRST QUARTER EARNINGS
  url: https://investor.conedison.com/news-releases/news-release-details/con-edison-reports-2026-first-quarter-earnings
- date: '2026-05-25'
  title: Con Edison Selects C3.ai for Big Data and Predictive ...
  url: https://c3.ai/utility-selects-c3-iot-big-data-predictive-analytics-platform-applications/
- date: '2026-05-25'
  title: Con Edison posts higher 2025 earnings, sets 2026 EPS view
  url: https://www.stocktitan.net/sec-filings/ED/8-k-consolidated-edison-inc-reports-material-event-0907b1b03c4d.html
random_paper: 7
rate_limits:
- limit_count: 1
  name: Consolidated Edison Rate Limits
  slug: consolidated-edison-rate-limits
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 14.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/consolidated-edison/refs/heads/main/screenshots/consolidated-edison-2026-07-25T210311.png
security:
- kind: domain-security
  name: Consolidated Edison Domain Security
  slug: consolidated-edison-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: consolidated-edison
tags:
- Energy
- Fortune 500
- Green Button
- Natural Gas
- New York
- Steam
- Utility
website: https://www.coned.com
---
