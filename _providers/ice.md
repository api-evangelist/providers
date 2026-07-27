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
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 4
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
modified: '2026-07-25'
name: U.S. Immigration and Customs Enforcement (ICE)
nav: Providers
network: true
overview: 'U.S. Immigration and Customs Enforcement (ICE) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Customs Enforcement, DHS, Federal Government, Government, and Immigration.


  U.S. Immigration and Customs Enforcement (ICE)''s developer surface includes product news and 9 more developer resources.'
plans:
- name: Ice Plans Pricing
  plan_count: 3
  slug: ice-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 5
  name: Ice Rate Limits
  slug: ice-rate-limits
score:
  band: emerging
  composite: 21.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 21.0
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 21.7
  schema_version: 0.5
  scored_at: '2026-07-27'
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
