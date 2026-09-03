---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 2.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: American Electric Power operates an Azure API Management instance (apim-aep-prod-use2-001) fronted by the "AEP API Management" developer portal at developer.aep.com and the gateway host api.aep.com. T
  name: AEP API Management
  slug: american-electric-power-api-management
artifact_total: 20
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/american-electric-power-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/american-electric-power
- group: company
  title: ''
  type: Website
  url: https://www.aep.com
- group: company
  title: ''
  type: About
  url: https://www.aep.com/about/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.aep.com/
- group: start
  title: ''
  type: SignUp
  url: https://developer.aep.com/signup
- group: start
  title: ''
  type: Login
  url: https://developer.aep.com/signin
- group: operate
  title: ''
  type: Support
  url: https://www.aep.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.aep.com/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aep.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aep.com/privacy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/american-electric-power-llms.txt
coverage:
  checked: '2026-09-02'
  detail: AEP runs a live Azure API Management program — portal at developer.aep.com, gateway at api.aep.com — but its anonymous catalog call GET /developer/apis?api-version=2022-04-01-preview returns an empty {"value":[]} list, so every API, operation and specification is invisible until a developer-portal account is created and approved.
  evidence:
  - status: 200
    url: https://developer.aep.com/developer/apis?api-version=2022-04-01-preview
  - status: 200
    url: https://developer.aep.com/developer/products?api-version=2022-04-01-preview
  - status: 404
    url: https://api.aep.com/
  - status: 404
    url: https://www.aep.com/.well-known/api-catalog
  reason: partner-login
  state: gated
created: '2024-11-15'
description: American Electric Power (AEP) is one of the largest electric utilities in the United States, delivering electricity to more than 5.6 million customers across 11 states through its regulated utility subsidiaries including AEP Ohio, AEP Texas, Appalachian Power, Indiana Michigan Power, Kentucky Power, Public Service Company of Oklahoma, and Southwestern Electric Power Company. AEP operates the nation's largest electricity transmission network spanning over 40,000 miles and maintains approximately 31,000 megawatts of generating capacity.
features:
- description: AEP operates the largest electricity transmission network in the nation, spanning more than 40,000 miles across its 11-state service territory.
  name: Electricity Transmission
- description: Approximately 31,000 megawatts of diverse generating capacity including coal, natural gas, nuclear, wind, and solar energy sources.
  name: Electric Power Generation
- description: Regulated electric distribution and customer service through seven operating utility subsidiaries serving residential, commercial, and industrial customers.
  name: Regulated Utility Services
- description: Commercial and industrial energy management, demand response programs, and customized energy solutions for large business customers.
  name: Energy Solutions for Business
- description: Site selection assistance, regional resource analysis, and energy infrastructure planning to support economic development across AEP's service territory.
  name: Economic Development Support
- description: Renewable energy options and clean energy transition programs for customers seeking sustainable electricity solutions.
  name: Renewable Energy Programs
- description: Real-time outage reporting, tracking, and restoration services for residential and business customers across all operating company service territories.
  name: Outage Management
- description: Advanced metering infrastructure and smart grid investments to improve reliability and enable future energy management capabilities.
  name: Smart Grid Infrastructure
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/american-electric-power.png
integrations:
- description: AEP operating companies participate in the Green Button initiative, enabling customers to download or share their energy usage data with authorized third-party applications.
  name: Green Button Connect
- description: Integration with grid operators (PJM, MISO, SPP) for demand response and ancillary services markets.
  name: Demand Response Programs
- description: Integration with customer-owned solar and distributed generation systems through net metering programs across AEP operating companies.
  name: Net Metering
layout: provider
modified: '2026-09-02'
name: American Electric Power
nav: Providers
network: true
overview: 'American Electric Power publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Electric Utility, Power, Electricity, and Transmission.


  American Electric Power''s developer surface includes signup flow, support, engineering blog, and 9 more developer resources.'
plans:
- name: American Electric Power Plans Pricing
  plan_count: 0
  slug: american-electric-power-plans-pricing
press:
- date: '2026-05-25'
  title: Investors Boost American Electric Power on AI Growth
  url: https://www.marketbeat.com/originals/investors-boost-american-electric-power-on-ai-growth/
- date: '2026-05-25'
  title: AEP Reports Third-Quarter 2025 Operating Earnings ...
  url: https://www.aep.com/news/stories/view/10534/
- date: '2026-05-25'
  title: AEP ANNOUNCES PUBLIC OFFERING OF COMMON ...
  url: https://www.prnewswire.com/news-releases/aep-announces-public-offering-of-common-stock-with-a-forward-component-302770068.html
- date: '2026-05-25'
  title: American Electric Power expects strong growth in new data ...
  url: https://www.reuters.com/business/energy/american-electric-power-beats-q2-profit-estimates-data-center-demand-boost-2024-07-30/
- date: '2026-05-25'
  title: AEP Receives U.S. Department of Energy Loan Guarantee ...
  url: https://www.aep.com/news/stories/view/10501/
random_paper: 12
rate_limits:
- limit_count: 0
  name: American Electric Power Rate Limits
  slug: american-electric-power-rate-limits
score:
  band: emerging
  composite: 17.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/american-electric-power/refs/heads/main/screenshots/american-electric-power-2026-06-20T171909.png
security:
- kind: domain-security
  name: American Electric Power Domain Security
  slug: american-electric-power-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: american-electric-power
tags:
- Energy
- Electric Utility
- Power
- Electricity
- Transmission
- Generation
- Fortune 500
use_cases:
- description: Providing reliable electric service, billing, outage management, and energy efficiency programs to homeowners and renters across 11 states.
  name: Residential Electricity Service
- description: Meeting the high-voltage, high-capacity power needs of commercial businesses and industrial manufacturers with reliable transmission and distribution.
  name: Commercial and Industrial Power
- description: Enabling large customers and businesses to procure renewable energy and meet their sustainability and corporate ESG goals.
  name: Renewable Energy Procurement
- description: Supporting businesses evaluating new facility locations with energy cost, capacity, and infrastructure data for AEP service territories.
  name: Economic Development
- description: Delivering rebate programs and energy efficiency resources to help customers reduce consumption and lower their electricity costs.
  name: Energy Efficiency Programs
website: https://www.aep.com
---
