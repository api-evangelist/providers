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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 3
apis:
- description: 'The Online Detainee Locator System is a public-facing search tool that allows the public to locate detainees currently in ICE custody by A-Number and country of birth, or by biographical information. '
  name: ICE Online Detainee Locator System (ODLS)
  slug: ice-online-detainee-locator-system
- description: Enforcement and Removal Operations (ERO) publishes custody arrest, enforcement, and removal statistics in machine-readable formats (CSV/Excel) at regular reporting cadence. These datasets are publishe
  name: ICE ERO Custody and Enforcement Statistics
  slug: ice-ero-statistics
- description: ICE's Freedom of Information Act (FOIA) program provides a public reading room and electronic FOIA library with frequently requested records, policy directives, and data releases. Records are released
  name: ICE FOIA Library
  slug: ice-foia
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ice-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/u-s-immigration-and-customs-enforcement-ice
- group: company
  title: ''
  type: Website
  url: https://www.ice.gov/
- group: company
  title: ''
  type: News
  url: https://www.ice.gov/news/all
- group: other
  title: ''
  type: Statistics
  url: https://www.ice.gov/statistics
- group: other
  title: ''
  type: FOIA
  url: https://www.ice.gov/foia
- group: other
  title: ''
  type: Detainee Locator
  url: https://locator.ice.gov/
- group: operate
  title: ''
  type: Contact
  url: https://www.ice.gov/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ice.gov/about/privacy
- group: other
  title: ''
  type: Open Data
  url: https://www.dhs.gov/data
created: '2025-03-01'
description: U.S. Immigration and Customs Enforcement (ICE) is a federal law enforcement agency under the U.S. Department of Homeland Security responsible for enforcing federal immigration and customs laws. ICE does not publish a general-purpose developer API portal, but provides public-facing systems, open data, statistics, and FOIA resources used by researchers, attorneys, journalists, and the public.
finops:
- name: Ice Finops
  service_category: API
  slug: ice-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ice.png
layout: provider
modified: '2026-04-28'
name: U.S. Immigration and Customs Enforcement (ICE)
nav: Providers
network: true
overview: 'U.S. Immigration and Customs Enforcement (ICE) publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Customs Enforcement, DHS, Federal Government, Government, and Immigration.


  U.S. Immigration and Customs Enforcement (ICE)''s developer surface includes product news and 9 more developer resources.'
plans:
- name: Ice Plans Pricing
  plan_count: 3
  slug: ice-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 5
  name: Ice Rate Limits
  slug: ice-rate-limits
score:
  band: emerging
  composite: 22.7
  delta: -0.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 22.9
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 21.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ice/refs/heads/main/screenshots/ice-2026-06-20T183202.png
security:
- kind: domain-security
  name: Ice Domain Security
  slug: ice-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ice
tags:
- Customs Enforcement
- DHS
- Federal Government
- Government
- Immigration
- Law Enforcement
- Open Data
website: https://www.ice.gov/
---
