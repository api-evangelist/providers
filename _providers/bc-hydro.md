---
access_model:
  confidence: high
  label: Free · Own-account customer login required
  onboarding: unknown
  pricing: free
  public: false
  source:
  - documentation
  - authentication
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bc-hydro-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bc-hydro-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bc-hydro-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bc-hydro-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bc-hydro-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/bc-hydro-packages.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/bc-hydro-outages-map.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bc-hydro-llms.txt
- group: auth
  title: ''
  type: Compliance
  url: https://www.bchydro.com/work-with-us/suppliers/doing-business-with-bchydro/contractor-cybersecurity.html
- group: company
  title: ''
  type: Website
  url: https://www.bchydro.com/
- group: company
  title: ''
  type: About
  url: https://www.bchydro.com/about.html
- group: docs
  title: ''
  type: Documentation
  url: https://app.bchydro.com/accounts-billing/bill-payment/view-bill.html
- group: docs
  title: ''
  type: Documentation
  url: https://app.bchydro.com/accounts-billing/rates-energy-use/access-load-data.html
- group: auth
  title: ''
  type: Authentication
  url: https://www.bchydro.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.bchydro.com/contact.html
- group: operate
  title: ''
  type: HelpCenter
  url: https://app.bchydro.com/accounts-billing/get-help.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bchydro.com/siteinfo/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bchydro.com/siteinfo/privacy.html
- group: other
  title: ''
  type: Accessibility
  url: https://www.bchydro.com/toolbar/about/accountability_reports/accessibility.html
- group: company
  title: ''
  type: Blog
  url: https://www.bchydro.com/news/press_centre.html
- group: company
  title: ''
  type: News
  url: https://www.bchydro.com/news.html
- group: other
  title: ''
  type: Tariff
  url: https://www.bchydro.com/toolbar/about/strategies-plans-regulatory/tariffs-terms-conditions.html
- group: other
  title: ''
  type: OpenData
  url: https://catalogue.data.gov.bc.ca/organization/bc-hydro-and-power-authority
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bc-hydro
- group: other
  title: ''
  type: Regulator
  url: https://www.bcuc.com/
- group: other
  title: ''
  type: Standard
  url: https://www.greenbuttonalliance.org/
created: '2026-07-27'
description: 'British Columbia Hydro and Power Authority (BC Hydro) is a provincial Crown corporation whose sole shareholder is the Province of British Columbia, and which states that it generates and delivers electricity to "95% of the population of B.C." and serves "over five million people." It is the vertically integrated end of the value chain in a market with no retail competition: BC Hydro owns the generation fleet (predominantly large hydroelectric), owns and operates the provincial transmission and distribution system, and is the monopoly retailer that bills the customer — all under rate regulation by the B.C. Utilities Commission (BCUC), not under any consumer data right. That regulatory fact drives the entire API posture. Ontario Regulation 633/21 compels Ontario distributors to implement Green Button Download My Data and Connect My Data; British Columbia has no equivalent, and no Canadian federal energy data mandate exists. BC Hydro has nonetheless adopted Green Button voluntarily
  — but only the file half of it. BC Hydro''s own MyHydro billing pages state that a customer can "Download a CSV or Green Button XML file with your metered electricity use," available through the previous day and up to three years back. There is no Connect My Data, no OAuth authorization surface, no third-party vendor onboarding, and no published resource base URI: a third party cannot obtain a customer''s usage data through any documented API, only the account holder can, by logging in and downloading a file. On the market-data side the picture is just as closed. There is no developer.bchydro.com, api.bchydro.com, data.bchydro.com or docs.bchydro.com (all DNS failures), no /developers, /api or /data path, no OpenAPI or Swagger definition anywhere, and no open data portal. Wholesale transmission information is posted to an OATI-hosted OASIS node that only registered transmission customers may use, and the BCUC-ordered transaction-data postings are documents rather than feeds. The single
  deliberate open-data artifact is one 2013 mapping layer published to the provincial BC Data Catalogue under the org "bc-hydro-and-power-authority." The finding is a utility that is closed on both axes: consumer data exists in a real standard but only as a human-initiated download behind a customer login, and grid/market data is either registration-gated or absent.'
image: https://www.bchydro.com/content/experience-fragments/bchydro-web/header/master/_jcr_content/root/container/container/image.coreimg.svg/1723787760686/logo-bchydro.svg
json_schemas:
- name: BC Hydro outage map feed record
  property_count: 0
  slug: bc-hydro-outages-map
layout: provider
modified: '2026-07-27'
name: BC Hydro
nav: Providers
network: true
overview: 'BC Hydro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Canada, Utilities, Electricity, and Crown Corporation.


  BC Hydro''s developer surface includes authentication, documentation, support, engineering blog, product news, and 21 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 12
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 15.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 31.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bc-hydro/refs/heads/main/screenshots/bc-hydro-2026-08-07T162216.png
security:
- kind: authentication
  name: Bc Hydro Authentication
  slug: bc-hydro-authentication
  summary_line: session-sso · 1 scheme
- kind: domain-security
  name: Bc Hydro Domain Security
  slug: bc-hydro-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bc-hydro
tags:
- Energy
- Canada
- Utilities
- Electricity
- Crown Corporation
- Hydroelectric
- Renewables
- Grid
- Transmission
- Distribution
- Smart Metering
- Green Button
- Energy Data
- EV Charging
website: https://www.bchydro.com/
---
