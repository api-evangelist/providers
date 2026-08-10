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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bureau Of Justice Statistics Agentic Access
  operation_count: 6
  slug: bureau-of-justice-statistics-agentic-access
  summary_line: 6 operations
api_count: 5
apis:
- description: Provides access to victimization data from the National Crime Victimization Survey (NCVS), covering personal and household victimization data along with population estimates. No authentication require
  name: National Crime Victimization Survey (NCVS) API
  slug: ncvs-api
- description: A suite of interactive web-based data tools providing access to BJS statistical data on crime, corrections, courts, law enforcement, and victimization. Tools include LEARCAT (law enforcement agency cr
  name: BJS Data Analysis Tools
  slug: bjs-data-analysis-tools
- description: The Property Crime API from Bureau of Justice Statistics — 2 operation(s) for property crime.
  name: Bureau of Justice Statistics Property Crime API
  slug: bureau-of-justice-statistics-property-crime-api
- description: The Victimization API from Bureau of Justice Statistics — 2 operation(s) for victimization.
  name: Bureau of Justice Statistics Victimization API
  slug: bureau-of-justice-statistics-victimization-api
- description: The Violent Crime API from Bureau of Justice Statistics — 2 operation(s) for violent crime.
  name: Bureau of Justice Statistics Violent Crime API
  slug: bureau-of-justice-statistics-violent-crime-api
artifact_total: 11
collections:
- collection_type: open
  name: BJS NIBRS National Estimates API
  slug: open-bureau-of-justice-statistics
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bureau-of-justice-statistics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bureau-of-justice-statistics-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bureau-of-justice-statistics
- group: company
  title: ''
  type: Website
  url: https://bjs.ojp.gov/
- group: start
  title: ''
  type: Portal
  url: https://bjs.ojp.gov/data
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bjs.ojp.gov/legal/privacy-policy
- group: build
  title: ''
  type: Data Collections
  url: https://bjs.ojp.gov/data-collections/search
- group: start
  title: ''
  type: Data Portal
  url: https://catalog.data.gov/dataset?organization=ojp-gov
created: '2024-11-30'
description: The Bureau of Justice Statistics (BJS) publishes information on crime, criminal offenders, victims of crime, and the operation of justice systems.
finops:
- name: Bureau Of Justice Statistics Finops
  service_category: API
  slug: bureau-of-justice-statistics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bureau-of-justice-statistics.png
layout: provider
modified: '2026-05-19'
name: Bureau of Justice Statistics
nav: Providers
network: true
overview: 'Bureau of Justice Statistics publishes 3 APIs on the [APIs.io](https://apis.io/) network: Property Crime API, Victimization API, and Violent Crime API. Tagged areas include Crime, Federal Government, Justice, Statistics, and Victimization.


  Bureau of Justice Statistics'' developer surface includes developer portal and 7 more developer resources.'
plans:
- name: Bureau Of Justice Statistics Plans Pricing
  plan_count: 3
  slug: bureau-of-justice-statistics-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 5
  name: Bureau Of Justice Statistics Rate Limits
  slug: bureau-of-justice-statistics-rate-limits
score:
  band: thin
  composite: 33.6
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 48.8
    developer_ergonomics: 8.7
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 33.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bureau-of-justice-statistics/refs/heads/main/screenshots/bureau-of-justice-statistics-2026-06-20T173810.png
security:
- kind: domain-security
  name: Bureau Of Justice Statistics Domain Security
  slug: bureau-of-justice-statistics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bureau-of-justice-statistics
tags:
- Crime
- Federal Government
- Justice
- Statistics
- Victimization
- Recidivism
website: https://bjs.ojp.gov/
---
