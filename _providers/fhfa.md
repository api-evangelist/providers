---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - plans
  trial: false
  try_now: false
api_count: 7
apis:
- description: The FHFA House Price Index (HPI) is a comprehensive, publicly available dataset measuring changes in single-family home values across all 50 states and over 400 American cities, with data extending ba
  name: FHFA House Price Index (HPI) API
  slug: fhfa-house-price-index-api
- description: The National Mortgage Database (NMDB) is a nationally representative, longitudinal database of residential mortgages providing aggregate statistics on outstanding residential mortgages and mortgage or
  name: FHFA National Mortgage Database (NMDB) API
  slug: fhfa-national-mortgage-database-api
- description: The FHFA Enterprise Public Use Database (PUDB) provides loan-level data on single-family and multifamily mortgages acquired by Fannie Mae and Freddie Mac, as well as data on Federal Home Loan Bank mem
  name: FHFA Enterprise Public Use Database (PUDB) API
  slug: fhfa-public-use-database-api
- description: FHFA publishes annual conforming loan limit (CLL) values establishing the maximum mortgage amounts that Fannie Mae and Freddie Mac may purchase. Data is available at the county level for all U.S. stat
  name: FHFA Conforming Loan Limits API
  slug: fhfa-conforming-loan-limits-api
- description: The FHFA Uniform Appraisal Dataset (UAD) Aggregate Statistics provide data on residential appraisals submitted to Fannie Mae and Freddie Mac, covering appraisal values, property characteristics, and g
  name: FHFA Uniform Appraisal Dataset (UAD) Aggregate Statistics API
  slug: fhfa-uad-aggregate-statistics-api
- description: FHFA's agency data catalog, published as a Project Open Data v1.1 (DCAT-US) JSON-LD document at https://www.fhfa.gov/data/data.json. 39 datasets and 50 distributions covering the House Price Index, Fe
  name: Federal Housing Finance Agency Data Catalog
  slug: federal-housing-finance-agency
- description: The FHFA House Price Index distributed as bulk files over anonymous HTTPS GET. The master series at https://www.fhfa.gov/hpi/download/monthly/hpi_master.json returns 186,011 observations spanning 1975
  name: FHFA House Price Index Data
  slug: house-price-index
artifact_total: 14
common:
- group: operate
  title: ''
  type: Support
  url: https://www.fhfa.gov/contact/data-and-research
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fhfa.gov/about/privacy
- group: auth
  title: ''
  type: Security
  url: security/fhfa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fhfa-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fhfa-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fhfa-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fhfa-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fhfa-data-model.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/fhfa-data-catalog.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fhfa-hpi-master.json
- group: build
  title: ''
  type: Examples
  url: examples/fhfa-hpi-master-examples.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fhfa-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fhfa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fhfa.gov
- group: docs
  title: ''
  type: Documentation
  url: https://www.fhfa.gov/data/developer-information
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fhfa.gov/about/fhfa-policies/api-terms-of-service
- group: other
  title: ''
  type: Datasets
  url: https://www.fhfa.gov/data/datasets
- group: company
  title: ''
  type: Blog
  url: https://www.fhfa.gov/news
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fhfa
- group: other
  title: ''
  type: X
  url: https://x.com/FHFA
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/fhfa
- group: commercial
  title: ''
  type: Plans
  url: plans/fhfa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fhfa-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fhfa-finops.yml
created: '2026-06-13'
description: The Federal Housing Finance Agency (FHFA) is an independent federal regulator established in 2008 that supervises Fannie Mae, Freddie Mac, and the Federal Home Loan Bank System. FHFA provides publicly accessible data APIs and datasets covering house price indexes (FHFA HPI), mortgage market surveys, conforming loan limits, National Mortgage Database (NMDB) aggregate statistics, Public Use Databases (PUDB) for Fannie Mae and Freddie Mac, Uniform Appraisal Dataset (UAD) statistics, and GSE performance and duty-to-serve data. Data is available in CSV, JSON, XML, and Excel formats with open public access under FHFA's API Terms of Service.
finops:
- name: Fhfa Finops
  service_category: API
  slug: fhfa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fhfa.png
json_schemas:
- name: FHFA House Price Index — hpi_master record
  property_count: 0
  slug: fhfa-hpi-master
jsonld:
- class_count: 22
  name: Fhfa Context
  property_count: 18
  slug: fhfa-context
layout: provider
modified: '2026-06-13'
name: Federal Housing Finance Agency (FHFA)
nav: Providers
network: true
overview: 'Federal Housing Finance Agency (FHFA) publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Housing Finance, House Price Index, Mortgage, Government, and GSE.


  The Federal Housing Finance Agency (FHFA) catalog on APIs.io includes 1 JSON-LD context.


  Federal Housing Finance Agency (FHFA)''s developer surface includes support, code examples, documentation, engineering blog, and 20 more developer resources.'
plans:
- name: Fhfa Plans Pricing
  plan_count: 1
  slug: fhfa-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Fhfa Rate Limits
  slug: fhfa-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/fhfa/refs/heads/main/screenshots/fhfa-2026-06-20T181144.png
security:
- kind: domain-security
  name: Fhfa Domain Security
  slug: fhfa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Fhfa Vulnerability Disclosure
  slug: fhfa-vulnerability-disclosure
  summary_line: Bugcrowd
slug: fhfa
tags:
- Housing Finance
- House Price Index
- Mortgage
- Government
- GSE
- Fannie Mae
- Freddie Mac
- Federal
website: https://www.fhfa.gov
---
