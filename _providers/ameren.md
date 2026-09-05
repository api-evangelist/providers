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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 17.6
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: The Ameren Illinois Share My Usage API implements the Green Button Connect My Data program, providing authorized third parties access to up to 24 months of historical electric energy usage data for re
  name: Ameren Share My Usage API
  slug: share-my-usage-api
- description: 'The Ameren Renewables Portal enables generation owners to manage community solar and collectively owned generation facilities, track subscriber accounts, and manage billing usage credits in Illinois. '
  name: Ameren Renewables Portal API
  slug: renewables-portal-api
artifact_total: 21
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
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ameren-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ameren-security.txt
- group: auth
  title: ''
  type: Security
  url: security/ameren-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ameren-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ameren-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ameren-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ameren-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ameren-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/ameren-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ameren-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/ameren-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ameren-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ameren-finops.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.ameren.com/partners/account-and-data/share-my-usage
- group: operate
  title: ''
  type: Support
  url: https://www.ameren.com/customer-service
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ameren.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ameren.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://gp.ameren.com/third-party-registration/instructions
- group: start
  title: ''
  type: Login
  url: https://login.eiam.ece.ameren.com/am/XUI/
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
modified: '2026-09-02'
name: Ameren
nav: Providers
network: true
overview: 'Ameren publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Utility, Energy, Electric, Natural Gas, and Smart Grid.


  Ameren''s developer surface includes authentication, documentation, support, signup flow, developer portal, and 20 more developer resources.'
plans:
- name: Ameren Plans Pricing
  plan_count: 0
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
- limit_count: 0
  name: Ameren Rate Limits
  slug: ameren-rate-limits
scopes:
- name: Ameren Scopes
  scope_count: 0
  slug: ameren-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 34.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 64.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ameren/refs/heads/main/screenshots/ameren-2026-08-07T174227.png
security:
- kind: authentication
  name: Ameren Authentication
  slug: ameren-authentication
  summary_line: 2 schemes
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
