---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
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
  score: 7.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Customer-authorized access to CenterPoint Energy interval usage, daily register reads, monthly billing reads, meter and premise attributes and on-demand reads, through the Smart Meter Texas (SMT) Data
  name: CenterPoint Energy Usage History via Smart Meter Texas Data Access API
  slug: usage-history-inquiry
- description: NAESB ESPI (Energy Services Provider Interface) Green Button export of a CenterPoint Energy electric customer's 15-minute interval usage, delivered as an ad-hoc REST call to the /greenbutton/ resource
  name: CenterPoint Energy Green Button Connect My Data (NAESB ESPI)
  slug: green-button-connect-my-data
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.centerpointenergy.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/centerpoint-energy
- group: operate
  title: ''
  type: Support
  url: https://www.centerpointenergy.com/en-us/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.centerpointenergy.com/en-us/about-us/news
- group: commercial
  title: ''
  type: Pricing
  url: https://www.centerpointenergy.com/en-us/our-services/rates-tariffs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.centerpointenergy.com/en-us/about-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.centerpointenergy.com/en-us/about-us/legal/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://www.centerpointenergy.com/en-us/for-business/industry/competitive-retailers/processes-standards-forms
- group: start
  title: ''
  type: Portal
  url: https://www.centerpointenergy.com/en-us/for-business/industry/competitive-retailers
- group: other
  title: ''
  type: Services
  url: https://www.centerpointenergy.com/en-us/for-business/industry/builders-developers
- group: build
  title: ''
  type: Tools
  url: https://energydataportal.centerpointenergy.com/
- group: company
  title: ''
  type: Partners
  url: https://www.smartmetertexas.com/
- group: other
  title: ''
  type: Standard
  url: https://www.energy.gov/data/green-button
- group: operate
  title: ''
  type: StatusPage
  url: https://www.centerpointenergy.com/en-us/for-business/industry/competitive-retailers
- group: design
  href: https://artifacts.apis.io/centerpoint-energy/conformance/centerpoint-energy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/centerpoint-energy-conformance.yml
- group: design
  href: https://artifacts.apis.io/centerpoint-energy/conventions/centerpoint-energy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/centerpoint-energy-conventions.yml
- group: design
  href: https://artifacts.apis.io/centerpoint-energy/errors/centerpoint-energy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/centerpoint-energy-problem-types.yml
- group: auth
  href: https://artifacts.apis.io/centerpoint-energy/authentication/centerpoint-energy-smt-authentication.yml
  title: ''
  type: Authentication
  url: authentication/centerpoint-energy-smt-authentication.yml
- group: design
  href: https://artifacts.apis.io/centerpoint-energy/lifecycle/centerpoint-energy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/centerpoint-energy-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/centerpoint-energy/rate-limits/centerpoint-energy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/centerpoint-energy-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/centerpoint-energy/plans/centerpoint-energy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/centerpoint-energy-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/centerpoint-energy/finops/centerpoint-energy-finops.yml
  title: ''
  type: FinOps
  url: finops/centerpoint-energy-finops.yml
- group: build
  href: https://artifacts.apis.io/centerpoint-energy/packages/centerpoint-energy-packages.yml
  title: ''
  type: Packages
  url: packages/centerpoint-energy-packages.yml
- group: agent
  href: https://artifacts.apis.io/centerpoint-energy/llms/centerpoint-energy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/centerpoint-energy-llms.txt
- group: auth
  href: https://artifacts.apis.io/centerpoint-energy/security/centerpoint-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/centerpoint-energy-domain-security.yml
created: '2026-03-21'
description: 'CenterPoint Energy is a domestic energy delivery company providing electric transmission and distribution, natural gas distribution and energy services to residential, commercial and industrial customers across Texas, Indiana, Minnesota, Ohio and Louisiana. Its machine-readable surfaces are B2B and regulator-driven rather than a public developer program: CenterPoint Energy Houston Electric is one of four Texas Transmission and Distribution Service Providers that jointly own and fund Smart Meter Texas, whose REST/SOAP interface at services.smartmetertexas.net serves 15-minute interval reads, daily register reads, monthly billing reads and NAESB ESPI Green Button exports to customer-authorized third parties over mutual TLS. CenterPoint also runs a Competitive Retailers Information Portal and publishes the TxSET (ANSI X12 EDI) transaction standards and SAC04 invoice codes retailers integrate against.'
finops:
- has_sources: true
  method: generated
  name: Centerpoint Energy Finops
  primary_unit: ''
  service_category: Utility (Energy + Gas)
  slug: centerpoint-energy-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/centerpoint-energy.png
layout: provider
modified: '2026-09-05'
name: CenterPoint Energy
nav: Providers
network: true
overview: 'CenterPoint Energy is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include EDI, ERCOT, Electricity, Energy, and Fortune 500.


  CenterPoint Energy''s developer surface includes support, engineering blog, pricing, documentation, developer portal, tooling, authentication, and 18 more developer resources.'
plans:
- name: Centerpoint Energy Plans Pricing
  plan_count: 2
  slug: centerpoint-energy-plans-pricing
press:
- date: ''
  title: Greater Houston Partnership
  url: https://www.facebook.com/GreaterHoustonPartnership/posts/apple-and-nvidias-partnership-with-foxconn-is-bringing-a-420m-ai-hardware-expans/1200617808761235/
- date: ''
  title: Q1 2026 Earnings Release
  url: https://investors.centerpointenergy.com/static-files/d00b1995-7237-4543-b5c5-0e8447637e39
- date: ''
  title: First CenterPoint Energy Resiliency Technology Summit ...
  url: https://www.prnewswire.com/news-releases/first-centerpoint-energy-resiliency-technology-summit-showcases-innovative-new-tools-to-help-improve-hurricane-preparedness-and-response-302491419.html
- date: ''
  title: Collaboration Leverages Technosylva's Advanced AI and ...
  url: https://investors.centerpointenergy.com/news-releases/news-release-details/centerpoint-energy-announces-collaboration-technosylva-advance
- date: ''
  title: Palantir Launches Chain Reaction to Build American AI ...
  url: https://www.businesswire.com/news/home/20251204391468/en/Palantir-Launches-Chain-Reaction-to-Build-American-AI-Infrastructure-Founding-Partners-Include-CenterPoint-Energy-and-NVIDIA
random_paper: 18
rate_limits:
- limit_count: 3
  name: Centerpoint Energy Rate Limits
  slug: centerpoint-energy-rate-limits
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 73.2
    operational_transparency: 47.4
  previous_composite: 36.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/centerpoint-energy/centerpoint-energy-2026-06-20T174124.png
security:
- kind: authentication
  name: Centerpoint Energy Smt Authentication
  slug: centerpoint-energy-smt-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Centerpoint Energy Domain Security
  slug: centerpoint-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: centerpoint-energy
tags:
- EDI
- ERCOT
- Electricity
- Energy
- Fortune 500
- Green Button
- Interval Data
- NAESB ESPI
- Natural Gas
- Smart Meter
- Texas
- TxSET
- Usage Data
- Utility
website: https://www.centerpointenergy.com
---
