---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: The DOJ News API exposes more than 14,000 press releases, speeches, and blog entries from the Office of Public Affairs as a JSON web service. Endpoints under /api/v1/ provide list and detail views for
  name: DOJ News API
  slug: doj-news-api
- description: The FOIA.gov developer resources expose annual FOIA report data as XML conforming to the FOIA Annual Report XML schema. Reports can be retrieved by agency abbreviation and year through a documented en
  name: FOIA.gov Annual Report API
  slug: foia-annual-report-api
- description: The Bureau of Justice Statistics NCVS API provides REST access to the National Crime Victimization Survey datasets. Endpoints expose Personal Victimization, Personal Population, Household Victimizatio
  name: BJS National Crime Victimization Survey (NCVS) API
  slug: bjs-ncvs-api
- description: 'The Bureau of Justice Statistics NIBRS National Estimates API provides REST access to the National Incident-Based Reporting System estimates including victimization counts and rates. Endpoints return '
  name: BJS NIBRS National Estimates API
  slug: bjs-nibrs-api
- description: DOJ publishes datasets through the Open Government program and the Department's Data Inventory. Datasets are also surfaced on Data.gov under the doj-gov organization and are accessible via the CKAN-co
  name: DOJ Open Data Catalog
  slug: doj-open-data-catalog
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/department-of-justice-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usdoj
- group: company
  title: ''
  type: Website
  url: https://www.justice.gov
- group: other
  title: ''
  type: Open Government
  url: https://www.justice.gov/open
- group: other
  title: ''
  type: Developer
  url: https://www.justice.gov/developer
- group: company
  title: ''
  type: News
  url: https://www.justice.gov/news
- group: other
  title: ''
  type: FOIA
  url: https://www.foia.gov
- group: other
  title: ''
  type: Office of Information Policy
  url: https://www.justice.gov/oip
- group: other
  title: ''
  type: Bureau of Justice Statistics
  url: https://bjs.ojp.gov
- group: other
  title: ''
  type: Office of Justice Programs
  url: https://www.ojp.gov
- group: other
  title: ''
  type: FBI
  url: https://www.fbi.gov
- group: other
  title: ''
  type: DEA
  url: https://www.dea.gov
- group: other
  title: ''
  type: ATF
  url: https://www.atf.gov
- group: other
  title: ''
  type: U.S. Marshals
  url: https://www.usmarshals.gov
- group: other
  title: ''
  type: Bureau of Prisons
  url: https://www.bop.gov
- group: other
  title: ''
  type: Data.gov DOJ Catalog
  url: https://catalog.data.gov/organization/doj-gov
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.justice.gov/legalpolicies
- group: operate
  title: ''
  type: Contact
  url: https://www.justice.gov/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usdoj
- group: design
  title: ''
  type: JSONLD
  url: json-ld/department-of-justice-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/department-of-justice-vocabulary.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/department-of-justice-capabilities.yml
- group: company
  title: ''
  type: Blog
  url: https://www.justice.gov/rss.xml
created: '2024-12-03'
description: The U.S. Department of Justice (DOJ) is the federal executive department responsible for enforcing the law and defending the interests of the United States. DOJ exposes a portfolio of public APIs and data feeds including the DOJ News API for press releases, speeches, and blog entries from the Office of Public Affairs, the FOIA.gov developer APIs, the Bureau of Justice Statistics NCVS and NIBRS APIs, and the DOJ Open Data Catalog.
finops:
- name: Department Of Justice Finops
  service_category: API
  slug: department-of-justice-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/department-of-justice.png
jsonld:
- class_count: 0
  name: Department Of Justice Context
  property_count: 7
  slug: department-of-justice-context
layout: provider
modified: '2026-04-28'
name: Department of Justice
nav: Providers
network: true
overview: 'Department of Justice publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Bureau of Justice Statistics, Crime, Federal Government, FOIA, and Justice.


  The Department of Justice catalog on APIs.io includes 1 JSON-LD context.


  Department of Justice''s developer surface includes product news, engineering blog, and 21 more developer resources.'
plans:
- name: Department Of Justice Plans Pricing
  plan_count: 3
  slug: department-of-justice-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Department Of Justice Rate Limits
  slug: department-of-justice-rate-limits
score:
  band: emerging
  composite: 26.2
  delta: -3.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 8.1
    developer_ergonomics: 2.2
    discoverability: 74.1
    governance: 10.4
    operational_transparency: 36.8
  previous_composite: 29.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 27.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/department-of-justice/refs/heads/main/screenshots/department-of-justice-2026-06-20T175938.png
security:
- kind: domain-security
  name: Department Of Justice Domain Security
  slug: department-of-justice-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: department-of-justice
tags:
- Bureau of Justice Statistics
- Crime
- Federal Government
- FOIA
- Justice
- News
- Open Data
- Press Releases
- Statistics
website: https://www.justice.gov
---
