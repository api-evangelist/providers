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
api_count: 3
apis:
- description: Automated access to residential and commercial billing history and electricity usage as measured by CenterPoint's Interval Data Recorders (IDRs), exposed through the Smart Meter Texas platform that Ce
  name: CenterPoint Energy Usage History Inquiry API
  slug: usage-history-inquiry
- description: 'CenterPoint Energy has committed to the Green Button initiative, providing customers and authorized third parties with secure download and Connect My Data API access to detailed interval energy usage '
  name: CenterPoint Energy Green Button Connect My Data
  slug: green-button-connect-my-data
- description: 'The Centerpoint API Developer Portal publishes Services API references, examples, and troubleshooting for partners integrating with the Centerpoint Connect field-service and workflow platform used by '
  name: Centerpoint Connect Services API
  slug: centerpoint-connect-services-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/centerpoint-energy-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/centerpoint-energy
- group: company
  title: ''
  type: Website
  url: https://www.centerpointenergy.com
- group: other
  title: ''
  type: Builder Developer Resources
  url: https://www.centerpointenergy.com/en-us/Services/Pages/builder-developer-resources.aspx
- group: start
  title: ''
  type: Energy Data Portal
  url: https://energydataportal.centerpointenergy.com/
- group: other
  title: ''
  type: Green Button
  url: https://www.energy.gov/data/green-button
- group: other
  title: ''
  type: Smart Meter Texas
  url: https://www.smartmetertexas.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.centerpointenergy.com/en-us/utility/pages/privacy-policy.aspx
created: '2026-03-21'
description: CenterPoint Energy is a domestic energy delivery company that provides electric transmission and distribution, natural gas distribution, and energy services operations serving residential, commercial, and industrial customers across multiple U.S. states. Developer-facing interfaces include the Smart Meter Texas (SMT) Usage History Inquiry API, Green Button Connect My Data exports for authorized third-party access to customer interval usage, and the Centerpoint Connect service API at api-portal.centerpointconnect.io used by contractor and field-service integrations.
finops:
- name: Centerpoint Energy Finops
  service_category: Utility (Energy + Gas)
  slug: centerpoint-energy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/centerpoint-energy.png
layout: provider
modified: '2026-04-23'
name: CenterPoint Energy
nav: Providers
network: true
overview: CenterPoint Energy publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Electricity, Energy, Fortune 500, Green Button, and Natural Gas.
plans:
- name: Centerpoint Energy Plans Pricing
  plan_count: 3
  slug: centerpoint-energy-plans-pricing
press:
- date: '2026-05-25'
  title: Greater Houston Partnership
  url: https://www.facebook.com/GreaterHoustonPartnership/posts/apple-and-nvidias-partnership-with-foxconn-is-bringing-a-420m-ai-hardware-expans/1200617808761235/
- date: '2026-05-25'
  title: Q1 2026 Earnings Release
  url: https://investors.centerpointenergy.com/static-files/d00b1995-7237-4543-b5c5-0e8447637e39
- date: '2026-05-25'
  title: First CenterPoint Energy Resiliency Technology Summit ...
  url: https://www.prnewswire.com/news-releases/first-centerpoint-energy-resiliency-technology-summit-showcases-innovative-new-tools-to-help-improve-hurricane-preparedness-and-response-302491419.html
- date: '2026-05-25'
  title: Collaboration Leverages Technosylva's Advanced AI and ...
  url: https://investors.centerpointenergy.com/news-releases/news-release-details/centerpoint-energy-announces-collaboration-technosylva-advance
- date: '2026-05-25'
  title: Palantir Launches Chain Reaction to Build American AI ...
  url: https://www.businesswire.com/news/home/20251204391468/en/Palantir-Launches-Chain-Reaction-to-Build-American-AI-Infrastructure-Founding-Partners-Include-CenterPoint-Energy-and-NVIDIA
random_paper: 42
rate_limits:
- limit_count: 3
  name: Centerpoint Energy Rate Limits
  slug: centerpoint-energy-rate-limits
score:
  band: emerging
  composite: 19.5
  delta: -3.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 22.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/centerpoint-energy/refs/heads/main/screenshots/centerpoint-energy-2026-06-20T174124.png
security:
- kind: domain-security
  name: Centerpoint Energy Domain Security
  slug: centerpoint-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: centerpoint-energy
tags:
- Electricity
- Energy
- Fortune 500
- Green Button
- Natural Gas
- Smart Meter
- Usage Data
- Utility
website: https://www.centerpointenergy.com
---
