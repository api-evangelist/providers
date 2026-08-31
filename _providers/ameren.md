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
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: The Ameren Illinois Share My Usage API implements the Green Button Connect My Data program, providing authorized third parties access to up to 24 months of historical electric energy usage data for re
  name: Ameren Share My Usage API
  slug: share-my-usage-api
- description: 'The Ameren Renewables Portal enables generation owners to manage community solar and collectively owned generation facilities, track subscriber accounts, and manage billing usage credits in Illinois. '
  name: Ameren Renewables Portal API
  slug: renewables-portal-api
artifact_total: 19
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ameren-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ameren-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AmerenCorp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ameren
- group: company
  title: ''
  type: Website
  url: https://www.ameren.com/
- group: start
  title: ''
  type: Portal
  url: https://www.ameren.com/partners/account-and-data/share-my-usage
created: '2026-03-23'
description: Ameren Corporation is a regulated electric and natural gas utility serving customers in Missouri and Illinois. The company provides reliable energy delivery, smart grid infrastructure, and renewable energy programs. Ameren Illinois implements the Green Button Connect My Data program (Share My Usage) based on the ESPI standard, enabling authorized third parties to access customer energy usage data. Ameren also operates a Renewables Portal for community solar generation owners and participates in grid modernization initiatives.
features:
- description: Standard-based program (ESPI/NAESB) enabling authorized third parties to access customer electric energy usage data with OAuth customer authorization for energy analysis, billing, and research.
  name: Green Button Connect My Data
- description: Advanced smart meter deployment enabling two-way communication, real-time usage monitoring, and automated data collection for Illinois and Missouri service territories.
  name: Smart Meter Infrastructure
- description: Online portal for community solar and generation owners to manage subscriber accounts and billing usage credits in Illinois.
  name: Community Solar Renewables Portal
- description: Advanced outage detection, automated notification, and faster power restoration capabilities through smart grid infrastructure.
  name: Outage Management and Restoration
- description: Rebates and incentive programs for residential and business customers to reduce energy consumption and improve efficiency.
  name: Energy Efficiency Programs
finops:
- name: Ameren Finops
  service_category: Utility / Energy
  slug: ameren-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ameren.png
integrations:
- description: Ameren Illinois participates in the national Green Button initiative providing standardized energy data access across utilities.
  name: Green Button Alliance
- description: Aclara serves as Ameren Illinois's authorized data custodian for the Share My Usage Green Button program.
  name: Aclara
- description: Energy Services Provider Interface standard from NAESB for energy usage data exchange in XML format via authenticated API.
  name: ESPI Standard
layout: provider
modified: '2026-04-19'
name: Ameren
nav: Providers
network: true
overview: 'Ameren publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Utility, Energy, Electric, Natural Gas, and Smart Grid.


  Ameren''s developer surface includes developer portal and 5 more developer resources.'
plans:
- name: Ameren Plans Pricing
  plan_count: 1
  slug: ameren-plans-pricing
press:
- date: '2026-05-25'
  title: St. Louis Public Radio
  url: https://www.facebook.com/stlpublicradio/posts/multiple-large-data-centers-have-signed-binding-electric-agreements-with-ameren-/1480897600709260/
- date: '2026-05-25'
  title: Avista, PG&E, Ameren AI demonstrations show great ...
  url: https://www.utilitydive.com/news/avista-pge-ameren-ai-utilities-modeling/740705/
- date: '2026-05-25'
  title: Document
  url: https://www.sec.gov/Archives/edgar/data/1002910/000100291026000013/q12026ex991earningsrelease.htm
- date: '2026-05-25'
  title: Ameren Announces 2025 Results, Affirms Guidance for ...
  url: https://www.prnewswire.com/news-releases/ameren-announces-2025-results-affirms-guidance-for-2026-earnings-and-issues-long-term-growth-guidance-302685673.html
- date: '2026-05-25'
  title: Ameren Announces 2025 Results, Affirms Guidance for 2026 ...
  url: https://www.amereninvestors.com/investors/financial-releases/financial-releases-details/2026/Ameren-Announces-2025-Results-Affirms-Guidance-for-2026-Earnings-and-Issues-Long-Term-Growth-Guidance/default.aspx
random_paper: 2
rate_limits:
- limit_count: 1
  name: Ameren Rate Limits
  slug: ameren-rate-limits
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 8
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 17.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 24.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ameren/refs/heads/main/screenshots/ameren-2026-08-07T174227.png
security:
- kind: domain-security
  name: Ameren Domain Security
  slug: ameren-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ameren Vulnerability Disclosure
  slug: ameren-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ameren
tags:
- Utility
- Energy
- Electric
- Natural Gas
- Smart Grid
- Green Button
- Renewable Energy
- Fortune 500
use_cases:
- description: Authorized third parties access up to 24 months of customer energy usage data for energy efficiency analysis, billing comparisons, and academic research.
  name: Energy Usage Data Analysis
- description: Generation owners manage community solar subscriber accounts and billing credits through the Renewables Portal.
  name: Community Solar Management
- description: Third-party apps and devices integrate with Ameren usage data via Green Button to provide energy management and automation services.
  name: Smart Home Integration
- description: Retail electric suppliers and comparison platforms access usage data to provide customers with competitive supply options.
  name: Retail Electric Supply Comparison
website: https://www.ameren.com/
---
